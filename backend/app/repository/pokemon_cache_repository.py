from sqlalchemy.orm import Session
from app.model.pokemon_cache import PokemonCache

class PokemonCacheRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_by_id(self, db_id: int) -> PokemonCache | None:
    return (
      self.db.query(PokemonCache)
      .filter(PokemonCache.db_id == db_id)
      .first()
    )
  
  def get_by_pokemon_id(self, pokemon_id: int) -> PokemonCache | None:
    return (
      self.db.query(PokemonCache)
      .filter(PokemonCache.pokemon_id == pokemon_id)
      .first()
    )
  
  def get_all(self) -> list[PokemonCache]:
    return self.db.query(PokemonCache).all()
  
  def cache_pokemon(self, pokemon_id: int, name: str, sprite_url: str, types: list[str]) -> PokemonCache:
    pokemon = PokemonCache(
      pokemon_id = pokemon_id,
      name = name,
      sprite_url = sprite_url,
      types = types
    )
    self.db.add(pokemon)
    self.db.commit()
    self.db.refresh(pokemon)
    
    return pokemon
  
  def update_pokemon(self, pokemon: PokemonCache, name:str, sprite_url: str, types: list[str]) -> PokemonCache:
    pokemon.name = name
    pokemon.sprite_url = sprite_url
    pokemon.types = types

    self.db.commit()
    self.db.refresh(pokemon)
 
    return pokemon
  
  def delete_pokemon(self, pokemon: PokemonCache) -> None:
    self.db.delete(pokemon)
    self.db.commit()
