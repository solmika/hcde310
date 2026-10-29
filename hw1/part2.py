# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

titles = [
    "The Bedroom",
    "Nighthawks",
    "American Gothic",
    "A Sunday on La Grande Jatte",
    "The Old Guitarist",
    "Water Lilies",
    "The Child's Bath",
    "Sky above Clouds IV",
    "Stacks of Wheat (End of Summer)",
    "Mao",
]
count = 0
for i in titles:
    count += 1
    print(f"{count}.", i)
    
count = 0
for i in titles:
    count += 1
print("Titles:", count)

count = 0
for i in titles:
    titles_low = i.lower()
    if "a" in titles_low:
        count += 1
print('Titles with an "a":', count)

long = ""
for i in titles:
    if len(i) > len(long):
        long = i

print("Longest:", long)
