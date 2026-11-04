# Assignment 16: Responses API baseline

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Baselines |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Compare Decisions to chat + JSON parsing.

## Steps

1. Same 30 dev `state` strings; prompt for JSON `{department, escalate, refund_safe}`.
2. Count parse failures and invalid JSON.
3. Compare department macro-F1 vs Decisions run.
4. Compare median latency on the same network.

## Deliverable

`eval-decisions/reports/baseline_responses.md` comparison table.

## Done when

Decisions advantage or disadvantage stated with numbers.



---

**Previous:** [Assignment 15](15-threshold-sweep.md) · **Next:** [Assignment 17](17-latency-benchmark.md)
