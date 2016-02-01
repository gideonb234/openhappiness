# control the forms in pages
from django import forms

class TwitterForm(forms.Form):
    search_query = forms.CharField(label="query", max_length=100)