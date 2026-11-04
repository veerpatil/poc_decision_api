# Assignment 13: Wilson interval on lockbox

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Statistics |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Report uncertainty honestly near 90%+ accuracy.

## Steps

1. Run harness on `split=lockbox` once (frozen `questions_v1`).
2. Point estimate of department accuracy.
3. Compute Wilson 95% CI (z = 1.96).
4. One paragraph: is CI width acceptable for a launch decision?

## Deliverable

`eval-decisions/reports/lockbox_wilson.md` with accuracy + CI.

## Done when

CI computed on lockbox only, not dev.



---

**Previous:** [Assignment 12](12-macro-f1.md) · **Next:** [Assignment 14](14-calibration.md)
