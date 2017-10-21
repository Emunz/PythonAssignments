# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import books, authors
# Create your views here.

def index(request):
    print books.objects.all().values()
    print authors.objects.all().values()
    print books.authors.get(id=4)
    return render(request, 'index.html')