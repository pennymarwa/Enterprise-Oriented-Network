# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from feeds.models import Registers

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length = 200)
	ar_text = models.TextField()
	post_by = models.ForeignKey(Registers, on_delete = models.CASCADE, null = True)
	post_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title