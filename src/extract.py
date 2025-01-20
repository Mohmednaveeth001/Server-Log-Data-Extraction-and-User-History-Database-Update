import re
import logging
import json
from datetime import datetime



def extract_emails_and_dates(log_file):
    logging.info("Starting email and date extraction.")
    # Regular expressions for email and date patterns
    with open(log_file, 'r') as file:
            text = file.read()
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    date_pattern = r'(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s+\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4}\s+\d{1,2}:\d{2}:\d{2}'
    
    # Initialize list to store results
    email_dates = []
    
    # Split text into lines
    lines = text.split('\n')
    current_date = None
    for line in lines:
        # Look for dates
        date_match = re.search(date_pattern, line)
        if date_match:
            current_date = date_match.group()
            
        # Look for emails
        email_matches = re.findall(email_pattern, line)
        for email in email_matches:
            if current_date and email:
                email_dates.append({
                    'email': email,
                    'date': current_date
                })
    
    # Remove duplicates while preserving order
    seen = set()
    unique_email_dates = []
    for item in email_dates:
        key = (item['email'], item['date'])
        if key not in seen:
            seen.add(key)
            unique_email_dates.append(item)
   
    logging.info(f"Extracted {len(unique_email_dates)} records.")
    
    return unique_email_dates
