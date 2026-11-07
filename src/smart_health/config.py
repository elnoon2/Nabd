from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_CLEAN = ROOT / "data" / "cleaned"
DB_PATH = ROOT / "data" / "smart_health.db"
GRAPH_CACHE = DATA_RAW / "cairo_graph.graphml"

SEED = 42
PLACE = "Cairo, Egypt"
MAX_SPEED_KMH = 120.0           # for admissible heuristic
DONOR_MAX_MINUTES = 45
MIN_DAYS_BETWEEN_DONATIONS = 56
DONOR_AGE_RANGE = (18, 60)
DONOR_MIN_WEIGHT_KG = 50
MISMATCH_PENALTY = 1e6          # minutes; effectively excludes a hospital

SPECIALTIES = ["emergency", "cardiology", "trauma", "pediatrics", "neurology", "obstetrics"]
