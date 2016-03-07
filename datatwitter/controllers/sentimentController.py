# Perform sentiment analysis using an API (currently TextBlob, may change in the future)

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import json, os
from .twitterController import TwitterController
from .fileController import FileController


class SentimentController:

    def analyse_line(self, line):
        blob = TextBlob(line)
        print(blob.sentiment)

    def analyse_dataset(self, file, opened_obj):
        # Check the file is csv/json
        ext = os.path.splitext(file.name)[1]
        count = 0
        positivity = 0
        negativity = 0
        if ext == '.json':
            for j_obj in opened_obj:
                str_obj = str(j_obj)
                blob = TextBlob(str_obj, analyzer=NaiveBayesAnalyzer())
                count += 1
                # positivity += blob.p_pos
                # negativity += blob.p_neg
                print(blob.sentiment)
            # positivity = (positivity / count)
            # negativity = (negativity / count)
            # print("Positive : " + positivity + " Negative : " + negativity)
            return blob.sentiment
        elif ext == '.csv':
            return '.csv'

    def analyse_twitter(self, query):
        avg_polarity = 0
        avg_subjectivity = 0
        tweet = TwitterController()
        results = tweet.search_query(query)
        # take those tweets and give an average subjectivity/polarity
        for result in results:
            str_result = str(result)
            blob = TextBlob(str_result, analyzer=NaiveBayesAnalyzer())
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