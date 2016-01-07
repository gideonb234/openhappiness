from django.db import models
from datetime import datetime

# Create your models here.

# class Dataset (models.Model):

class Tweet (models.Model):
    tweet_id = "id" #foreign key
    tweet_text = "tweet"
    tweet_datetime = "datetime"
    tweet_location = "location" #can be nulled

class Twitter (models.Model):
    tweet = Tweet.tweet_id
    datetime = datetime.now()
