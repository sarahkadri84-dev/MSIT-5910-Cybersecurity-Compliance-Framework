"""Lightweight evaluator for synthetic capstone test scenarios."""

def evaluate_control(actual, expected):
    return "PASS" if actual == expected else "EXCEPTION"


def evaluate_scenario(scenario):
    return {
        "control_id": scenario["control_id"],
        "result": evaluate_control(scenario["actual"], scenario["expected"]),
    }
