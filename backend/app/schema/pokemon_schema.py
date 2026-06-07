from datetime import datetime

from pydantic import BaseModel

class PokemonData(BaseModel):
  pokemon_id: int
  name: str
  sprite_url: str
  types: list[str]

class PokemonCacheResponse(BaseModel):
  db_id: int
  name: str
  pokemon_id: int
  sprite_url: str
  types: list[str]
  #created_at: datetime
  #updated_at: datetime