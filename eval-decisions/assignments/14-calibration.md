# Assignment 14: Calibration buckets

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Statistics |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Check whether `confidence` matches empirical accuracy.

## Steps

1. Bin dev rows by `confidence` decile (choice questions).
2. Per bin: mean confidence vs actual accuracy.
3. Approximate ECE: weighted mean of |accuracy − confidence|.
4. Flag bins where the model is overconfident.

## Deliverable

`eval-decisions/reports/calibration.md` (≤10 bins).

## Done when

At least one actionable miscalibration called out.



---

**Previous:** [Assignment 13](13-wilson-interval.md) · **Next:** [Assignment 15](15-threshold-sweep.md)
