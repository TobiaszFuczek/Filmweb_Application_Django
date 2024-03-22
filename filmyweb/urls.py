from filmyweb.views import wszystkie_filmy
from django.urls import path


urlpatterns = [
    path('wszystkie/', wszystkie_filmy)
    ]