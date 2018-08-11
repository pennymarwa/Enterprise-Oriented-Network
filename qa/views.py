# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from datetime import datetime

from feeds.models import Registers
from . models import Questions, Answers


# Create your views here.
def qa(request, id):
	if request.session.get('login_id'):
		ques = Questions.objects.all()
		answer = Answers.objects.all()
		return render(request, 'qa/index.html' , {'id':id, 'ques':ques, 'ans':answer})
	else:
		return redirect('../bootcamp/')

def ask_ques(request, id):
	return render(request, 'qa/ask_ques.html' , {'id':id})

def add_ques(request, id):
	ques = Questions.objects.all()
	answer = Answers.objects.all()
	reg = Registers.objects.get(username = id)
	add = Questions(ques_text = request.POST['ques_text'], posted_by = reg, pub_at = datetime.now())
	add.save()
	return render(request, 'qa/index.html' , {'id':id, 'ques':ques, 'ans':answer})

def your_ans(request, id):
	ques = Questions.objects.all()
	answer = Answers.objects.all()
	reg = Registers.objects.get(username = id)
	ques1 = Questions.objects.get(id = request.POST['ques'])
	add = Answers(ques_text = ques1, ans = request.POST['ans'], post_by = reg, pubtime = datetime.now())
	add.save()
	return render(request, 'qa/index.html' , {'id':id, 'ques':ques, 'ans':answer})