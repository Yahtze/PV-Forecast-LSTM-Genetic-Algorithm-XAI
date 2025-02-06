import requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

# API endpoint and query parameters
test_url = f"https://developer.nrel.gov/api/nsrdb/v2/solar/nsrdb-GOES-full-disc-v4-0-0-download.csv?api_key={API_KEY}&wkt=POINT(-104.991531 39.742043)&names=2022&interval=10&email=florianero12@gmail.com"
print(test_url)
try:
    # Send the GET request to download CSV directly
    response = requests.get(test_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Save the CSV file
    with open('solar_data.csv', 'wb') as file:
        file.write(response.content)
    print("CSV data successfully saved to 'solar_data.csv'.")
except requests.exceptions.RequestException as e:
    print(f"Error during the request: {e}")