# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from feeds.models import Registers

# Create your views here.
def network(request, id):
	if request.session.get('login_id'):
		register = Registers.objects.all()
		return render(request, 'network/index.html', {'register': register, 'id':id})
	else:
		return redirect('../bootcamp/')
	# if request.session.get('login_id'):
	# 	return render(request, 'network/index.html')
	# else:
	# 	return render(request, '../bootcamp/login.html')