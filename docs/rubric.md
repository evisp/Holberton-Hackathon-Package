# Evaluation Rubric

Scoring: 0–10 points per category. Total core: 50 points.  
Bonus: 0–10 points. Max total: 60 points.

General meaning 
- 0–2 = Missing / mostly not working
- 3–5 = Basic (works partly, many gaps)
- 6–8 = Good (works as intended, minor issues)
- 9–10 = Excellent (works very well, polished, thoughtful)

## 1) Product requirements fit (0–10)
Checks the “must build” items from the challenge brief.

- 0–2: Missing most required features.
- 3–5: Some required features exist, but key flow is incomplete.
- 6–8: All key requirements work: browse+filters, details page, ML estimate+range, comps.
- 9–10: All key requirements + very clear UX (easy navigation, good labels, good empty states).


## 2) Web app execution (0–10)
How well the app works end-to-end for a user.

- 0–2: App does not run or is too broken to demo.
- 3–5: Runs but has major issues (broken pages, frequent errors, hard to follow).
- 6–8: Smooth flow: browse → details → estimate → comps; basic styling is fine.
- 9–10: Polished UX (loading states, clear errors, clean layout, responsive).


## 3) ML quality + usefulness (0–10)
Whether ML adds value to the product (not just “a model exists”).

- 0–2: No ML, or ML is not connected to the app.
- 3–5: ML runs but results are confusing/unreliable; range missing or meaningless.
- 6–8: ML estimate + fair range shown; uses reasonable features; works on multiple examples.
- 9–10: Strong value add while staying simple (e.g., better range logic, good validation, uses extra useful signals like amenities).


## 4) Comparable properties (comps) (0–10)
Comps should support the valuation and feel relevant.

- 0–2: No comps.
- 3–5: Comps exist but similarity is weak or not explained.
- 6–8: Comps are clearly similar (nearby + similar sqm/rooms) and show price + at least one similarity reason.
- 9–10: Comps are well-ranked (clear similarity logic) and include helpful context (distance, €/sqm, key differences).


## 5) Engineering clarity (0–10)
Can judges run it quickly and understand what you built?

- 0–2: No clear run instructions; repo is confusing.
- 3–5: Basic README but missing important steps.
- 6–8: Clear README with setup/run steps; reasonable structure.
- 9–10: Quickstart works first try; minimal but clear API notes and consistent naming.


## Bonus: Advanced features (0–10)
Only score this if the core MVP flow works (browse → details → estimate+range → comps).

Examples (any mix):

- Overpriced / Fair / Underpriced label (explained).
- Favorites + compare (at least 2 saved listings).
- Market mini-insight (avg €/sqm nearby or by area grouping).
- “Why this estimate?” explanation (feature importance or amenities/tags from description).

Scoring guide:
- 0–2: Minor extras (small UI polish only).
- 3–5: One meaningful bonus feature works end-to-end.
- 6–8: Two meaningful bonus features work end-to-end.
- 9–10: Three+ meaningful bonus features, well integrated and polished.
