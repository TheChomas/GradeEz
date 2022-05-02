from django.http import HttpResponse
from django.shortcuts import render
from decouple import config

# Create your views here.


def home(request):
    return HttpResponse(config("EMAIL_USERNAME"))
