# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
I think the function "save_results(artworks, filename)" probably also needs to have a list of dictionaries, like data["data"], where the results will be saved. But I'm not sure exactly what each line should look like to save it to the text file.


## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
https://claude.ai/share/b645392e-567f-4399-8687-cc7e58f83695

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
Prediction: I think the file will save the results I got from Art Institution. The line  f.write(f"{title} - {artist} ({date})\n") will write down the title and the dash, artist, and date in parantasise. Then every artwork will start on a new line because of \n. 
I think it will have "Lion (One of a Pair, South Pedestal) - Edward Kemeys (1893)" and so on.
The second line will be "Baroque Pearl Mounted as a Cat Holding a Mouse - Unknown Artist (17th century)".

What actually happened: 
Lion (One of a Pair, South Pedestal) - Edward Kemeys (1893)
Baroque Pearl Mounted as a Cat Holding a Mouse - Unknown artist (17th century)
Nude with Cats - Pablo Picasso (1901)
Cat Making Up - Inagaki Tomoo (1962)
Homesickness - René Magritte (c. 1948)
Winter: Cat on a Cushion - Théophile-Alexandre Pierre Steinlen (1909)
Border Fragments - Nasca (100 BCE–200 CE)
The Return of Odysseus (Homage to Pinturicchio and Benin) - Romare Howard Bearden (1977)
Lions on the Dreyfus Fund III - Larry Rivers (1964)
Summer: Cat on a Balustrade - Théophile-Alexandre Pierre Steinlen (1909)

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I honestly thought my prediction was not right at all. I wrote it too general at first, but then I tried to actually see what could happen, and I think I figured this out after I understood exactly what results this text file would save after I ran the program.


## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. 
I changed the order of the artwork lines format -- f.write(f"{artist} - '{title}' ({date})\n"). I did this to see if artworks.txt will immediately save it the way I chanhed it inside the function.
I just checked the artworks.txt, and I actually did save all the changes!