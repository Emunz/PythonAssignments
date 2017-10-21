from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^review', views.add_review, name="review"),
    url(r'^create', views.create_review, name="new_review"),
    url(r'^(?P<book_id>\d+)$', views.single_book, name="book_page"),
    url(r'^destroy/(?P<book_id>\d+)$', views.destroy_book)
]
