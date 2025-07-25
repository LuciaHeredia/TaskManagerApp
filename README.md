# Upgraded Project: Personal Task Manager + PDF export (GitHub Actions pipeline)
**"Task manager"** exports the task list from the app as a *PDF*, and automatically commit and push it to a *repository* (or upload to S3 or GDrive) at a specific time using **GitHub Actions**.

## Features:
**Add Tasks** – Store tasks with due dates \
**List Tasks** – Show pending and completed tasks \
**Complete Tasks** – Mark tasks as done \
**Delete Tasks** – Remove tasks when no longer needed \
**Data Persistence** – Save tasks in a JSON file \
**Web UI** - For visualization and live updates via page reload \
*New Features:* \
✅ **PDF Export** – Automatically export a PDF and push it to a *repository* at a specific time

## Folders Structure:
```
task_manager/
│── app.py                      # Main Flask app
│── export_tasks.py             # NEW: Export tasks as PDF
│── requirements.txt            # NEW: Requirements file
│── .github/
│   └── workflow/
│       └── export-and-push.yml # NEW: Export PDF and push to a repository
│── routes/
│   └── task_routes.py          # Task-related routes
│── utils/
│   └── task_manager.py         # Task loading & saving logic
│── templates/
│   └── index.html              # HTML for visualization
│── static/
│   └── style.css               # CSS style
└── tasks.json                  # Stores tasks
```

## CLI Steps:
1️⃣ Clone this project using the web *URL*. \
2️⃣ Run: ```pip install -r requirements.txt``` \
3️⃣ Start the server with: ```python3 task_manager/app.py```
