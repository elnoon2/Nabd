# Smart Hospital and Blood Donor Finder
Integrated Mega Project, Fall 2026 | AI 306, CS 312, CO 208 | Badya University

Team: Youssef Essam (PM), Nour elcassy (Data/Stats), Mohamed osama (AI), Toqa Waleed (DB/Web), Nada Moataz (Quality/Docs)

> Decision-support tool only. In an emergency call the ambulance: **123**.

## Structure
| Path | Purpose |
|---|---|
| `data/` | Raw and cleaned data + `data_dictionary.md` |
| `notebooks/` | EDA and statistical analysis |
| `src/smart_health/` | Pipeline, AI component (A* + rules), evaluation, DB, web app |
| `tests/` | Automated tests |
| `docs/` | Proposal, diagrams, report, AI-use statement |

## Installation
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export PYTHONPATH=src                                # Windows PowerShell: $env:PYTHONPATH="src"
```

## Run the pipeline
```bash
python -m smart_health.data.osm_loader        # download + cache Cairo graph and hospitals
python -m smart_health.data.generate_data     # seeded synthetic wait logs, donors, requests
python -m smart_health.data.clean             # cleaned CSVs in data/cleaned
python -m smart_health.db.load_db             # create SQLite DB from schema.sql
python -m smart_health.evaluation.scenarios   # 1,000+ scenarios, A* vs baselines
```

## Run the web app
```bash
flask --app smart_health.web.app run
```
Open http://127.0.0.1:5000

## Tests
```bash
pytest
```

## Docker (optional bonus)
```bash
docker build -t smart-health .
docker run -p 5000:5000 smart-health
```

## Data licences
Road network and hospitals: OpenStreetMap contributors, ODbL. All other data is synthetic; no real people.
