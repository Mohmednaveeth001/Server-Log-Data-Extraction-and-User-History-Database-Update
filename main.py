from src.extract import extract_emails_and_dates
from src.transformer import transform_data
from src.mongodb_handler import insert_into_mongodb
from src.sql_handler import migrate_to_mysql
from src.analysis import run_analysis
from src.logs import setup_logging


def main():
    logger = setup_logging()

    log_file_path = "data/mbox.txt"  # Update this to your log file path

    try:
        # Extract data
        logger.info("Starting data extraction...")
        extracted_data = extract_emails_and_dates(log_file_path)
    
        # # Transform data
        logger.info("Transforming extracted data...")
        transformed_data = transform_data(extracted_data)

        # # Insert into MongoDB
        logger.info("Inserting transformed data into MongoDB...")
        insert_into_mongodb(transformed_data, logger)

        # # Migrate to MySQL
        logger.info("Migrating data to MySQL...")
        migrate_to_mysql(logger)

        # # # Run analysis
        logger.info("Running analysis queries...")
        run_analysis(logger)
        
        logger.info("Data pipeline executed successfully.")
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")

if __name__ == "__main__":
    main()