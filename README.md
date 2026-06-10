# GuessThePokemon

GuessThePokemon is een Python project waarin spelers tussen de eerste 151 Pokemon moeten raden op basis van een sprite of silhouette. De backend haalt de data op via de [PokeAPI](https://pokeapi.co/) en kan deze lokaal cachen in een database.

## Status

In development

## Features

- FastAPI-backend voor een Pokemon raadspel
- Integratie met de PokeAPI
- Lokale Pokemon-cache via SQLAlchemy
- Schemas voor game-sessies, guesses en leaderboard-data
- Basisconfiguratie via een `.env` bestand
- Voorbereide structuur voor game- en leaderboard-endpoints

## Installatie

Clone de repository en ga naar de backend-map:

```bash
git clone <repository-url>
cd GuessThePokemon/backend
```

Maak een virtual environment aan:

```bash
python -m venv .venv
```

Activeer de virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Installeer de dependencies:

```bash
pip install -r requirements.txt
```

## Configuratie

Maak in de map `backend/` een `.env` bestand aan:

```env
APP_NAME=GuessThePokemon
APP_VERSION=0.1.0
DEBUG=true

MIN_POKEMON_ID=1
MAX_POKEMON_ID=151
POKEMON_API_BASE_URL=https://pokeapi.co/api/v2

DB_URL=sqlite:///./guess_the_pokemon.db
```

## Applicatie starten

Start de FastAPI-server vanuit de map `backend/`:

```bash
uvicorn app.main:app --reload
```

Open daarna:

- API: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/`

De health check geeft bijvoorbeeld terug:

```json
{
  "status": "ok",
  "app": "GuessThePokemon"
}
```

## PokeAPI

Dit project gebruikt de publieke PokeAPI om Pokemon-informatie op te halen, zoals:

- Pokemon ID
- Naam
- Sprite URL
- Types

Meer informatie: [https://pokeapi.co/](https://pokeapi.co/)

