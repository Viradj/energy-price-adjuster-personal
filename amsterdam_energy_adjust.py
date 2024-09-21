from datetime import datetime, timedelta
import requests
import json
import pandas as pd
import pytz

# Function to get default or user-modified start and end dates
def get_default_dates():
    # Get the current date in Amsterdam timezone
    current_date = datetime.now(tz=pytz.timezone('Europe/Amsterdam'))

    # Start and end date default to today
    start_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = current_date.replace(hour=23, minute=59, second=59, microsecond=999999)

    return start_date, end_date

# Automatically get the start and end dates (pre-filled with current date)
start_date, end_date = get_default_dates()

# Adjust the dates to UTC and apply a 2-hour shift back
from_date = (start_date - timedelta(hours=2)).strftime("%Y-%m-%dT22:00:00.000Z")
till_date = (end_date - timedelta(hours=2)).strftime("%Y-%m-%dT21:59:59.999Z")

# Construct the API URL
url = f"https://api.energyzero.nl/v1/energyprices?fromDate={from_date}&tillDate={till_date}&interval=4&usageType=1&inclBtw=true"

# Fetching the data
response = requests.get(url)
stroomprijs_data = response.json()

# Extract the list of prices from the JSON response
prices = stroomprijs_data.get('Prices', [])

# Print the raw JSON response from the API
print("Raw API response:")
print(json.dumps(stroomprijs_data, indent=2))

# Adjust the output time to Amsterdam (UTC+2) and shift to the requested day
for entry in prices:
    iso_datetime_str = entry['readingDate']
    utc_datetime = datetime.strptime(iso_datetime_str, '%Y-%m-%dT%H:%M:%SZ')
    local_datetime = utc_datetime.astimezone(pytz.timezone('Europe/Amsterdam'))

    # Add 2 hours to the local time
    adjusted_datetime = local_datetime + timedelta(hours=2)

    # If the hour goes to the next day, adjust the day
    if adjusted_datetime.day != local_datetime.day:
        adjusted_datetime = adjusted_datetime.replace(hour=0)

    entry['readingDate'] = adjusted_datetime.strftime('%Y-%m-%dT%H:%M:%S')
    entry['date'] = adjusted_datetime.strftime('%Y-%m-%d')
    entry['hour'] = adjusted_datetime.strftime('%H:%M:%S')

    # Print the adjusted entry
    print(entry)

# Optionally, return the processed data as a JSON object
processed_json = json.dumps(prices, indent=2)
print("\nProcessed Data:")
print(processed_json)
