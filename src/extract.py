import re
import logging
from datetime import datetime

def extract_emails_and_dates(log_file):
    logging.info("Starting email and date extraction.")
    email_date_pattern = r"From\s+(\S+@\S+)\s+\w+\s+(\d+\s+\w+\s+\d+\s+\d+:\d+:\d+)"
    extracted_data = []
    
    with open(log_file, "r") as file:
        for line in file:
            match = re.search(email_date_pattern, line)
            if match:
                email, date_str = match.groups()
                try:
                    date = datetime.strptime(date_str, "%d %b %Y %H:%M:%S")
                    extracted_data.append({"email": email, "date": date})
                except ValueError as e:
                    logging.warning(f"Failed to parse date: {date_str} | Error: {e}")
    
    logging.info(f"Extracted {len(extracted_data)} records.")
    return extracted_data
