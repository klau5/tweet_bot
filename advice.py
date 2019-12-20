import json
import requests
import time

req = requests.get('https://api.adviceslip.com/advice', timeout=10)

data = json.loads(req.text)
data == req.json()
advice_tweet = data['slip']['advice']


if req.status_code == 200:
    advice_tweet
else:
    pass


print(advice_tweet)