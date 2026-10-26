# Demo Walkthrough

A reviewer can reproduce the current text-based demonstration locally.

## Run the demo

```bash
python run_demo.py
```

The demo loads the synthetic scenario dataset, evaluates each control state, and prints:

- number of scenarios evaluated
- correct classifications
- accuracy
- exception-detection rate
- false positives
- false negatives
- sample individual results

## Suggested 2-minute portfolio walkthrough

1. Explain the fragmented-control-monitoring problem.
2. Show the five-layer architecture.
3. Open `src/compliance_evaluator.py` and explain the rule catalog.
4. Run `python run_demo.py`.
5. Open the automated tests and GitHub Actions workflow.
6. Explain the privacy decision to publish only synthetic data.
7. Close with limitations and future authorized API integration.

A recorded video can be linked here later without changing the technical repository structure.
