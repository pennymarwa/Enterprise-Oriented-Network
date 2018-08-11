from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.articles, name = 'articles'),
    url(r'post_ar/$',  views.post_ar, name = 'post_ar'),
]
