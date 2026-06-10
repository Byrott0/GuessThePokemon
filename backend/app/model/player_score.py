from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class PlayerScore(Base):
    __tablename__ = "player_leaderboard"

    player_id: Mapped[str] = mapped_column(String(36), primary_key=True, index=True, default=lambda: str(uuid4()))
    player_name: Mapped[str] = mapped_column(String(100), nullable=False)
    high_score: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
