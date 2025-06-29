# Importing modules
import json
import os


# Creating a constant and linking it to the JSON file
FILENAME = "tasksManager.json"

# Function to load tasks
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_tasks():
    taskName = input("Add task name: ").strip()
    if not taskName:
        print("Task Name cannot be empty, please try again.")
        return
    
    taskInfo = {"task": taskName, "done": False}
    tasks = load_tasks()
    tasks.append(taskInfo)
    save_tasks(tasks)
    print("Task Info successfully added!")

# Function to view tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found!!!")
        return
    
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task.get("done", False) else " "
        print(f"{i}. [{status}] {task['task']}")
    print()  # for clean spacing after the list

#function for marking tasks as complete
def task_done():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    else:
        view_tasks()

    try:
        numTask = int(input("Enter task number to mark task as done: ").strip())
    except ValueError:
        print("Invalid Input")
        return
    
    index = numTask - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range")
        return
    else:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done")

#Creating function to delete tasks
def delete_task():
    tasks = load_tasks() 
    if not tasks:
        print("No tasks found.")
        return
    else:
        view_tasks()

    try:
        numTask = int(input("Enter task number to delete task: ").strip())
    except ValueError:
        print("Invalid Input")
        return
    
    index = numTask - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range")
        return
    else:
        choice = input("Are you sure you want to delete this task? (Press 'y' to delete and 'n' to go to main menu)").strip().lower()
        if choice == "y":
            tasks.pop(index)
            print("Task successfully deleted.")
            return
        elif choice == "n":
            print("Task not deleted. Returning to main menu...")
            return

#Function to edit tasks
def edit_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Tasks not found.")
        return
    else:
        view_tasks()

    try:
        numTask = int(input("Enter task number to edit task: ").strip())
    except ValueError:
        print("Invalid Input")
        return
    
    index = numTask - 1
    if index < 0 or index >= len(tasks):
        print("Task number out of range")
        return
    else:
        current_task = tasks[index]["task"]
        print(f"The current task that you will edit is {current_task}.")

        choice = input("Are you sure you want to edit this task? (Press 'y' to delete and 'n' to go to main menu)").strip().lower()
        if choice == "y":
            new_name = input("Enter a new name for this task: ")
            if new_name:
                tasks[index]["task"] = new_name
                save_tasks(tasks)
                print("Task successfully edited.")
                return
            else:
                print("Changes not made/saved.")
                return

        elif choice == "n":
            print("Task not edited. Returning to main menu...")
            return



# Main function to run the app
def main():
    while True:
        print("\n=== Welcome to the Tasks App ===")
        print("What would you like to do?")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")

        selection = int(input("Your selection is: ").strip())

        if selection == 1:
            add_tasks()
        elif selection == 2:
            view_tasks()
        elif selection == 3:
            task_done()
        elif selection == 4:
            delete_task()
        elif selection == 5:
            edit_tasks()
        elif selection == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid Option. Please enter a number between 1 and 6!")
            return

# Run the program
main()
