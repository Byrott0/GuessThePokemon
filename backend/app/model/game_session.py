from datetime import datetime
from uuid import UUID, uuid4
from dataclasses import dataclass


@dataclass
class GameSession:
  game_id: str
  player_name: str
  pokemon_id: int
  pokemon_name: str
  sprite_url: str
  hint_type: str
  status: str
  attempts: int
  max_attempts: int 
  score_gained: int
  created_at: datetime
  completed_at: datetime | None
