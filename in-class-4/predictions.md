# Class 4: Five broken snippets

Your name: 
Collaborator: 

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? The last line -- print("Find it in room " + exhibit["Room"]). The word "Room" is capitalize, but should not be.
- What error will Python show? (the kind and the message) -- Key Error
- What's the fix? To write exhibit["room].

## Snippet 2
- Which line breaks? print("Find it in room " + exhibit["room"])
- What error will Python show? (the kind and the message) -- TypeError, because string doesn't add to the integer.
- What's the fix? Maybe, to put coma instead of the plus.

## Snippet 3
- Which line breaks? line 17 maybe + 1  and line 18 (i + 1) -- it is a str + int
- What error will Python show? (the kind and the message) IndexError and TypeError
- What's the fix? I am not sure.

## Snippet 4
- Which line breaks? line 31
- What error will Python show? (the kind and the message) NameError
- What's the fix? To fis word "visit" to "visits"

## Snippet 5
- Which line breaks? line 36
- What error will Python show? (the kind and the message) NameError
- What's the fix? I think to put []

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke? line 8
- What error did Python show? KeyError
- What's the fix? to change ["Room"] to ["room"]

## Snippet 2
- Which line broke? line 13
- What error did Python show? TypeError
- What's the fix? tipe , instead of + (the same for the snippet 1 to make it run)

## Snippet 3
- Which line broke? line 17
- What error did Python show? TypeError
- What's the fix? remove + 1 from range(len(exhibits + 1)).

## Snippet 4
- Which line broke? line 31
- What error did Python show? NameError
- What's the fix? print(count_visits(visit, 243)) change "visit" to "visits"

## Snippet 5
- Which line broke? line 43
- What error did Python show? AttributeError 
- What's the fix? instead of print(longest) has to be return longest

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 5
- Our guess before asking: on the predicting par,t I thought that longest = "" is not correct (I was wrong!)
- Chat:
Me: def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    print(longest)

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())

AI: This code will crash with an AttributeError, and the cause is that longest_title prints its result instead of returning it.

What happens when it runs:

longest_title(...) finds "Water Lilies" and prints it (so you’ll see Water Lilies in the output).
The function has no return statement, so it returns None.
title is therefore None, and title.upper() raises:
AttributeError: 'NoneType' object has no attribute 'upper'

The fix: change print(longest) to return longest:

python
def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    return longest

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())

Output:

WATER LILIES

Since the docstring says the function should return the longest title, return is what matches its intent. Printing inside the function is a common slip, and it works fine until you try to use the result, as you did with title.upper().
Two optional refinements: you could use max(titles, key=len) to replace the loop entirely (it returns the first longest item on ties, same as your loop), and you may want to decide what the function should do for an empty list, since the current version returns "" in that case.

Me: I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I'm a beginner. Please act as my tutor.
Rules: - Never write code for my assignment, even if I ask. If I ask, remind me of this rule and give me a hint instead. - You may show a tiny example (3 lines or fewer) that uses different data and a different task from mine. - Ask me one guiding question at a time, and wait for my answer. - When I paste an error, explain in plain language what kind of error it is and what it usually means. Ask me which line I think it points to before you tell me.
My routine is Try → Predict → Run → Explain → Log. Help me follow it: - If I haven't shown you my attempt, ask for it first. - Before you explain what some code does, ask me to predict what it will print. - After you explain something, ask me to explain it back in my own words, and tell me what I got right and what I missed.
now what was wrong about that code

AI: Since I already showed you the fix earlier, let's walk through it so it sticks, and I'll follow your routine from here on.

Look at the last two lines of your code, the call to `longest_title(...)` and then `print(title.upper())`. **Predict:** what do you think gets printed to the screen, and in what order? If you think something goes wrong, say where.

- Did it give you too much? What did you do? Yes, it did. It gave me the full answer and explanation, but after I put the same snippet and the tutor prompt and it stoped giving me all the answers and started guiding me. So, from now on, I will make sure that at the beginning of every chat I put the tutor prompt. 
