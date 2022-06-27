from bs4 import BeautifulSoup
import requests
url = "https://frontpagemetrics.com/top"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("td", class_ = "tod")
count = 0
import json
subreddits = {}
for t in results:
    if count%3 == 1:
        subreddits[t.text[3:]] = 1
    count+=1
print(subreddits)

with open("subreddit_listing.json", "w") as f:
    json.dump(subreddits,f)