# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import Books

# Create your views here.

def homepage(request):
    context = {
        'books': Books.objects.all()
        # 'users_books': Users.reviews.all()
    }
    return render(request, 'reviews_app/homepage.html', context)

def add_review(request):
    return render(request, 'reviews_app/reviews.html')

def create_review(request):
    errors = Books.objects.review_validation(request.POST)
    title = request.POST['title']
    author = request.POST['author']
    review = request.POST['review']
    rating = request.POST['rating']
    if len(errors):
        for error in errors:
            messages.warning(request, error)
        return redirect('/books/review')
    else:
        Books.objects.create(title=title, author=author, review=review, rating=rating)
        return redirect('/books')

def single_book(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id)
    }
    return render(request, 'reviews_app/single_book.html', context)

def destroy_book(request, book_id):
    Books.objects.get(id=book_id).delete()
    return redirect('/books')

