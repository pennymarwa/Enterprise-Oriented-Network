# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def feeds(request, id):
	if request.session.get('login_id'):
		return render(request, 'feeds/index.html' , {'id':id})
	else:
		return redirect('../bootcamp/')