AI LOG:
https://claude.ai/share/9b9ee63a-5d46-4057-9939-b0c631a5600f

This time I didn't use the Stage 3 helper, only Stage 2 and our class slides from Monday.

The only thing that surprised me is that after just sending the empty search bar, the result page was still showing 10 artworks. I didn't know how to fix it, so AI suggested to me to add .strip() at the end of artist = request.args.get("artist_search", ""), .strip() removes extra spaces in the search bar, so now the program can see an empty string (if the user submits it or just spaces) and return the helpful message.

Also, when typing a randon nonsenseword to the serach bar, it will return a list of artworks instead of "No artworks were found". I asked AI about it, and it said that the API is fuzzy. But when I checked with just a random number, it did show the message.