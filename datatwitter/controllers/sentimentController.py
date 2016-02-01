# Perform sentiment analysis using an API (currently TextBlob, may change in the future)

from textblob import TextBlob

# from .twitterController import TwitterController

class Sentiment:

    def __init__(self):
        data = "none"

    def analyse_line(self, line):
        blob = TextBlob(line)
        self.print_sentiment(blob)

    def analyse_dataset(self, dataset):
        return "good"

    # def analyse_twitter(self, query):
        # tweet = TwitterController()
        # results = tweet.search_query(query)
        # for result in results:
        #     blob = TextBlob(result)
        #     self.print_sentiment(blob)

    def save_analysis(self, result, database_conn):
        return "saved for your problems later"

    def print_sentiment(self, blob):
        print(blob.sentiment)

senti = Sentiment()
senti.analyse_line("hello world you are amazing!")
# senti.analyse_twitter("kish_soup")