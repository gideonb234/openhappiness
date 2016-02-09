from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .controllers.formController import TwitterForm, SentimentForm
from .controllers.twitterController import TwitterController
from .controllers.sentimentController import SentimentController
# Create your views here.


def index(request):
    # return "hello world"
    return render(request, './static/index.html')


def poc(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TwitterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(request.POST)
            tweet = TwitterController()
            tweet.search_query(request.POST['search_query'])
            return HttpResponseRedirect('/datatwitter/poc/search_query')

    # if a GET (or any other method) we'll create a blank form
    # if request.method == 'GET':
    #     form = SentimentForm(request.GET)
    #     if form.is_valid():
    #         print(request.GET)
    #         analysis = Sentiment()
    #         analysis.request.GET['sentiment']
    #         return HttpResponseRedirect('/datatwitter/poc')
    else:
        form = TwitterForm()
    return render(request, 'datatwitter/static/poc.html', {'form': form})

def analyse_words(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            print(request.POST)
            sentiment = SentimentController()
            sentiment.analyse_line(request.POST)
            return HttpResponseRedirect('/datatwitter/poc/analyse_words')
        else:
            form = SentimentForm()
    return render('/datatwitter/static/poc.html', {'form':form})