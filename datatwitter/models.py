from django.db import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib.postgres.fields import ArrayField
import json

# Create your models here.

# class Dataset (models.Model):

# Save tweets to here
class Tweets (models.Model):
    tweet_text = ArrayField(models.IntegerField(),size=100, default=[1,2,3,4], blank=True)
# define a place for file storage
fs = FileSystemStorage(location='/datatwitter/files/')

# keeps a track of datasets saved to the server
class Dataset(models.Model):
    # define a file path for the data to be stored in
    def content_name(self, filename):
        return '/'.join(['datasets', self.file_title, filename])

    file_title = models.TextField(max_length=100, default="Untitled")
    fs = FileSystemStorage()
    file_path = models.FileField(upload_to=content_name, storage=fs)

    # this is what it Dataset returns when it is called by other functions
    def __str__(self):
        return self.file_title

    # upload dataset to the server
    def upload(self, file_title, file_path):
        instance = Dataset(file_path=file_path, file_title=file_title)
        instance.save()
        return instance.pk

    # remove dataset from the server
    def remove(self, file_id):
        if file_id == self.objects.get(file_id):
            file = self.objects.get(file_id)
            file.delete()

# store results from comparison (dataset version)
# Major difference is the link to the Dataset model
class DatasetResult(models.Model):
    datetime = datetime.now()
    average = models.BigIntegerField()
    d_range = ArrayField(models.IntegerField(),size=5, default=[1,2,3,4],blank=True)
    median = models.BigIntegerField()
    sentiment = models.TextField(max_length=20)
    dataset = models.ForeignKey(Dataset)
    dataset_sentiment = ArrayField(models.IntegerField(), size=100, default=[1,2,3,4], blank=True)

    # save results to the database server and return the primary key for the instance
    def upload(self, dataset_result):
        instance = DatasetResult(average=dataset_result[1], d_range=dataset_result[2], median=dataset_result[3],
                                 sentiment=dataset_result[0], dataset_id=dataset_result[4])
        instance.save()
        return instance.pk

# store results from comparison (twitter query version)
# Major difference is able to save the query and the tweets from it
class QueryResult(models.Model):
    datetime = datetime.now()
    average = models.BigIntegerField()
    d_range = ArrayField(models.IntegerField(),size=5, default=[1,2,3,4],blank=True)
    twitter_sentiment = ArrayField(models.IntegerField(),size=100, default=[1,2,3,4],blank=True)
    median = models.BigIntegerField()
    sentiment = models.CharField(max_length=20)
    twitter_query = models.CharField(max_length=100)
    twitter_fk = models.ForeignKey(Tweets, null=True)
    # save results to the database server and return the primary key for the instance
    def upload(self, query_result):
        instance = QueryResult(average=query_result[1], d_range=query_result[2], median=query_result[3],
                               sentiment=query_result[0], twitter_query=query_result[4])
        instance.save()
        return instance.pk
