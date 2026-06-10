from pydantic import BaseModel, Field


class LeaderboardEntry(BaseModel):
  rank: int
  player_id: str
  player_name: str
  total_score: int


class LeaderboardResponse(BaseModel):
  entries: list[LeaderboardEntry] = Field(default_factory=list)
