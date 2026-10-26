# Research Report (Sanitized Portfolio Version)

## Cybersecurity Compliance Monitoring Framework Using Rippling IT

### Abstract

This capstone investigates whether a lightweight cybersecurity compliance-monitoring framework can improve the repeatability and traceability of selected identity, access, device, endpoint, and policy controls in a small organization. The academic prototype combines a rule-based evaluator, service layer, SQLite evidence storage, automated testing, and documented deployment and maintenance practices. Synthetic observations are used instead of production employee or security data. The project is organized around NIST Cybersecurity Framework 2.0 concepts while remaining vendor-neutral at the evaluation layer. Controlled testing demonstrated correct classification of twenty predefined compliant and exception scenarios, and the expanded test suite verifies unit, integration, system, and acceptance behavior. The project shows how explicit control definitions, traceable evidence, automated validation, and privacy-aware documentation can make compliance monitoring more reproducible without claiming that a prototype replaces formal governance, production certification, or enterprise GRC platforms.

### Problem

Security and compliance evidence can become fragmented when identity, device, endpoint, and policy information is distributed across multiple operational systems. Manual reviews may be inconsistent, time-consuming, and difficult to reproduce. The project therefore focuses on a narrower problem: how to normalize selected observations, evaluate them against explicit expected states, preserve evidence, and make the result understandable to technical and operational stakeholders.

### System Design

The solution uses five logical layers:

1. Workforce and security inputs
2. Rippling IT control plane
3. Endpoint-security telemetry, including SentinelOne status where available
4. Rule-based compliance evaluation
5. Evidence storage and reporting

The evaluator contains ten representative controls spanning multifactor authentication, offboarding, role-based access, privileged-access review, device encryption, operating-system patch age, device enrollment, endpoint-protection state, minimum password length, and inactive-account age. Rules use equality, minimum, or maximum comparisons so that the decision logic remains inspectable.

### Implementation

Python 3.12 is used for the core evaluator and service layer. SQLite provides a lightweight evidence store. PyTest and pytest-cov support automated verification, while GitHub Actions runs the test suite for pushes and pull requests. Git/GitHub provide change traceability.

The portfolio uses synthetic data only. This allows reviewers to reproduce behavior without exposing production employee information, credentials, security configurations, or live telemetry.

### Evaluation

The controlled scenario dataset contains twenty predefined compliant and exception states. The evaluator produced:

- 20/20 correct classifications
- 100% controlled-scenario accuracy
- 100% exception detection rate
- 0 false positives
- 0 false negatives

The repository also includes integration testing for the service/evaluator/database path and acceptance tests for whitespace tolerance, invalid controls, missing fields, and invalid payload types.

An earlier CI run exposed an environment-specific import-path problem, which was corrected by making the source package importable and setting the repository root in the CI environment. Later system testing emphasized input normalization at service boundaries. Retaining these failure-and-fix examples is important because software quality is demonstrated by debugging and regression evidence, not by presenting only successful runs.

### Security and Ethics

The design emphasizes data minimization, least privilege, credential protection, privacy, and explicit limits on monitoring. The public portfolio contains no real employee records, tokens, passwords, API keys, or confidential configuration values. Any future production integration should include authorization, retention controls, access logging, and organizational governance.

### Limitations

This is an academic prototype. It does not provide formal certification, penetration testing, unrestricted monitoring, or production-scale guarantees. The current public implementation relies on synthetic observations rather than live authorized vendor APIs.

### Future Work

Future development could add scoped Rippling and SentinelOne adapters, authenticated multi-user access, stronger evidence-retention controls, broader framework mappings, richer reporting, longitudinal exception tracking, and deployment packaging.

### Conclusion

The capstone demonstrates that a small, explicit compliance-evaluation framework can make selected cybersecurity controls easier to test, explain, and reproduce. Its main contribution is not the claim that automation proves compliance, but the demonstration that clear control definitions, traceable evidence, layered testing, and privacy-aware implementation can improve the quality of compliance-monitoring workflows.
