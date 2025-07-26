import boto3
import os
from datetime import datetime

# Load environment variables
bucket_name = os.getenv("S3_BUCKET_NAME")
region = os.getenv("AWS_REGION")

# Find the PDF in the 'reports' folder
reports_folder = "task_manager/reports"
pdf_files = [f for f in os.listdir(reports_folder) if f.endswith(".pdf")]

if not pdf_files:
    raise FileNotFoundError("❌ No PDF files found in the 'reports' folder.")

pdf_file = pdf_files[0]
original_path = os.path.join(reports_folder, pdf_file)

# Rename the file for upload
timestamp = datetime.today().strftime('%d-%m-%Y_%H-%M-%S')
new_filename = f"tasks_report_{timestamp}.pdf"

# Upload to root of S3 bucket (no folders)
s3 = boto3.client("s3", region_name=region)
s3.upload_file(original_path, bucket_name, new_filename)
print(f"✅ Uploaded as s3://{bucket_name}/{new_filename}")
