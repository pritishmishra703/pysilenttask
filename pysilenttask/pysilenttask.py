import os
import sys
import subprocess
import csv
import traceback
import pandas as pd
import psutil
from datetime import datetime

# Get the directory where the script is located
SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TASKS_CSV = os.path.join(SCRIPT_DIRECTORY, "tasks.csv")

def create_task(py_file_path, task_name):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    output_file = os.path.join(SCRIPT_DIRECTORY, f"tmp.txt")
    process = subprocess.Popen(
        [sys.executable, py_file_path],
        startupinfo=startupinfo,
        stdout=open(output_file, "w"),
        stderr=subprocess.STDOUT
    )

    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TASKS_CSV, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([process.pid, task_name, start_time])
    print(f"Task '{task_name}' created with PID: {process.pid}")


def kill_task(pid):
    tasks_df = pd.read_csv(TASKS_CSV)
    if int(pid) in tasks_df["PID"].values:
        os.kill(int(pid), 9)
        tasks_df = tasks_df[tasks_df["PID"] != int(pid)]
        tasks_df.to_csv(TASKS_CSV, index=False)
        print(f"Task with PID {pid} has been terminated.")
    else:
        print(f"No task found with PID {pid}.")


def task_list():
    tasks_df = pd.read_csv(TASKS_CSV)
    if len(tasks_df) > 0:
        tasks_df["Start Time"] = pd.to_datetime(tasks_df["Start Time"])
        tasks_df["Duration"] = (datetime.now() - tasks_df["Start Time"]).dt.total_seconds()
        print("Current running tasks:")
        print(tasks_df[["PID", "Description", "Duration"]])
    else:
        print('No Running Tasks.')


def main():
    try:
        # Check if tasks.csv exists, and if not, create it with column names
        if not os.path.exists(TASKS_CSV):
            with open(TASKS_CSV, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["PID", "Description", "Start Time"])

        # Remove completed tasks from tasks.csv
        if os.path.exists(TASKS_CSV):
            tasks_df = pd.read_csv(TASKS_CSV)
            for pid in tasks_df["PID"]:
                if not psutil.pid_exists(int(pid)):
                    tasks_df = tasks_df[tasks_df["PID"] != pid]
            tasks_df.to_csv(TASKS_CSV, index=False)
        
        # Get the command
        command = sys.argv[1]

        if command == "create-task":
            py_file_path = sys.argv[2]
            task_name = sys.argv[3]

            if not task_name.isalnum() or len(task_name) > 20:
                print("[ERROR]: Invalid task name. Task name should be " \
                      "alphanumeric and less than 20 characters.")
            else:
                create_task(py_file_path, task_name)

        elif command == "kill-task":
            pid = sys.argv[2]
            kill_task(pid)

        elif command == "task-list":
            task_list()

        elif command == "--help":
            print("Usage:")
            print("pysilenttask create-task <py_file_path> <task_name>")
            print("pysilenttask kill-task <pid_of_task>")
            print("pysilenttask list-tasks")
            print("pysilenttask --help")
            sys.exit(0)
        
        else:
            print("ERROR: Unrecognized command.\nUse 'pysilenttask --help' " \
                  "to learn more about available commands.")
    
    except Exception as e:
        traceback.print_exc()

if __name__ == "__main__":
    main()
