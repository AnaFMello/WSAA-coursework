# Topic 2 Lab

import requests

api_url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()

    print(data)

    try:
        current_temperature = data['current']['temperature_2m']
        print(f"Current Temperature: {current_temperature}°C")
    except KeyError as e:
        print(f"Error: {e}. Unable to extract current temperature from the response.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
