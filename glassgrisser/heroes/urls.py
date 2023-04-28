from django.urls import path
from .views import *


urlpatterns = [
    path("", heroes_table),
    path("<str:hero_name>", hero_page)
]
