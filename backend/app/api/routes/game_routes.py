from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repository.leaderboard_repository import LeaderboardRepository
from app.repository.pokemon_cache_repository import PokemonCacheRepository
from app.schema.game_schema import StartGameRequest, StartGameResponse, GuessRequest, GameSessionResponse
from app.service.game_service import GameService
from app.service.leaderboard_service import LeaderboardService
from app.service.pokemon_service import PokemonService

router = APIRouter(prefix="/api", tags=["game_session"])

def get_pokemon_repository(db: Session = Depends(get_db)) -> PokemonCacheRepository:
  return PokemonCacheRepository(db)

def get_pokemon_service(
    pokemon_repository: PokemonCacheRepository = Depends(get_pokemon_repository),
) -> PokemonService:
  return PokemonService(pokemon_repository)

def get_leaderboard_repository(db: Session = Depends(get_db)) -> LeaderboardRepository:
  return LeaderboardRepository(db)

def get_leaderboard_service(
    leaderboard_repository: LeaderboardRepository = Depends(get_leaderboard_repository),
) -> LeaderboardService:
  return LeaderboardService(leaderboard_repository)

def get_game_service(
    leaderboard_service: LeaderboardService = Depends(get_leaderboard_service),
    pokemon_service: PokemonService = Depends(get_pokemon_service),
) -> GameService:
  return GameService(
    leaderboard_service=leaderboard_service,
    pokemon_service=pokemon_service,
  )

@router.post("/start_game", response_model=StartGameResponse)
def start_game(
    request: StartGameRequest,
    game_service: GameService = Depends(get_game_service),
):
    return game_service.start_game(request.player_name)

@router.post("/guess", response_model=GameSessionResponse)
def make_guess(
    request: GuessRequest,
    game_service: GameService = Depends(get_game_service),
):
    return game_service.check_guess(request.game_id, request.guess)

@router.get("/game_session/{game_id}", response_model=GameSessionResponse)
def get_game_session(
    game_id: str,
    game_service: GameService = Depends(get_game_service),
):
    return game_service.get_game_session(game_id)

@router.post("/finish_game/{game_id}", response_model=GameSessionResponse)
def finish_game(
    game_id: str,
    game_service: GameService = Depends(get_game_service),
):
    return game_service.finish_game(game_id)
