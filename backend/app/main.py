from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import game_routes, leaderboard_routes
from app.core.config import APP_NAME, APP_VERSION, DEBUG
from app.core.database import Base, engine
from app.model import player_score, pokemon_cache, game_session

FRONTEND_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(
        title=APP_NAME,
        version=APP_VERSION,
        debug=DEBUG,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=FRONTEND_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(game_routes.router)
    app.include_router(leaderboard_routes.router)


    @app.get("/")
    def health_check():
        return {"status": "ok", "app": APP_NAME}

    return app


app = create_app()
