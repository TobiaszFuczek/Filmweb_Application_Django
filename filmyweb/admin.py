from django.contrib import admin
from .models import Film
# Register your models here.

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["title", "description", "year"]
    #exclude = ["description"]
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ["title"]
    search_fields = ["title", "description"]


