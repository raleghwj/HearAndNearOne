#-*- coding: UTF-8 -*-

from django.conf.urls import patterns, url
from Users.views import Users_Register, Users_LogIn, Users_LogOut, Users_CheckUsers


urlpatterns = patterns('',
    url(r'^register/$', Users_Register,name = 'register'),
    url(r'^login/$', Users_LogIn, name='login'),
    url(r'^logout/$', Users_LogOut, name='logout'),
    url(r'^check/(username)$', Users_CheckUsers, name='CheckUsers'),
)