# Assignment 17: Latency micro-benchmark

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Baselines |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Measure p50/p95 for hot-path suitability.

## Steps

1. 20 sequential Decisions calls (single question, fixed input).
2. Record `latency_ms`; compute p50 and p95.
3. Repeat with a 3-question request; note delta.
4. Log `usage.input_tokens` when present.

## Deliverable

`eval-decisions/reports/latency_summary.json` with p50/p95 for both configs.

## Done when

Both configs measured; no cherry-picked cold start only.



---

**Previous:** [Assignment 16](16-responses-baseline.md) · **Next:** [Assignment 18](18-robustness.md)
