# HW2 Part 2 – One dict = one thing
#
# In `part2.py`, print each artwork as `Title - Artist (Year)`, for example `The Bedroom - Vincent van
# Gogh (1889)`. Use `.get()` so a missing artist or year prints `Unknown` instead of crashing.
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
for i in artworks:
    artist = i.get("artist", "Unknown")
    year = i.get("year", "Unknown")
    title = i["title"]
    print(f"{title} - {artist} ({year})")


