from datetime import datetime
import pandas as pd


def transform_data(data_list):
    
    # Convert to DataFrame for easier processing
    df = pd.DataFrame(data_list)
    
    # Convert date strings to standard datetime format
    def standardize_date(date_str):
        # Parse the date string
        dt = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S')
        # Convert to standard format YYYY-MM-DD HH:MM:SS
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    
    # Apply date standardization
    df['date'] = df['date'].apply(standardize_date)
    
    df = df.drop_duplicates(subset=['email', 'date'], keep='first')
    # Sort by date for better organization
    df = df.sort_values('date')
    
    # Reset index to ensure clean sequential indexing
    df = df.reset_index(drop=True)
    
    # Convert DataFrame back to list of dictionaries
    processed_data = df.to_dict('records')
    return processed_data

