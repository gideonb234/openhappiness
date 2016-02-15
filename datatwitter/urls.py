from django.conf.urls import url

from . import views

app_name = "datatwitter"
urlpatterns = [
    url(r'poc/', views.poc, name="poc"),
    url(r'index', views.index, name="index"),
    url(r'$', views.index, name="default"),
]