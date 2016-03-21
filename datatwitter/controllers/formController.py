# control the forms in pages
from django import forms
from ..models import Dataset


class TwitterForm(forms.Form):
    search_query = forms.CharField(label="query", max_length=100)


class DetailedTwitterForm(forms.Form):
    search_query = forms.CharField(label="query", max_length=100)
    # filters go here


class SentimentForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)


class SentimentTwitterForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)


class SentimentDatasetForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


class RemoveFileForm(forms.Form):
    file = forms.ModelChoiceField(queryset=Dataset.objects.all())


class ComparisonForm(forms.Form):
    file = forms.ModelChoiceField(label="dataset", queryset=Dataset.objects.all())
    query = forms.CharField(label="query", max_length=50)