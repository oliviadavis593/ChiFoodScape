# 🛒 ChiFoodScape: Mapping Real Food Access in Chicago

## 🧭 Overview

ChiFoodScape is a civic tech project that maps and analyzes Chicago's food landscape—going beyond city records to expose the **real availability of full-service grocery stores, urban farms, and compost infrastructure**.

Using open data, spatial joins, and visual storytelling, the project aims to:
- Show which neighborhoods are structurally excluded from **fresh food**
- Visualize which areas are underserved by **composting and urban agriculture**
- Help residents, nonprofits, and city leaders target **food justice interventions**

🔗 **Live Map Preview**  
Explore the interactive grocery store map: [ChiFoodScape](https://oliviadavis593.github.io/ChiFoodScape/grocery_stores_chicago_map_v1.html)


🗺️ **v1 Interactive Store Map**  
v1             |  v1
:-------------------------:|:-------------------------:
<img width="1105" alt="Screenshot 2025-05-13 at 8 13 50 PM" src="https://github.com/user-attachments/assets/a3e376b4-f9b8-4afd-877d-16c6fc171f6f" /> | <img width="1064" alt="Screenshot 2025-05-13 at 8 13 28 PM" src="https://github.com/user-attachments/assets/a9a31ea1-d634-4c70-bd12-11b05eb727ca" />

🔗 **Choropleth Map by Community Area**  
View updated store density map: [Choropleth Map v2](https://oliviadavis593.github.io/ChiFoodScape/grocery_choropleth_by_area_v2.html)


🗺️ **v1 Choropleth Map** 
Map
:-------------------------:
<img width="893" alt="Screenshot 2025-05-23 at 10 08 25 PM" src="https://github.com/user-attachments/assets/aed26ad0-bea7-423b-a275-c6c5400abc40" />


🔗 **Choropleth Map with Access Scores**  
Visualize community access scores with labels: [Access Score Choropleth](https://oliviadavis593.github.io/ChiFoodScape/access_score_choropleth.html)


---

## 🔍 Two-Map Framework: *City vs. Reality*

**Map 1 – City Map**  
Shows *all* licensed food vendors according to city records.  
🟡 Includes gas stations, dollar stores, 7-Elevens, etc.

**Map 2 – Reality Map**  
Filters to only **real grocery stores** with fresh produce and essentials.  
🟢 Excludes junk stores that don't meaningfully support food access.

Together, these maps reveal where the **official data misrepresents actual access**, especially in Black and Brown communities historically underinvested by design.

---

## 🗂️ Current Scope (V1): Grocery Store Mapping

✅ Built and working:
- Loads filtered inspection data (from the Chicago Data Portal)
- Flags real grocery stores vs. junk stores
- Deduplicates store records by address/name
- Generates a sharable interactive map
- Exports ZIP-level summaries (`real`, `junk`, `unclassified`)

---

## 🔨 Project Structure

| Notebook                                | Purpose                                                                 |
|----------------------------------------|-------------------------------------------------------------------------|
| `01_data_cleaning.ipynb`               | Cleans raw food inspection data (drops nulls, bad coordinates)         |
| `01b_clean_grocery_stores.ipynb`       | Adds `IS_REAL_GROCERY` / `IS_JUNK_STORE` flags based on store names    |
| `01d_clean_grocery_stores.ipynb`       | Merges clean inspections + flags, removes duplicates for final dataset |
| `01e_clean_filtered_grocery_stores.ipynb` | Filters stores based on specific logic refinements       |
| `02_access_score.ipynb`                | Scoring logic for future equity metrics                   |
| `03_visualizations.ipynb`              | Builds map using Folium with color-coded markers + tooltips            |
| `03_visualizations_by_zip_v1.ipynb`    | Groups stores by ZIP and saves summary CSV                             |
| `04_geo_join_by_area.ipynb`            | Joins store data to community area shapefile (GeoJSON)                 |
| `05_unclassified_review.ipynb`         | Lists unclassified stores for manual review and reclassification       |
| `05b_review_real_grocery_stores.ipynb` | Audits stores flagged as "real groceries" for false positives  |
| `06_choropleth_by_area.ipynb`          | Creates choropleth map of grocery density by community area            |
| `clean_urban_ag_sites.ipynb`           | Cleans urban farm dataset for later overlay               |

---

## 📦 Output Files

| File                                      | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `food_inspections_cleaned.csv`           | Cleaned food inspection data from the Chicago Data Portal                  |
| `grocery_stores_labeled.csv`             | Inspection data with real/junk classification flags                        |
| `grocery_stores_cleaned_v1.csv`          | Deduplicated + cleaned dataset of labeled stores used for mapping          |
| `grocery_stores_with_community.csv`      | Grocery dataset spatially joined with community areas                      |
| `grocery_stats_by_zip.csv`               | Summary counts of store types by ZIP code                                  |
| `grocery_stores_chicago_map_v1.html`     | Interactive map (green = real, red = junk, gray = unknown)                 |
| `grocery_choropleth_by_area_v2.html`        | Choropleth map showing store counts per community area                     |

---

## ✅ Current Status

- [x] Cleaned and labeled store data
- [x] Deduplicated per store location
- [x] Built interactive HTML map with color-coded markers
- [x] Added tooltip + popup interactivity to marker map
- [x] Summarized counts by ZIP code
- [x] Spatially joined grocery stores with community areas
- [x] Created community-level choropleth map of store density
- [ ] Calculate summary stats (real vs. junk by neighborhood)
- [ ] Systematically review unclassified stores
- [ ] Final round of junk/real grocery keyword improvements
- [ ] Identify food access gaps using food desert overlays
- [ ] Optionally add urban farm or compost site overlays

### 🔜 Phase 5: Analysis & UX Upgrades

- [ ] Filter: Only show stores that passed inspection
- [ ] Display violations in popups or tooltips
- [ ] Add grocery access scoring layer
- [ ] Publish full app via Streamlit, Flask, or GitHub Pages

---

## 🔜 Next Steps (V1 Finish Line)

1. **📦 Improve Labeling Logic**
   - Fix false negatives (e.g. “Whole Foods #123”, “Costco Wholesale”)
   - Supplement name-matching with better keywords or license info

2. **📍 Enhance Map UX**
   - Add popup with address, inspection result, store type
   - Refine icons by store category

3. **📊 ZIP + Community Area Stats**
   - Use shapefile to join stores with community areas
   - Add choropleth layers for “grocery store density”

4. **🌐 Export & Share**
   - Save final `grocery_stores_chicago_map.html` for easy distribution
  
🔹 **Phase 1 – MVP Finish Line**
 Join stores with community areas 

 - Add choropleth layers for store count per area (density or per capita if later we have pop data)

 - Improve map UX: add popup w/ inspection result, store type, maybe emoji/icon updates

 - Re-export public-facing HTML map (grocery_store_map_by_area.html)

🔹 **Phase 2 – Parallel Refinement**
 - Chip away at unclassified stores when convenient (especially by ZIP or known gaps)

 - Improve keyword logic (e.g. Whole Foods #123 or Costco Wholesale)

 - Add license type or external lists

---

## 🧠 Future Features (V2+ Vision)

- Add food desert overlays (e.g. USDA-defined or custom-calculated)
- Incorporate compost drop-off and urban farm layers
- Build “food access scores” per neighborhood
- Allow filtering by inspection result (e.g. Pass/Fail/Out of Business)
- Compare official licensing data vs. on-the-ground availability
- Add filter options and search tools in the interactive maps
- Explore a mobile-optimized public-facing dashboard

---

## 🤔 Framing Questions

- What does food access *actually* look like in your neighborhood?
- How many real grocery stores are within a mile of your block?
- Why does the city count corner stores and 7-Elevens the same as Aldi or Mariano’s?
- Who gets access to fresh food—and who never did?

---

## Notes

- Can update `grocery_keywords` and `junk_keywords` inside `01b_clean_grocery_stores.ipynb`
- Data transformations use **Pandas**
- Maps are rendered with **Folium** (Leaflet.js)
- Stats grouped via **Pandas**, future spatial joins may use **GeoPandas**

---

*Built with public data. Inspired by public good.*
