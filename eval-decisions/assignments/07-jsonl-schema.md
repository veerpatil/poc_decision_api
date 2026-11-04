# Assignment 07: JSONL schema v1

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Dataset |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Define the eval row your harness will read.

## Steps

1. Fields: `id`, `state`, `gold_department`, `gold_escalate`, `gold_refund_safe`, `stratum`, `split`, `eval_set_version`.
2. `state` = only text available at routing time (no agent reply after the decision point).
3. Author 10 synthetic rows covering each gold class at least once.
4. Optional: add `eval-decisions/data/schema.json` (JSON Schema).

## Deliverable

`eval-decisions/data/dev_v1.jsonl` (10 lines) + short schema note in `eval-decisions/data/README.md`.

## Done when

Valid JSONL; no label leakage in `state`.



---

**Previous:** [Assignment 06](06-multi-question.md) · **Next:** [Assignment 08](08-strata-rare-classes.md)
