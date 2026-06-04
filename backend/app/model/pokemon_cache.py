from datetime import datetime
from dataclasses import dataclass

@dataclass
class PokemonCache:
  db_id: int
  name: str
  pokemon_id: int
  sprite_url: str
  types: list[str]
  created_at: datetime
  updated_at: datetime
