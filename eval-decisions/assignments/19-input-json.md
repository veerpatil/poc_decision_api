# Assignment 19: Structured input_json evidence

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Inputs |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Evaluate ticket + order object without string hacks.

## Steps

1. Add structured order fields to 5 JSONL rows.
2. User message: `input_text` + `input_json` data `{ticket, order}`.
3. Predicate: duplicate charge supported by `order.charges`.
4. Compare probabilities vs text-only input on the same rows.

## Deliverable

`eval-decisions/reports/input_json_compare.md` (5-row comparison).

## Done when

JSON input validates; probabilities logged both ways.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 18](18-robustness.md) · **Next:** [Assignment 20](20-conversation-eval.md)
