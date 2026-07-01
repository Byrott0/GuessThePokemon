# GuessThePokemon

GuessThePokemon is een project waarin spelers tussen de eerste 151 Pokemon moeten raden op basis van een sprite of silhouette. De backend haalt de data op via de [PokeAPI](https://pokeapi.co/) en kan deze lokaal cachen in een database in SQLite.



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

Installeer de dependencies:

Backend:
```bash
pip install -r requirements.txt
```
Frontend:
```bash
npm run build
```

## Applicatie starten

Start de FastAPI-server vanuit de map `backend/`:

```bash
uvicorn app.main:app --reload
```
Voor de `frontend/`:
```bash
npm run dev
```

## De applicatie runt op de volgende locaties:
- API docs: `http://127.0.0.1:8000/docs`

- Frontend pagina: `http://localhost:5173`



## PokeAPI

Dit project gebruikt de publieke PokeAPI om Pokemon informatie op te halen, zoals:

- Pokemon ID
- Naam
- Sprite URL
- Types

Meer informatie: [https://pokeapi.co/](https://pokeapi.co/)
