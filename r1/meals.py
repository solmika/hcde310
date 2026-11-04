

import requests

term = input("Enter a meal's cuisine: ")

url = "https://www.themealdb.com/api/json/v1/1/filter.php"
params = {"a": term}
response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    #when just putting print(data) it prints the whole dictionary.
    if data["meals"] is None:
        print("No result. Please try again.")
    else:
        for i in data["meals"]:
            print(i["strMeal"])
else:
    print("Request failed:", response.status_code, response.reason)