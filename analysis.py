import tweepy
from textblob import textblob

consumer_key =  'OK8J0FgLbUu0qDExLnwi891cf'
consumer_secret =  'RCJY2YC4GIXsV5Jbh1L2gucJVtRLftUoiUmkTalnhwsxgBgdhi'

access_token = ' 98364081-3gGXbPG0FAIGJ8apArHj3Vq06DuvfuwAiLqIQK1tt'
access_token_secret = ' xLURFQuIxmQgk0ywmwYw2OOiCo5zU6Uaw7OngKbPP13Ek'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('Putin')


for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     
