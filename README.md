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
View updated store density map: [Choropleth Map](https://oliviadavis593.github.io/ChiFoodScape/grocery_choropleth_by_area.html)  

🗺️ **Choropleth Map**  
| Map |
|-----|
| ![Screenshot](https://github.com/user-attachments/assets/aed26ad0-bea7-423b-a275-c6c5400abc40) |

🔗 **Choropleth Access Score Map**  
View grocery access scores by community area: [Access Score Choropleth](https://oliviadavis593.github.io/ChiFoodScape/access_score_choropleth.html)

| Map |
|-----|
<img width="786" alt="Screenshot 2025-05-25 at 10 17 46 AM" src="https://github.com/user-attachments/assets/cf40d511-1647-4e99-9de9-20336b7ddaf4" />

---

## 🔍 Two-Map Framework: *City vs. Reality*
**Map 1 – City Map**  
🟡 Includes gas stations, dollar stores, 7-Elevens.

**Map 2 – Reality Map**  
🟢 Filters to real grocery stores with fresh produce and essentials.

These maps reveal the **gap between official data and actual access**—particularly in historically excluded communities.

---

## 🗂️ Current Scope (V1): Grocery Store Mapping
✅ Built:
- Loads filtered inspection data (Chicago Data Portal)
- Flags real vs. junk stores
- Deduplicates by address/name
- Generates interactive map
- Exports ZIP summaries (`real`, `junk`, `unclassified`)

---

## 🔨 Project Structure
| Notebook                                | Purpose |
|----------------------------------------|---------|
| `01_data_cleaning.ipynb`               | Clean raw data |
| `01b_clean_grocery_stores.ipynb`       | Flag real/junk stores |
| `01d_clean_grocery_stores.ipynb`       | Merge & deduplicate |
| `01e_clean_filtered_grocery_stores.ipynb` | Refine filtering |
| `02_access_score.ipynb`                | Develop scoring logic |
| `07_generate_access_scores.ipynb`      | Generate access scores |
| `03_visualizations.ipynb`              | Build interactive map |
| `04_geo_join_by_area.ipynb`            | Join stores to community areas |
| `05b_review_real_grocery_stores.ipynb` | Audit real store flags |
| `06_choropleth_by_area.ipynb`          | Create store density choropleth |
| `clean_urban_ag_sites.ipynb`           | Clean urban ag data |

---

## 📦 Output Files
| File                                | Description |
|------------------------------------|-------------|
| `grocery_stores_chicago_map_v1.html` | Interactive map |
| `grocery_choropleth_by_area.html`    | Updated store density map |
| `access_score_choropleth.html`       | Access score map |
| `grocery_stores_cleaned_v1.csv`      | Deduplicated dataset |
| `community_area_scores.csv`          | Access score table |

---

## ✅ Current Status
- [x] Clean & label data
- [x] Deduplicate
- [x] Interactive map w/ tooltips
- [x] Choropleth by community area
- [x] Access score choropleth
- [x] Automate updates (move HTML to `/docs`)
- [ ] Systematic review of unclassified stores
- [ ] Food access gap analysis

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
