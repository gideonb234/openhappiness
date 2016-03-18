# Facilitate comparison between datasets and Twitter data

from ..models import DatasetResult, QueryResult
from statistics import median

class ComparisonController:
    def __init__(self):
        return

    def compare_against_data(self,dataset_result,twitter_result):
        # Take the two results and compare the results to see which one is more positive/negative and generate average, range and median for each
        # Then compare the sentiment to each other to see which if both are pos/neg or if they differ and where
        # Lastly save each completed comparison to the database (result table)
        dataset_average = self.generate_average(dataset_result[3])
        dataset_range = self.generate_range(dataset_result[3])
        dataset_median = self.generate_median(dataset_result[3])
        dataset_sentiment = self.calc_sentiment(dataset_result[3])
        dataset_completed_comparison = [dataset_sentiment, dataset_average, dataset_range, dataset_median]
        query_average = self.generate_average(twitter_result[3])
        query_range = self.generate_range(twitter_result[3])
        query_median = self.generate_median(twitter_result[3])
        query_sentiment = self.calc_sentiment(twitter_result[3])
        query_completed_comparison = [query_sentiment, query_average, query_range, query_median]
        compare_sentiment = self.compare_final_comparisons(dataset_sentiment, query_sentiment)
        self.save_comparison(dataset_completed_comparison)
        self.save_comparison(query_completed_comparison)
        return ":)"

    def save_comparison(self,completed_comparison):
        # This just adds the completed comparison to the database and returns an id for it

        return completed_comparison

    def generate_average(self, result):
        count = len(result)
        total_pos = 0
        total_neg = 0
        for r in result:
            total_pos += r[1]
            total_neg += r[2]
        avg_pos = total_pos / count
        avg_neg = total_neg / count
        avg = avg_pos + avg_neg / count
        return avg

    def generate_range(self, result):
        max_pos = 0
        max_neg = 0
        min_pos = result[0][1]
        min_neg = result[0][2]
        for r in result:
            if r[1] > max_pos:
                max_pos = r[1]
            elif min_pos > r[1]:
                min_pos = r[1]
            if r[2] > max_neg:
                max_neg = r[2]
            elif min_neg > r[2]:
                min_neg = r[2]
        if min_neg < min_pos:
            min = min_neg
        else:
            min = min_pos
        if max_neg > max_pos:
            max = max_neg
        else:
            max = max_pos
        total_range = [max, min]
        return total_range

    def generate_median(self, result):
        # generate separate lists for pos/neg then use median function from statistics library to calc median
        pos_list = []
        neg_list = []
        for r in result:
            pos_list.append(r[1])
            neg_list.append(r[2])
        pos_median = median(pos_list)
        neg_median = median(neg_list)
        print(pos_median)
        print(neg_median)
        final_median = median([pos_median, neg_median])
        return final_median

    def calc_sentiment(self, result):
        neg = 0
        pos = 0
        for r in result:
            neg += r[2]
            pos += r[1]
        if neg > pos:
            return "Negative"
        elif pos > neg:
            return "Positive"
        elif pos == neg:
            return "Literally 50/50"

    def compare_final_comparisons(self, result_dataset, result_query):
        dataset_sentiment = result_dataset[0]
        query_sentiment = result_query[0]
        final_string = ""
        if dataset_sentiment == query_sentiment:
            final_string = "Final results show that both the dataset and twitter query are of " + result_dataset[0] + " sentiment."
        elif dataset_sentiment != query_sentiment:
            final_string = "Final results show that the dataset is of " + result_dataset[0] + "sentiment and that the query is of " + \
                            result_query[0] + "sentiment."
        return final_string
