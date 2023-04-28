from django.urls import path
from .views import *


urlpatterns = [
    path("", heroes_table)
]
