# ChiFoodScape: Mapping Real Food Access in Chicago

## Overview

ChiFoodScape is a civic tech project that maps and analyzes Chicago's food landscape—going beyond city records to expose the **real availability of full-service grocery stores, urban farms, and compost infrastructure**.

Using open data, spatial joins, and visual storytelling, the project aims to:
- Show which neighborhoods are structurally excluded from **fresh food**
- Visualize which areas are underserved by **composting and urban agriculture**
- Help residents, nonprofits, and city leaders target **food justice interventions**
 
ChiFoodScape Website (All Maps): [ChiFoodScape](https://oliviadavis593.github.io/ChiFoodScape)

🔗 **v1 Interactive Store Mapw**  
Explore the interactive grocery store map: [Store Map](https://oliviadavis593.github.io/ChiFoodScape/grocery_stores_chicago_map_v1.html)
 
Store Map v1             |  Store Map v1  
:-------------------------:|:-------------------------:  
<img width="1105" alt="Screenshot 2025-05-13 at 8 13 50 PM" src="https://github.com/user-attachments/assets/a3e376b4-f9b8-4afd-877d-16c6fc171f6f" /> | <img width="1064" alt="Screenshot 2025-05-13 at 8 13 28 PM" src="https://github.com/user-attachments/assets/a9a31ea1-d634-4c70-bd12-11b05eb727ca" />

🔗 **Choropleth Map by Community Area**  
View updated store density map: [Choropleth Map](https://oliviadavis593.github.io/ChiFoodScape/grocery_choropleth_by_area.html)  

| Choropleth Map |
|-----|
| ![Screenshot](https://github.com/user-attachments/assets/aed26ad0-bea7-423b-a275-c6c5400abc40) |

🔗 **Choropleth Access Score Map**  
View grocery access scores by community area: [Access Score Choropleth](https://oliviadavis593.github.io/ChiFoodScape/access_score_choropleth.html)

|  Access Score Map |
|-----|
<img width="1451" alt="Screenshot 2025-06-03 at 11 15 49 PM" src="https://github.com/user-attachments/assets/e3dc5584-c3dd-4d51-8386-89d741275bf8" />


---

## 🔍 Mapping Reality vs. Official Records

City datasets often lump together gas stations, dollar stores, and corner marts alongside full-service grocers — masking food access gaps.

ChiFoodScape filters, classifies, and reviews stores to build a **“reality map”** of Chicago’s food infrastructure, enabling targeted insights around equity and access.

---

## Current Scope (V1): Grocery Store Mapping
✅ Built:
- Loads filtered inspection data (Chicago Data Portal)
- Flags real vs. junk stores
- Deduplicates by address/name
- Allows manual classification of edge cases
- Fully reviewed unclassified stores by neighborhood
- Fully reviewed junk stores by neighborhood
- Generates interactive maps + access scores
- Exports ZIP and community area summaries

---

##  Project Structure
| Notebook                                      | Purpose |
|----------------------------------------------|---------|
| `01_data_cleaning.ipynb`                     | Clean raw urban agriculture data |
| `01d_clean_grocery_stores.ipynb`             | Clean, deduplicate, and classify grocery stores |
| `03_visualizations.ipynb`                    | Build interactive map with clustering |
| `04_geo_join_by_area.ipynb`                  | Spatially join stores to community areas |
| `05_unclassified_review.ipynb`               | Export unclassified stores per neighborhood for review |
| `05_junk_review.ipynb`                       | Export junk stores per neighborhood for review |
| `06_choropleth_by_area.ipynb`                | Create choropleth showing store density |
| `07_generate_access_scores.ipynb`            | Render choropleth of access scores per area |
| `07_merge_unclassified_reviewed_csvs.ipynb`  | Merge manually reviewed unclassified stores |
| `07_merge_junk_reviewed_csvs.ipynb`          | Merge manually reviewied junk stores |
| `clean_urban_ag_sites.ipynb`                 | Refine and clean urban agriculture site data |


---

## Output Files
| File                                | Description |
|------------------------------------|-------------|
| `grocery_stores_chicago_map_v1.html` | Interactive map |
| `grocery_choropleth_by_area.html`    | Updated store density map |
| `access_score_choropleth.html`       | Access score map |
| `grocery_stores_cleaned_v1.csv`      | Fully deduplicated + classified dataset |
| `community_area_scores.csv`          | Access score table by community area |

---

## ⚙️ How It Works: Notebook Order by Output

This project includes three key visual outputs:  
🗺️ **Interactive Store Map**, 📊 **Store Count Choropleth**, and 📊 **Access Score Choropleth**.

Each map relies on a chain of notebooks. Here's how to run the full pipeline:

---

### 1. Interactive Store Map  
**Output**: `grocery_stores_chicago_map_v1.html`

**Run Order**:
1. `01d_clean_grocery_stores.ipynb`  ← cleans, deduplicates, and classifies stores
2. `05_unclassified_review.ipynb`  ← exports unclassified stores by community for manual review
3. *(Manual Step)*: Review the CSVs in `data/unclassified_review/`
4. `07_merge_unclassified_reviewed_csvs.ipynb` ← updates original dataset with reviewed labels
5. `03_visualizations.ipynb` ← builds interactive map with color-coded clustering by store type

---

### 2. Grocery Store Choropleth  
**Output**: `grocery_choropleth_by_area.html`

**Run Order**:
1. `04_geo_join_by_area.ipynb` ← spatial join: map stores to Chicago community areas
2. `06_choropleth_by_area.ipynb` ← aggregates store counts + renders density map

---

### 3. Grocery Access Score Choropleth  
**Output**: `access_score_choropleth.html`

**Run Order**:
1. `02_access_score.ipynb` ← calculates access score per area (0–4 scale)
2. `07_generate_access_scores.ipynb` ← builds labeled choropleth using `AccessScore`


---

### 📤 Deployment Notes
- All `.html` maps are saved to `/docs/` and served via GitHub Pages
- Make sure you commit new versions of those files after running
- Test locally by opening `docs/index.html` or pushing live to GitHub

---


## ✅ Current Status
- [x] Clean & label data
- [x] Deduplicate
- [x] Interactive map w/ tooltips
- [x] Choropleth by community area
- [x] Access score choropleth
- [x] Reviewed all previously unclassified stores
- [x] Merged reviewed store classifications
- [x] Updated all map outputs
- [x] Junk store re-review
- [ ] Real store re-review
- [ ] Food access gap analysis
- [ ] Introduce helper-text across maps for users (e.g., MarkerCluster coloring reasoning)

---

## 🧠 Future Features (V2+ Vision)
- Add food access scores normalized by population (per capita)
- Overlay food deserts (e.g., USDA-defined or custom)
- Incorporate compost drop-off sites and urban farms into the map
- Compare official licensing data to observed reality (spot mismatches)
- Enable inspection result filtering (e.g., Pass/Fail/Out of Business)
- Add filter and search tools to the map UI (e.g., by ZIP, store name)
- Explore mobile-optimized, public-facing dashboard version
- Integrate user-facing explanations into maps (e.g., what access scores mean, marker color logic)

---

## 🤔 Framing Questions
- What does food access *actually* look like in your neighborhood?
- How many real grocery stores are within a mile of your block?
- Why does the city count corner stores and 7-Elevens the same as Aldi or Mariano’s?
- Who gets access to fresh food—and who never did?

---

## Notes
- `grocery_keywords` and `junk_keywords` are editable in `01b_clean_grocery_stores.ipynb`
- Data transformations use **Pandas**
- Maps are rendered with **Folium** (Leaflet.js)
- Spatial joins and shapes rely on **GeoPandas**

---

*Built with public data. Inspired by public good.*
