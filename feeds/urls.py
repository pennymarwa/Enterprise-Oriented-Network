from django.conf.urls import url, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.feeds, name = 'feeds'),
]
