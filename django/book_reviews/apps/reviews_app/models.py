# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import Users

# Create your models here.

class BookManager(models.Manager):
    def review_validation(self, postData):
        errors = []
        if len(postData['title']) < 1:
            errors.append('Please enter a book title')
        if len(postData['author']) < 1:
            errors.append('Please enter an author')
        if len(postData['review']) < 1:
            errors.append('Please enter a review')
        return errors

        
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    # poster = models.ForeignKey('login_app.Users')
    objects=BookManager()
