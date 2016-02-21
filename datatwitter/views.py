from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.utils import timezone

from .controllers.formController import *
from .controllers.twitterController import TwitterController
from .controllers.sentimentController import SentimentController
from .controllers.fileController import FileController
# Create your views here.

from .models import Dataset

def index(request):
    # return "hello world"
    return render(request, 'datatwitter/index.html')


def poc(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        if request.POST['form-type'] == 'twitter-form':
            form = TwitterForm(request.POST)
            if form.is_valid():
                tweet = TwitterController()
                tweet.search_query(request.POST['search_query'])
                return HttpResponseRedirect('/datatwitter/poc/')
        elif request.POST['form-type'] == 'dataset-form':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                Dataset.upload(0, request.POST['title'], request.FILES['file'])
                return HttpResponseRedirect('/datatwitter/poc/')
        elif request.POST['form-type'] == 'remove-dataset-form':
            form = RemoveFileForm(request.post,request.FILES)
            if form.is_valid():
                Dataset.get_all()
        elif request.POST['form-type'] == 'sentiment-form':
            form = SentimentForm(request.POST)
            if form.is_valid():
                line = str(request.POST['sentiment_query'])
                sentiment = SentimentController()
                sentiment.analyse_line(line)
                return HttpResponseRedirect('/datatwitter/poc/')
        elif request.POST['form-type'] == 'sentiment-twitter-form':
            form = SentimentTwitterForm(request.POST)
            if form.is_valid():
                line = str(request.POST['sentiment_query'])
                sentiment = SentimentController()
                sentiment.analyse_twitter(line)
                return HttpResponseRedirect('/datatwitter/poc/')
    else:
        form = SentimentForm()
    return render(request, 'datatwitter/static/poc.html', {
        'twitter_form': TwitterForm,
        'dataset_form': UploadFileForm,
        'remove_dataset_form': RemoveFileForm,
        'sentiment_form': SentimentForm,
        'sentiment_twitter_form': SentimentTwitterForm
    })


def file(request, dataset_id):
    return HttpResponse("This is file " % Dataset.view_file(dataset_id))