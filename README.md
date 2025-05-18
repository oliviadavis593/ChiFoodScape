# 🛒 ChiFoodScape: Mapping Real Food Access in Chicago

## 🧭 Overview

ChiFoodScape is a civic tech project that maps and analyzes Chicago's food landscape—going beyond city records to expose the **real availability of full-service grocery stores, urban farms, and compost infrastructure**.

Using open data, spatial joins, and visual storytelling, the project aims to:
- Show which neighborhoods are structurally excluded from **fresh food**
- Visualize which areas are underserved by **composting and urban agriculture**
- Help residents, nonprofits, and city leaders target **food justice interventions**

🔗 **Live Map Preview**  
Explore the interactive grocery store map: [ChiFoodScape](https://oliviadavis593.github.io/ChiFoodScape/).

🗺️ **v1 Map**  
v1             |  v1
:-------------------------:|:-------------------------:
<img width="1105" alt="Screenshot 2025-05-13 at 8 13 50 PM" src="https://github.com/user-attachments/assets/a3e376b4-f9b8-4afd-877d-16c6fc171f6f" /> | <img width="1064" alt="Screenshot 2025-05-13 at 8 13 28 PM" src="https://github.com/user-attachments/assets/a9a31ea1-d634-4c70-bd12-11b05eb727ca" />

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
| `03_visualizations.ipynb`              | Builds map using Folium with color-coded markers + tooltips            |
| `03_visualizations_by_zip_v1.ipynb`    | Groups stores by ZIP and saves summary CSV                             |
| `02_access_score.ipynb`                | *(Optional)* Scoring logic for future equity metrics                   |
| `clean_urban_ag_sites.ipynb`           | *(Optional)* Cleans urban farm dataset for later overlay               |

---

## 📦 Output Files

| File                                      | Description                                                  |
|-------------------------------------------|--------------------------------------------------------------|
| `food_inspections_cleaned.csv`           | Cleaned inspection dataset                                  |
| `grocery_stores_labeled.csv`             | Inspection data + real/junk flags                           |
| `updated_grocery_stores.csv`             | Final deduplicated dataset for mapping                      |
| `grocery_stores_chicago_map.html`        | Interactive map (green = real, red = junk, gray = unknown)  |
| `grocery_stats_by_zip.csv`               | Summary of store counts by ZIP                              |

---

## ✅ Current Status

- [x] Cleaned and labeled store data
- [x] Deduplicated per store location
- [x] Built interactive HTML map
- [x] Summarized counts by ZIP
- [ ] Add tooltip + popup interactivity *(in progress)*
- [ ] Add community area-level grouping *(coming soon)*

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
   - 

🔹 **Phase 1 – MVP Finish Line**
 Join stores with community areas 

 - Add choropleth layers for store count per area (density or per capita if you later have pop data)

 - Improve map UX: add popup w/ inspection result, store type, maybe emoji/icon updates

 - Re-export public-facing HTML map (grocery_store_map_by_area.html)

🔹 **Phase 2 – Parallel Refinement**
 - Chip away at unclassified stores when convenient (especially by ZIP or known gaps)

 - Improve keyword logic (e.g. Whole Foods #123 or Costco Wholesale)

 - Add license type or external lists

---

## 🧠 Future Features (V2+ Vision)

- Add food desert overlays (via USDA or built from scratch)
- Join compost drop-off sites and urban farms
- Build “food access scores” per neighborhood
- Allow filtering by inspection result (Pass/Fail)
- Compare public claims vs. on-the-ground reality

---

## 🤔 Framing Questions

- What does food access *actually* look like in your neighborhood?
- How many real grocery stores are within a mile of your block?
- Why does the city count corner stores and 7-Elevens the same as Aldi or Mariano’s?
- Who gets access to fresh food—and who never did?

---

## ✏️ Notes

- You can update `grocery_keywords` and `junk_keywords` inside `01b_clean_grocery_stores.ipynb`
- Data transformations use **Pandas**
- Maps are rendered with **Folium** (Leaflet.js)
- Stats grouped via **Pandas**, future spatial joins may use **GeoPandas**

---

*Built with public data. Inspired by public good.*
