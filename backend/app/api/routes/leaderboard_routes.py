from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.core.database import get_db

from app.repository.leaderboard_repository import LeaderboardRepository
from app.schema.leaderboard_schema import LeaderboardResponse
from app.service.leaderboard_service import LeaderboardService

router = APIRouter(prefix="/apiV1", tags = ["leaderboard"])

@router.get("/get_leaderboard", response_model=LeaderboardResponse)
def leaderboard_ranking(db: Session = Depends(get_db)):
  leaderboard_repository = LeaderboardRepository(db)
  leaderboard_service = LeaderboardService(leaderboard_repository)
  return leaderboard_service.get_leaderboard()
