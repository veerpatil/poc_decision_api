# Assignment 11: Accuracy + confusion matrix

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Harness |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Score department `choice` vs `gold_department`.

## Steps

1. Map API `choice` to gold; treat `other` separately in analysis.
2. Compute overall accuracy on dev.
3. Build confusion matrix (gold × predicted).
4. List top 3 confused pairs; inspect 2 examples each.

## Deliverable

`eval-decisions/reports/metrics_department.md` with matrix.

## Done when

Matrix cell counts sum to N; two failure cases explained in prose.



---

**Previous:** [Assignment 10](10-batch-runner.md) · **Next:** [Assignment 12](12-macro-f1.md)
