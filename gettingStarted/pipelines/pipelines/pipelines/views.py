from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'NJK','place':'KTM'}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("About <a href='/'>back</a>")

def details(request):
    return HttpResponse("Details <a href='/'>back</a>")
