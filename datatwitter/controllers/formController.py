# control the forms in pages
from django import forms
from ..models import Dataset
from django.core.validators import ValidationError

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
    title = forms.CharField(max_length=50, required=True)

    def validate_file_extension(self):
        import os
        ext = os.path.splittext(self.file)[1]
        valid_extensions = ['.csv', '.json']
        if ext not in valid_extensions:
            raise ValidationError(u'File not supported!')

    file = forms.FileField(validators=[validate_file_extension], required=True)



class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class RemoveFileForm(forms.Form):
    file = forms.ModelChoiceField(queryset=Dataset.objects.all())