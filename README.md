# Task-Tracker 📑

https://roadmap.sh/projects/task-tracker
## Description
Task-Tracker is a simple project designed to manage and track tasks. The repository includes a `main.py` file written in Python, which contains the core logic of the application, and a `task.json` file used for storing task data.

---

## Features
- Task Management: Allows users to add, edit, and delete tasks effortlessly.
- Data Storage: Utilizes a `task.json` file to save and retrieve task information conveniently
- Lightweight and User-Friendly: Designed to be straightforward and easy to use for individuals looking for a basic task-tracking tool.

---

## Prerequisites
Before you begin, make sure you have the following installed:
- Python 3.7+
---

## Installation
Follow these steps to set up the project locally:

  1. Clone the repository:
     ```bash
     git clone https://github.com/ibrahim-sisar/Task-Tracker.git
     ```
  2. Navigate to the project directory:
    ```bash
    cd Task-Tracker 
    ```
  3. Run code:
     ```bash
     python main.py
     ```
## Usage
  ```
  # Adding a new task
  task-cli add "Buy groceries"
  # Output: Task added successfully (ID: 1)

  # Updating and deleting tasks
  task-cli update 1 "Buy groceries and cook dinner"
  task-cli delete 1

  # Marking a task as in progress or done
  task-cli mark-in-progress 1
  task-cli mark-done 1

  # Listing all tasks
  task-cli list

  # Listing tasks by status
  task-cli list done
  task-cli list todo
  task-cli list in-progress
  ```
  
## Technologies Used
  - python
  - json lib

## Contributing
  #### Contributions are welcome! Please follow these steps:
   1. Fork the repository.
   2. Create a new branch:
      ```bash
        git checkout -b feature-name
      ```
   3. Commit your changes:
      ```bash
      git commit -m "Add your message here"
      ```
   4. Push to the branch:
      ```bash
      git push origin feature-name
      ```
   5. Open a pull request.

## License
   This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

  
