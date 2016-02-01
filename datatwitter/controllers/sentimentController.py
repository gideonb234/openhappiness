# Perform sentiment analysis using an API (currently TextBlob, may change in the future)

from textblob import TextBlob

class Sentiment:

    def analyse_line(self,line):
        blob = TextBlob(line)
        print(blob.sentiment)

    def analyse_dataset(self,dataset):
        return "good"

    def analyse_twitter(self,query):
        return "bad"

    def save_analysis(self,result,database_conn):
        return "saved for your problems later"

senti = Sentiment()
senti.analyse_line("hello world you are amazing!")