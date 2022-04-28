from django.shortcuts import render

def home(request):
    return render(request, 'Site/home.html', {})
    
def library(request):
    return render(request, 'Site/library.html', {})

def about(request):
    return render(request, 'Site/about.html', {})
