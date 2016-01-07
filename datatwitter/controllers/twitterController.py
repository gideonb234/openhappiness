from TwitterAPI import TwitterAPI

#Twitter API stuff


api = TwitterAPI(consumer_key, consumer_secret, access_token, access_secret)

r = api.request('search/tweets', {'q':'pizza'})
for item in r:
    print(item)
