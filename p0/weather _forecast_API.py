import requests
import json
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 52.52, "longitude": 13.41}
headers={"User-Agent": "MyP0App (solokle@uw.edu)"}
response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Success:", response.status_code)
    print(data) 
else:
    print("Request failed:", response.status_code, response.reason)

