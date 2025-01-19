from pymongo import MongoClient

def insert_into_mongodb(data, logger):
    """Insert the transformed data into MongoDB."""
    try:
        client = MongoClient("mongodb+srv://mdnaveeth001:Naveeth1993@cluster0.fdi4o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client.server_logs
        collection = db.user_history

        for record in data:
            collection.update_one(
                {"email": record["email"], "timestamp": record["timestamp"]},
                {"$set": record},
                upsert=True
            )
        logger.info("Data successfully inserted into MongoDB.")
    except Exception as e:
        logger.error(f"Error inserting into MongoDB: {e}")
    finally:
        client.close()
