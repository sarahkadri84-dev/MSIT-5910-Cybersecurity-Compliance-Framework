"""Rule-based compliance evaluator for the MSIT 5910 capstone.

The module evaluates controlled cybersecurity scenarios against documented
expected states. It intentionally uses synthetic values rather than production
employee or security data.
"""

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List


@dataclass(frozen=True)
class ControlRule:
    control_id: str
    name: str
    operator: str
    target: Any


CONTROL_CATALOG: Dict[str, ControlRule] = {
    "IAM-01": ControlRule("IAM-01", "Multifactor authentication enabled", "equals", True),
    "IAM-02": ControlRule("IAM-02", "Offboarded account disabled", "equals", "disabled"),
    "IAM-03": ControlRule("IAM-03", "Role-based access approved", "equals", "approved"),
    "IAM-04": ControlRule("IAM-04", "Privileged access review current", "equals", "current"),
    "DEV-01": ControlRule("DEV-01", "Device encryption enabled", "equals", True),
    "DEV-02": ControlRule("DEV-02", "Operating-system patch age", "max", 30),
    "DEV-03": ControlRule("DEV-03", "Device enrolled in management", "equals", True),
    "EDR-01": ControlRule("EDR-01", "SentinelOne protection active", "equals", "active"),
    "POL-01": ControlRule("POL-01", "Minimum password length", "min", 14),
    "IAM-05": ControlRule("IAM-05", "Inactive-account age", "max", 90),
}


def normalize_value(value: Any) -> Any:
    """Normalize common CSV-style scalar values before rule evaluation."""
    if not isinstance(value, str):
        return value

    cleaned = value.strip()
    lowered = cleaned.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False

    try:
        return int(cleaned)
    except ValueError:
        return lowered


def is_compliant(control_id: str, observed_value: Any) -> bool:
    """Return True when an observed value satisfies the documented control rule."""
    if control_id not in CONTROL_CATALOG:
        raise KeyError(f"Unknown control_id: {control_id}")

    rule = CONTROL_CATALOG[control_id]
    observed = normalize_value(observed_value)
    target = rule.target

    if rule.operator == "equals":
        return observed == target
    if rule.operator == "max":
        return float(observed) <= float(target)
    if rule.operator == "min":
        return float(observed) >= float(target)

    raise ValueError(f"Unsupported operator: {rule.operator}")


def evaluate_scenario(scenario: Dict[str, Any]) -> Dict[str, Any]:
    """Classify one controlled scenario and compare it with its expected label."""
    control_id = scenario["control_id"]
    expected = scenario["expected_label"].strip().upper()
    actual = "COMPLIANT" if is_compliant(control_id, scenario["observed_value"]) else "EXCEPTION"

    return {
        "test_id": scenario["test_id"],
        "control_id": control_id,
        "control_name": CONTROL_CATALOG[control_id].name,
        "expected_label": expected,
        "actual_label": actual,
        "correct": actual == expected,
    }


def evaluate_batch(scenarios: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    """Evaluate a batch and calculate accuracy and exception-detection metrics."""
    results: List[Dict[str, Any]] = [evaluate_scenario(item) for item in scenarios]
    total = len(results)
    if total == 0:
        raise ValueError("At least one scenario is required")

    correct = sum(item["correct"] for item in results)
    true_exceptions = sum(
        item["expected_label"] == "EXCEPTION" and item["actual_label"] == "EXCEPTION"
        for item in results
    )
    expected_exceptions = sum(item["expected_label"] == "EXCEPTION" for item in results)
    false_positives = sum(
        item["expected_label"] == "COMPLIANT" and item["actual_label"] == "EXCEPTION"
        for item in results
    )
    false_negatives = sum(
        item["expected_label"] == "EXCEPTION" and item["actual_label"] == "COMPLIANT"
        for item in results
    )

    return {
        "results": results,
        "total": total,
        "correct": correct,
        "accuracy": correct / total,
        "exception_detection_rate": (
            true_exceptions / expected_exceptions if expected_exceptions else 1.0
        ),
        "false_positives": false_positives,
        "false_negatives": false_negatives,
    }
