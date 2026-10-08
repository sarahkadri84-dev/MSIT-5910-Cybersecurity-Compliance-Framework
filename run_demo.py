import csv
from pathlib import Path

from src.compliance_evaluator import evaluate_batch


def main():
    path = Path("tests/sample_scenarios.csv")
    with path.open(newline="") as handle:
        scenarios = list(csv.DictReader(handle))

    summary = evaluate_batch(scenarios)
    print("Cybersecurity Compliance Evaluation")
    print("-" * 38)
    print(f"Scenarios evaluated: {summary['total']}")
    print(f"Correct classifications: {summary['correct']}")
    print(f"Accuracy: {summary['accuracy']:.0%}")
    print(f"Exception detection rate: {summary['exception_detection_rate']:.0%}")
    print(f"False positives: {summary['false_positives']}")
    print(f"False negatives: {summary['false_negatives']}")
    print("\nSample results:")
    for item in summary["results"][:6]:
        print(
            f"{item['test_id']} | {item['control_id']} | "
            f"expected={item['expected_label']} | actual={item['actual_label']} | "
            f"correct={item['correct']}"
        )


if __name__ == "__main__":
    main()
