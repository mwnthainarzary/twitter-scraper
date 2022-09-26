import snscrape.modules.twitter as sntwitter
import pandas as pd

query="wannacryattack"
tweets = []
limit=100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Datetime', 'Username', 'Tweet'])

to_csv = df.to_csv (r'wannacry.csv', index = False, header=True)

print(df.head())