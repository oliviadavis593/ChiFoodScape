# 📦 Imports
import pandas as pd
import os
import re

# 📍 File paths
RAW_PATH = '../data/raw/urban_agriculture_sites.csv'
FIXED_PATH = '../data/cleaned/urban_agriculture_sites_cleaned.csv'

# 📥 Load file (no headers)
df = pd.read_csv(RAW_PATH, header=None, names=['Raw'])

# 🧪 Preview first few lines
print("🔍 Sample rows:")
print(df.head())

# 🧹 Clean up lat/lon strings
# Extract two numbers from each string: (e.g., '9661725, -87.64...')
df[['Y', 'X']] = df['Raw'].str.extract(r'([\d\.]+),\s*(-?[\d\.]+)')

# Convert to float
df['X'] = pd.to_numeric(df['X'], errors='coerce')  # longitude
df['Y'] = pd.to_numeric(df['Y'], errors='coerce')  # latitude or projected

# Drop rows with parsing failures
df = df.dropna(subset=['X', 'Y'])

# 🧠 Heuristic check: are these X/Y values in WGS84 or projected?
if df['Y'].max() > 90:  # latitude should never be > 90
    print("⚠️ These coordinates are probably in a projected format — not usable directly for mapping.")
    print("❗ Please confirm if these are State Plane or another projection.")
else:
    print("✅ Coordinates appear to be WGS84 (standard lat/lon)")

# 📝 Rename to match your other files
df = df.rename(columns={'X': 'Longitude', 'Y': 'Latitude'})

# 📉 Drop duplicates or invalids
df = df[(df['Latitude'] != 0) & (df['Longitude'] != 0)]
df = df.drop_duplicates(subset=['Latitude', 'Longitude'])

# Add placeholder fields so it matches expected structure
df['Site Name'] = 'Urban Farm'
df['City'] = 'Chicago'
df['Zip'] = ''
df['Site Type'] = 'Urban Agriculture'

# Reorder columns
df = df[['Site Name', 'City', 'Zip', 'Latitude', 'Longitude', 'Site Type']]

# 💾 Save cleaned version
os.makedirs(os.path.dirname(FIXED_PATH), exist_ok=True)
df.to_csv(FIXED_PATH, index=False)
print(f"✅ Cleaned urban ag data saved to: {FIXED_PATH}")
print(f"🧮 Final row count: {df.shape[0]}")
