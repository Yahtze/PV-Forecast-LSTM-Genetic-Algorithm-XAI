import requests, os, sys
from dotenv import load_dotenv

print(sys.path)
load_dotenv()

API_KEY = os.getenv("API_KEY")
EMAIL = os.getenv("EMAIL")
LOCATION = "POINT(-104.991531 39.742043)" #Change Location Coordinates
START_YEAR = 2018  # Change to your desired start year
END_YEAR = 2023  # Change to the latest year
INTERVAL = 10 #Change Sampling Interval
CSV_FILE_PATH = "data/raw/"

# API Configuration
API_URL = f"https://developer.nrel.gov/api/nsrdb/v2/solar/nsrdb-GOES-full-disc-v4-0-0-download.csv?api_key={API_KEY}&wkt={LOCATION}&email={EMAIL}"


def fetch_data(year):
    """Fetch data from the API for a specific year."""
    try:
        params = {"names": year,
                  "interval" : INTERVAL}  # Modify based on API query format

        response = requests.get(API_URL, params=params)
        print(f"Requesting Data From {response.url}")
        response.raise_for_status()

        file_path = os.path.join(CSV_FILE_PATH, f"solar_data_{year}.csv")
        print(f"Data Stored In {file_path}")
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print("Successfully Fetched Data!")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {year}: {e}")
        return None


def fetch_multiple_years(start_year, end_year, save_path):
    """Fetch data for multiple years and save to a CSV file."""
    for year in range(start_year, end_year + 1):
        print(f"Requesting Data For Year {year}")
        fetch_data(year)


if __name__ == "__main__":
    fetch_multiple_years(START_YEAR, END_YEAR, CSV_FILE_PATH)

