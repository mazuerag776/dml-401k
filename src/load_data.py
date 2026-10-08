from doubleml.datasets import fetch_401K
from paths import DATA_DIR

# Load dataset
data = fetch_401K(return_type="DataFrame")

# Save dataset to CSV
data.to_csv(DATA_DIR / "401k.csv", index=False)

print("Dataset saved successfully.")
