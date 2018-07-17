import tweepy

from os import environ as e
consumer_key=e["CONSUMER_KEY"]
consumer_secret=e["CONSUMER_SECRET"]
access_token_key=e["ACCESS_TOKEN"]
access_token_secret=e["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

id = "982333086238158848"

tweet = api.get_status(id)

print(f'User: {tweet.user.screen_name}\nTweet:{tweet.text}\nDate: {tweet.created_at.strftime("%B %e, %Y")}')
