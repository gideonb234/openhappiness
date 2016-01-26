# Handle all the interactions between the program and Twitter

import tweepy

from . import twitterKeys

#Twitter API stuff
consumer_key = twitterKeys.consumer_key
consumer_secret = twitterKeys.consumer_secret
access_token = twitterKeys.access_token
access_secret = twitterKeys.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.setAccessToken = access_token, access_secret

class TwitterController:
    def __init__(self):
        self = tweepy.API(auth)

    def search_query(self, query):
        return "blank"

    def save_query(self,query,database_conn):
        return "h3h3"

    def check_query(self,query):
        return "yes"

test = TwitterController
test.search_query("fuck")