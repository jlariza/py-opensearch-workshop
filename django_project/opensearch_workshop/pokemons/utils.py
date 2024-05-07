import requests
from django.conf import settings

from .models import PokeAbility, Pokemon, PokeMove, PokeType


def create_pokemons_from_api():
    url = settings.POKEAPI_URL
    response = requests.get(url, params={"limit": 100})
    data = response.json()
    for pokemon in data["results"]:
        poke_url = pokemon["url"]
        poke_response = requests.get(poke_url)
        poke_data = poke_response.json()
        poke_id = poke_data["id"]
        poke_name = poke_data["name"]
        poke_abilities = [
            PokeAbility.objects.get_or_create(name=ability["ability"]["name"])[0]
            for ability in poke_data["abilities"]
        ]
        poke_moves = [
            PokeMove.objects.get_or_create(name=move["move"]["name"])[0]
            for move in poke_data["moves"]
        ]
        poke_types = [
            PokeType.objects.get_or_create(name=poke_type["type"]["name"])[0]
            for poke_type in poke_data["types"]
        ]
        poke_image = poke_data["sprites"]["front_default"]

        pokemon, _ = Pokemon.objects.get_or_create(
            pokemon_id=poke_id,
            defaults={
                "name": poke_name,
                "image": poke_image,
            },
        )
        pokemon.types.set(poke_types)
        pokemon.moves.set(poke_moves)
        pokemon.abilities.set(poke_abilities)
