# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message

skleban@Solomiias-MacBook-Pro hw2 % /usr/local/bin/p
ython3 /Users/skleban/Desktop/hcde310/hw2/part3.py
Traceback (most recent call last):
  File "/Users/skleban/Desktop/hcde310/hw2/part3.py", line 24, in <module>
    artist = artworks.get("artist", "Unknown")
             ^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'get
### 2. What I thought it meant
My first thougth was that I can't write artowrks.get() because this is the list with the dictionaries in it and it doesn't work like that with lists probably. 

### 3. What it actually meant
It meant that I asked list to do something that only dictionary can do. 

### 4. The fix
I created a new dictionary count = {} and used .get() to add artist this this dictionary, so i.get("artist", "Unknown") will check every artist in the loop and when a dictionary does not have any, it will return Unknown instead and add it to the new dictionary count. Now, calling .get() only on one painting inside a loop fixes it. 

## Entry 2

### 1. Error message
skleban@Solomiias-MacBook-Pro hw2 % /usr/local/bin/python3 /Users/skleban/Desktop/hcde310/hw2/part2.py
The Bedroom - Vincent van Gogh 1889
Nighthawks - Edward Hopper 1942
American Gothic - Grant Wood 1930
A Sunday on La Grande Jatte - Georges Seurat 1884
The Old Guitarist - Pablo Picasso 1903
Water Lilies - Claude Monet 1906
Traceback (most recent call last):
  File "/Users/skleban/Desktop/hcde310/hw2/part2.py", line 22, in <module>
    print(i["title"], "-", i["artist"], i["year"])
                                        ~^^^^^^^^
KeyError: 'year'

### 2. What I thought it meant
I thought that Python probably crusehd because one dictionary didn't have they key "year", so KeyError indicated that

### 3. What it actually meant
This actually means that Python coulnd't run because one dictionary didn't have a key "year" 

### 4. The fix
adding "year = i.get("year", "Unknown")", and instead of writing in print i["year"] at the end, write just {year}, so print(f"{title} - {artist} ({year})"). Now Python won't crush it because even if one dictionary doesn't have a key year, it will orint "Unknown" instead