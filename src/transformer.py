from datetime import datetime

def transform_data(data):
    """Transform extracted data for database insertion."""
    transformed_data = []
    for email, timestamp in data:
        try:
            standardized_timestamp = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
            transformed_data.append({"email": email, "timestamp": standardized_timestamp})
        except ValueError:
            continue
    return transformed_data
