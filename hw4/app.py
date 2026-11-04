# 
# 1) needs flask, render_template and a request.
# 2) create website itself -- app = Flask(__name__)
# 3) creating the first home page where people can serach for the artist -- 
#    @app.route("/")
# 4) creating function home() and returning "Home page"
# 5) making home.html, so the home screen looks like my sketch -- 
#    with the empty search bar (a text "artist" next to it) and 
#    the search button.
#
# 6) do the almost the same code as with home page 
# @app.route("/results")
# def results():
#   return "Results"
# but now it needs code for the missing data, no API response, or empty serach bar
# 7) all the results should go to the results.html file and displays after 
# the serched artist. It shouls show the title and a year.

from flask import Flask, render_template, request
from api import search_art

app = Flask(__name__) #creating a webpage itself

@app.route("/") #creates the home page and home.html does what the user sees on the screen
def home():
   return render_template("home.html") 

@app.route("/results") #creates results page (what a user sees after searching for artist)
def results():
    #reads what user typed into the search bar (artist search)
    #and .strip() trims extra spaces, so a box with only spaces counts as empty
    artist = request.args.get("artist_search", "").strip()
    #if nothing was typed into the search bar
    if not artist:
        return render_template("home.html", message="Enter the artist's name")
    artwork = search_art(artist) # function search(artist) in api.py sends a request to the API and returns the list of artworks.
    #if API is not responding or answers with an error, so search_art returns None; an error message is handled by the home.html 
    if artwork is None:
        return render_template("home.html", message="Error. Please try again in a moment")
    #API answered, but it didn't find matching artist
    if not artwork:
        return render_template("home.html", message="No artworks were found")
    return render_template("results.html", artwork=artwork, artist=artist)

