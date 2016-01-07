from django.conf.urls import url

from . import views

urlpatterns = [
    # datatwitter
    url(r'$', views.index, name="index"),
]