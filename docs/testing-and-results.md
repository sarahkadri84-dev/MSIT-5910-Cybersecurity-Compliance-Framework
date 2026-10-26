# Testing and Results

## Test Strategy

The project uses multiple test levels:

- Unit testing for rule boundaries, normalization, error handling, and batch metrics
- Integration testing for service -> evaluator -> SQLite communication
- System testing across twenty controlled compliant and exception states
- Acceptance testing for valid input, invalid controls, missing fields, and whitespace tolerance
- CI validation through GitHub Actions

## Controlled Results

The Unit 5 controlled scenario set produced:

- 20 scenarios evaluated
- 20 correct classifications
- 100% controlled-scenario accuracy
- 100% exception detection rate
- 0 false positives
- 0 false negatives

The Unit 7 system suite adds:

- service/evaluator/database integration
- 20 end-to-end system scenarios
- whitespace-tolerance acceptance testing
- invalid-control handling
- missing-field handling

An early CI run also exposed a Python import-path problem. The workflow was corrected by making `src` importable and setting the repository root in the CI environment. This failure-and-fix history is retained because it demonstrates real debugging and regression validation.

## Reproduce

Run:

```bash
python -m pip install pytest pytest-cov
python -m pytest -q
python run_demo.py
```

The repository contains only synthetic test data.
