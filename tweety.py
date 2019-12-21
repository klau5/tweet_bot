import tweepy
import time
from keys import *
import schedule
import json
import requests

# Advice API
req = requests.get('https://api.adviceslip.com/advice', timeout=10)
data = json.loads(req.text)
data == req.json()
advice_tweet = data['slip']['advice']
print(advice_tweet)

# Tweepy API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = api.me()

# post Tweet
# tweet = api.update_status(advice_tweet)

def post_tweet():
    return advice_tweet
print('\nReceived Quote\n')
# print('\nTweet sent\n')

schedule.every(10).seconds.do(post_tweet)

while 1:
    t = time.ctime()
    schedule.run_pending()
    time.sleep(1)
    print(f'Sleep Start {t}')
