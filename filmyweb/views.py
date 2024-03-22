from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Film
def wszystkie_filmy(request):
    #return HttpResponse("This is our first test")
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy':wszystkie})
