from pathlib import Path
from dotenv import dotenv_values
import logging

# logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)

logger = logging.getLogger(__name__)

# ENV setup
ENV_FILE = Path(__file__).resolve().parents[2] / ".env"
ENV_VALUES = dotenv_values(ENV_FILE)


def get_required_env(name: str) -> str:
    value = ENV_VALUES.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

    
# APP CONFIG
APP_NAME = get_required_env("APP_NAME")
APP_VERSION = get_required_env("APP_VERSION")
DEBUG = get_required_env("DEBUG").lower() == "true"

# pokemon settings game
MIN_POKEMON_ID = int(get_required_env("MIN_POKEMON_ID"))
MAX_POKEMON_ID = int(get_required_env("MAX_POKEMON_ID"))

# POKE API
POKE_API_BASE_URL = get_required_env("POKEMON_API_BASE_URL")

# Database configuration
DB_URL = get_required_env("DB_URL")
