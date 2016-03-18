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

    def analyse_dataset(self, opened_obj, file_id):
        count = 0
        positivity = 0
        negativity = 0
        individual_result = []
        for j_obj in opened_obj:
            str_obj = str(j_obj)
            blob = TextBlob(str_obj, analyzer=NaiveBayesAnalyzer())
            individual_result.append([count, blob.sentiment.p_pos, blob.sentiment.p_neg])
            count += 1
            positivity += blob.sentiment.p_pos
            negativity += blob.sentiment.p_neg
            print(individual_result)
        #   make a list so for each pass, it adds to a separate list I can use later
        positivity = (positivity / count)
        negativity = (negativity / count)
        classification = self.calc_classification(positivity, negativity)
        result = [positivity, negativity, classification, individual_result, file_id]
        print("Positive : " + str(positivity) + " Negative : " + str(negativity) + " Classified as: " + str(classification))
        return result

    def analyse_twitter(self, query):
        positivity = 0
        negativity = 0
        count = 0
        individual_result = []
        tweet = TwitterController()
        results = tweet.search_query(query)
        # take those tweets and give an average subjectivity/polarity (this literally takes forever with naivebayesanalyzer)
        for result in results:
            str_result = str(result)
            blob = TextBlob(str_result, analyzer=NaiveBayesAnalyzer())
            individual_result.append([count, blob.sentiment.p_pos, blob.sentiment.p_neg])
            count += 1
            positivity += blob.sentiment.p_pos
            negativity += blob.sentiment.p_neg
            #   make a list so for each pass, it adds to a separate list I can use later
            print(blob.sentiment)
        positivity = (positivity / count)
        negativity = (negativity / count)
        classification = self.calc_classification(positivity, negativity)
        result = [positivity,negativity,classification, individual_result]
        print("Positive : " + str(positivity) + " Negative : " + str(negativity) + " Classified as: " + str(classification))
        return result

    def save_analysis(self, result, database_conn):
        return "saved for your problems later"

    def calc_classification(self,pos, neg):
        if (pos > neg):
            return "Positive"
        elif (neg > pos):
            return "Negative"
        elif (neg == pos):
            return "50/50"

# senti = Sentiment()
# senti.analyse_line("hello world you are amazing!")
# senti.analyse_twitter("synergy_blitz")