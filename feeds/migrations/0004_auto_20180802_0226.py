# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-02 02:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_delete_hello'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='Registers',
        ),
    ]