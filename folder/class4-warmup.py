def label(year):
    if year < 1900:
        return "old"
    return "modern"

print(label(1889), label(1942))

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]
for t in titles:
    if "the" in t.lower():
        print(t)

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]
def titles_with(word, titles):
    """ Returns a list of titles with the word in it. """
    titles_with_word = []
    for t in titles:
        if word in t.lower():
            titles_with_word.append(t)
    return titles_with_word
print(titles_with("the", titles))

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]
def titles_with(word, titles):
    """ Return a list with titles with the word in it."""
    list_titles = []
    for t in titles:
        if word in t.lower():
            list_titles.append(t)
            return list_titles

print(titles_with("the", titles))
print(titles_with("sky", titles))



