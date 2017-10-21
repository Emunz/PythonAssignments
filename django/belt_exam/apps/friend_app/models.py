# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users

# Create your models here.


class Friends(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    user_id = models.IntegerField(null=True)
    friends = models.ForeignKey(Users, related_name='friends')