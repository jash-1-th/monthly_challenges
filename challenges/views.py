from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponseNotFound, HttpResponse


def challengeshome(request, month):
    challenges_text = "jash hello"
    if month == "january":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "february":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "march":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "april":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "may":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "june":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "july":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "august":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "september":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "october":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "november":
        challenges_text = "hello jash welcome , push yourself"
    elif month == "december":
        challenges_text = "hello jash welcome , push yourself"
    else:
        return HttpResponseNotFound("ledra babai")
    return HttpResponse(challenges_text)
