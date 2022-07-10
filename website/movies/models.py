from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Категории Categories"""
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField(verbose_name='Имя', max_length=100)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='actors/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('movies:actor_detail', kwargs={'slug': self.name})

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'
        ordering = ['name']


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Movie(models.Model):
    """Фильм"""
    title = models.CharField(verbose_name='Название', max_length=100)
    tagline = models.CharField(verbose_name='Слоган', max_length=100, default='')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(verbose_name='Постер', upload_to='movies/')
    year = models.PositiveIntegerField(verbose_name='Дата выхода', default=2022)
    country = models.CharField(verbose_name='Страна', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    world_premiere = models.DateField(verbose_name='Мировая примьера', default=date.today)
    budget = models.PositiveIntegerField(verbose_name='Бюджет', default=0, help_text='сумму указывать в долларах')
    fees_in_usa = models.PositiveIntegerField(
        verbose_name='Сборы в США', default=0, help_text='сумму указывать в долларах'
    )
    fees_in_world = models.PositiveIntegerField(
        verbose_name='Сборы в мире', default=0, help_text='сумму указывать в долларах'
    )
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(verbose_name='Черновик', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title']


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE, related_name='movieshots')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильмов'
        ordering = ['movie']


class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.SmallIntegerField(verbose_name='Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField(verbose_name='IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField(verbose_name='Имя', max_length=100)
    text = models.TextField(verbose_name='Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
