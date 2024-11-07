# Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# Go to: https://newsapi.org/ and explore the various options to build you application
import requests
import json

query = input("What type of news u want? ")
url = "https://newsapi.org/v2/everything?q={query}&from=2024-07-07&sortBy=publishedAt&apiKey=e7a39ba7b8494599bd4dbff03d36a8ee"

r = requests.get(url)
news = json.loads(r.text)

i = 0
for article in news["articles"]:
    i = i+1
    if i == 5:
        break    
    print(i)
    print(article["title"])
    print(article["description"])
    print("-----------------------------------")
    

