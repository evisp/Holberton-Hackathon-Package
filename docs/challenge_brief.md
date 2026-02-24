# Hackathon Challenge Brief - Tirana Real Estate Companion

## Goal
Build a small real-estate web app for Tirana that helps users explore listings and understand pricing using ML + evidence.

You are not building a “prediction page”; you are building a simple product experience.

## What you have
- A real dataset of property listings (price, location, rooms, sqm, amenities, and a description text).

## What you must build (key requirements)
1) Listings browser + filters  
- Show a list of properties from the dataset.  
- Users can filter by at least: price range, bedrooms, bathrooms, and square meters (sqm).  
- Add at least 1 more filter (e.g., furnishing, elevator, terrace).

2) Listing details page  
- Clicking a listing opens a details page.  
- Show the property’s key fields (beds, baths, sqm, floor, furnishing, elevator/terrace) and the description text.  
- Show the address (and optionally the map location if you want).

3) ML price estimate + fair range  
- On the details page, show:  
  - Estimated price (EUR).  
  - A “fair range” (low–high).  
- Keep it simple: a baseline model is OK if it works reliably.

4) Comparable properties (comps)  
- For each listing, show 5 comparable listings selected by similarity (nearby location + similar size/rooms).  
- Display their prices and why they are “similar” (at least distance and one other reason).  
Comparable properties (“comps”) are a common real-estate way to support/justify a valuation. 

## Bonus requirements (pick up to 3)
- Overpriced / Fair / Underpriced label (based on listing price vs predicted range or comps).  
- Favorites + compare (save listings and compare key numbers).  
- Market mini-insight (e.g., average €/sqm for nearby listings or an area grouping).

## Constraints
- Time: 2 sessions × 4 hours.
- Use only the provided dataset (no external paid APIs).
- Your app must run locally for demo.

## Deliverables (what you submit)
- A GitHub repository with:
  - Working instructions in `README.md`.
  - Code for training (notebook or script) + saved model (or training step explained).
  - Backend + frontend (or a simple UI that demonstrates the flows).
- A short demo (2–3 minutes): browse → open listing → show estimate + range → show comps.

## Evaluation (how you’ll be judged)
- A working MVP that matches the requirements matters most. 
- Clear UX: easy to understand, not cluttered.
- ML is integrated into the product (estimate + evidence), not isolated.
- Code clarity: readable, reasonable structure, runs without surprises.
