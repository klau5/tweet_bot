import tweepy
import time
from keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# # Auto-follow
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'username'  # follow one person at a time
#     follower.follow()
#     break

''' Favourite/retweet based on keyword
    apply limit_handler() if necessary
'''
tweet_keyword = 'overwatch'  # enter keyword as string
number_of_tweets = 5  # optional but should remain int

for tweet in tweepy.Cursor(api.search, tweet_keyword).items(number_of_tweets):
    try:
        tweet.favorite()  # favorite can be substituted for retweet
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
