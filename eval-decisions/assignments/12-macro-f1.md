# Assignment 12: Macro-F1 + per-class recall

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Harness |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Protect rare classes from headline accuracy.

## Steps

1. Per-class precision, recall, F1 for department.
2. Macro-F1 across department classes.
3. For escalate: binarize predicate at threshold 0.5 vs `gold_escalate`.
4. Note which metric best matches business cost.

## Deliverable

Table in `eval-decisions/reports/metrics_classification.md` (P/R/F1 + macro-F1).

## Done when

Escalate recall reported separately from overall accuracy.



---

**Previous:** [Assignment 11](11-confusion-matrix.md) · **Next:** [Assignment 13](13-wilson-interval.md)
