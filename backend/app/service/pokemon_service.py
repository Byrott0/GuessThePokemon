import random
import requests

from app.core.config import MAX_POKEMON_ID, MIN_POKEMON_ID, POKE_API_BASE_URL
from app.model.pokemon_cache import PokemonCache
from app.repository.pokemon_cache_repository import PokemonCacheRepository


class PokemonService:
    def __init__(self, pokemon_repository: PokemonCacheRepository):
        self.pokemon_repository = pokemon_repository

    def get_pokemon_by_id(self, pokemon_id: int) -> PokemonCache:
        cached_pokemon = self.pokemon_repository.get_by_pokemon_id(pokemon_id)

        if cached_pokemon:
            return cached_pokemon

        pokemon_data = self.fetch_pokemon_from_api(pokemon_id)

        return self.pokemon_repository.cache_pokemon(
            pokemon_id=pokemon_data["id"],
            name=pokemon_data["name"],
            sprite_url=pokemon_data["sprite_url"],
            types=pokemon_data["types"],
        )

    def get_random_pokemon(self) -> PokemonCache:
        pokemon_id = random.randint(MIN_POKEMON_ID, MAX_POKEMON_ID)
        return self.get_pokemon_by_id(pokemon_id)

    def fetch_pokemon_from_api(self, pokemon_id: int) -> dict:
        response = requests.get(
            f"{POKE_API_BASE_URL}/pokemon/{pokemon_id}",
            timeout=10,
        )

        if response.status_code == 404:
            raise ValueError("Pokemon not found")

        response.raise_for_status()
        data = response.json()

        return {
            "id": data["id"],
            "name": data["name"],
            "sprite_url": data["sprites"]["front_default"],
            "types": [pokemon_type["type"]["name"] for pokemon_type in data["types"]],
        }
