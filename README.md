# Energy Price API Adjustment Project

This is a personal project that adjusts energy price data to account for local time in Amsterdam (UTC+2). It fetches energy prices using the `EnergyZero` API, adjusts the timestamps from UTC to local Amsterdam time, and applies a 2-hour shift to align the data with the local time zone.

## What It Does

This script performs the following tasks:

1. **Fetches Energy Price Data**: Retrieves energy prices for a given date range from the `EnergyZero` API.
2. **Applies a 2-Hour Adjustment**: Since Amsterdam is in UTC+2, the API results (which are in UTC) are adjusted by 2 hours to reflect the correct local time.
3. **Handles Day Transitions**: If adding 2 hours causes the time to cross into the next day, the date is adjusted accordingly to maintain proper alignment.
4. **Outputs Adjusted Data**: The final output contains energy prices with corrected timestamps for the Amsterdam timezone.

## Output

The output is a JSON structure where:
- **readingDate**: Reflects the timestamp after the 2-hour adjustment, aligned with local Amsterdam time.
- **date**: The day after applying the shift.
- **hour**: The corresponding hour for each data point, adjusted to the Amsterdam timezone.

### Note
This project was initially created when there wasn't a publicly available API or the help of advanced AI tools. I built the first version from scratch. Now, I have cleaned up the code with the help of ChatGPT and put it online for personal use.

While this project is functional, there is a better, more efficient API available for accessing energy prices. If you're looking for a more robust and reliable solution, I recommend using that API for professional purposes.

### Example Output

```json
{
  "price": 0.1,
  "readingDate": "2024-01-01T00:00:00",
  "date": "2024-01-01",
  "hour": "00:00:00"
}
