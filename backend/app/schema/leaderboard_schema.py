from datetime import datetime

from pydantic import BaseModel, Field

class LeaderboardEntry(BaseModel):
  player_id: int
  player_name: str
  total_score: int
  last_played: datetime


class LeaderboardResponse(BaseModel):
  entries: list[LeaderboardEntry] = Field(default_factory=list)
