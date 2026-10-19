# HW2 Part 4 – Your first functions
#
# In `part4.py`, turn code you already wrote into functions:
#
# 1. `works_by(artist, artworks)` → returns a list of titles by that artist, from the list you pass in
#    (an empty list if there are none)
# 2. `count_by_artist(artworks)` → returns your counting dictionary from Part 3
# 3. Replace each `TODO` docstring with one line saying what the function takes and what it returns
#
# Don't change the `print` lines at the bottom of `part4.py`. `check.py` uses them.
artworks = [
    {"title": "The Bedroom", "artist": "Vincent van Gogh", "year": 1889, "medium": "Oil on canvas"},
    {"title": "Nighthawks", "artist": "Edward Hopper", "year": 1942},
    {"title": "American Gothic", "artist": "Grant Wood", "year": 1930, "medium": "Oil on beaver board"},
    {"title": "A Sunday on La Grande Jatte", "artist": "Georges Seurat", "year": 1884, "medium": "Oil on canvas"},
    {"title": "The Old Guitarist", "artist": "Pablo Picasso", "year": 1903},
    {"title": "Water Lilies", "artist": "Claude Monet", "year": 1906, "medium": "Oil on canvas"},
    {"title": "The Child's Bath", "artist": "Mary Cassatt"},
    {"title": "Sky above Clouds IV", "artist": "Georgia O'Keeffe", "year": 1965},
    {"title": "Stacks of Wheat (End of Summer)", "artist": "Claude Monet", "year": 1890},
    {"title": "Untitled (vase)"},
]

#['Water Lilies', 'Stacks of Wheat (End of Summer)']
#[]
#{'Vincent van Gogh': 1, 'Edward Hopper': 1, 'Grant Wood': 1, 'Georges Seurat': 1, 'Pablo Picasso': 1, 'Claude Monet': 2, 'Mary Cassatt': 1, "Georgia O'Keeffe": 1, 'Unknown': 1}

from artworks import artworks

def works_by(artist, artworks):
    """Return the title by the called artist."""
    found = []
    for i in artworks:    #i is this whole entile dictionary
        if i.get("artist") == artist:   #if evaluates as False, it is none, so returns empty []
            found.append(i["title"])
    return found


def count_by_artist(artworks):
    """Returns the counting dictionary"""

    count = {}
    for i in artworks:
        artist = i.get("artist", "Unknown")
        count[artist] = count.get(artist, 0) + 1 #right side -- count.get "is the first i is in the dictionary count? No? now it is 0 + 1, so 1. Left side, now python connects that 1 to the artist and saves it into the dictionary
    return count


print(works_by("Claude Monet", artworks))
print(works_by("Nobody", artworks))
print(count_by_artist(artworks))
