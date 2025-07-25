import json
from fpdf import FPDF
from datetime import datetime

# Load tasks from JSON file
with open("task_manager/tasks.json", "r") as f:
    tasks = json.load(f)

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
current_datetime = datetime.today().strftime('%d-%m-%Y_%H-%M-%S') # day-month-year_hour-min-sec
pdf.cell(200, 10, txt=f"Daily Task Report for {current_datetime}", ln=True, align="C")
pdf.ln(10)

# Add task list
for i, task in enumerate(tasks, start=1):
    desc = task.get("description", "No description")
    status = "Done" if task.get("completed") else "Not done"
    pdf.cell(200, 10, txt=f"{i}. {desc} [{status}]", ln=True)

# Save with current date
filename = f"tasks_report_{current_datetime}.pdf"
pdf.output(filename)
print(f"Saved: {filename}")
