# Performance Evaluation Summary

The integrated academic prototype was exercised through the service, evaluator, and SQLite persistence path using 500 sequential operations.

## Observed local results

| Metric | Result |
|---|---:|
| Operations | 500 |
| Records persisted | 500 |
| Mean latency | ~1.54 ms |
| P95 latency | ~1.85 ms |
| Approximate throughput | ~650 evaluations/second |
| Observed record-loss events | 0 |

These measurements describe a local academic test environment. They are included as evaluation evidence and are **not** production-capacity or enterprise-scale performance claims.

The project also reports controlled classification metrics separately in [results/README.md](README.md).
