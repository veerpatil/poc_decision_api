# Assignment 08: Strata and rare classes

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Dataset |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Oversample what production under-represents.

## Steps

1. Add stratum tags: `channel`, `language`, `week`, `noisy_stt` (boolean).
2. Expand to 30 rows; ensure `gold_escalate=true` at least 8 times.
3. Document sampling weight per row (default `1.0`).
4. Split: 70% `dev` / 30% `lockbox` via `split` field.

## Deliverable

30-row JSONL in `eval-decisions/data/` with `split` and `stratum`.

## Done when

Lockbox partition has ≥8 escalate positives; no empty gold classes.



---

**Previous:** [Assignment 07](07-jsonl-schema.md) · **Next:** [Assignment 09](09-version-questions.md)
