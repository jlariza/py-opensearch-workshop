from typing import Any

from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from opensearchpy.helpers.query import Q

from .documents import PokemonDocument
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
            name = data["name"]
            query = Q(
                "bool",
                should=[
                    Q("query_string", query=f"*{name}*", fields=["name"]),
                    Q(
                        "nested",
                        path="types",
                        query=Q(
                            "query_string", query=f"*{name}*", fields=["types.name"]
                        ),
                    ),
                    Q(
                        "nested",
                        path="moves",
                        query=Q(
                            "query_string", query=f"*{name}*", fields=["moves.name"]
                        ),
                    ),
                    Q(
                        "nested",
                        path="abilities",
                        query=Q(
                            "query_string", query=f"*{name}*", fields=["abilities.name"]
                        ),
                    ),
                ],
                minimum_should_match=1,
            )
            os_query = (
                PokemonDocument.search()
                .query(query)
                .sort("pokemon_id")
                # los resultados de opensearch se deben paginar
                # pero está fuera del scope de este taller
                .extra(size=1000, track_total_hits=True)
            )
            queryset = os_query.to_queryset()
        return queryset
