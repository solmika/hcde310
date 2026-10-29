# In-class 6: NASA EPIC (photos of the whole Earth from space), with the key kept in .env
#
# 1. Load the key from .env (python-dotenv: load_dotenv(), then os.getenv("NASA_API_KEY"))
# 2. Call https://api.nasa.gov/EPIC/api/natural with your key as the api_key parameter,
#    and timeout=10 so it gives up instead of hanging if the server is slow
# 3. Check r.status_code before you use the data
# 4. The reply is a list of today's photos. Print the caption and the date of the first one

import os
import requests
from dotenv import load_dotenv

def newest_photo(photos):
#Your function here
    new = photos[0]   
    for i in photos:
        if i["date"] > new["date"]:
            new = i
    return new

load_dotenv()
key = os.getenv("NASA_API_KEY")

r = requests.get("https://api.nasa.gov/EPIC/api/natural", params={"api_key": key}, timeout=10)
print(r.status_code)
if r.status_code == 200:
    data = r.json()
    print(r.json()[0]["caption"])
    print(r.json()[0]["date"])
    win = newest_photo(data)
else :
    print("Request failed:", r.status_code, r.reason)

