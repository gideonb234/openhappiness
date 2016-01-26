# Perform sentiment analysis using an API (currently TextBlob, may change in the future)

from textblob import base, TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

class Sentiment:
    def __init__(self):
        self = "3"

    def analyse_dataset(self,dataset):
        return "good"

    def analyse_twitter(self,query):
        return "bad"

    def save_analysis(self,result,database_conn):
        return "saved for your problems later"
