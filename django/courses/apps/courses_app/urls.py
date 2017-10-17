from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_course$', views.create_course),
    url(r'^delete/(?P<course_id>\d+)$', views.delete),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy)
]