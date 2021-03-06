"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from shunchuang import views as shunchuang_views

urlpatterns = [
    url(r'^$', shunchuang_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', shunchuang_views.login),
    url(r'^logout/$', shunchuang_views.logout),
    url(r'^sign/$', shunchuang_views.create_user),
    url(r'^search/$', shunchuang_views.search),
    url(r'^class/$', shunchuang_views.classpage),
    url(r'^auction/$', shunchuang_views.auction),
    url(r'^my/$', shunchuang_views.my),
    url(r'^editinfo/$', shunchuang_views.editinfo),
    url(r'^reply/$', shunchuang_views.reply),
    url(r'^news/$', shunchuang_views.news),
    url(r'^crowd/$', shunchuang_views.crowd),
]
