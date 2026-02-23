# Starter Web (Static)

This is a tiny 2-page web demo that calls the Starter API and displays:
- A listings page (browse)
- A listing details page (open one listing)

It’s meant to prove the API ↔ Web integration works, not to be the final hackathon solution.

## Prerequisites
- The Starter API must be running at: http://localhost:8000

## Run locally

From the repo root:

### 1) Start the API (in Terminal 1)
```bash
cd starter/api
source .venv/bin/activate
python main.py
```

### 2) Serve the web folder (in Terminal 2)
```bash
cd starter/web
python3 -m http.server 5500
```

Open in your browser:
- http://localhost:5500/index.html

## Pages
- `index.html`: fetches `GET /listings` and renders listing cards.
- `listing.html?id=<id>`: fetches `GET /listings/<id>` and renders details.

## Configuration
- The API base URL is hardcoded as:
  - `starter/web/app.js` → `API_BASE`
  - `starter/web/listing.html` → `API_BASE`

If you change the API port or host, update `API_BASE` in both places.

## Troubleshooting
- “Could not load listings”: check the API is running on http://localhost:8000 and try:
  ```bash
  curl http://localhost:8000/health
  ```
- Blank page / no styles: make sure you opened the page via `http://localhost:5500/...` (not `file://...`).
