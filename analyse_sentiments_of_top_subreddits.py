import praw

id = "XYZ"
secret = "XYZ"
password = "XYZ"
agent = "XYZ"
username = "XYZ"
redirect_uri = "XYZ"

reddit = praw.Reddit(
    client_id = id,
    client_secret = secret,
    password = password,
    user_agent = agent,
    username = username,
    redirect_uri = redirect_uri"
)
print(reddit.auth.url(["identity"], "...", "permanent"))
reddit.read_only = True


import json

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

with open('subreddit_listing.json','r') as f:
    data = json.load(f)


SR_names = list(data.keys())
print(SR_names)

d = {}

for j in SR_names:
    sample_set = []
    subreddit = reddit.subreddit(j)
    for submission in subreddit.hot(limit=100):
        sample_set.append(submission.title)

    count = 0
    summ = 0
    for i in sample_set:
        count+=1
        temp = sia.polarity_scores(i)
        summ += temp['compound']

    print(f'Average for r/{j} = {round(summ/count,3)} ')
    d[j] = round(summ/count,3)


with open('SentimentSubreddits.json', 'w') as f:
    json.dump(d, f)

print("Done!")
