from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from datatwitter.controllers import twitterController
# Create your views here.

def index(request):
    # return "hello world"
    return render(request, 'datatwitter/static/index.html')

def poc(request):
    twitter_poc = twitterController.TwitterController()
    return render(request, 'datatwitter/static/poc.html')
