from django.urls import path
from .views import *


urlpatterns = [
    path("", heroes_table, name="heroes"),
    path("<str:hero_name>", hero_page)
]
