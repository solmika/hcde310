term = input("Search for: ")
print("You searched for", term)
print(type(term))

import os
import requests
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/EPIC/api/natural"
#response = requats.get(url, param={"api_key":key})
# response = requasts.get(url+"?api_key="+key)
params = {"api_key":key}
# response = requats.get(url,params=params)
url = f"https://api.nasa.gov/EPIC/api/natural?api_key={key}"
response = requests.get(url)
# print(response.status_code)
if response.status_code==200:
    # do all the stuff here
    print(response.json())
else:
    print(response.status_code, "error!")

