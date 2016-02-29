from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "datatwitter"

urlpatterns = [
    url(r'poc', views.poc, name="poc"),
    url(r'index', views.index, name="index"),
    url(r'^dataset/(?P<dataset_id>[0-9]+)', views.dataset, name="files"),
    url(r'', views.index, name="default"),
]

