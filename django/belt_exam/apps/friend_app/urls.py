from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^/users/(?P<user_id>\d+)$', views.single_user),
    url(r'^/addfriend/(?P<user_id>\d+)$', views.add_friend),
    url(r'^/destroyfriend/(?P<friend_id>\d+)$', views.destroy_friend),
    url(r'^/destroy/(?P<user_id>\d+)$', views.destroy_profile),
    url(r'^', views.homepage),
]


# (?P<user_id>\d+)$'