import tweepy
from time import sleep
from keys import *
import schedule

# Tweepy API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = api.me()

# book
book = open('golden-hours.txt', 'r')
lines = book.readlines()
book.close()

def tweet():
    for line in lines:
        try:
            print(line)
            if line != '\n':
                api.update_status(line) # tweet
                sleep(900)
            else:
                pass
        except tweepy.TweepError as err:
            print(err.reason)
            sleep(10)

tweet()
