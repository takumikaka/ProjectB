from django.contrib import admin
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "descp", "magnet_url")
    ordering = ["name"]


admin.site.register(Movie, MovieAdmin)
