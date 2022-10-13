from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hello jash welcome , push yourself")


def jan(request):
    return HttpResponse("jan")


def feb(request):
    return HttpResponse("feb")


def mar(request):
    return HttpResponse("mar")


def apr(request):
    return HttpResponse("")


def may(request):
    return HttpResponse("")


def jun(request):
    return HttpResponse("")


def jul(request):
    return HttpResponse("jul")


def aug(request):
    return HttpResponse("")


def sep(request):
    return HttpResponse("")


def oct(request):
    return HttpResponse("")


def nov(request):
    return HttpResponse("")


def dec(request):
    return HttpResponse("")
