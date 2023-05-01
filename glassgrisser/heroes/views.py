from django.http import HttpResponse
from django.shortcuts import render
from .models import *


menu = [
    {"title": "Главная страница", "url_name": "heroes"}
]


def heroes_table(request):
    heroes = Hero.objects.all()
    context = {
        "title": "placeholder",
        "menu": menu,
        "heroes": heroes
    }
    return render(request, "heroes/heroes_table.html", context)


def hero_page(request, hero_url):
    context = {
        "title": hero_url,
        "menu": menu,
        "hero_name": hero_url
    }
    return render(request, "heroes/hero_page.html", context)
