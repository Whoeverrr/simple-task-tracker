# 📝 Task Manager (CLI Version)

A simple command-line Python app that allows users to manage their personal to-do tasks.  
Built to practice file handling, list management, and user interaction — without relying on external libraries.

---

## 🚀 Features

- ✅ Add new tasks
- 📄 View all current tasks
- ✔️ Mark tasks as done
- 🗑️ Delete tasks
- ✏️ Edit task names
- 📦 JSON-based storage (data is saved between runs)

---

## 💻 Technologies Used

- **Python 3**
- Built-in modules:
  - `json`
  - `os`

---

## 🧠 How It Works

Tasks are stored as a list of dictionaries in a JSON file (`tasksManager.json`).  
Each task has two properties:
- `"task"`: the task name (string)
- `"done"`: status (True/False)

Example:
```json
[
  {
    "task": "Study Python",
    "done": false
  }
]

