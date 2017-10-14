# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string  

# Create your views here.

def index(request):
    return render(request, 'generateword_app/index.html')

def generate(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    request.session['random_word'] = get_random_string(length=14)
    return redirect(index)

def reset(request):
    request.session.clear()
    return redirect(index)