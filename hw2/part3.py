# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)
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
from artworks import artworks
count = {}
for i in artworks:
    artist = i.get("artist", "Unknown")
    count[artist] = count.get(artist, 0) + 1 #right side -- count.get "is the first i is in the dictionary count? No? now it is 0 + 1, so 1. Left side, now python connects that 1 to the artist and saves it into the dictionary
print(count)

most_artist = ""
most_count = 0
for i in count:
    if count[i] > most_count:
        most_artist = i
        most_count = count[i]
print(f"Most works: {most_artist} ({most_count})")


    
  





