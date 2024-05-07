from django.urls import path

from .views import PokemonListView

app_name = "users"
urlpatterns = [
    path("", view=PokemonListView.as_view(), name="list"),
]
