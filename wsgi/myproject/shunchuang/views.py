#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from shunchuang.kevins import SignModel
from shunchuang.kevins import Index
from shunchuang.kevins import Login
from shunchuang.kevins import Search
from shunchuang.kevins import ClassPage
from shunchuang.kevins import Auction
from shunchuang.kevins import My
from shunchuang.kevins import Editinfo
from shunchuang.kevins import Reply
from shunchuang.kevins import News
from shunchuang.kevins import Crowd

# Create your views here.

def index(request):
    index = Index()
    result = index.index(request)
    return result

def login(request):
    login = Login()
    result = login.login(request)
    return result

def logout(request):
    login = Login()
    result = login.logout(request)
    return result

def create_user(request):
    sign = SignModel()
    result = sign.create_user(request)
    return result

def search(request):
    search = Search()
    result = search.search(request)
    return result

def classpage(request):
    classpage = ClassPage()
    result = classpage.classpage(request)
    return result

def auction(request):
    auction = Auction()
    result = auction.auction(request)
    return result

def my(request):
    my = My()
    result = my.my(request)
    return result

def editinfo(request):
    editinfo = Editinfo()
    result = editinfo.editinfo(request)
    return result

def reply(request):
    reply = Reply()
    result = reply.reply(request)
    return result

def news(request):
    news = News()
    result = news.news(request)
    return result

def crowd(request):
    crowd = Crowd()
    result = crowd.crowd(request)
    return result
