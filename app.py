from openpyxl import load_workbook
from datetime import date
import requests
from bs4 import BeautifulSoup

file_name = r"C:\Users\marya\OneDrive\Desktop\job_tracker.xlsx"

job_link = input("Enter job link: ")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(job_link, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Try to get page title
page_title = soup.title.string.strip() if soup.title else ""

print("Detected page title:", page_title)

job_title = input("Enter job title or press Enter to use detected title: ")
company = input("Enter company: ")

if job_title == "":
    job_title = page_title

wb = load_workbook(file_name)
ws = wb.active

ws.append([
    job_title,
    company,
    "",              # Date of Posting
    date.today(),    # Date Applied
    "",              # Due Date
    job_link,
    "Not Applied",
    "",
    ""
])

wb.save(file_name)

print("✅ Job added to tracker!")