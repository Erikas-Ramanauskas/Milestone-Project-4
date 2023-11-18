from django.shortcuts import render


def home(request):
    """"A view to return the index page"""
    return render(request, 'home/home.html')