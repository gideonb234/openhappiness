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
    def content_name(instance, filename):
        return '/'.join(['content', instance.file_title, filename])

    file_title = models.TextField(max_length=100, default="Untitled")
    file_path = models.FileField(upload_to=content_name, storage=fs)

    def upload(self, file_title, file_path):
        instance = Dataset(file_path=file_path, file_title=file_title)
        instance.save()

    def view_file(self, q_id):
        if (q_id == Dataset._meta.get_field(self.id)):
            for file in Dataset:
                return str(file) + " hit"