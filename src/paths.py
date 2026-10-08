from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"
NOTEBOOKS_DIR = ROOT / "notebooks"
SRC_DIR = ROOT / "src"

# Ensure output directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
