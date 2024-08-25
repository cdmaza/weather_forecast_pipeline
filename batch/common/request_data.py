import requests
import json

def request_data():
  api_endpoint = "https://api.data.gov.my/weather/forecast?limit=3"

  response = requests.get(api_endpoint)

  if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print(data)

  else:
    return print(f"Error: {response.status_code}")

  return data