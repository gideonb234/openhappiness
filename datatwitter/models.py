from django.db import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your models here.

# class Dataset (models.Model):


class Tweet (models.Model):
    tweet_id = "id" #foreign key
    tweet_text = "tweet"
    tweet_datetime = "datetime"
    tweet_location = "location" #can be nulled


class Twitter (models.Model):
    tweet = models.ForeignKey(Tweet, default="00")
    datetime = datetime.now()

fs = FileSystemStorage(location='/datatwitter/files/')


class Dataset(models.Model):
    def content_name(self, filename):
        return '/'.join(['datasets', self.file_title, filename])

    file_title = models.TextField(max_length=100, default="Untitled")
    fs = FileSystemStorage()
    file_path = models.FileField(upload_to=content_name, storage=fs)

    def __str__(self):
        return self.file_title

    def upload(self, file_title, file_path):
        instance = Dataset(file_path=file_path, file_title=file_title)
        instance.save()
        return instance.pk

    def remove(self, file_id):
        if file_id == self.objects.get(file_id):
            file = self.objects.get(file_id)
            file.delete()


class DatasetResult(models.Model):
    datetime = datetime.now()
    average = models.BigIntegerField()
    d_range = [models.IntegerField()]
    median = models.BigIntegerField()
    sentiment = models.TextField(max_length=20)
    dataset = models.ForeignKey(Dataset)

    def upload(self, dataset_result):
        # saves dataset result to the database
        # Range is converted to [x] in order to be stored inside the list
        instance = DatasetResult(average=dataset_result[1], d_range=dataset_result[2], median=dataset_result[3],
                                 sentiment=dataset_result[0], dataset_id=dataset_result[4])
        instance.save()
        return instance.pk

class QueryResult(models.Model):
    datetime = datetime.now()
    average = models.BigIntegerField()
    q_range = [models.IntegerField()]
    median = models.BigIntegerField()
    sentiment = models.TextField(max_length=20)
    query = models.TextField(max_length=100)

    def upload(self, query_result):
        instance = query_result(average=query_result[1], q_range=query_result[2], median=query_result[3],
                                sentiment=query_result[0], query=query_result[4])
        instance.save()
        return instance.pk
