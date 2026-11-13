# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page


def test_blank_search_form():
    client = app.test_client()
    page = client.get("/results?author_search=") 
    assert page.status_code == 200 
    assert b"No search term entered" in page.data

def test_nonsence_word_in_search():
    client = app.test_client()
    page = client.get("/results?author_search=tfhrsdk") 
    assert page.status_code == 200 
    assert b"No results found" in page.data
    