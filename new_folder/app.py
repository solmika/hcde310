from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    artworks = [{"title": "Lilies"}, {"title": "Nighthawks"}]
    return render_template("home.html", artworks=artworks)

