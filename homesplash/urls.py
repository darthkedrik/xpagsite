from django.conf.urls import url
from homesplash import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]
