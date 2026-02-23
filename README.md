# Holberton School Albania: ML + Web Hackathon Package

This repository contains the documents and dataset for the Holberton School Albania hackathon: build a small Tirana real-estate web app that uses Machine Learning for pricing + comparable properties (comps).

## Hackathon goal (what you’re building)
Teams will build a simple product experience:
- Browse + filter property listings
- Open a listing details page
- Show an ML price estimate (with a low–high range)
- Show comparable properties (“comps”) to support the estimate

All details are in `docs/challenge_brief.md`.

## Quick start (clone)
Clone the repository and open it locally:

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
- `data/data_dictionary.md` — Field descriptions (what each column means, types, notes).

Note: Teams should create their own train/test split from the JSON.

## Recommended workflow (high level)
1) Read `docs/challenge_brief.md` and agree on your MVP.
2) Explore the dataset (check missing values and weird/outlier values).
3) Train a baseline model to predict `price_in_euro`.
4) Build a backend API and a web UI and connect them.
5) Add comps + (optional) bonus features if time allows.

## Questions
If something is unclear (requirements, fields, scoring), ask organizers early; don’t guess for hours.

> If you want to go fast, go alone. If you want to go far, go together.