# Assignment 02: Playground: predicate probability

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Basic |
| **Module** | Foundations |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

See how predicate answers differ from chat yes/no.

## Steps

1. Open the Decisions Playground from the guide.
2. Input: short angry billing ticket text.
3. Question: predicate `duplicate_charge` — does the message describe a duplicate charge?
4. Run 5 paraphrases; record `probability` each time.
5. Note any `refusal` answers.

## Deliverable

Table in `eval-decisions/spec/playground_predicate.md`: input snippet → probability (5 rows).

## Done when

You can explain `probability` vs a parsed JSON boolean.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 01](01-decision-map.md) · **Next:** [Assignment 03](03-playground-choice.md)
