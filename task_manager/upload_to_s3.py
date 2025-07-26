import boto3
import os
from datetime import datetime

# Load environment variables
bucket_name = os.getenv("S3_BUCKET_NAME")
region = os.getenv("AWS_REGION")

# Find the PDF in the 'reports' folder
reports_folder = "reports"
pdf_files = [f for f in os.listdir(reports_folder) if f.endswith(".pdf")]

if not pdf_files:
    raise FileNotFoundError("❌ No PDF files found in the 'reports' folder.")

pdf_file = pdf_files[0]
pdf_path = os.path.join(reports_folder, pdf_file)

# Upload to S3 with full key: e.g. reports/filename_datetime.pdf
current_datetime = datetime.today().strftime('%d-%m-%Y_%H-%M-%S') # day-month-year_hour-min-sec
s3 = boto3.client("s3", region_name=region)
s3.upload_file(pdf_path, bucket_name, f"{reports_folder}/{pdf_file}_{current_datetime}")

print(f"✅ Uploaded {pdf_file} to s3://{bucket_name}/{reports_folder}/{pdf_file}_{current_datetime}")
