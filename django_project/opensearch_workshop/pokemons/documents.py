from django_opensearch_dsl import Document, fields
from django_opensearch_dsl.registries import registry

from .models import Pokemon


@registry.register_document
class PokemonDocument(Document):

    types = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "name": fields.TextField(),
        }
    )
    moves = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "name": fields.TextField(),
        }
    )
    abilities = fields.NestedField(
        properties={
            "id": fields.IntegerField(),
            "name": fields.TextField(),
        }
    )

    class Django:
        model = Pokemon
        fields = [
            "pokemon_id",
            "name",
        ]

    class Index:
        name = "pokemons"  # Name of the Opensearch index
