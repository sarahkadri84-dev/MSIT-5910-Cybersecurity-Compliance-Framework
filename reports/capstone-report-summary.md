# Capstone Report - Portfolio Summary

## Title

**Cybersecurity Compliance Monitoring Framework Using Rippling IT**

## Purpose

The capstone investigates whether a lightweight, explicit control-evaluation framework can improve the repeatability and traceability of cybersecurity compliance monitoring for a small organization.

## Method

The work progressed through problem definition, project planning, architecture, rule implementation, unit testing, CI/CD, system integration, performance evaluation, deployment planning, maintenance planning, and final technical documentation.

## Implementation

The portfolio implementation includes:

- a rule catalog for ten representative security controls
- normalization and classification logic
- synthetic scenario data
- SQLite evidence storage
- a service layer connecting validation, evaluation, and persistence
- PyTest-based unit, integration, system, and acceptance tests
- GitHub Actions for automated validation

## Findings

The controlled 20-scenario dataset produced 100% classification accuracy and 100% exception detection with no false positives or false negatives. System-level work also highlighted the importance of validating module boundaries and environment-specific CI behavior.

## Limitations

The portfolio uses synthetic data and does not claim production certification, live vendor coverage, penetration testing, or enterprise-scale performance.

## Future Work

Future work includes authorized Rippling/SentinelOne adapters, broader control coverage, authenticated multi-user access, stronger evidence retention controls, richer reporting, and longitudinal evaluation.

The full academic report is submitted through the course LMS. This portfolio summary is intentionally sanitized for public review.
