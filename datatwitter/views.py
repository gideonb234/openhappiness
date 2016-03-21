from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms
from .controllers.formController import *
from .controllers.twitterController import TwitterController
from .controllers.sentimentController import SentimentController
from .controllers.fileController import FileController
from .controllers.comparisonController import ComparisonController
import json
# Create your views here.

from .models import Dataset

def index(request):
    # return "hello world"
    return render(request, 'datatwitter/index.html')


# def poc(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         print(request.POST)
#         if request.POST['form-type'] == 'twitter-form':
#             form = TwitterForm(request.POST)
#             if form.is_valid():
#                 tweet = TwitterController()
#                 tweet.search_query(request.POST['search_query'])
#                 return HttpResponseRedirect('/datatwitter/poc/')
#         elif request.POST['form-type'] == 'dataset-form':
#             form = UploadFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 Dataset.upload(0, request.POST['title'], request.FILES['file'])
#                 return HttpResponseRedirect('/datatwitter/poc/')
#         elif request.POST['form-type'] == 'remove-dataset-form':
#             form = RemoveFileForm(request.POST, request.FILES)
#             if form.is_valid():
#                 print(request.POST['file'])
#                 Dataset.remove(request.POST['file'])
#         elif request.POST['form-type'] == 'sentiment-form':
#             form = SentimentForm(request.POST)
#             if form.is_valid():
#                 line = str(request.POST['sentiment_query'])
#                 sentiment = SentimentController()
#                 sentiment.analyse_line(line)
#                 return HttpResponseRedirect('/datatwitter/poc/')
#         elif request.POST['form-type'] == 'sentiment-twitter-form':
#             form = SentimentTwitterForm(request.POST)
#             if form.is_valid():
#                 line = str(request.POST['sentiment_query'])
#                 sentiment = SentimentController()
#                 sentiment.analyse_twitter(line)
#                 return HttpResponseRedirect('/datatwitter/poc/')
#         elif request.POST['form-type'] == 'sentiment-dataset-form':
#             form = SentimentDatasetForm(request.POST, request.FILES)
#             if form.is_valid():
#                 # print("im valid")
#                 file = request.FILES['file']
#                 # print(type(file))
#                 fc = FileController()
#                 saved_file = Dataset.upload(0, request.POST['title'], request.FILES['file'])
#                 opened_file = fc.open_file(file, saved_file)
#                 print(opened_file)
#                 sentiment = SentimentController()
#                 sentiment.analyse_dataset(opened_file)
#                 return HttpResponseRedirect('/datatwitter/poc')
#         elif request.POST['form-type'] == 'comparison-form':
#             form = ComparisonForm(request.POST, request.FILES)
#             if form.is_valid():
#                 file = request.POST['file']
#                 fc = FileController()
#                 opened_file = fc.open_file_id(file)
#                 # print(opened_file)
#                 sentiment = SentimentController()
#                 file_result = sentiment.analyse_dataset(opened_file, file)
#                 twitter_result = sentiment.analyse_twitter(request.POST['query'])
#                 compare = ComparisonController()
#                 compare.compare_against_data(file_result, twitter_result)
#                 return HttpResponseRedirect('/poc')
#     else:
#         form = SentimentForm()
#     return render(request, 'datatwitter/static/poc.html', {
#         'twitter_form': TwitterForm,
#         'dataset_form': UploadFileForm,
#         'remove_dataset_form': RemoveFileForm,
#         'sentiment_form': SentimentForm,
#         'sentiment_twitter_form': SentimentTwitterForm,
#         'sentiment_dataset_form': SentimentDatasetForm,
#         'comparison_form': ComparisonForm,
#     })


def dataset(request, dataset_id):
    try:
        dataset = get_object_or_404(Dataset, pk=dataset_id)
        file = dataset.file_path.open()
        parsed_json = json.loads(str(file))
        print(parsed_json)
    except Dataset.DoesNotExist:
        raise Http404("Dataset does not exist")
    return render(request, 'datatwitter/dataset-view.html', {'dataset': dataset, 'file': file})

def dataset_upload(request):
    if request.method == 'POST':
        if request.POST['form-type'] == 'dataset-form':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = Dataset.upload(0, request.POST['title'], request.FILES['file'])
                return HttpResponseRedirect('/twitter', {"twitter_form" : TwitterForm, "file": file})
    return render(request, 'datatwitter/dataset.html', {'dataset_form': UploadFileForm})

def twitter_query(request):
    return render(request, 'datatwitter/twitter-upload.html')

def output_view(request):
    return render(request, 'datatwitter/output.html')

def comparison(request):
    return render(request, 'datatwitter/comparison.html')