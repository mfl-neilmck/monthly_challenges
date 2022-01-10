from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Eat no meat in " + month
    elif month == 'february':
        challenge_text = "did you eat no meat in  " + month
    else:
        return HttpResponseNotFound("This is not a real month")

    return HttpResponse(challenge_text)

def january(request):
    return HttpResponse("This kinda works")

def february(request):
    return HttpResponse("Walk for at least 20 feet e everyday")
