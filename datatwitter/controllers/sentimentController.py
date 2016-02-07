# Perform sentiment analysis using an API (currently TextBlob, may change in the future)

from textblob import TextBlob

from . import twitterController

class Sentiment:

    def __init__(self):
        data = "none"

    def analyse_line(self, line):
        blob = TextBlob(line)
        print(blob.sentiment)

    def analyse_dataset(self, dataset):
        return "good"

    def analyse_twitter(self, query):
        tweet = twitterController.TwitterController()
        results = tweet.search_query(query)
        for result in results:
            blob = TextBlob(result)
            print(blob.sentiment)

        return results

    def save_analysis(self, result, database_conn):
        return "saved for your problems later"


senti = Sentiment()
senti.analyse_line("hello world you are  amazing!")
#senti.analyse_twitter("kish_soup")