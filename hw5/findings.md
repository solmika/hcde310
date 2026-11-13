# HW5 findings

## 1. Drawing: one search for "Monet"
![drawing](drawing.png)

## 2. Two questions about the code
1. What does "except Exception as e:" do?
2. What does {e} do here -- "message=f"Something broke the request: {e}"?

## 3. Checks (4 or more, at least 2 as pytest tests)
| # |              Check             | Pass or fail |
                                     |              |
| 1 |Serach for an artist in         |              |
|   |the search bar and see if       |     Pass     |
|   |the result page shows the       |              |
|   |title, date, artist and image.  |              |

| 2 |Type a space " " in the search  |
|   |bar to see if it shows a message|     Pass     |
|   |"No search term entered"        |              |

| 3 |test_blank_search_form()        |     Pass     |

| 4 |test_nonsence_word_in_search()  |     Fail     |

## 4. AI review
What it found that I missed: In app.py line 22 -- return render_template("results.html", artist=artis t, artworks=artworks) it says that this line passes an empty list without flagging it when artist returns no matches. Line 20 has very broad "except Exception" block. "Exception hides programming bugs like KeyError or TypeError. In api.py, AI said line 4 is missing tumbnail  field fir alt_text and justified it that without requesting thumbnail the results.html template cannot render meaningful alt attributes for screen readers. In app.py, line 13 --  @app.route("/results", methods=["GET", "POST"]) has unnecessary Post method. It is better to use Get instead of Post for search beacsue Post is for changing data , when Get is for viewing pages. AI also said other things connected to security problems that I didn't fully understand.

What it got wrong: I couldn't find what AI got wrong.

Answers to my two questions, in my own words: 
1. What does "except Exception as e:" do? This line of code helps with unexpected crashes, like the website going offline. "as e" takes the error message and saves it inside that variable "e".

2. What does {e} do here -- "message=f"Something broke the request: {e}"? {e} passes the error into the text with the error message that was saved in the variable "e".

## 5. My fix
What was wrong: When I tried to search for a nonsense word in the search bar (for example "kfhfgk") it gave me list of artworks anyway. This is a problem because I want the website's response to match the serached artist or not give anything if nothing mached.

What I changed: I asked AI to help me fix this. It recommended fixing the api.py file, so now it checks all artworks and sees if something matches the searched artist, if not, it returns an empty list.

How I checked it works: I run the app.py and pasted the link into my browser and typed a nonsense word and instead of list of random artworks it showed me "No results found."
Also, I checked it with pytest, and it didn't work again. I asked Claude what a possible bug was, and I found out that my text in assert b"" was wrong and it had to match the one in results.html. Now it all works!

Commit before: a30dbc7 
Commit after: c67c50a

## 6. Can we ship it? (100–150 words)
Yes or no, and why: 
No, we cannot ship this app. This home app page doesn't work with a Tab key. It doesn't show images under the title and year, but it is in the Fields. This app is also very simple in design, and it only has the basics for a website to work. The app only shows 10 artworks because of the limit, but if an artist has more artworks, the user won't see them all. Also errors could be shown to users as a raw message. Line 20 saves the error and line 21 show it to the user. All these problems do not let the app tp be shipped.

One thing my HW4 does better: HW4 has accessibility basics similar to AI's app, but my home page works with Tab. AI's doesn't.
One thing the AI's app does better: When I type a nonsense word into AI's app, I don't get any list of artworks. 

AI use goes in `ai_use.md` (the five points on the AI Use Card).

