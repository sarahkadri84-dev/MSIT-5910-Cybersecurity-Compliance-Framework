# Project Overview

## Cybersecurity Compliance Monitoring Framework Using Rippling IT

This MSIT 5910 capstone explores a lightweight way to centralize evidence for selected identity, access, device, endpoint, and policy controls.

### Problem

Small organizations often verify cybersecurity controls across multiple operational systems. That can create fragmented evidence, inconsistent review, and avoidable manual effort.

### Proposed Solution

The project separates the solution into five logical layers:

1. Workforce and security inputs
2. Rippling IT control plane
3. Endpoint-security telemetry, including SentinelOne status where available
4. Rule-based compliance evaluation
5. Evidence storage and reporting

The academic implementation uses synthetic observations rather than production employee records, credentials, or confidential security telemetry.

### Technologies

- Python 3.12
- PyTest and pytest-cov
- SQLite
- Git and GitHub
- GitHub Actions
- NIST Cybersecurity Framework 2.0 as a control-organizing reference

### Scope

The prototype evaluates ten representative controls across identity, access, device, endpoint, and policy domains. It is a capstone prototype, not a certification engine, penetration-testing system, or production GRC replacement.
