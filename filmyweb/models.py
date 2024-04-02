#Tu przechowujemy rzeczy które są w Naszej bazie danych. Np. Filmy, produkty etc.
from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4,decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    additional = models.OneToOneField("AdditionalInfo", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)

class AdditionalInfo(models.Model):
    GENRE = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Comedy'),
        (3, 'Sc-Fi'),
        (4, 'Drama'),
    }

    duration = models.PositiveSmallIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)

class Rate(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    films = models.ManyToManyField(Film)


