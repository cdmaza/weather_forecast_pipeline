import pandas as pd
import requests
import json

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..','config'))

import input_log

def request_data():
  
  api_endpoint = "https://api.data.gov.my/weather/forecast?limit=3"

  response = requests.get(api_endpoint)

  if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('data1.csv', index=False)

    input_log.process_input(data)

  else:
    input_log.process_input(response.status_code)

    return print(f"Error: {response.status_code}")

  return data

request_data()