import csv
from pathlib import Path

import pytest

from src.compliance_evaluator import evaluate_batch, evaluate_scenario, is_compliant


def load_scenarios():
    path = Path(__file__).with_name("sample_scenarios.csv")
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


@pytest.mark.parametrize(
    "control_id,observed,expected",
    [
        ("IAM-01", "true", True),
        ("IAM-01", "false", False),
        ("DEV-02", "30", True),
        ("DEV-02", "31", False),
        ("POL-01", "14", True),
        ("POL-01", "13", False),
        ("EDR-01", "active", True),
        ("EDR-01", "inactive", False),
    ],
)
def test_rule_boundaries(control_id, observed, expected):
    assert is_compliant(control_id, observed) is expected


def test_all_controlled_scenarios_classify_correctly():
    summary = evaluate_batch(load_scenarios())
    assert summary["total"] == 20
    assert summary["accuracy"] == 1.0
    assert summary["exception_detection_rate"] == 1.0
    assert summary["false_positives"] == 0
    assert summary["false_negatives"] == 0


def test_csv_boolean_values_are_normalized():
    result = evaluate_scenario(
        {
            "test_id": "BOOL-1",
            "control_id": "DEV-01",
            "observed_value": "true",
            "expected_label": "COMPLIANT",
        }
    )
    assert result["actual_label"] == "COMPLIANT"


def test_unknown_control_is_rejected():
    with pytest.raises(KeyError):
        is_compliant("UNKNOWN", "true")


def test_empty_batch_is_rejected():
    with pytest.raises(ValueError):
        evaluate_batch([])
