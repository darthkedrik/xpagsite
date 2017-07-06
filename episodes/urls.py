from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EpisodeListing.as_view(), name='episodes'),
]
