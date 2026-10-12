# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
*i am not sure about the last line*

**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11


**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?
My prediction was almost correct except for the last line in the code. Now it makes sense why the line "print(len(titles[0]))" gives 11. The first item in the list is "The Bedroom" and it has 11 characters (10 letters and 1 space), so now len(titles[0]) counts the characters in the specific word in the list but not how many items are in the whole list, as the line "print(len(titles))" does.

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?
I understand Python better now that I've refreshed my memory! In HW0, where I had to put my percentage of understanding, I put 70% because I thought it was about the app itself, not only the code. I definitely misunderstood that question. Now, looking at the code again, I still don't understand it that well because it's not in Python, but JavaScript. To still try, I asked AI to rewrite my app in Python instead. Now I can recognise lists and loops! In HW0, I made a timeline from 2026 to 1678, and in the code I see a list named year and a loop in the range (2026, 1677, -1). I think it counts down from 2026 by 1 each time, and it stops on year 1678, before 1677. So, the loop puts each year into the list.

