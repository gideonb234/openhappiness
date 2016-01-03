from django.conf.urls import url

from . import views

urlpatterns = [
    #/static
    url(r'^$', views.index, name="static/"),
]