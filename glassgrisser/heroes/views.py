from django.http import HttpResponse
from django.shortcuts import render


def heroes_table(request):
    return HttpResponse("Placeholder")


def hero_page(request, hero_name):
    return HttpResponse(f"hero {hero_name} placeholder")
