from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.all_users),
    url(r'^new$', views.new_user),
    url(r'^user/(?P<user_id>\d+)$', views.single_user),
    url(r'^create_user$', views.create_user),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^edit_user/(?P<user_id>\d+)$', views.edit_user),
    url(r'^delete/(?P<user_id>\d+)$', views.delete_user),
]