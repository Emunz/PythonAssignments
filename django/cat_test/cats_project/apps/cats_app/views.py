# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    print "Made it to index!"
    return render(request, "index.html")

def cat_list(request):
    return render(request, "cat_list.html")