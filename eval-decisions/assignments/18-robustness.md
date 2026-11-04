# Assignment 18: Option order + paraphrase

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Robustness |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Detect brittle choice definitions.

## Steps

1. Pick 10 dev rows; shuffle choice order in `questions_v2.json`.
2. Re-run; measure choice flip rate vs v1.
3. Paraphrase instructions only (same semantics) in `questions_v3.json`.
4. If flip rate > 5%, revise instructions.

## Deliverable

`eval-decisions/reports/robustness.md` with flip rates for v2 and v3.

## Done when

Document whether to keep v1 or adopt v3.



---

**Previous:** [Assignment 17](17-latency-benchmark.md) · **Next:** [Assignment 19](19-input-json.md)
