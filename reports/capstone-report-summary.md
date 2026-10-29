# Capstone Report - Portfolio Summary

## Title

**Cybersecurity Compliance Monitoring Framework Using Rippling IT**

## Purpose

The capstone investigates whether a lightweight, explicit control-evaluation framework can improve the repeatability and traceability of cybersecurity compliance monitoring for a small organization.

## Method

The work progressed through problem definition, project planning, architecture, rule implementation, unit testing, continuous integration, system integration, performance evaluation, deployment planning, maintenance planning, and final technical documentation.

## Implementation

The portfolio implementation includes:

- a rule catalog for ten representative security controls
- normalization and classification logic
- synthetic scenario data
- SQLite evidence storage
- a service layer connecting validation, evaluation, and persistence
- PyTest-based unit, integration, system, acceptance, and regression tests
- GitHub Actions for automated continuous-integration validation
- batch and integrated service/database demonstrations

## Final Findings

The final public repository verifies 39 passing automated tests with 100% source-code coverage. The controlled 20-scenario dataset produced 100% classification accuracy and 100% exception detection with no false positives or false negatives. A documented 500-operation local performance exercise persisted all 500 records, with mean latency of approximately 1.54 ms, P95 latency of approximately 1.85 ms, and approximate throughput of 650 evaluations per second.

These results describe synthetic and local academic evaluation and are not production-security, certification, or enterprise-scale performance claims.

## Development Evidence

Earlier system testing exposed a whitespace-normalization defect at the service boundary. The issue was corrected and the regression suite was rerun successfully. CI work also exposed an environment/import-path issue that was corrected before the final workflow reached its 100% coverage gate.

## Limitations

The portfolio uses synthetic data and does not claim production certification, live vendor coverage, penetration testing, or enterprise-scale performance.

## Future Work

Future work includes authorized Rippling/SentinelOne adapters, broader control coverage, authenticated multi-user access, stronger evidence retention controls, richer reporting, and longitudinal evaluation.

The full academic report is submitted through the course LMS. This portfolio summary is intentionally sanitized for public review.
