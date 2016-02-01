from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .controllers.formController import TwitterForm
from .controllers.twitterController import TwitterController
# Create your views here.

def index(request):
    # return "hello world"
    return render(request, 'datatwitter/static/index.html')

def poc(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = TwitterForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(request.GET)
            tweet = TwitterController()
            tweet.search_query(request.GET['search_query'])
            return HttpResponseRedirect('/datatwitter/poc/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TwitterForm()
    return render(request, 'datatwitter/static/poc.html', {'form': form})