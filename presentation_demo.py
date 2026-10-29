"""Integrated presentation demo for the MSIT 5910 capstone.

Run from the repository root:
    python presentation_demo.py

This demo uses synthetic observations only. It evaluates two controls through the
service layer, persists the results to SQLite, and reads the evidence records back.
"""
from pathlib import Path
from src.service import evaluate_and_store, list_evaluations

DB = Path("presentation_demo.db")
if DB.exists():
    DB.unlink()

samples = [
    {
        "test_id": "demo-compliant",
        "control_id": " IAM-01 ",
        "observed_value": True,
        "expected_label": "COMPLIANT",
    },
    {
        "test_id": "demo-exception",
        "control_id": "DEV-02",
        "observed_value": 45,
        "expected_label": "EXCEPTION",
    },
]

print("Integrated Compliance Demo")
print("=" * 34)
for sample in samples:
    result = evaluate_and_store(sample, DB)
    print(
        f"{result['test_id']}: {result['control_id']} -> "
        f"{result['actual_label']} (record_id={result['record_id']})"
    )

print("\nPersisted SQLite evidence")
print("-" * 34)
for row in list_evaluations(DB):
    print(row)

print(f"\nDatabase created: {DB.resolve()}")
