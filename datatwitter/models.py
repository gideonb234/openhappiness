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


class Files(models.Model):
    file_title = models.TextField(max_length=100, default="Untitled")
    file_path = models.FileField(upload_to="%y%m%d/%f", storage=fs)
