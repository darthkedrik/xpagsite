from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.CastMemberPage.as_view(), name='detail'),
    url(r'^$', views.CastHome.as_view(), name='about'),
]
