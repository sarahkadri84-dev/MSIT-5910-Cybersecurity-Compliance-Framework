# Results

## Controlled Scenario Evaluation

The controlled test dataset contains 20 representative compliant and exception states across identity, access, device, endpoint, and policy controls.

Reported controlled results:

| Metric | Result |
|---|---:|
| Scenarios evaluated | 20 |
| Correct classifications | 20 |
| Accuracy | 100% |
| Exception detection rate | 100% |
| False positives | 0 |
| False negatives | 0 |

These values describe the synthetic academic test set and should not be interpreted as production-security effectiveness.

## Additional Evidence

- Unit and boundary tests: [tests/test_compliance_evaluator.py](../tests/test_compliance_evaluator.py)
- Integration/system/acceptance tests: [tests/test_system.py](../tests/test_system.py)
- Test methodology: [docs/testing-and-results.md](../docs/testing-and-results.md)
