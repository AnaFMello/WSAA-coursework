# Topic 2 Lab

import requests

api_url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=wind_speed_10m,wind_direction_10m"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    try:
        wind_speed_10m = data['current']['wind_speed_10m']
        wind_direction_10m = data['current']['wind_direction_10m']

        print(f"Current Wind Speed (10m): {wind_speed_10m} km/h")
        print(f"Current Wind Direction (10m): {wind_direction_10m} degrees")
    except KeyError as e:
        print(f"Error: {e}. Unable to extract wind information from the response.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
