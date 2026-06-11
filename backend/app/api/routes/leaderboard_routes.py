from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.core.database import get_db

from app.repository.leaderboard_repository import LeaderboardRepository
from app.schema.leaderboard_schema import LeaderboardResponse
from app.service.leaderboard_service import LeaderboardService

router = APIRouter(prefix="/api", tags = ["leaderboard"])

def get_leaderboard_repository(db: Session = Depends(get_db)) -> LeaderboardRepository:
  return LeaderboardRepository(db)

def get_leaderboard_service(leaderboard_repository: LeaderboardRepository = 
                            Depends(get_leaderboard_repository)) -> LeaderboardService:
  return LeaderboardService(leaderboard_repository)

@router.get("/get_leaderboard", response_model=LeaderboardResponse)
def leaderboard_ranking(leaderboard_service: LeaderboardService = Depends(get_leaderboard_service)):
  return leaderboard_service.get_leaderboard()
