"""This snippet accesses the tweeter and consumes it's API."""
import os
import tweepy
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
    print tweet.created_at

# get user object to get more infor about them
user = api.get_user('gvanrossum')
print user.screen_name
print user.followers_count
for friend in user.friends():
    print friend.screen_name
