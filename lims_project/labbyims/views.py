# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the home page.")