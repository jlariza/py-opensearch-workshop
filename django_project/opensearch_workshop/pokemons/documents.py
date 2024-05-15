from django_opensearch_dsl import Document, fields
from django_opensearch_dsl.registries import registry
from .models import Pokemon


@registry.register_document
class PokemonDocument(Document):
    class Django:
        model = Pokemon
        fields = [
            "pokemon_id",
            "name",
        ]

    class Index:
        name = "pokemons"  # Name of the Opensearch index
