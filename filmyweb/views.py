from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


def all_films(request):
    #return HttpResponse("This is our first test")
    all = Film.objects.all()
    return render(request, 'filmy.html', {'filmy':all})
@login_required()
def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(all_films)
    return render(request, 'film_form.html', {'form': form})
@login_required()
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect(all_films)
    return render(request, 'film_form.html', {'form': form})
@login_required()
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm.html', {'film': film})