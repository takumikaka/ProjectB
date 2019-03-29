from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.

def dy(request):
    movies = Movie.objects.all()
    return render(request, "blog/dy.html", {"movies": movies})

def dy_detail(request, article_id):
    article = get_object_or_404(Movie, id=article_id)
    name = article.name
    return render(request, "blog/dy_detail.html", {"article": article, "name": name})


