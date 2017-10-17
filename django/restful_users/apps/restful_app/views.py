# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Users

# Create your views here.

def all_users(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request, 'restful_app/all_users.html', context)

def new_user(request):
    return render(request, 'restful_app/new_user.html')

def create_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    Users.objects.create(first_name=first_name, last_name=last_name, email=email)
    
    return redirect(all_users)

def single_user(request, user_id):
    context = {
        'users': Users.objects.get(id=user_id)
    }
    return render(request, 'restful_app/single_user.html', context)

def edit(request, user_id):
    context = {
        'users': Users.objects.get(id=user_id)
    }
    return render(request, 'restful_app/edit_user.html', context)

def edit_user(request, user_id):
    edit = Users.objects.get(id=user_id)
    edit.first_name = request.POST['first_name']
    edit.last_name = request.POST['last_name']
    edit.email =  request.POST['email']
    edit.save()
    return redirect(all_users)

def delete_user(request, user_id):
    Users.objects.get(id=user_id).delete()
    return redirect(all_users)