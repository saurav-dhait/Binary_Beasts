from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


def home(request):
    return render(request, "index/home.html")


def about(request):
    return render(request, "index/about.html")


def chatbot(request):
    return render(request, "index/chatbot.html")
