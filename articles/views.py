# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .form import ArticleForm
from django.shortcuts import render

# Create your views here.
def articles(request, id):
	if request.session.get('login_id'):
		return render(request, 'articles/index.html', {'id':id})
	else:
		return redirect('../bootcamp/')

def post_ar(request, id):
	form = ArticleForm
	return render(request, 'articles/add_post.html', {'id':id, 'form':form })