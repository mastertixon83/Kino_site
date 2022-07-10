from django import template

from movies.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    """Возвращает список категорий"""
    return Category.objects.all()


@register.simple_tag()
def get_rating(movie):
    """Возвращает рейтинг к фильму"""
    print(Movie.objects.get(pk=movie.pk).rating_set.all()[0].star)
    return Movie.objects.get(pk=movie.pk).rating_set.all()[0].star


@register.inclusion_tag('movies/tags/last_movies.html')
def get_last_movies(count=5):
    """Вывод последних добавленных фильмов"""
    movies = Movie.objects.order_by('pk')[:count]
    return {'last_movies': movies}
