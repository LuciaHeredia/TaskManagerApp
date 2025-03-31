from flask import Blueprint, render_template, request, redirect, url_for
from utils import task_manager

task_bp = Blueprint('tasks', __name__)
TASK_FILE = "tasks.json"

@task_bp.route('/')
def index():
    tasks = task_manager.load_tasks(TASK_FILE)
    return render_template("index.html", tasks=tasks)

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
