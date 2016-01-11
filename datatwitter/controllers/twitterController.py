# Handle all the interactions between the program and Twitter

from TwitterAPI import TwitterAPI

from . import twitterKeys

#Twitter API stuff
consumer_key = twitterKeys.consumer_key
consumer_secret = twitterKeys.consumer_secret
access_token = twitterKeys.access_token
access_secret = twitterKeys.access_secret

class TwitterController:
    def __init__(self):
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)

    def search_tweets(self, query):
        search_query = self.api.request('search/tweets', {'q': query})
        for item in search_query:
            print(item)

    def search_user(self,user):
        search_query = self.api.request('search/users', {'q' : user})
        for item in search_query:
            print(item)


test = TwitterController
test.search_tweets("happiness")