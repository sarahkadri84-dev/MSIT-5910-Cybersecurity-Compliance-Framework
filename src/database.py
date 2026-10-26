"""SQLite evidence store for the integrated capstone prototype."""

import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id TEXT NOT NULL,
    control_id TEXT NOT NULL,
    observed_value TEXT NOT NULL,
    expected_label TEXT NOT NULL,
    actual_label TEXT NOT NULL,
    correct INTEGER NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


def init_db(db_path):
    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as conn:
        conn.execute(SCHEMA)
        conn.commit()


def save_result(db_path, result):
    init_db(db_path)
    with sqlite3.connect(db_path) as conn:
        cur = conn.execute(
            """INSERT INTO evaluations
               (test_id, control_id, observed_value, expected_label, actual_label, correct)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                result["test_id"],
                result["control_id"],
                str(result["observed_value"]),
                result["expected_label"],
                result["actual_label"],
                int(result["correct"]),
            ),
        )
        conn.commit()
        return cur.lastrowid


def fetch_results(db_path):
    init_db(db_path)
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        return [
            dict(row)
            for row in conn.execute(
                """SELECT id, test_id, control_id, observed_value, expected_label,
                          actual_label, correct
                   FROM evaluations
                   ORDER BY id"""
            )
        ]
