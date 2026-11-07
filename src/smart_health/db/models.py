import sqlite3
from smart_health import config


def get_conn():
    con = sqlite3.connect(config.DB_PATH)
    con.row_factory = sqlite3.Row
    return con
