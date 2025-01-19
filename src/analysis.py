# Example SQL queries for analysis
import mysql.connector

queries = {
    "unique_emails": "SELECT DISTINCT email FROM user_history;",
    "daily_email_count": "SELECT DATE(timestamp) as date, COUNT(*) FROM user_history GROUP BY date;",
    "first_last_email": "SELECT email, MIN(timestamp) as first_email, MAX(timestamp) as last_email FROM user_history GROUP BY email;",
    "domain_count": "SELECT SUBSTRING_INDEX(email, '@', -1) as domain, COUNT(*) as count FROM user_history GROUP BY domain ORDER BY count DESC;"
}

def run_analysis(logger):
    """Run analysis queries on the MySQL database."""
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='server_logs'
        )

        if connection.is_connected():
            logger.info("Connected to MySQL database for analysis.")

        cursor = connection.cursor()

        # Execute each query
        for query_name, query in queries.items():
            logger.info(f"Running query: {query_name}")
            cursor.execute(query)
            results = cursor.fetchall()

            logger.info(f"Results for {query_name}:")
            for row in results:
                logger.info(row)

    except mysql.connector.Error as e:
        logger.error(f"MySQL Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logger.info("MySQL connection closed.")
