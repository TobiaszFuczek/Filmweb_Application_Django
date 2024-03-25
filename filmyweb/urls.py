from filmyweb.views import wszystkie_filmy, nowy_film
from django.urls import path

urlpatterns = [
    path('wszystkie/', wszystkie_filmy),
    path('nowy/', nowy_film),
    ]