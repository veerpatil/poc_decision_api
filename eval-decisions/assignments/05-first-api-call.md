# Assignment 05: First API call (SDK or curl)

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Basic |
| **Module** | Foundations |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Reproduce one Playground choice call in code.

## Steps

1. `POST /v1/decisions` with model `gpt-6-luna`.
2. Use the same ticket string as Assignment 03.
3. Log the full `answers[0]` JSON.
4. Handle `type: refusal` in a branch.

## Deliverable

`eval-decisions/scripts/decide_once.py` or `decide_once.ts` — runnable script.

## Done when

Script prints `choice` and `confidence`; exits with code 0.

## References

- https://developers.openai.com/api/docs/guides/decisions
- https://developers.openai.com/api/reference/resources/decisions/methods/create

---

**Previous:** [Assignment 04](04-playground-score.md) · **Next:** [Assignment 06](06-multi-question.md)
