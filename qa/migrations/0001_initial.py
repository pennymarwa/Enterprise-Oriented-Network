# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-02 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_text', models.CharField(max_length=200)),
                ('posted_by', models.CharField(max_length=200)),
                ('pub_at', models.CharField(max_length=200)),
            ],
        ),
    ]
