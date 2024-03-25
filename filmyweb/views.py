from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Film
from .forms import FilmForm
def wszystkie_filmy(request):
    #return HttpResponse("This is our first test")
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy':wszystkie})

def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'nowy_film.html', {'form': form})
