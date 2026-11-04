# Assignment 03: Playground: choice + fallback

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Basic |
| **Module** | Foundations |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Design categories with an explicit escape hatch.

## Steps

1. Choices: `billing`, `technical`, `shipping`, `other`.
2. Instructions: observable cues only; do not guess account state.
3. Run 3 in-domain tickets + 2 off-topic inputs (weather, joke).
4. Record `choice`, `confidence`, and margin between top two options.

## Deliverable

5-row result table in `eval-decisions/spec/playground_choice.md` including off-topic cases.

## Done when

Off-topic inputs route to `other` or show low confidence; you document the policy.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 02](02-playground-predicate.md) · **Next:** [Assignment 04](04-playground-score.md)
