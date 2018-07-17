import tweepy
from urllib.parse import urlparse

from os import environ as e
consumer_key=e["CONSUMER_KEY"]
consumer_secret=e["CONSUMER_SECRET"]
access_token_key=e["ACCESS_TOKEN"]
access_token_secret=e["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

# id = "982333086238158848"

# tweet = api.get_status(id)

# print(f'User: {tweet.user.screen_name}\nTweet:{tweet.text}\nDate: {tweet.created_at.strftime("%B %e, %Y")}')

def get_tweet_id(url: str) -> str:
    """
    Get tweet id from url, i.e. the last part of a url in this form:
    e.g. 'https://twitter.com/diyclassics/status/1013816168371687424'
    should return '1013816168371687424'
    """
    url_parsed = urlparse(url)
    url_parts = url_parsed[2].rpartition('/')
    tweet_id = url_parts[-1]
    return tweet_id

def get_tweet_screenname(id: str) -> str:
    return api.get_status(id).user.screen_name

def get_tweet_text(id: str) -> str:
    return api.get_status(id).text

def get_tweet_date(id: str) -> str:
    return api.get_status(id).created_at
