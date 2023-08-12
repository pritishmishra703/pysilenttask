# PySilentTask

Effortlessly create and manage background-running Python scripts using PySilentTask. This command-line tool provides a convenient way to handle tasks, making it easy to create, list, and terminate them while keeping track of their execution.

**Table of Contents:**
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Examples](#examples)
- [Contributing](#contributing)
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

## Examples

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.