# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Registers(models.Model):
	username = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)

	def __str__(self):
		return self.username


