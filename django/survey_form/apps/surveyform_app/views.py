# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def results(request):
    request.session['name_answer'] = request.POST['name']
    request.session['location_answer'] = request.POST['location']
    request.session['language_answer'] = request.POST['language']
    request.session['comment_answer'] = request.POST['comment']
    return render(request, 'results.html')
