from django.urls import path
from .views import *

app_name = 'movies'

urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('add_rating/', AddStarRating.as_view(), name='add_rating'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('json-filter/', JsonFilterMoviesView.as_view(), name='json_filter'),
    path("<slug:slug>/", MovieDetail.as_view(), name="movie_detail"),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", ActorView.as_view(), name="actor_detail"),
]
