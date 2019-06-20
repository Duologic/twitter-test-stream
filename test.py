import os
import tweepy

auth = tweepy.OAuthHandler(os.environ.get('KEY1'), os.environ.get('KEY2'))
auth.set_access_token(os.environ.get('KEY3'), os.environ.get('KEY4'))

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print('tweet received')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['car'])
