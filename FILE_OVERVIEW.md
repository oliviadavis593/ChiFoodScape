| **Notebook**                               | **Purpose**                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| `01_data_cleaning.ipynb`                  | Core pipeline to clean raw food inspection data (drops nulls, trims).      |
| `01b_clean_grocery_stores.ipynb`          | Adds `IS_REAL_GROCERY` and `IS_JUNK_STORE` flags based on name keywords.   |
| `01d_clean_grocery_stores.ipynb`          | Final merge: joins labels with inspection records + prepares for mapping.  |
| `01e_clean_filtered_grocery_stores.ipynb` | Loads export from portal (2,300 rows), deduplicates to ~1,600 true stores. |
| `02_access_score.ipynb`                   | (Optional) Computes access scores per ZIP/community. Useful in V2.         |
| `03_visualizations.ipynb`                 | Basic map with color-coded pins using Folium + MarkerCluster.              |
| `03_visualizations_by_zip_v1.ipynb`       | ZIP-level summary: counts real, junk, unclassified grocery stores.         |
| `clean_urban_ag_sites.ipynb`              | Prepares urban agriculture dataset. Not used in V1 but retained.           |

### 📌 Future Notebooks (Planned)

| **Notebook**                                | **Planned Purpose**                                                              |
|--------------------------------------------|----------------------------------------------------------------------------------|
| `04_visualizations_by_community.ipynb`     | Spatially joins grocery stores to community areas using a shapefile.            |
| `05_clean_compost_sites.ipynb`             | Loads and standardizes compost drop-off locations.                              |
| `06_clean_food_deserts.ipynb`              | Prepares food desert shapefiles or boundaries for overlays.                     |
| `07_merged_all_sites_view.ipynb`           | Combines groceries + compost + farms into one dataset for unified visualization.|
| `08_grocery_gap_analysis.ipynb`            | Detects “gaps” where no real grocery exists within a certain radius.            |
| `09_export_static_assets.ipynb`            | Converts maps and summaries into shareable `.html` and `.csv` exports.          |
