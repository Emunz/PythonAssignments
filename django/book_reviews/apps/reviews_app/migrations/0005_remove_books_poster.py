# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0004_auto_20171019_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='poster',
        ),
    ]
