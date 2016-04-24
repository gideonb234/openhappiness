# This does URL Routing and is used by django to create custom urls based on the views created

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "datatwitter"

urlpatterns = [
    # url(r'poc', views.poc, name="poc"),
    url(r'index', views.index, name="index"),
    url(r'start', views.dataset_upload, name="dataset"),
    url(r'twitter', views.twitter_query, name="twitter"),
    url(r'comparison', views.comparison, name="comparison"),
    url(r'output', views.output_view, name="output"),
    url(r'visualisation', views.visualisation_select, name="visualisation"),
    url(r'^dataset/(?P<dataset_id>[0-9]+)', views.dataset, name="files"),
    url(r'', views.index, name="default"),
]

