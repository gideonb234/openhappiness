# import all the libraries required by the views page in order to run
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .controllers.formController import *
from .controllers.twitterController import TwitterController
from .controllers.sentimentController import SentimentController
from .controllers.fileController import FileController
from .controllers.comparisonController import ComparisonController
from .controllers.visualisationController import VisualisationController
import json
# Create your views here.

from .models import Dataset

# Index page
# Render the index page, it's as simple as that
def index(request):
    # return "hello world"
    return render(request, 'datatwitter/index.html')

# this entire page (poc) is just a test page for all of the functions I need for the site

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


# View a dataset given a dataset id
def dataset(request, dataset_id):
    try:
        dataset = get_object_or_404(Dataset, pk=dataset_id)
        file = dataset.file_path.open()
        parsed_json = json.loads(str(file))
        print(parsed_json)
    except Dataset.DoesNotExist:
        raise Http404("Dataset does not exist")
    return render(request, 'datatwitter/dataset-view.html', {'dataset': dataset, 'file': file})

# Upload a dataset using this page (this is the only reason the python requires sudo)
def dataset_upload(request):
    if request.method == 'POST':
        if request.POST['form-type'] == 'dataset-form':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = Dataset.upload(0, request.POST['title'], request.FILES['file'])
                request.session['file'] = file
                print(request.session['file'])
                return HttpResponseRedirect('/twitter',{"twitter_form": TwitterForm, "file": file})
    return render(request, 'datatwitter/dataset.html', {'dataset_form': UploadFileForm})

# Twitter query
# Select a London borough from here (can also be a text box query depending on what is chosen in Forms Controller)
def twitter_query(request):
    file = request.session['file']
    if request.method == 'POST':
        print('hit1')
        if request.POST['form-type'] == 'twitter-form':
            print('hit2')
            form = TwitterForm(request.POST)
            if form.is_valid():
                print('hit3')
                tweet = TwitterController()
                tweet.search_query(request.POST['search_query'])
                request.session['search_query'] = request.POST['search_query']
                return HttpResponseRedirect('/comparison')
    return render(request, 'datatwitter/twitter-upload.html', {'twitter_form': TwitterForm, "file": file })

# Output Page
# Outputs the compared data into a variable which can then be read by JS and used to generate a chart using
# Google Charts API
def output_view(request):
    file_result = request.session['file_result']
    twitter_result = request.session['twitter_result']
    comparison_data = request.session['comparison_data']
    vis_con = VisualisationController()
    cleaned_file_result = vis_con.removeStringsFromData(file_result)
    cleaned_twitter_result = vis_con.removeStringsFromData(twitter_result)
    return render(request,'datatwitter/output.html',{"file_result": cleaned_file_result,
                                                     "twitter_result": cleaned_twitter_result,
                                                     "comparison_data_file": comparison_data[0],
                                                     "comparison_data_twitter": comparison_data[1],
                                                     "final_comparison": comparison_data[2]})

# The view for the comparison
# Generates the comparison data and passes it to the output page where JS will then render a chart
# This will also allow for the user to select a type of analysis in the future (probs not for disso)
def comparison(request):
    if request.method == "POST":
        if request.POST['form-type'] == 'comparison-form':
            form = ComparisonForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.session['file']
                query = request.session['search_query']
                fc = FileController()
                opened_file = fc.open_file_id(file)
                # print(opened_file)
                sentiment = SentimentController()
                file_result = sentiment.analyse_dataset(opened_file, file)
                twitter_result = sentiment.analyse_twitter(query)
                request.session['file_result'] = file_result
                request.session['twitter_result'] = twitter_result
                compare = ComparisonController()
                request.session['comparison_data'] = compare.compare_against_data(file_result, twitter_result)
            return HttpResponseRedirect('/visualisation')
    return render(request, 'datatwitter/comparison.html', {'comparsion_form': ComparisonForm})

# Visualisation Select
# Lets the user pick a visualisation select (actually allowing the user to select a visualisation is still to do)
def visualisation_select(request):
    file_result = request.session['file_result']
    twitter_result = request.session['twitter_result']
    comparison_data = request.session['comparison_data']
    return render(request,'datatwitter/visualisation-select.html',{"file_result": file_result,
                                                                   "twitter_result": twitter_result,
                                                                   "comparison_data": comparison_data})
