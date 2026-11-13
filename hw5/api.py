import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()

# AI generated code to filter the list of titles and return only those that match the artist name.
    results = response.json().get("data", [])
    search_term = artist.lower()
    
    # Keep only artworks where the searched name matches artist_title
    filtered = [
        art for art in results
        if search_term in (art.get("artist_title") or "").lower()
    ]
    return filtered[:10]
