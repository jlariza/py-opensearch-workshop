from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from .forms import SearchPokemonForm
from .models import Pokemon


# Create your views here.
class PokemonListView(FormMixin, ListView):

    model = Pokemon
    paginate_by = 10  # if pagination is desired
    form_class = SearchPokemonForm
    context_object_name = "pokemons"

    def get_initial(self):
        return self.request.GET

    def get_queryset(self) -> QuerySet[Any]:
        form = SearchPokemonForm(self.request.GET)
        queryset = super().get_queryset()
        if form.is_valid():
            data = form.cleaned_data
            queryset = queryset.filter(name__icontains=data["name"])
        return queryset
