# Class 3 in-class exercise: decisions and dictionaries (AI off)
# Run it:  python3 exercise.py      Check it:  python3 check.py
# Your output must match expected/exercise.txt exactly.

visits = [
    {"visitor": "Ana", "gallery": "Impressionism", "minutes": 25},
    {"visitor": "Ben", "gallery": "Modern", "minutes": 10},
    {"visitor": "Chen", "gallery": "Impressionism", "minutes": 40},
    {"visitor": "Dee", "gallery": "Photography", "minutes": 5},
    {"visitor": "Eli", "gallery": "Modern", "minutes": 35},
    {"visitor": "Fatima", "gallery": "Impressionism", "minutes": 30},
    {"visitor": "Gus", "gallery": "Photography"},
]

# 1. Print each visit as:   Ana – Impressionism

for a in visits:
    print(a["visitor"], "–", a["gallery"])

# 2. Print a blank line. Then, for each visit, print "long" if minutes is 30 or more, otherwise "short":
#       Ana: short
#    Gus has no "minutes". Use .get() so a missing value counts as 0.
print()
for a in visits:
    a["minutes"] = a.get("minutes",0)
    if a["minutes"] >= 30:
        print(a["visitor"] + ": long")
    elif a["minutes"] < 30:
        print(a["visitor"] + ": short")



# 3. Print a blank line. Then build a dictionary counting visits per gallery, and print it:
#       {'Impressionism': 3, 'Modern': 2, 'Photography': 2}
print()
count = {}
for a in visits:
    gallery = a["gallery"]
    if gallery in count:
        count[gallery] = count[gallery] + 1
    else:
        count[gallery] = 1
print(count)



# BONUS (optional): Is Gus really "short"?
# In #2, .get("minutes", 0) labeled Gus "short." But we don't know how long Gus stayed.
# Is "short" honest? What would be a better default, and what would you print for Gus instead?
# Who might be misled if this were a real museum report?
# Write your answers as comments here. Don't change the output above, so check.py still passes.