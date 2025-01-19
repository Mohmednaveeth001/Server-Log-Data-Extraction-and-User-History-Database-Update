import mysql.connector
from mysql.connector import Error

def migrate_to_mysql(logger):
    """Migrate data from MongoDB to MySQL."""
    from pymongo import MongoClient

    try:
        client = MongoClient("mongodb+srv://mdnaveeth001:Naveeth1993@cluster0.fdi4o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client.server_logs
        collection = db.user_history

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='server_logs'
        )

        if connection.is_connected():
            logger.info("Connected to MySQL database.")

        cursor = connection.cursor()
        logger.info("Creating table if it does not exist...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                timestamp DATETIME NOT NULL
            )
        ''')

        logger.info("Starting data migration...")
        for record in collection.find():
            logger.debug(f"Migrating record: {record}")
            cursor.execute(
                '''INSERT INTO user_history (email, timestamp) VALUES (%s, %s)
                   ON DUPLICATE KEY UPDATE timestamp = VALUES(timestamp)''',
                (record["email"], record["timestamp"])
            )

        connection.commit()
        logger.info("Data successfully migrated to MySQL.")
    except Error as e:
        logger.error(f"Error migrating to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logger.info("MySQL connection closed.")
        client.close()
