from django.db import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from open_happy import settings

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

    def remove(self, file_id):
        if file_id == self.objects.get(file_id):
            file = self.objects.get(file_id)
            file.delete()

    def view_file(self, q_id):
        get_file = Dataset.objects.get(id=q_id)
        return get_file


class Result(models.Model):
    datetime = datetime.now()
    subjecivity = models.BigIntegerField()
    polarity = models.BigIntegerField()
    Dataset = models.ForeignKey(Dataset)
