# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,medium_display"

# Functions go here (above the code that runs)
def count_by_artist(artworks):

    count = {}
    for i in artworks:
        artist_title = i.get("artist_title")
        if artist_title is None:
            artist_title = "Unknown"
        count[artist_title] = count.get(artist_title, 0) + 1 
    return count

# AI-written
def save_results(artworks, filename):
    """Takes a list of artwork dictionaries and a filename, writes one line per artwork to that file, and returns nothing."""
    with open(filename, "w", encoding="utf-8") as f:
        for art in artworks:
            title = art.get("title") or "Unknown title"
            artist = art.get("artist_title") or "Unknown artist"
            date = art.get("date_display") or "Unknown date"
            f.write(f"{artist} - '{title}' ({date})\n")

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = { "q": term, "fields": FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)


# TODO step 3: check response.status_code before you use the data
if response.status_code == 200:
    data = response.json()
    if len(data["data"]) == 0:
            print("No results")
    else:
        for i in data["data"]:
            artist_title = i.get("artist_title")
            if artist_title is None:
                artist_title = "Unknown Artist"
            date_display = i.get("date_display")
            if date_display is None:
                date_display = "Unknown Date"
            title = i.get("title")
            if title is None:
                title = "Unknown Title"
            medium_display = i.get("medium_display")
            if medium_display is None:
                medium_display = "Unknown Medium"
            print(f"{title} - {artist_title} ({date_display}), {medium_display}")

        print(count_by_artist(data["data"]))
        save_results(data["data"], "artworks.txt" )

else:
    print("Request failed:", response.status_code, response.reason)

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

    # data["data"][0]["title"].
    # data["data"][0]["date_display"]. 
    # data["data"][0]["medium_display"]
    # data["data"][0]["artist_title"]