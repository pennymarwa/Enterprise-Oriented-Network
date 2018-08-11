"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'signup/$', views.signup, name = 'signup'),
    url(r'^$', views.login, name = 'login'),
    url(r'bootcamp/$', views.bootcamp, name = 'bootcamp'),
    url(r'logout/', views.logout, name = 'logout'),
    url(r'check/', views.check, name = 'check'),
    url(r'register/', views.register, name = 'register'),
    url(r'^(?P<id>[\w\d_.-]+)/feeds/', include('feeds.urls')),
    url(r'^(?P<id>[\w\d_.-]+)/articles/', include('articles.urls')),
    url(r'^(?P<id>[\w\d_.-]+)/network/', include('network.urls')),
    url(r'^(?P<id>[\w\d_.-]+)/qa/', include('qa.urls')),
    url(r'^admin/', admin.site.urls),
]
