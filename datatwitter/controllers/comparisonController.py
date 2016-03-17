# Facilitate comparison between datasets and Twitter data

from ..models import Result

class ComparisonController:
    def __init__(self):
        return

    def compare_against_data(self,dataset_result,twitter_result):
        # Take the two results and compare the results to see which one is more positive/negative and generate average, range and median
        dataset_average = self.generate_average(dataset_result)
        dataset_range = self.generate_range(dataset_result)
        dataset_median = self.generate_median(dataset_result)
        dataset_sentiment = self.calc_sentiment(dataset_result)
        dataset_completed_comparison = [dataset_sentiment, dataset_average, dataset_range, dataset_median]
        query_average = self.generate_average(twitter_result)
        query_range = self.generate_range(twitter_result)
        query_median = self.generate_median(twitter_result)
        query_sentiment = self.calc_sentiment(twitter_result)
        query_completed_comparison = [query_sentiment, query_average, query_range, query_median]
        return ":)"

    def save_comparison(self,completed_comparison):
        # This just adds the completed comparison to the database and returns an id for it

        return completed_comparison

    def generate_average(self, result):
        count = len(result)
        total = 0
        for r in result:
            total += r
        avg = total / count
        return avg

    def generate_range(self, result):
        max = 0
        min = result[0]
        for r in result:
            if r > max:
                max = r
            if r < min:
                min = r
        total_range = [max, min]
        return total_range

    def generate_median(self, result):
        return "median"

    def calc_sentiment(self, result):
        neg = 0
        pos = 0
        for r in result:
            neg += result.p_neg
            pos += result.p_pos
        if neg > pos:
            return "Negative"
        elif pos > neg:
            return "Positive"
        elif pos == neg:
            return "Literally 50/50"