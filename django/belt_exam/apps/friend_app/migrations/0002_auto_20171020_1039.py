# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='friends',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
