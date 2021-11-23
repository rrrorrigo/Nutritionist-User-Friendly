from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """render Home page"""
    return HttpResponse("Hello world")
    