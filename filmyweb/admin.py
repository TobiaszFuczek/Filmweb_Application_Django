from django.contrib import admin
from .models import Film, AdditionalInfo, Rate, Actor
# Register your models here.

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["title", "description", "year"]
    #exclude = ["description"]
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ["title"]
    search_fields = ["title", "description"]


admin.site.register(AdditionalInfo)
admin.site.register(Rate)
admin.site.register(Actor)