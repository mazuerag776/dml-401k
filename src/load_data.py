from pathlib import Path
from doubleml.datasets import fetch_401K

# Creates a root directory based on the assumption that this file 
# lives one directory below the project root
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# Creating data directory if necessary
DATA_DIR.mkdir(exist_ok=True)

# Load dataset
data = fetch_401K(return_type="DataFrame")

# Save dataset to CSV
data.to_csv(DATA_DIR / "401k.csv", index=False)

print("Dataset saved successfully.")
