from django.shortcuts import render
from .models import Movie

# Create your views here.

def dy(request):
    movies = Movie.objects.all()
    return render(request, "blog/dy.html", {"movies": movies})


