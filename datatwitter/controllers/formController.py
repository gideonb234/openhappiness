# control the forms in pages
from django import forms


class TwitterForm(forms.Form):
    search_query = forms.CharField(label="query", max_length=100)


class SentimentForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)


class SentimentTwitterForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)
