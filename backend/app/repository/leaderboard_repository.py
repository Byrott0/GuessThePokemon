from sqlalchemy.orm import Session
from app.model.player_score import PlayerScore
from datetime import datetime


class LeaderboardRepository:
  def __init__(self, db: Session):
    self.db = db

  def get_by_player_id(self, player_id: str) -> PlayerScore | None:
    return (
      self.db.query(PlayerScore)
      .filter(PlayerScore.player_id == player_id)
      .first()
    )

  def get_all_players(self) -> list[PlayerScore]:
    return self.db.query(PlayerScore).all()
  
  
  def get_leaderboard(self, limit:int = 10) -> list[PlayerScore]:
    return(
    self.db.query(PlayerScore)
    .order_by(PlayerScore.high_score.desc(), PlayerScore.updated_at.asc())
    .limit(limit).all()
  )
  
  def save_player(self, id: str, name: str, score: int) -> PlayerScore:
    player = PlayerScore(
      player_id = id,
      player_name = name,
      high_score = score,
    )
    self.db.add(player)
    self.db.commit()
    self.db.refresh(player)

    return player
  

  def update_player_score(self, player_id: str, score: int, updated_at: datetime) -> PlayerScore | None:
    player = (
      self.db.query(PlayerScore)
      .filter(PlayerScore.player_id == player_id)
      .first()
    )

    if player is None:
      return None
    if score > player.high_score:
      player.high_score = score 
      player.updated_at = updated_at
      
      self.db.commit()
      self.db.refresh(player)

    return player
  
  
  def delete_player(self, player: PlayerScore, player_name: str) -> None:
    player = (
      self.db.query(PlayerScore)
      .filter(PlayerScore.player_name == player_name)
      .first()
    )

    if player is None:
      return None
    
    self.db.delete(player)
    self.db.commit()