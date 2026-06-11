from dependency_injector import containers, providers

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repository.pokemon_cache_repository import PokemonCacheRepository
from app.service.pokemon_service import PokemonService

from app.service.leaderboard_service import LeaderboardService
from app.repository.leaderboard_repository import LeaderboardRepository

class Dependencies:
  def __init__(self):
    pass
   
    # self.pokemon_repository = PokemonCacheRepository
    # self.pokemon_service = PokemonService
    # self.leaderboard_repository = LeaderboardRepository
    # self.leaderboard_service = LeaderboardService




dependencies = Dependencies()
