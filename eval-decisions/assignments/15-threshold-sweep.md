# Assignment 15: Threshold sweep (dev only)

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Policy |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Pick auto-route vs human review cutoffs.

## Steps

1. Sweep confidence threshold t from 0.5 to 0.95 step 0.05.
2. Plot accuracy vs coverage (% auto-routed) on dev.
3. Pick separate thresholds for escalate and refund predicates.
4. Document false-positive vs false-negative tradeoff in bullets.

## Deliverable

`eval-decisions/reports/thresholds.md` with chosen values + coverage stats.

## Done when

Thresholds justified by cost, not maximum accuracy alone.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 14](14-calibration.md) · **Next:** [Assignment 16](16-responses-baseline.md)
