# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "Hallo World<br /><a href='/rango/about'>About</a>")


def about(request):
    return HttpResponse(
        "This is the about page <br /><a href ='/rango/'>Home</a>")
