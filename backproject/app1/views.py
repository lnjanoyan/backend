from django.shortcuts import render
from django.http import HttpResponse
from .models import Books1, Characters583


# Create your views here.

def home(request):
    return HttpResponse("hello from home page")


def book_list(request):
    books = Books1.objects.all()
    data = str([book.name for book in books])
    return HttpResponse(data, content_type="text/plain")


def character_list(request):
    characters = Characters583.objects.all()
    data = str(
        [f"{character.name} appears in {character.povBooks}" for character in characters])
    return HttpResponse(data, content_type="text/plain")
