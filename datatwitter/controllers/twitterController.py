# Handle all the interactions between the program and Twitter

import tweepy, json

#Twitter API stuff
consumer_key = "J4OMh7MfrDoFz749gZak2ng14"
consumer_secret = "ExtZwZ07mxlCjw1AeGRAHI9K7rb7O9wQZ5g54r8Ja2SvdMnk0b"
access_token = "2998349633-tz0TRmbsZPoC1JNA3KRJPF7zAiRe7Rhe9qUjbcW"
access_secret = "GxUkuGMAUOZLof8yaQcx8JNrVTzLiw5cvc906t5tWzXVO"
# set up the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.setAccessToken = access_token, access_secret

class TwitterController():
    api = tweepy.API(auth)

    def __init__(self):
        print("initiated")

    def search_query(self, query):
        try:
            # take user query and return latest 100 tweets
            results = self.api.search(q=query, count=100)
        except(tweepy.RateLimitError) as e:
            print(e.message[0]['code'])
        except(tweepy.TweepError) as e:
            print(e.message[0]['code'])
        # turn this off before deployment otherwise server encoding won't work properly
        # for result in results:
        #     print(result.text + "\n")

        return results

# test = TwitterController()
# test.search_query("#SaladGate")
