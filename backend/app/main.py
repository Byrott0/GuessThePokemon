from fastapi import FastAPI

from app.api.routes import game_routes, leaderboard_routes
from app.core.config import APP_NAME, APP_VERSION, DEBUG
from app.core.database import Base, engine
from app.model import pokemon_cache


def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(
        title=APP_NAME,
        version=APP_VERSION,
        debug=DEBUG,
    )

    
    #app.include_router(game_routes.router)
    #app.include_router(leaderboard_routes.router)


    @app.get("/")
    def health_check():
        return {"status": "ok", "app": APP_NAME}

    return app


app = create_app()