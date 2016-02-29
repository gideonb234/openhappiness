# Perform sentiment analysis using an API (currently TextBlob, may change in the future)

from textblob import TextBlob

from .twitterController import TwitterController
from .fileController import FileController


class SentimentController:

    def analyse_line(self, line):
        blob = TextBlob(line)
        print(blob.sentiment)

    def analyse_dataset(self, file):
        blob = TextBlob(file)
        print(blob.sentiment)

    def analyse_twitter(self, query):
        avg_polarity = 0
        avg_subjectivity = 0
        tweet = TwitterController()
        results = tweet.search_query(query)
        # take those tweets and give an average subjectivity/polarity
        for result in results:
            str_result = str(result)
            blob = TextBlob(str_result)
            avg_polarity = avg_polarity + blob.polarity
            avg_subjectivity = avg_subjectivity + blob.subjectivity

        avg_polarity = avg_polarity / len(results)
        avg_subjectivity = avg_subjectivity / len(results)

        print("Polarity : " + str(avg_polarity) + " , Subjectivity: " + str(avg_subjectivity))

    def save_analysis(self, result, database_conn):
        return "saved for your problems later"

    def analyse_dataset_num(self, file):
        blob = TextBlob(file)
        print(blob.sentiment)

# senti = Sentiment()
# senti.analyse_line("hello world you are amazing!")
# senti.analyse_twitter("synergy_blitz")