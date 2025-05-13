# 🛒 Chicago Food Access Map

## 🎯 Project Goal

Build a clean, interactive map of **Chicago grocery stores** using food inspection data.  
This map aims to:

- Show only **real grocery stores**, not junk/low-nutrition retailers
- Remove **duplicates** from multiple inspections per site
- Support **interactive visualization** with tooltips and clustering
- Be exportable as an `.html` file for community use

---

## 🗂️ Project Structure & Notebooks

| Notebook                            | Purpose                                                                 |
|-------------------------------------|-------------------------------------------------------------------------|
| `01_data_cleaning.ipynb`            | Loads raw inspection data and drops unusable rows (e.g. no coordinates) |
| `01b_clean_grocery_stores.ipynb`    | Adds `IS_REAL_GROCERY` and `IS_JUNK_STORE` flags based on store names  |
| `01d_clean_grocery_stores.ipynb`    | Merges cleaned data + labels, deduplicates rows, and outputs clean file |
| `03_visualizations.ipynb`           | Creates full map of all stores (real, junk, unknown) with color-coded pins |
| `03_visualizations_by_zip_v1.ipynb` | Adds ZIP-level summaries of store counts by type, exports CSV           |
| `02_access_score.ipynb`             | (Optional) Score access based on distance and availability               |
| `clean_urban_ag_sites.ipynb`        | (Future phase) For mapping compost drop-off or urban agriculture sites  |

---

## 📂 Key Data Files

| File Name                          | Description                                          |
|------------------------------------|------------------------------------------------------|
| `food_inspections_filtered.csv`    | Raw export from Chicago Data Portal                 |
| `grocery_stores_labeled.csv`       | Adds real/junk flags to full dataset                |
| `updated_grocery_stores.csv`       | Deduplicated, filtered list of just valid grocery stores |
| `grocery_stores_cleaned_v1.csv`    | Current V1 clean grocery-only export                |
| `grocery_stats_by_zip.csv`         | Aggregated store count by ZIP code                  |
| `grocery_stores_chicago_map.html`  | Interactive exported Folium map                     |

---

## ✅ Current Status

- [x] Cleaned and filtered food inspections
- [x] Labeled stores using grocery/junk keyword logic
- [x] Deduplicated per location
- [x] Visualized in `folium` with `MarkerCluster`
- [x] Grouped stores by ZIP
- [x] Exported summary table
- [x] Saved interactive map to HTML

---

## 🔜 Upcoming Work (V1 Completion)

1. **📦 Improve Labeling Logic**
   - Fix cases like `Whole Foods #123`, `Costco Wholesale`, etc.
   - Use fuzzy matching or regex if needed
   - Optionally leverage external grocery lists or NAICS codes

2. **📍 Add Map Interactivity**
   - Show address, inspection result, or DBA in tooltip/popups
   - Consider “hover” effects if using advanced libraries later

3. **📊 Add Community Area Summaries**
   - Download Chicago community shapefile
   - Use `geopandas` to join stores to community areas
   - Export: `grocery_stats_by_area.csv`

4. **🌐 Export Views**
   - `grocery_map_real.html`: real groceries only
   - `grocery_map_junk.html`: junk stores only (optional)
   - `grocery_map_combined.html`: all types

5. **🧪 Optional Enhancements**
   - Add filter by “inspection result” (e.g. `Pass`)
   - Include violations in popup
   - Later: Add farm, compost overlays + access scoring

---

## 🧼 Cleanup Recommendations

### ✅ Keep

- `01_data_cleaning.ipynb`
- `01b_clean_grocery_stores.ipynb`
- `01d_clean_grocery_stores.ipynb`
- `03_visualizations.ipynb`
- `03_visualizations_by_zip_v1.ipynb`
- `02_access_score.ipynb` (optional)
- `clean_urban_ag_sites.ipynb` (optional)

### 🗑️ Safe to Delete

- `01c_clean_grocery_stores.ipynb` (if replaced by `01d`)
- `grocery_stores_labeled-checkpoint.csv`, `.ipynb_checkpoints`, etc.
- Any unused `.csv` version duplicates that aren't tracked intentionally

---

## 🧠 Notes for Future Phases

- Overlay **food desert shapefiles**
- Add **farm/compost drop-off points**
- Build a **multi-layer access scoring dashboard**
- Deploy map using `Streamlit`, `Flask`, or GitHub Pages

best-practice pipeline: clean ➝ dedupe ➝ enrich ➝ visualize