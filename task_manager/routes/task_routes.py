from flask import Blueprint, render_template, request, redirect, url_for
from utils import task_manager

task_bp = Blueprint('tasks', __name__)
TASK_FILE = "task_manager/tasks.json"

@task_bp.route('/')
def index():
    tasks = task_manager.load_tasks(TASK_FILE)
    # incomplete tasks (completed = False) come first, completed ones go to the end.
    sorted_tasks = sorted(tasks, key=lambda t: t['completed'])
    # save sorted tasks to JSON file
    task_manager.save_tasks(TASK_FILE, sorted_tasks)
    return render_template("index.html", tasks=sorted_tasks)

@task_bp.route('/add', methods=['POST'])
def add_task():
    # grabs text that the user entered for their task
    description = request.form.get("description")
    task_manager.add_task(description, TASK_FILE)
    return redirect(url_for("tasks.index"))

@task_bp.route('/delete/<int:index>')
def delete_task(index):
    task_manager.delete_task(index, TASK_FILE)
    return redirect(url_for("tasks.index"))

@task_bp.route('/complete/<int:index>')
def complete_task(index):
    task_manager.complete_task(index, TASK_FILE)
    return redirect(url_for("tasks.index"))
