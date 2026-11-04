# Assignment 21: Refusal and safety policy

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Production |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Define behavior when `answer.type` is `refusal`.

## Steps

1. Craft or collect 3 inputs likely to produce refusals.
2. Log refusal rate on dev and lockbox runs.
3. Write policy: route to human, no automatic retry, alert if rate exceeds X%.
4. Add refusal counter to runner metrics.

## Deliverable

`eval-decisions/spec/refusal_policy.md` + metric in runner output.

## Done when

Every refusal path maps to a product action.



---

**Previous:** [Assignment 20](20-conversation-eval.md) · **Next:** [Assignment 22](22-prompt-caching.md)
