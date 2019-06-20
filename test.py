import os
import time
import tweepy
import datetime

auth = tweepy.OAuthHandler(os.environ.get('KEY1'), os.environ.get('KEY2'))
auth.set_access_token(os.environ.get('KEY3'), os.environ.get('KEY4'))

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        now = datetime.datetime.now()
        print('{}: tweet received'.format(now))

    def on_error(self, status_code):
        now = datetime.datetime.now()
        print('{}: error: {}'.format(now, status_code))

    def on_timeout(self):
        now = datetime.datetime.now()
        print('{}: timeout'.format(now))
        return true

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, timeout=5)

while True:
    try:
        myStream.filter(track=['car'])
    except Exception as e:
        now = datetime.datetime.now()
        print('{}: {}'.format(now, e))
        time.sleep(5)
