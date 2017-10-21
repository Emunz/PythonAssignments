# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
import bcrypt
from django.contrib import messages
from models import Users
# Create your views here.

def index(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'login_app/index.html', context)

def registration(request):
    errors = Users.objects.registration_validation(request.POST)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    email = request.POST['email']
    password = request.POST['password']
    if len(errors):
        for error in errors:
            messages.warning(request, error)
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))
        Users.objects.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=hashed_password)
        user_login = Users.objects.get(email=email)
        request.session['name'] = user_login.first_name
        request.session['user_id'] = user_login.id
        return redirect(reverse('reviews:homepage'))
    

def login(request):
    errors = Users.objects.login_validation(request.POST)
    password = request.POST['password']
    try:
        user_login = Users.objects.get(email=request.POST['email'])
    except Exception:
        errors.append('Email not in our database')
        for error in errors:
            messages.warning(request, error)
        return redirect('/')

    password_check = bcrypt.checkpw(password.encode(), user_login.password.encode())

    if password_check == True:
        request.session['name'] = user_login.first_name
        request.session['user_id'] = user_login.id
        return redirect(reverse('reviews:homepage'))
    else:
        errors.append('Email/Password is incorrect')
        for error in errors:
            messages.warning(request, error)
        return redirect('/')

def logout(request):
    request.session['name'] = ''
    return redirect('/')

# $2b$12$nmLxzfTq2Ixi7Hi39hpG.unJPRxdcnvWw57KAZOJbTWAnulB17ZCe