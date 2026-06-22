from datetime import datetime
from uuid import uuid4

from app.schema.game_schema import GameSessionResponse
from app.service.leaderboard_service import LeaderboardService
from app.service.pokemon_service import PokemonService

ACTIVE_GAMES: dict[str, GameSessionResponse] = {}

class GameService:
  def __init__(self, leaderboard_service: LeaderboardService, pokemon_service: PokemonService):
    self.leaderboard_service = leaderboard_service
    self.pokemon_service = pokemon_service
    self.active_games = ACTIVE_GAMES


  def start_game(self, player_name: str) -> GameSessionResponse:
    game_id = str(uuid4())
    pokemon = self.pokemon_service.get_random_pokemon()

    game_session = GameSessionResponse(
      game_id=game_id,
      player_name=player_name,
      pokemon_id=pokemon.pokemon_id,
      pokemon_name=pokemon.name,
      sprite_url=pokemon.sprite_url,
      hint_type="type",
      status="active",
      attempts=0,
      max_attempts=6,
      score_gained=0,
      created_at=datetime.now(),
      completed_at=None
    )
    self.active_games[game_id] = game_session
    return game_session


  def get_game_session(self, game_id: str) -> GameSessionResponse:
    if game_id not in self.active_games:
        raise ValueError("Game session not found")

    return self.active_games[game_id]


  def check_guess(self, game_id: str, guess: str) -> GameSessionResponse:
    game_session = self.get_game_session(game_id)

    if game_session.status != "active":
        raise ValueError("Game session is not active")

    game_session.attempts += 1

    normalized_guess = guess.strip().lower()
    normalized_answer = game_session.pokemon_name.strip().lower()

    if normalized_guess == normalized_answer:
        game_session.status = "won"
        game_session.score_gained = max(
            0,
            (game_session.max_attempts - game_session.attempts + 1) * 7,
        )
        game_session.completed_at = datetime.now()

        self.leaderboard_service.save_player_score(
            player_id=game_session.player_name.lower(),
            player_name=game_session.player_name,
            score=game_session.score_gained,
        )

    elif game_session.attempts >= game_session.max_attempts:
        game_session.status = "lost"
        game_session.score_gained = 0
        game_session.completed_at = datetime.now()

    return game_session


  def finish_game(self, game_id: str) -> GameSessionResponse:
    game_session = self.get_game_session(game_id)
    game_session.status = "finished"
    game_session.completed_at = datetime.now()
    return game_session
  
