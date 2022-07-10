from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Регистрация модели категорий"""
    save_on_top = True
    save_as = True
    save_as_continue = True

    list_display = ['pk', 'name', 'url']
    list_display_links = ['name']


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Регистрация модели фильмов"""
    save_on_top = True
    save_as = True
    save_as_continue = True

    list_display = ['pk', 'title', 'category', 'url', 'draft']
    list_display_links = ['title']
    list_filter = ['category', 'year']
    search_fields = ['title', 'category__name']
    list_editable = ['draft']
    inlines = [ReviewInline]
    save_as = True
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster")
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "classes": ("collapse",),
            "fields": (("url", "draft"),)
        }),
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Регистрация модели отзывы"""
    list_display = ['pk', 'name', 'email', 'parent', 'movie']
    readonly_fields = ['name', 'email']
    save_on_top = True
    save_as = True
    save_as_continue = True


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Регистрация модели актеров"""
    save_on_top = True
    save_as = True
    save_as_continue = True
    readonly_fields = ['get_image']
    list_display = ['name', 'age', 'get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Регистрация модели жанров"""
    save_on_top = True
    save_as = True
    save_as_continue = True


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Регистрация модели кадры из фильма"""
    save_on_top = True
    save_as = True
    save_as_continue = True


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    """Регистрация модели звезды рейтинга"""
    save_on_top = True
    save_as = True
    save_as_continue = True


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Регистрация модели рейтинга"""
    save_on_top = True
    save_as = True
    save_as_continue = True
    list_display = ['pk', 'movie', 'ip', 'star']
    list_display_links = ['movie']


admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"