# Starter API (Flask)

This is a minimal Flask JSON API used only to power the `starter/web` demo for the hackathon package.

## Run locally

```bash
cd starter/api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

API runs on: http://localhost:8000

## Endpoints
- `GET /` → small API index (shows available endpoints)
- `GET /health` → `{ "ok": true, "count": <number_of_listings> }`
- `GET /listings` → paginated list of listing “cards”
  - Query params (all optional): `limit`, `offset`, `q`, `min_price`, `max_price`, `bedrooms`, `bathrooms`, `min_sqm`, `max_sqm`
- `GET /listings/<id>` → full JSON for a single listing

## Quick tests (copy/paste)

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
curl "http://localhost:8000/listings?limit=3"
curl "http://localhost:8000/listings?q=Tiran%C3%AB&limit=3"
curl http://localhost:8000/listings/0
```

## Notes
- CORS is enabled so a frontend running on a different port (like `starter/web`) can call this API from the browser. 
- If you change the API port, update the `API_BASE` value in the web files.
