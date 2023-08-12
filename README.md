# PySilentTask

Effortlessly create and manage background-running Python scripts using PySilentTask. This command-line tool provides a convenient way to handle tasks, making it easy to create, list, and terminate them while keeping track of their execution.

**Table of Contents:**
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Installation

Install PySilentTask using pip:
```
pip install pysilenttask
```

## Usage

Use the following command to interact with PySilentTask through the command line:

```
pysilenttask <command> [options]
```

- Create a new task using a Python script:
  ```
  pysilenttask create-task path/to/script.py task_name
  ```

- Terminate a task using its Process ID (PID):
  ```
  pysilenttask kill-task <pid>
  ```

- List all active tasks. Use this to check task's Process ID (PID):
  ```
  pysilenttask task-list
  ```

- Display usage instructions and available commands:
  ```
  pysilenttask --help
  ```

## Examples

To provide a clearer understanding of how PySilentTask works, let's walk through an example using a long-running task. We'll demonstrate how to create, manage, and terminate the task using PySilentTask's commands.

1. **Create an Example Task:**
   We'll create an example Python script named `example.py` that simulates a long-running task. This script will generate numbers and print them to the console. Save this script in a directory of your choice.

   ```python
   # example.py

   import time

   def main():
       for i in range(1, 11):
           print(f"Current number: {i}")
           time.sleep(5)

   if __name__ == "__main__":
       main()
   ```

2. **Run the Task in the Background:**
   To run the `example.py` script as a background task, use the `create-task` command as follows:

   ```sh
   $ pysilenttask create-task path/to/example.py example
   Task example created with PID: 21156
   ```

   The task will start running in the background, and you'll see its output on the console.

3. **List Running Tasks:**
   You can list all currently running tasks using the `task-list` command:

   ```sh
   $ pysilenttask task-list

   Current running tasks:

     PID   Description  Duration
     21156     example  13.615608
   ```

   The output will show the currently running task(s). Note that completed or terminated tasks won't appear in the list.

4. **Terminate a Task:**
   If you decide to terminate a running task, you can use the `kill-task` command with the corresponding Process ID (PID). Find the PID of the task you want to terminate from the output of the `task-list` command, and then run:

   ```sh
   $ pysilenttask kill-task 21156
   Task with PID 21156 has been terminated.
   ```

   The task will be terminated.

Remember that this example demonstrates a simple use case. PySilentTask can be used to manage more complex and real-world tasks effectively. Feel free to explore additional features and functionalities to suit your specific use cases.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.