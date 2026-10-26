"""Service layer connecting request validation, rule evaluation, and evidence storage."""

from .compliance_evaluator import evaluate_scenario
from .database import fetch_results, save_result


def evaluate_and_store(payload, db_path):
    if not isinstance(payload, dict):
        raise TypeError("payload must be a dictionary")
    if "control_id" not in payload or "observed_value" not in payload:
        raise ValueError("control_id and observed_value are required")

    expected = str(payload.get("expected_label", "COMPLIANT")).strip().upper()
    scenario = {
        "test_id": str(payload.get("test_id", "interactive")).strip(),
        "control_id": str(payload["control_id"]).strip(),
        "observed_value": payload["observed_value"],
        "expected_label": expected,
    }

    result = evaluate_scenario(scenario)
    result["observed_value"] = payload["observed_value"]
    result["record_id"] = save_result(db_path, result)
    return result


def list_evaluations(db_path):
    return fetch_results(db_path)
