# Facilitate comparison between datasets and Twitter data

from ..models import DatasetResult, QueryResult
from statistics import median

class ComparisonController:
    def __init__(self):
        return

    def compare_against_data(self,dataset_result,twitter_result,file_id):
        dataset_result = self.prep_data(dataset_result)
        # Take the two results and compare the results to see which one is more positive/negative and generate average, range and median for each
        # Then compare the sentiment to each other to see which if both are pos/neg or if they differ and where
        # Lastly save each completed comparison to the database (result table)
        dataset_sentiment = self.dataset_calc_sentiment(dataset_result)
        dataset_completed_comparison = [dataset_sentiment, self.dataset_generate_average(dataset_result),
                                        self.dataset_generate_range(dataset_result), self.dataset_generate_median(dataset_result),
                                        file_id]
        query_sentiment = self.twitter_calc_sentiment(twitter_result[3])
        query_completed_comparison = [query_sentiment, self.twitter_generate_average(twitter_result[3]),
                                     self.twitter_generate_range(twitter_result[3]), self.twitter_generate_median(twitter_result[3]),
                                     twitter_result[4]]
        compare_sentiment = self.compare_final_comparisons(dataset_sentiment, query_sentiment)
        self.save_dataset_comparison(dataset_completed_comparison)
        self.save_query_comparison(query_completed_comparison)
        results_to_return = [dataset_completed_comparison, query_completed_comparison, compare_sentiment]
        return results_to_return

    def save_dataset_comparison(self,dataset_comparison):
        # This just adds the completed comparison to the database and returns an id for it
        id = DatasetResult.upload(0, dataset_comparison)
        return id

    def save_query_comparison(self,query_comparison):
        # This just adds the completed comparison to the database and returns an id for it
        id = QueryResult.upload(0, query_comparison)
        return id

    def twitter_generate_average(self, result):
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

    def twitter_generate_range(self, result):
        # create separate max/min values for pos and neg then put all that into a list
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
        total_range = [max_pos, min_pos, max_neg, min_neg]
        return total_range

    def twitter_generate_median(self, result):
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


    def dataset_generate_average(self, result):
        average_total = 0
        for r in result:
            average_total += r[0]
        final_average = average_total / len(result)
        return final_average


    def dataset_generate_range(self, result):
        print(result)
        min_num = 0
        max_num = result[0][1]
        for r in result:
            if r[1] > max_num:
                max_num = r[1]
            elif min_num > r[1]:
                min_num = r[1]
        final_range = [max_num, min_num]
        return final_range


    def dataset_generate_median(self, result):
        num_list = []
        for r in result:
            num_list.append(r[0])
            num_list.append(r[1])
            num_list.append(r[2])
        final_median = median(num_list)
        return final_median


    def dataset_calc_sentiment(self, result):
        neg = 0
        pos = 0
        for r in result:
            if r[1] > 0.75:
                pos += r[1]
            elif r[1] < 0.75:
                neg += r[2]
        if neg > pos:
            return "Negative"
        elif pos > neg:
            return "Positive"
        elif pos == neg:
            return "Literally 50/50"

    def twitter_calc_sentiment(self, result):
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


    # cast data to int and make them below 1
    def prep_data(self, result):
        for r in result:
            r[0] = float(r[0])/10
            r[1] = float(r[1])/10
            r[2] = float(r[2])/10
        return result


    def compare_final_comparisons(self, result_dataset, result_query):
        dataset_sentiment = result_dataset[0]
        query_sentiment = result_query[0]
        final_string = ""
        if dataset_sentiment == query_sentiment:
            final_string = "Final results show that both the dataset and twitter query are of " + result_dataset[0] + " sentiment."
        elif dataset_sentiment != query_sentiment:
            final_string = "Final results show that the dataset is of " + result_dataset[0] + " sentiment and that the query is of " + \
                            result_query[0] + " sentiment."
        return final_string
