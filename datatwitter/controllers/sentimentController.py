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
    #incorrect use another thing
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
            print(count);
            print(blob.sentiment)
        positivity = (positivity / count)
        negativity = (negativity / count)
        classification = self.calc_classification(positivity, negativity)
        result = [positivity,negativity,classification, individual_result, query]
        # print(result)
        print("Positive : " + str(positivity) + " Negative : " + str(negativity) + " Classified as: " + str(classification))
        return result

    # rewrite of how json files will be read
    # Get column from json data which matches query, take the average ratings from each one
    # Return them as an array
    def read_from_quantitive_json(self, query, opened_file):
        result = []
        life_satisfaction = []
        # worthwhile = []
        happiness = []
        # anxiety = []
        for j_obj in opened_file:
            str_query = self.fix_query_names(query)
            if j_obj['column3'] == str_query:
                print(j_obj['column3'])
                print('match')
                # I'm not sure if there is a more efficient way to do this, but lets add average/range to a these things
                life_satisfaction.append(j_obj['column4'])
                life_satisfaction.append(j_obj['column6'])
                life_satisfaction.append(j_obj['column7'])
                result.append(life_satisfaction)
                # worthwhile.append(j_obj['column11'])
                # worthwhile.append(j_obj['column13'])
                # worthwhile.append(j_obj['column14'])
                # result.append(worthwhile)
                happiness.append(j_obj['column18'])
                happiness.append(j_obj['column20'])
                happiness.append(j_obj['column21'])
                result.append(happiness)
                # anxiety.append(j_obj['column25'])
                # anxiety.append(j_obj['column27'])
                # anxiety.append(j_obj['column28'])
                # result.append(anxiety)
        print(result)
        return result

    def fix_query_names(self, query):
        other_names = ["Barking", "Dagenham", "Hammersmith", "Fulham", "Kingston", "Richmond"]
        if query == other_names[0] or query == other_names[1]:
            return "Barking and Dagenham"
        elif query == other_names[2] or query == other_names[3]:
            return "Hammersmith and Fulham"
        elif query == other_names[4]:
            return "Kingston upon Thames"
        elif query == other_names[5]:
            return "Richmond upon Thames"
        else:
            return query



    # calculate a classification of pos or neg
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