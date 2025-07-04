import requests
from send_email import send_email

api_key = "d9580e75f40b4ef2a08e8d0694b96850"

url = (f"https://newsapi.org/v2/everything?"
       "q=google"
       "&from=2025-06-30&to=2025-06-30"
       "&sortBy=popularity"
       "&apiKey=d9580e75f40b4ef2a08e8d0694b96850"
       "&language=en")
headers = {"User-Agent": "Mozilla/5.0"}

# make a request
request = requests.get(url, headers=headers)

# dict with data
content = request.json() # creates request object type

# display the article titles
body = "Subject: Today's Tech News Re: Google" + "\n"
for article in content["articles"][:5]:
    if article["title"] is not None and article["url"] is not None:
        body = (body + article["title"] + "\n" +  article["description"] +
                "\n" + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(body)