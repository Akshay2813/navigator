from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def navigator(request):
    return HttpResponse("Navigtor PAGE")
