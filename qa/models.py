# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from feeds.models import Registers

# Create your models here.

class Questions(models.Model):
	ques_text = models.CharField(max_length = 200)
	posted_by = models.ForeignKey(Registers, on_delete = models.CASCADE, null = True)
	pub_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.ques_text


class Answers(models.Model):
	ques_text = models.ForeignKey(Questions, on_delete = models.CASCADE, null = True)
	ans = models.CharField(max_length = 200)
	post_by = models.ForeignKey(Registers, on_delete = models.CASCADE, null = True)
	pubtime = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.ans
		