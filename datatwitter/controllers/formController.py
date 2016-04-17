# control the forms input in the views of the application (each of these do different things and some of them are only needed for the Proof of Concept page)
from django import forms
from ..models import Dataset


class TwitterForm(forms.Form):
    # search_query = forms.CharField(label="query", max_length=100)
    borough_choices = (("Barking and Dagenham", "Barking and Dagenham"),
                       ("Barnet", "Barnet"),
                       ("Bexley", "Bexley"),
                       ("Brent", "Bromley"),
                       ("Camden", "Camden"),
                       ("Croydon", "Croydon"),
                       ("Ealing", "Ealing"),
                       ("Enfield", "Enfield"),
                       ("Greenwich", "Greenwich"),
                       ("Hackney", "Hackney"),
                       ("Hammersmith", "Hammersmith"),
                       ("Fulham", "Fulham"),
                       ("Haringey", "Haringey"),
                       ("Harrow", "Harrow"),
                       ("Hillingdon", "Hillingdon"),
                       ("Hounslow", "Hounslow"),
                       ("Islington", "Islington"),
                       ("Kensington", "Kensington"),
                       ("Chelsea", "Chelsea"),
                       ("Kingston", "Kingston"),
                       ("Lambeth", "Lambeth"),
                       ("Lewisham", "Lewisham"),
                       ("Merton", "Merton"),
                       ("Newham", "Newham"),
                       ("Redbridge", "Redbridge"),
                       ("Richmond", "Richmond"),
                       ("Southwark", "Southwark"),
                       ("Sutton", "Sutton"),
                       ("Tower Hamlets", "Tower Hamlets"),
                       ("Waltham Forest", "Waltham Forest"),
                       ("Wandsworth", "Wandsworth"),
                       ("Westminster", "Westminster"),
                       )
    search_query = forms.ChoiceField(label="query", choices=borough_choices)
# analyse a line of code
class SentimentForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)
# Analyse a twitter query
class SentimentTwitterForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)
# analyse a dataset
class SentimentDatasetForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
# Upload a file
class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
# Remove a file
class RemoveFileForm(forms.Form):
    file = forms.ModelChoiceField(queryset=Dataset.objects.all())
# Compare an uploaded file and a query
class ComparisonForm(forms.Form):
    file = forms.HiddenInput()
    query = forms.HiddenInput()
