import os
import json

def load_tasks(task_file):
    """Load tasks from JSON file"""
    if os.path.exists(task_file):
        # open file in read mode ("r") safely using a with statement (which automatically closes the file afterward)
        with open(task_file, "r") as f:
            # reads file and converts JSON data into a Python list (usually a list of task dictionaries)
            return json.load(f)
    # if file doesn’t exist, return an empty list to start with a clean task list
    return []

def save_tasks(task_file, tasks):
    """Save tasks to the JSON file"""
    # open file in write mode ("w"):
    # if file exists-> overwrite it, else-> create it
    with open(task_file, "w") as f:
        # convert list to JSON-formatted string and write it to the file
        json.dump(tasks, f, indent=4)

def add_task(description, task_file):
    """Add new task to the JSON file"""
    if description: # isn't empty
        tasks = load_tasks(task_file)
        tasks.append({"description": description, "completed": False})
        save_tasks(task_file, tasks)

def delete_task(index, task_file):
    """Delete task based on its position from the JSON file"""
    tasks = load_tasks(task_file)
    # ensure index is valid — must be within bounds of list
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(task_file, tasks)

def complete_task(index, task_file):
    """Mark task as DONE in the JSON file"""
    tasks = load_tasks(task_file)
    # ensure index is valid — must be within bounds of list
    if 0 <= index < len(tasks):
        # mark task (at specified index) as completed by setting its "completed" field to True
        tasks[index]["completed"] = True
        save_tasks(task_file, tasks)
