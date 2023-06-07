from django.shortcuts import render
from django.http import HttpResponse
def second(request):
    return HttpResponse('<marquee><h1>my second view</h1>></marquee>')

# Create your views here.
