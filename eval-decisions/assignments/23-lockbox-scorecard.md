# Assignment 23: Lockbox scorecard

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Sign-off |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Single-page ship/no-ship against criteria you define.

## Steps

1. Freeze `questions_v1` and thresholds from Assignment 15.
2. Run lockbox **once**; no further tuning.
3. Scorecard: macro-F1, escalate recall, ECE, p95 latency, refusal rate.
4. Pass/fail gates (example): escalate recall ≥ 0.85, p95 < 400 ms.

## Deliverable

`eval-decisions/reports/scorecard.md` with PASS or FAIL per gate.

## Done when

Lockbox evaluated only once for final numbers.



---

**Previous:** [Assignment 22](22-prompt-caching.md) · **Next:** [Assignment 24](24-ci-monitoring.md)
