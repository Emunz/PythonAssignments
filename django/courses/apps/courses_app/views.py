# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Courses

# Create your views here.

def index(request):
    context = {
        'courses': Courses.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create_course(request):
    name = request.POST['course_name']
    desc = request.POST['description']
    Courses.objects.create(name=name, desc=desc)
    return redirect(index)

def delete(request, course_id):
    context = {
        'course': Courses.objects.get(id=course_id)
    }
    return render(request, 'courses_app/delete.html', context)

def destroy(request, course_id):
    Courses.objects.get(id=course_id).delete()
    return redirect(index)