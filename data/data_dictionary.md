# Data Dictionary — tirana_house_prices.json

This dataset contains Tirana property listings that you will use to build a small real-estate web app (browse listings, open details) and train an ML model to estimate price and show comparable properties. A data dictionary describes the fields in a dataset so it can be understood and used correctly. 

## File format
- `data/tirana_house_prices.json` is a JSON array.
- Each item in the array is **one property listing**.

## Target (what to predict)
- `price_in_euro` (number): The listing price in EUR (recommended target).

## Fields

| Field | Type | Meaning | Notes |
|---|---|---|---|
| main_property_description_text_content_original_text | string | Free-text listing description | Albanian text; may include extra info like “parking”, “oxhak”, etc. Optional feature. |
| main_property_floor | number \| null | Floor number | Example: 2, 7. |
| main_property_furnishing_status | string \| null | Furnishing status | Example: `fully_furnished`. Can be null. |
| main_property_has_carport | boolean \| null | Has carport | null = unknown/not provided. |
| main_property_has_elevator | boolean \| null | Has elevator | Example: true/false. |
| main_property_has_garage | boolean \| null | Has garage | null = unknown/not provided. |
| main_property_has_garden | boolean \| null | Has garden | null = unknown/not provided. |
| main_property_has_parking_space | boolean \| null | Has parking space | null = unknown/not provided. |
| main_property_has_terrace | boolean \| null | Has terrace | Example: true/false. |
| main_property_location_city_zone_city_city_name | string \| null | City name | Example: `tirane`. |
| main_property_location_city_zone_formatted_address | string \| null | Address (formatted) | Example: “Rruga …, Tiranë, Albania”. Useful for display/search. |
| main_property_location_lat | number \| null | Latitude | Example: 41.31. |
| main_property_location_lng | number \| null | Longitude | Example: 19.80. |
| main_property_price | number \| null | Raw listing price | Usually matches `price_in_euro` when currency is EUR. Prefer `price_in_euro` as target. |
| main_property_price_currency | string \| null | Currency code | Example: `EUR`. |
| main_property_property_composition_balconies | number \| null | Number of balconies | Example: 1, 2. |
| main_property_property_composition_bathrooms | number \| null | Number of bathrooms | Example: 2. |
| main_property_property_composition_bedrooms | number \| null | Number of bedrooms | Example: 3. |
| main_property_property_composition_kitchens | number \| null | Number of kitchens | Example: 1. |
| main_property_property_composition_living_rooms | number \| null | Number of living rooms | Example: 1. |
| main_property_property_status | string \| null | Listing status | Example: `for_sale`. |
| main_property_property_type | string \| null | Property type | Example: `apartment`. |
| price_in_euro | number \| null | Price in EUR | Recommended target label. |
| main_property_property_square | number \| null | Area in square meters (sqm) | Example: 205.0, 151.0. |

## Important notes (read this)
- Some fields may be `null` (missing/unknown). You must decide how to handle them (drop, fill, create “unknown” category, etc.).
- Some values may be abnormal/outliers (very high/low prices, strange sqm, etc.). You must decide whether to keep, cap, or remove them, and explain your choice briefly. 
- If there is no stable `id` field in the JSON, create one during preprocessing (for example, use the row index) so your app can open a listing details page and fetch comps.
