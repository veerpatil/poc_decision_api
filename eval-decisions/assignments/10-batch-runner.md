# Assignment 10: Batch runner (metrics later)

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Harness |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Run Decisions on every dev row; store raw responses.

## Steps

1. Loop `split=dev` rows; build `input` from `state` only.
2. Retry on HTTP 429 with backoff; log `latency_ms` per row.
3. Write `eval-decisions/runs/dev_run_001.jsonl` (`id`, `answers`, `latency_ms`).
4. Do not tune wording yet — observe failures and refusals.

## Deliverable

`eval-decisions/scripts/run_eval.py` (or `.ts`) + one full dev run file.

## Done when

100% dev rows attempted; refusal count logged.

## References

- https://developers.openai.com/api/reference/resources/decisions/methods/create

---

**Previous:** [Assignment 09](09-version-questions.md) · **Next:** [Assignment 11](11-confusion-matrix.md)
