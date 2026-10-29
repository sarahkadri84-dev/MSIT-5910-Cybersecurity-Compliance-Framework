# Professional Portfolio Guide

This repository is the portfolio version of the MSIT 5910 capstone **Cybersecurity Compliance Monitoring Framework Using Rippling IT**.

## Start Here

- [Project overview](docs/project-overview.md)
- [Architecture diagram](architecture.png)
- [Core evaluator](src/compliance_evaluator.py)
- [Integrated service layer](src/service.py)
- [SQLite evidence store](src/database.py)
- [Synthetic scenarios](tests/sample_scenarios.csv)
- [Automated tests](tests/)
- [Testing and results](docs/testing-and-results.md)
- [Results summary](results/README.md)
- [Performance summary](results/performance-summary.md)
- [Security and privacy](docs/security-and-privacy.md)
- [Deployment and maintenance](docs/deployment-and-maintenance.md)
- [Prototype workflow visual](screenshots/prototype-workflow.svg)
- [Batch demo](run_demo.py)
- [Integrated service + SQLite demo](presentation_demo.py)
- [Demo walkthrough](demo/README.md)
- [Sanitized research report](reports/research-report.md)
- [Capstone report portfolio summary](reports/capstone-report-summary.md)

## Verified Final Evidence

- 39 automated tests passing
- 100% source-code coverage enforced in GitHub Actions
- 20/20 controlled classifications correct
- 100% controlled accuracy and exception detection
- 0 false positives and 0 false negatives
- 500/500 performance-test records persisted
- ~1.54 ms mean latency and ~1.85 ms P95 latency in the documented local academic test
- ~650 evaluations/second in the same local test environment

These metrics are synthetic/local academic evaluation results and are not production certification or capacity claims.

## Skills Demonstrated

Python, rule-based compliance evaluation, SQLite, Git/GitHub, continuous integration, PyTest, system and regression testing, debugging, cybersecurity architecture, NIST CSF 2.0 alignment, privacy-aware documentation, deployment planning, and maintenance planning.

## Portfolio Safety

Only synthetic or sanitized artifacts belong in this repository. Production credentials, employee data, confidential configurations, and sensitive security telemetry must not be published.
