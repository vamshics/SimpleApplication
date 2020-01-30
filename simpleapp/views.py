from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
   text = "<h1><center>welcome to Django Application!</center></h1>"
   vamshi = "<h2>Krishna Racharla</h2>"
   return HttpResponse(text, "<h2>Krishna Racharla</h2>")