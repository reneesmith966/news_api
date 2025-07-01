import requests
import time

time.sleep(2)
api_key = "d9580e75f40b4ef2a08e8d0694b96850"
url = ("https://newsapi.org/v2/everything?q=apple&from=2025-06-30&to"
       "=2025-06-30&sortBy=popularity&apiKey=d9580e75f40b4ef2a08e8d0694b96850")
headers = {"User-Agent": "Mozilla/5.0"}

# make a request
request = requests.get(url, headers=headers)

# dict with data
content = request.json() # creates request object type

# display the article titles
for article in content["articles"]:
    print(article["title"])
    print("\n")
    print(article["description"])
