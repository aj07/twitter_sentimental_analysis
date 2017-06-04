import tweepy
from textblob import textblob

consumer_key =  'Put your data'
consumer_secret =  'Put your data'

access_token = 'Put your data'
access_token_secret = ' Put your data'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('Putin')


for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     
