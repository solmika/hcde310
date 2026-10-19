# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
I think 'artworks' is a list of dictionaries because it helps every key (title, artirst, etc) to have their index in the list, so it is easier to call specific dictionary and what it holds. If one big dictionary would have many keys with "artist" it would print only the last artist and Python won't flag it as an error, so it would be hard to spot. But when we have a list of these separated dictionaries then we can call that dictionary because it is in the list, so for example artworks[1]['artist'], so Python doesn't just call the last artist and earlier ones disappear.

## 2. Which fields are sometimes missing? What should the app show when they are?
The field is missing the key "medium" in artworks[1](the second dictionary). I think if someone asks for artworks[1]["medium"] then Python will show a KeyError because a key medium doesn't exist in artworks[1]. If I use artworks[1].get("medium", "Unknown"), then when the key medium is missing from the second disctionary, Python won't crush but show Unknown instead.
