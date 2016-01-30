from django.conf.urls import url

from . import views

urlpatterns = [
    # datatwitter
    url(r'poc', views.poc, name="poc"),
    url(r'$', views.index, name="index"),
]