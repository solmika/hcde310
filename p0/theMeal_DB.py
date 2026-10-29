

import requests
import json
url = "https://www.themealdb.com/api/json/v1/1/search.php"
params = {"s": "Arrabiata"}
headers={"User-Agent": "MyP0App (solokle@uw.edu)"}
response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Success:", response.status_code)
    print(data) 
else:
    print("Request failed:", response.status_code, response.reason)