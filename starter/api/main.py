import json
import os

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "data", "tirana_house_prices.json")
)

def load_listings():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    # Ensure each item has an integer id (use array index)
    for i, item in enumerate(items):
        item["id"] = i
    return items

LISTINGS = load_listings()

@app.get("/")
def home():
    return jsonify({
        "message": "Holberton Hackathon Starter API",
        "count": len(LISTINGS),
        "endpoints": {
            "health": "/health",
            "listings": "/listings?limit=20&offset=0&q=",
            "listing_detail": "/listings/<id>"
        }
    })

@app.get("/health")
def health():
    return jsonify({"ok": True, "count": len(LISTINGS)})

@app.get("/listings")
def listings():
    # pagination
    limit = request.args.get("limit", default=20, type=int)
    offset = request.args.get("offset", default=0, type=int)

    # basic filters (all optional)
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    bedrooms = request.args.get("bedrooms", type=float)      # stored as float in your sample
    bathrooms = request.args.get("bathrooms", type=float)    # stored as float in your sample
    min_sqm = request.args.get("min_sqm", type=float)
    max_sqm = request.args.get("max_sqm", type=float)
    q = request.args.get("q", default="", type=str).strip().lower()

    # keep responses small
    limit = max(1, min(limit, 100))
    offset = max(0, offset)

    filtered = []
    for item in LISTINGS:
        price = item.get("price_in_euro")
        sqm = item.get("main_property_property_square")
        addr = (item.get("main_property_location_city_zone_formatted_address") or "").lower()

        if min_price is not None and (price is None or price < min_price):
            continue
        if max_price is not None and (price is None or price > max_price):
            continue
        if bedrooms is not None and item.get("main_property_property_composition_bedrooms") != bedrooms:
            continue
        if bathrooms is not None and item.get("main_property_property_composition_bathrooms") != bathrooms:
            continue
        if min_sqm is not None and (sqm is None or sqm < min_sqm):
            continue
        if max_sqm is not None and (sqm is None or sqm > max_sqm):
            continue
        if q and q not in addr:
            continue

        # small "card" for list page
        filtered.append({
            "id": item["id"],
            "address": item.get("main_property_location_city_zone_formatted_address"),
            "price_in_euro": price,
            "sqm": sqm,
            "bedrooms": item.get("main_property_property_composition_bedrooms"),
            "bathrooms": item.get("main_property_property_composition_bathrooms"),
            "lat": item.get("main_property_location_lat"),
            "lng": item.get("main_property_location_lng"),
            "property_type": item.get("main_property_property_type"),
        })

    total = len(filtered)
    page = filtered[offset: offset + limit]

    return jsonify({
        "total": total,
        "limit": limit,
        "offset": offset,
        "items": page,
    })

@app.get("/listings/<int:listing_id>")
def listing_detail(listing_id: int):
    if listing_id < 0 or listing_id >= len(LISTINGS):
        abort(404)

    return jsonify(LISTINGS[listing_id])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
