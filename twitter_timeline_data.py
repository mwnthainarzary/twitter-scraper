import snscrape.modules.twitter as sntwitter
import pandas as pd

query="(cyberthreat OR cyberthreat warning OR wannacry OR alert) until:2022-09-26 since:2021-01-01"
tweets = []
limit=5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Datetime', 'Username', 'Tweet'])

to_csv = df.to_csv (r'wannacry_timeline_6.csv', index = False, header=True)

print(df.head())