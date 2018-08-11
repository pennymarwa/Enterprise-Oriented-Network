from django.conf.urls import url
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.qa, name = 'qa'),
    url(r'ask_ques/',  views.ask_ques, name = 'ask_ques'),
    url(r'add_ques/',  views.add_ques, name = 'add_ques'),
    url(r'your_ans/',  views.your_ans, name = 'your_ans'),
    # url(r'first_login/',  bootcamp.views.login, name = 'login'),
]
