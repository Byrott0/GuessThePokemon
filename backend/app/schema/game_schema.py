from datetime import datetime

from pydantic import BaseModel, Field

class StartGameRequest(BaseModel): 
  player_name: str = Field(min_length = 2, max_length = 25)

class StartGameResponse(BaseModel):
  game_id: str
  pokemon_id: int
  pokemon_name: str
  sprite_url: str
  hint_type: str

class GuessRequest(BaseModel):
  game_id: str
  guess: str = Field(min_length = 1, max_length = 25)

class GuessResponse(BaseModel):
  correct: bool
  pokemon_id: int
  pokemon_name: str
  sprite_url: str
  hint_type: str
  attempts_left: int
  score_gained: int

class GameSessionResponse(BaseModel):
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
  expires_at: datetime
  completed_at: datetime | None