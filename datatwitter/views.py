from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .controllers.formController import *
from .controllers.twitterController import TwitterController
from .controllers.sentimentController import SentimentController
from .controllers.fileController import FileController
# Create your views here.


def index(request):
    # return "hello world"
    return render(request, './static/index.html')


def poc(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        if request.POST['form-type'] == 'twitter-form':
            # create a form instance and populate it with data from the request:
            form = TwitterForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                tweet = TwitterController()
                tweet.search_query(request.POST['search_query'])
                return HttpResponseRedirect('/datatwitter/poc/')
        elif request.POST['form-type'] == 'dataset-form':
            form = UploadFileForm(request.POST, request.FILES)
            print("hit me")
            if form.is_valid():
                print("hit you")
                fileconn = FileController(request.POST['title'])
                # fileconn.handle_file_upload(request.FILES['file'])
                return HttpResponseRedirect('/datatwitter/poc/')
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
    # if a GET (or any other method) we'll create a blank form
    # if request.method == 'GET':
    #     form = SentimentForm(request.GET)
    #     if form.is_valid():
    #         print(request.GET)
    #         analysis = Sentiment()
    #         analysis.request.GET['sentiment']
    #         return HttpResponseRedirect('/datatwitter/poc')
    else:
        form = SentimentForm()
    return render(request, 'datatwitter/static/poc.html', {
        'twitter_form': TwitterForm,
        'dataset_form': UploadFileForm,
        'sentiment_form': SentimentForm,
        'sentiment_twitter_form': SentimentTwitterForm})