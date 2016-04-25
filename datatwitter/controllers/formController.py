# control the forms input in the views of the application
# (each of these do different things and some of them are only needed for the Proof of Concept page)
from django import forms
from ..models import Dataset

# Borough_Choices is used for the JSON dataset
class TwitterForm(forms.Form):
    # search_query = forms.CharField(label="query", max_length=100)
    borough_choices = (("Barking", "Barking"),
                       ("Barnet", "Barnet"),
                       ("Bexley", "Bexley"),
                       ("Brent", "Bromley"),
                       ("Camden", "Camden"),
                       ("Croydon", "Croydon"),
                       ("Dagenham", "Dagenham"),
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
# analyse a line of text using sentiment analysis
class SentimentForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)
# Analyse a twitter query using sentiment analysis
class SentimentTwitterForm(forms.Form):
    sentiment_query = forms.CharField(label="sentiment", max_length=100)
# analyse a dataset using sentiment analysis
class SentimentDatasetForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
# Upload a file to the server
class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
# Compare an uploaded file and a query to each other
# (using hidden input as the inputs are POST/FILES requests from earlier pages)
class ComparisonForm(forms.Form):
    file = forms.HiddenInput()
    query = forms.HiddenInput()
# Allow user to select a visualisation
class VisualisationForm(forms.Form):
    choices = (
        ("box", "Box Plot"),
        ("scatter", "Scatter Graph"),
    )
    visualisation_choice = forms.ChoiceField(label="vis_choice", choices=choices)