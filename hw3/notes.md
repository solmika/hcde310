# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
The data variable is response.json(), then the path to the first artwork's title is inside the data list, in the first dictionary (index 0 in the list), then key "title" holds the first artwork title, "Lion (One of a Pair, South Pedestal)".
data["data"][0]["title"].

## 2. Find 3 more fields you'd want to show a user, and their paths
First field is "artist_title" and the paths is data["data"][0]["artist_title"]. Second field is "date_display" and the path is data["data"][0]["date_display"]. And the third field is  "medium_display", and the path is data["data"][0]["medium_display"].

## 3. Which fields are `null` for some works?
data["data"][2][ "artist_title"];
data["preference"] is also null.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
When I run it, in the terminal I will see "Search the Art Institute for: " and I have to type anything I want to find in the Art Insititute, but I think it will crash.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
It asked for the cat after "Search the Art Institute for:” appeared and it crashed after that. Looks like line 16 caused it -- response = requests.get(url, params=params). I think it's because the URL and params are empty. 
