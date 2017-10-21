# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import Users
from models import Friends
# Create your views here.

def homepage(request):
    your_friends = Friends.objects.filter(friends_id=request.session['user_id'])
    your_friends_ids = []
    non_friends = []
    for friend in your_friends:
        your_friends_ids.append(friend.user_id)
    users = Users.objects.all()
    for user in users:
        if user.id not in your_friends_ids and user.id != request.session['user_id']:
            non_friends.append(user)
    context = {
        'users': non_friends,
        'friends': your_friends,
    }
    return render(request, 'friend_app/homepage.html', context)

def add_friend(request, user_id):
    this_user = Users.objects.get(id=request.session['user_id'])
    added_friend = Users.objects.get(id=user_id)
    Friends.objects.create(first_name=added_friend.first_name, last_name=added_friend.last_name, user_id=added_friend.id, friends=this_user)
    return redirect('/friends')

def destroy_friend(request, friend_id):
    Friends.objects.get(id=friend_id).delete()
    return redirect('/friends')

def destroy_profile(request, user_id):
    Users.objects.get(id=user_id).delete()
    return redirect('/')
    

def single_user(request, user_id):
    context = {
        'user': Users.objects.get(id=user_id)
    }
    return render(request, 'friend_app/single_user.html', context)



# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

# this_author = Author.objects.get(id=2)
# books = Book.objects.filter(author=this_author)
# one-line version:
# books = Book.objects.filter(author=Author.objects.get(id=2))