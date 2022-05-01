from django.shortcuts import render, redirect


def home(request):
    return render(request, 'main/home.html', {})


def about(request):
    return render(request, 'main/about.html', {})

