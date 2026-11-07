"""Create SQLite DB from schema.sql (then load cleaned CSVs)."""
import sqlite3
from pathlib import Path
from smart_health import config


def main():
    schema = (Path(__file__).parent / "schema.sql").read_text()
    with sqlite3.connect(config.DB_PATH) as con:
        con.executescript(schema)
    print("Created", config.DB_PATH)
    # TODO: insert specialties, blood_types, and load cleaned CSVs


if __name__ == "__main__":
    main()
