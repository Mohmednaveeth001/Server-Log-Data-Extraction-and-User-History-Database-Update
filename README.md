### README.md

# Email Log Data Pipeline

## Overview
This project processes email logs to extract email addresses and dates, stores the data in MongoDB and SQLite databases, and performs data analysis using SQL queries.

---

## Project Structure
```
project/
├── data/                  # Directory for input and database files
│   ├── mbox.txt           # Input log file
├── src/                   # Source code
│   ├── extract.py         # Module for data extraction
│   ├── mongodb_handler.py # Module for MongoDB operations
│   ├── sql_handler.py     # Module for SQLite operations
│   ├── analysis.py        # SQL queries for data analysis
│   └── main.py            # Main entry point for the pipeline
├── requirements.txt       # Dependencies
├── README.md              # Documentation
```

---

## Prerequisites
1. Python 3.7 or above
2. MongoDB installed and running locally or on a server
3. SQLite3 (built into Python)

---

## Installation
1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd project
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage
1. Place the input log file (`mbox.txt`) in the `data/` directory.
2. Run the main script:
    ```bash
    python src/main.py
    ```
3. View analysis results in the terminal.

---

## Example SQL Queries
1. List all unique email addresses:
    ```sql
    SELECT DISTINCT email FROM user_history;
    ```
2. Count emails received per day:
    ```sql
    SELECT DATE(date), COUNT(*) FROM user_history GROUP BY DATE(date);
    ```
3. Find the first and last email date for each email address:
    ```sql
    SELECT email, MIN(date), MAX(date) FROM user_history GROUP BY email;
    ```
4. Count emails by domain:
    ```sql
    SELECT SUBSTR(email, INSTR(email, '@') + 1) AS domain, COUNT(*) FROM user_history GROUP BY domain;
    ```

---



Add the following to `requirements.txt`:
```
pymongo

mysql-connector-python
pandas
```

