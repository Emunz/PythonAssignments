# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def new(request):
    return render(request, "new.html")

def create(request):
    return redirect(index)

def show(request, digit):
    context = {'number': digit
    }
    return render(request, "blog_num.html", context)

def edit(request, digit):
    context = {'number': digit
    }
    return render(request, "edit.html", context)

def destroy(request, digit):
    context = {'number': digit
    }
    return redirect(index)