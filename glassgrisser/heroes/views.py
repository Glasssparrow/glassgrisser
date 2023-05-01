from django.http import HttpResponse
from django.shortcuts import render
from .models import *


menu = ["Главная страница", "123"]


def heroes_table(request):
    heroes = Hero.objects.all()
    arguments = {
        "title": "placeholder",
        "menu": menu,
        "heroes": heroes
    }
    return render(request, "heroes/heroes_table.html", arguments)


def hero_page(request, hero_name):
    arguments = {
        "title": hero_name,
        "menu": menu,
        "hero_name": hero_name
    }
    return render(request, "heroes/hero_page.html", arguments)
