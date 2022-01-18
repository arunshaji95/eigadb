from django.contrib import admin

from movies.models import Actor, Genre, Language, Movie

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Movie)
