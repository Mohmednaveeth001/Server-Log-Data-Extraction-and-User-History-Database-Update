from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
# def insert_into_mongodb(data, logger):
#     """Insert the transformed data into MongoDB."""
#     try:
#         client = MongoClient("mongodb+srv://mdnaveeth001:Naveeth1993@cluster0.fdi4o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#         db = client.server_logs
#         collection = db.user_history

#         for record in data:
#             collection.update_one(
#                 {"email": record["email"], "timestamp": record["timestamp"]},
#                 {"$set": record},
#                 upsert=True
#             )
#         logger.info("Data successfully inserted into MongoDB.")
#     except Exception as e:
#         logger.error(f"Error inserting into MongoDB: {e}")
#     finally:
#         client.close()

def insert_into_mongodb(data, logger):
    """
    Insert transformed data into MongoDB with connection verification and database/collection creation.
    
    Args:
        data: List of dictionaries containing records to insert
        logger: Logger object for recording operations and errors
    """
    client = None
    try:
        # Establish connection
        client = MongoClient("mongodb+srv://mdnaveeth001:Naveeth1993@cluster0.fdi4o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        
        # Verify connection
        client.admin.command('ping')
        logger.info("Successfully connected to MongoDB.")
        
        # Get or create database and collection
        db = client.server_logs
        collection = db.user_history
        
        # Create indexes if needed (optional)
        collection.create_index([("email", 1), ("date", 1)], unique=True)
        
        # Insert/update records
        for record in data:
            result = collection.update_one(
                {"email": record["email"], "date": record["date"]},
                {"$set": record},
                upsert=True
            )
            if result.modified_count > 0:
                logger.debug(f"Updated record for email: {record['email']}")
            elif result.upserted_id:
                logger.debug(f"Inserted new record for email: {record['email']}")
                
        logger.info(f"Successfully processed {len(data)} records in MongoDB.")
        
    except ConnectionFailure as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise
    except OperationFailure as e:
        logger.error(f"MongoDB operation failed: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while working with MongoDB: {e}")
        raise
    finally:
        if client:
            client.close()
            logger.debug("MongoDB connection closed.")