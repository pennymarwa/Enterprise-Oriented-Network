# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from feeds.models import Registers
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

# Create your views here.
def bootcamp(request):
	if request.session.get('login_id'):
		return render(request, 'bootcamp/index.html' )
	else:
		return render(request, 'bootcamp/login.html')

def signup(request):
	return render(request, 'bootcamp/signup.html')

def login(request):
	return render(request, 'bootcamp/login.html')

def register(request):
	add = Registers(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
	add.save()
	return render(request, 'bootcamp/login.html')

def check(request):
	try:
		compare = Registers.objects.get(username = request.POST['username'])
		user = request.POST['username']
		password = request.POST['password']
		if user == compare.username and password == compare.password:
			request.session['login_id'] = compare.id
			return render(request, 'bootcamp/index.html' , {'id':compare})
		else:
			return redirect('login')
	except:
		return redirect('login')

def logout(request):
	del request.session['login_id']
	return redirect('login')