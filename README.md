# Job Tracker Bot

A simple Python script that helps you track job applications by saving them into an Excel spreadsheet automatically.

---

## Features

* Takes a job link as input
* Automatically extracts the page title
* Lets you confirm or edit the job title
* Stores job details in an Excel file
* Tracks application date
* Keeps everything organized in one place

---

## Tech Stack

* Python
* `openpyxl` (Excel handling)
* `requests` (fetch web pages)
* `BeautifulSoup` (parse HTML)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/job-tracker-bot.git
cd job-tracker-bot
```

2. Install dependencies:

```bash
pip install openpyxl requests beautifulsoup4
```

---

## Setup

Update the file path in `app.py`:

```python
file_name = r"C:\Users\yourname\OneDrive\Desktop\job_tracker.xlsx"
```

Make sure:

* The Excel file exists
* It is closed before running the script

---

## Usage

Run the script:

```bash
python app.py
```

Then follow the prompts:

* Enter job link
* Confirm or edit job title
* Enter company name

---

## Data Stored

Each job entry includes:

* Job Title
* Company
* Date of Posting
* Date Applied
* Due Date
* Job Link
* Status (default: Not Applied)
* Notes

---

## Notes

* Close the Excel file before running (prevents permission errors)
* Some websites may block scraping
* Best results with standard job posting pages

---

## Future Improvements

* Auto-detect company name
* Add status updates (Applied, Interview, Rejected)
* GUI version
* Database storage instead of Excel

---

## Contributing

Feel free to fork the project and experiment with improvements!
