# Holberton School Albania: ML + Web Hackathon Package

This repository contains the dataset + documents for the Holberton School Albania hackathon: build a small Tirana real-estate web app that uses ML for pricing and comparable properties (“comps”).  

## Hackathon goal (what you’re building)
Teams will build a simple product experience:
- Browse + filter property listings
- Open a listing details page
- Show an ML price estimate (with a low–high range)
- Show comparable properties (“comps”) to support the estimate

All details are in `docs/challenge_brief.md`.

## Quick start (clone)
```bash
git clone https://github.com/evisp/Holberton-Hackathon-Package.git
cd Holberton-Hackathon-Package
```

## Repository contents (at a glance)

### `docs/`
- `docs/challenge_brief.md` — The challenge requirements (what you must build).
- `docs/rubric.md` — How projects are scored (core points + bonus points).
- `docs/submission.md` — What to submit and how the demo should look.
- `docs/quick_reference.md` — Suggested tools/libraries + recommended workflow (you are free to use others).

### `data/`
- `data/tirana_house_prices.json` — The dataset (JSON array of property listings).
- `data/data_dictionary.md` — Field descriptions (what each field means, types, notes).

Note: Teams should create their own train/test split from the JSON.

## Starter demo (optional)
There is a small working demo in `starter/` to show API ↔ Web integration:
- `starter/api` — Minimal Flask API (`/`, `/health`, `/listings`, `/listings/<id>`).
- `starter/web` — Minimal 2-page web UI (`index.html` + `listing.html`) that calls the API.

### Run the starter API (Terminal 1)
```bash
cd starter/api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Test quickly:
```bash
curl http://localhost:8000/health
curl "http://localhost:8000/listings?limit=3"
```

### Run the starter web (Terminal 2)
Serve the static files locally (don’t open with `file://`). [web:556]  
```bash
cd starter/web
python3 -m http.server 5500
```

Open:
- http://localhost:5500/index.html

Note: CORS is enabled in the starter API so the browser can call it from a different port. 

## Recommended workflow (high level)
1) Read `docs/challenge_brief.md` and agree on your MVP.
2) Explore the dataset (check missing values and weird/outlier values).
3) Train a baseline model to predict `price_in_euro`.
4) Build a backend API and a web UI and connect them.
5) Add comps + (optional) bonus features if time allows.

## Questions
If something is unclear (requirements, fields, scoring), ask organizers early; don’t guess for hours.

> If you want to go fast, go alone. If you want to go far, go together.
