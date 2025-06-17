# ChiFoodScape: Mapping Real Food Access in Chicago

## Overview

ChiFoodScape is a civic tech project that maps and analyzes Chicago's food landscape—going beyond city records to expose the **real availability of full-service grocery stores, urban farms, and compost infrastructure**.

Using open data, spatial joins, and visual storytelling, the project aims to:
- Show which neighborhoods are structurally excluded from **fresh food**
- Visualize which areas are underserved by **composting and urban agriculture**
- Help residents, nonprofits, and city leaders target **food justice interventions**

ChiFoodScape Website (All Maps): [ChiFoodScape](https://oliviadavis593.github.io/ChiFoodScape)

---

### v2 Interactive Store Map  
A per-neighborhood clustered view with type toggles (Real, Junk, Unclassified) and on-click zoom/filter.  
**Try it:** [V2 Interactive Store Map](https://oliviadavis593.github.io/ChiFoodScape/grocery_stores_chicago_map_v2.html)  

| Map (v2) | Map (v2) | Map (v2) |
|:---------------------:|:--------------:|:--------------:
| <img width="1218" alt="Screenshot 2025-06-16 at 11 19 35 PM" src="https://github.com/user-attachments/assets/c583b3fe-3b3f-4aa7-833d-dd31aa2a55dd" /> |<img width="770" alt="Screenshot 2025-06-16 at 10 57 50 PM" src="https://github.com/user-attachments/assets/414ae5b6-acc4-4882-b231-8e05784fd65f" /> |<img width="785" alt="Screenshot 2025-06-16 at 11 21 45 PM" src="https://github.com/user-attachments/assets/a6ca6774-c438-4b9b-a6d9-118636c24c7e" />





---

### v1 Interactive Store Map  
Original Folium + MarkerCluster implementation (static clusters across the whole city).  
**Try it:** [Store Map v1](https://oliviadavis593.github.io/ChiFoodScape/grocery_stores_chicago_map_v1.html)  

| Store Map v1             |  Store Map v1  |
|:-------------------------:|:--------------:|
| ![v1-1](https://github.com/user-attachments/assets/a3e376b4-f9b8-4afd-877d-16c6fc171f6f) | ![v1-2](https://github.com/user-attachments/assets/a9a31ea1-d634-4c70-bd12-11b05eb727ca) |

---

## Choropleth Maps


🔹 **Store Density by Community Area**  
[grocery_choropleth_by_area.html](https://oliviadavis593.github.io/ChiFoodScape/grocery_choropleth_by_area.html)  

| Density Choropleth |
|:------------------:|
| ![Choropleth](https://github.com/user-attachments/assets/aed26ad0-bea7-423b-a275-c6c5400abc40) |

🔹 **Access Score Choropleth**  
[access_score_choropleth.html](https://oliviadavis593.github.io/ChiFoodScape/access_score_choropleth.html)  

| Access Score Map |
|:----------------:|
| ![AccessScore](https://github.com/user-attachments/assets/e3dc5584-c3dd-4d51-8386-89d741275bf8) |

---

## 🔍 Mapping Reality vs. Official Records

City datasets often lump together gas stations, dollar stores, and corner marts alongside full-service grocers—masking real food access gaps.

ChiFoodScape filters, classifies, and reviews stores to build a **“reality map”** of Chicago’s food infrastructure, enabling targeted insights around equity and access.

---

## Current Scope

### ✅ v1: Grocery Store Mapping  
- Load & clean inspection data  
- Flag real vs. junk vs. unclassified  
- Deduplicate by name/address  
- Manual edge-case review  
- **Interactive Map v1** (Folium + MarkerCluster)  
- Community-level **Choropleth** & **Access Score**  

### ✅ v2: Neighborhood-Interactive Map  
- Per-community clusters with type toggles  
- GeoJSON overlay + click-to-zoom/filter  
- Custom icons for each store type  
- Configurable API key via `docs/config.js`  

---

## 🧠 Future Features (v3+)

- Street-network isochrone access scoring (1 mile / 20 min isochrones → residential grid → % coverage → bucket into Very Low→Excellent)  
- Overlay USDA / custom food deserts  
- Add compost sites & urban farms  
- Inspection result filtering (Pass/Fail)  
- ZIP and store-name search UI  
- Mobile-optimized, public-facing dashboard  
- On-map helper text & legends  

---

## 🔗 v3: Network-Based Access Scoring

In **v3**, we’ll move from community-averaged counts to a **street-network coverage** model:


| Step                  | Description                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Build isochrones      | Generate 1-mile (or 20 min) walking isochrones for each store via **OSMnx** or an Isochrone API.                                  |
| Residential grid      | Sample points (~200 m) across each community polygon to approximate residential locations.                                        |
| Compute coverage      | Spatially join grid → isochrones to identify which points fall **inside** any store’s service area.                               |
| Derive metrics        | Per community: <br>• **% Covered** = covered_points / total_points<br>• (Optional) Avg. network distance to nearest N stores.     |
| Bucket categories     | Threshold % Covered: <20% = Very Low, 20–40% = Low, …, >80% = Excellent.                                                            |
| Visualize choropleth  | Update `07_generate_access_scores.ipynb` (or create `08_network_score.ipynb`) to render the new coverage field.                    |

> **Why this matters**  
> Instead of assuming “Logan Square is Excellent” because it has 22 stores, we’ll surface which blocks fall outside a 1-mile walk—proof of micro-“food deserts” in green areas.  


## Project Structure

| Notebook                                      | Purpose                                                          |
|-----------------------------------------------|------------------------------------------------------------------|
| `01_data_cleaning.ipynb`                      | Clean raw urban agriculture data                                 |
| `01d_clean_grocery_stores.ipynb`              | Clean, deduplicate, and classify grocery stores                  |
| `03_visualizations.ipynb`                     | Build interactive map with clustering                            |
| `04_geo_join_by_area.ipynb`                   | Spatially join stores to community areas                         |
| `05_unclassified_review.ipynb`                | Export unclassified stores per neighborhood for review           |
| `05_junk_review.ipynb`                        | Export junk stores per neighborhood for review                   |
| `05_real_review.ipynb`                        | Export real stores per neighborhood for review                   |
| `06_choropleth_by_area.ipynb`                 | Create choropleth showing store density                          |
| `07_generate_access_scores.ipynb`             | Render choropleth of access scores per area                      |
| `07_merge_unclassified_reviewed_csvs.ipynb`   | Merge manually reviewed unclassified stores                      |
| `07_merge_junk_reviewed_csvs.ipynb`           | Merge manually reviewed junk stores                              |
| `clean_urban_ag_sites.ipynb`                  | Refine and clean urban agriculture site data                     |

---

## Output Files

| File                                           | Description                                         |
|-----------------------------------------------:|-----------------------------------------------------|
| `docs/grocery_stores_chicago_map_v1.html`      | v1 Folium-based interactive store map               |
| `docs/grocery_stores_chicago_map_v2.html`      | v2 Neighborhood-click interactive store map         |
| `docs/grocery_choropleth_by_area.html`         | Store density choropleth by community area          |
| `docs/access_score_choropleth.html`            | Grocery access score choropleth                     |
| `data/cleaned/grocery_stores_cleaned_v3.csv`   | Cleaned & classified store dataset                  |
| `data/geo/community_areas.geojson`             | Chicago community area boundaries                   |

---

## How to Run Locally

1. **Clone & install**  
   ```bash
   git clone https://github.com/oliviadavis593/ChiFoodScape.git
   cd ChiFoodScape
   pip install -r requirements.txt


## ⚙️ How It Works: Notebook Order by Output

This project includes three key visual outputs:  
🗺️ **Interactive Store Map**, 📊 **Store Count Choropleth**, and 📊 **Access Score Choropleth**.  

Each map relies on a chain of notebooks. Here's how to run the full pipeline:

---

### 1. Interactive Store Map  
**Output**: `grocery_stores_chicago_map_v1.html`

**Run Order**:
1. `01d_clean_grocery_stores.ipynb` ← cleans, deduplicates, and classifies stores  
2. `05_unclassified_review.ipynb` ← exports unclassified stores by community for manual review  
3. *(Manual Step)*: Review the CSVs in `data/unclassified_review/`  
4. `07_merge_unclassified_reviewed_csvs.ipynb` ← updates original dataset with reviewed labels  
5. `03_visualizations.ipynb` ← builds interactive map with color-coded clustering by store type  

---

### 2. Grocery Store Choropleth  
**Output**: `grocery_choropleth_by_area.html`

**Run Order**:
1. `04_geo_join_by_area.ipynb` ← spatial join: map stores to Chicago community areas  
2. `06_choropleth_by_area.ipynb` ← aggregates store counts & renders density map  

---

### 3. Grocery Access Score Choropleth  
**Output**: `access_score_choropleth.html`

**Run Order**:
1. `02_access_score.ipynb` ← calculates access score per area (0–4 scale)  
2. `07_generate_access_scores.ipynb` ← builds labeled choropleth using `AccessScore`  

---

### 📤 Deployment Notes
- All `.html` maps are saved to `/docs/` and served via GitHub Pages  
- After running, commit updated files in `docs/`  
- Test locally by opening `docs/index.html` or pushing live to GitHub  

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
