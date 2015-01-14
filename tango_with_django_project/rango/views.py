from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("home page    \
                        <br/> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("This tutorial has been put together by William Kavanagh 2079532   \
                        <br/> <a href='/rango/'>Index</a>")
