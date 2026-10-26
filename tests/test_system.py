from pathlib import Path

import pytest

from src.service import evaluate_and_store, list_evaluations


SCENARIOS = [
    ("IAM-01", "true", "COMPLIANT"),
    ("IAM-01", "false", "EXCEPTION"),
    ("IAM-02", "disabled", "COMPLIANT"),
    ("IAM-02", "active", "EXCEPTION"),
    ("IAM-03", "approved", "COMPLIANT"),
    ("IAM-03", "excessive", "EXCEPTION"),
    ("IAM-04", "current", "COMPLIANT"),
    ("IAM-04", "overdue", "EXCEPTION"),
    ("DEV-01", "true", "COMPLIANT"),
    ("DEV-01", "false", "EXCEPTION"),
    ("DEV-02", "30", "COMPLIANT"),
    ("DEV-02", "31", "EXCEPTION"),
    ("DEV-03", "true", "COMPLIANT"),
    ("DEV-03", "false", "EXCEPTION"),
    ("EDR-01", "active", "COMPLIANT"),
    ("EDR-01", "inactive", "EXCEPTION"),
    ("POL-01", "14", "COMPLIANT"),
    ("POL-01", "13", "EXCEPTION"),
    ("IAM-05", "90", "COMPLIANT"),
    ("IAM-05", "91", "EXCEPTION"),
]


def test_integration_service_evaluator_database(tmp_path):
    db = tmp_path / "integration.db"
    result = evaluate_and_store(
        {
            "test_id": "INT-01",
            "control_id": "IAM-01",
            "observed_value": "false",
            "expected_label": "EXCEPTION",
        },
        db,
    )
    rows = list_evaluations(db)
    assert result["actual_label"] == "EXCEPTION"
    assert len(rows) == 1
    assert rows[0]["correct"] == 1


@pytest.mark.parametrize("control_id, observed, expected", SCENARIOS)
def test_system_end_to_end_scenarios(tmp_path, control_id, observed, expected):
    db = tmp_path / f"{control_id.replace('-', '_')}.db"
    result = evaluate_and_store(
        {
            "test_id": f"SYS-{control_id}",
            "control_id": control_id,
            "observed_value": observed,
            "expected_label": expected,
        },
        db,
    )
    assert result["actual_label"] == expected


def test_acceptance_whitespace_tolerance(tmp_path):
    result = evaluate_and_store(
        {
            "test_id": "ACC-01",
            "control_id": " IAM-01 ",
            "observed_value": "false",
            "expected_label": "EXCEPTION",
        },
        tmp_path / "acceptance.db",
    )
    assert result["actual_label"] == "EXCEPTION"


def test_acceptance_invalid_control_is_rejected(tmp_path):
    with pytest.raises(KeyError):
        evaluate_and_store(
            {
                "test_id": "ACC-02",
                "control_id": "UNKNOWN",
                "observed_value": "true",
                "expected_label": "COMPLIANT",
            },
            tmp_path / "invalid.db",
        )


def test_acceptance_missing_field_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        evaluate_and_store(
            {"test_id": "ACC-03", "control_id": "IAM-01"},
            tmp_path / "missing.db",
        )


def test_acceptance_non_dictionary_payload_is_rejected(tmp_path):
    with pytest.raises(TypeError):
        evaluate_and_store(
            "not-a-dictionary",
            tmp_path / "type_error.db",
        )
