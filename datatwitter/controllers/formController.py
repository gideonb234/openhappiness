# control the forms in pages
from django import forms
from ..models import Files

class TwitterForm(forms.Form):
    search_query = forms.CharField(label="query", max_length=100)


class DetailedTwitterForm(forms.Form):
    search_query = forms.CharField(label="query", max_length=100)
    # filters go here


class SentimentForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)


class SentimentTwitterForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class RemoveFileForm(forms.ModelForm):
    class File:
        model = Files
        fields = ['file_title', 'file_path']
    # file = forms.CharField(widget=forms.Select(choices=Files.objects.all()))