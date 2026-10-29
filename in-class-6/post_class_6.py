
def newest_photo(photos):
#Your function here
    new = photos[0]   
    for i in photos:
        if i["date"] > new["date"]:
            new = i
    return new
