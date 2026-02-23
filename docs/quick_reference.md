# Suggested Tools & Workflow 

Your goal is to build a small real-estate web app (browse + filters, listing details, price estimate + range, and comparable properties). This document suggests tools and a simple workflow to help you move fast; you are free to use other technologies.

## Recommended approach (simple)
1) Load the JSON dataset, explore it, and decide how to handle missing (`null`) values and abnormal values (outliers).
2) Build a backend API that returns JSON for listings, details, predictions, and comps.
3) Build a web UI that calls the API and renders results.

## Suggested ML tools (Python)
- `pandas`: load/clean the dataset and prepare features.
- `scikit-learn`: train a baseline regression model.
- `joblib`: save/load your trained model so you don’t retrain every time you run the API. 

## Suggested backend tools

Option A (recommended): Flask (Python)
- Simple and fast to start for a small JSON API.
- If your frontend runs on a different port than your backend, you may need CORS. A common solution is the `Flask-CORS` extension. 

Option B: FastAPI (Python)
- Also great for building JSON APIs quickly, and it works well with ML code. 
- If you need CORS, FastAPI supports it via `CORSMiddleware`. 

Option C: Something else
- You may use any backend you want (Node/Express, Django, etc.) as long as:
  - You expose HTTP endpoints that return JSON.
  - Your web app can call the backend.
  - You can run everything locally for the demo.


## Suggested frontend tools (JavaScript)
Minimal option (recommended for speed):
- HTML + CSS + Vanilla JS
- Use `fetch()` to call your backend endpoints and `response.json()` to read the JSON response.

Optional:
- React or other frameworks are allowed, but only use them if your team can move fast with them.

## Suggested API design (high level)
You can design it your way, but you may find these endpoints useful:
- `GET /listings` (filters + pagination)
- `GET /listings/{id}` (details)
- `POST /predict` (estimated price + low/high range)
- `GET /listings/{id}/comps` (5 comparable properties)

## Suggested team workflow 
- Agree on the API contract first (what endpoints return what JSON), then split work:
  - ML team: cleaning + baseline model + prediction logic + comps logic.
  - Full Stack team: API endpoints + UI pages + integration.
- Start with a working MVP early, then add bonus features (favorites/compare, overpriced label, market insights).

## Notes
- Use Git often (small commits) so you can collaborate safely.
- Keep the solution simple and working. A clean end-to-end demo beats extra features that don’t work.
