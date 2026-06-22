# GuessThePokemon

GuessThePokemon is een project waarin spelers tussen de eerste 151 Pokemon moeten raden op basis van een sprite of silhouette. De backend haalt de data op via de [PokeAPI](https://pokeapi.co/) en kan deze lokaal cachen in een database.

## Status

In development

## Installatie

Clone de repository en ga naar de backend-map:

```bash
git clone https://github.com/Byrott0/GuessThePokemon.git
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

## Applicatie starten

Start de FastAPI-server vanuit de map `backend/`:

```bash
uvicorn app.main:app --reload
```

Open daarna:

- API docs: `http://127.0.0.1:8000/docs`


## PokeAPI

Dit project gebruikt de publieke PokeAPI om Pokemon informatie op te halen, zoals:

- Pokemon ID
- Naam
- Sprite URL
- Types

Meer informatie: [https://pokeapi.co/](https://pokeapi.co/)
