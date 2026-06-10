from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class PokemonCache(Base):
  __tablename__ = "pokemon_cache"

  db_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
  name: Mapped[str] = mapped_column(String(100), nullable=False)
  pokemon_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True, index=True)
  sprite_url: Mapped[str] = mapped_column(String(200), nullable=False)
  types: Mapped[list[str]] = mapped_column(JSON, nullable=False)  
  #created_at: Mapped[int] = mapped_column(DateTime, default=datetime.now)
  #updated_at: Mapped[int] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
