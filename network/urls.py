from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.network, name = 'network'),
]
