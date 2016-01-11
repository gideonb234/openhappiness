from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'datatwitter/static/index.html')

