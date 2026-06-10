from app.schema.leaderboard_schema import LeaderboardEntry, LeaderboardResponse
from app.repository.leaderboard_repository import LeaderboardRepository
from datetime import datetime, timezone

class LeaderboardService:
  def __init__(self, leaderboard_repository: LeaderboardRepository):
    self.leaderboard_repository = leaderboard_repository
  
  def get_leaderboard(self) -> LeaderboardResponse:
    players_ranking = self.leaderboard_repository.get_leaderboard()
    
    ranking = [
      LeaderboardEntry(
      rank= index + 1,
      player_id = player.player_id,
      player_name = player.player_name,
      total_score = player.high_score
    )
    for index, player in enumerate(players_ranking)
  ] 
    return LeaderboardResponse(entries = ranking)
  
  def save_player_score(self, player_id, player_name, score):
    existing_player = self.leaderboard_repository.get_by_player_id(player_id)

    if existing_player:
      return self.leaderboard_repository.update_player_score(player_id, score, updated_at = datetime.now())
    
    return self.leaderboard_repository.save_player(player_id, player_name, score)
  