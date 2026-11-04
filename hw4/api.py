import requests
import json

#function that send the request to URL and get a response with the list of afrworks
def search_art(term):
    url = "https://api.artic.edu/api/v1/artworks/search"
    FIELDS = "title,artist_title,date_display"
    headers = {"AIC-User-Agent": "HCDE310 student project"}
    params = { "q": term, "fields": FIELDS}
    response = requests.get(url, params=params, headers=headers)

#if API failed it returns none, and app.py helps with the message and home.html shows it to the user
    if response.status_code != 200:
        print("Request failed. Your status code is", response.status_code, response.reason)
        return None

    return response.json()["data"]



        