from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'poc', views.poc, name="poc"),
    url(r'index', views.index, name="index"),
    url(r'$', views.index, name="default"),
]