from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Film, AdditionalInfo, Rate
from .forms import FilmForm, AdditionalInfoForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def all_films(request):
    #return HttpResponse("This is our first test")
    all = Film.objects.all()
    return render(request, 'filmy.html', {'filmy':all})
@login_required()
def new_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_additional = AdditionalInfoForm(request.POST or None)
    if all((form_film.is_valid(), form_additional.is_valid())):
        film = form_film.save(commit=False)
        additional = form_additional.save(commit=False)
        additional.save()
        film.additional = additional
        film.save()
        return redirect(all_films)
    return render(request, 'film_form.html', {'form': form_film, 'form_additional': form_additional, 'nowy':True})
@login_required()
def edit_film(request, id):
    film = get_object_or_404(Film, pk=id)
    rate = Rate.objects.filter(film=film)

    try:
        additional = AdditionalInfo.objects.get(film=film.id)
    except ObjectDoesNotExist:
        additional = None
    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_additional = AdditionalInfoForm(request.POST or None, instance=additional)
    if all((form_film.is_valid(), form_additional.is_valid())):
        film = form_film.save(commit=False)
        additional = form_additional.save(commit=False)
        additional.film = film
        additional.save()
        film.save()
        return redirect(all_films)
    return render(request, 'film_form.html', {'form': form_film, 'form_additional': form_additional, 'rate': rate, 'nowy':False})
@login_required()
def delete_film(request, id):
    film = get_object_or_404(Film, pk=id)
    if request.method == "POST":
        film.delete()
        return redirect(all_films)

    return render(request, 'confirm.html', {'film': film})