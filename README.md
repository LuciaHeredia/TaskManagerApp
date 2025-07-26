# 📋 Task Manager  
### Automates your tasks with Python, GitHub Actions, and AWS S3

**"Task manager"** is an automation tool that manages your tasks, exports them as a *PDF*, and uploads the report to an **AWS S3 bucket** every day at a scheduled time using **GitHub Actions**.
> You must clone this project using the web *URL* and save it in your own **Github repository** for the **GitHub Actions** to work.

<img src="zREADME-pics/tasks.png"/> <br/>

## 🧩 Features:
✅ **Add Tasks** – Store tasks with due dates \
✅ **List Tasks** – Show pending and completed tasks \
✅ **Complete Tasks** – Mark tasks as done \
✅ **Delete Tasks** – Remove tasks when no longer needed \
✅ **Data Persistence** – Save tasks in a JSON file \
✅ **Web UI** - For visualization and live updates via page reload \
✅ **PDF Export** – Automatically export a PDF and uploads it to an AWS S3 bucket at a specific time

## 📁 Folders Structure:
```
TaskManagerApp
│── .github/
│   └── workflow/
│       └── export-and-push.yml     # Export PDF and upload to a S3 bucket
└── task_manager/
    │── app.py                      # Main Flask app
    │── export_tasks.py             # Export tasks as PDF
    │── upload_to_s3.py             # Upload PDF to a S3 bucket
    │── requirements.txt            # Requirements file
    │── reports/
    │   └── tasks_report.pdf        # PDF tasks report
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

## 🧠 Logic Flow:
1. At e.g. **00:00** UTC daily 
2. **GitHub Actions** pulls the latest version of your repository
3. Runs *export_tasks.py* → generates *tasks_report_DATE.pdf*
4. Runs *upload_pdf_to_s3.py* → uploads the *PDF* to your **AWS S3 bucket**

## 🕹️ Manual test:
1. Push your latest *tasks.json* to **GitHub**
2. Go to **GitHub** → "Actions tab" → "Export Tasks and Upload to S3"
3. Click “Run workflow”, it will run the full *pipeline* and upload the *PDF*

## 📦 Requirements:
1. Create an **AWS S3 Bucket**:
    - Go to "AWS S3 Console" → "Create bucket"
    - Fill *Name*(e.g. tasks-pdf-storage), *Region* and uncheck *Block all public access* only if you want public files
    - Click "Create bucket"
2. Create an **IAM User** for uploading:
    - Go to "IAM" → "Users"
    - Add *user*: tasks-pdf-bot
    - Attach *policy*: Use *AmazonS3FullAccess* (for testing) Or create a custom policy for limited access
    - Click "Create user"
3. Create *Access key* for new user:
    - Click the user you created → "Security credentials" → "Access keys" → "Create Access key"
    - Choose "Third-party service" → Next → "Create access key"
    - Save the *Access Key ID* and *Secret Access Key*
3. Add **GitHub Secrets** in your repository :
    - Go to your "GitHub" repository → "Settings" → "Secrets" → "Actions" 
    - Click "New repository secret"
    - Add:
        - AWS_ACCESS_KEY_ID : Your Access Key ID
        - AWS_SECRET_ACCESS_KEY : Your Secret Access Key
        - AWS_REGION : 	e.g. us-east-2
        - S3_BUCKET_NAME : e.g. tasks-pdf-storage

## 💻 CLI Steps:
> Change *schedule time* in **workflow** *export-and-push.yml* before you start.

1️⃣ Clone this project using the web *URL* and also save it in your own **Github repository**. \
2️⃣ Run: ```pip install -r task_manager/requirements.txt``` \
3️⃣ Start the server with: ```python3 task_manager/app.py```
