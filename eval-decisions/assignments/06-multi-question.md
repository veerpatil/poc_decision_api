# Assignment 06: Multi-question, shared input

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Basic |
| **Module** | Foundations |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Batch independent questions in one request.

## Steps

1. One `input`: ticket body + one-line order context.
2. Questions: department (`choice`), `duplicate_charge` (`predicate`), urgency (`score`).
3. Give each question a unique `name`; print all answers keyed by name.
4. Read the guide: dependent decisions need separate requests — write one example.

## Deliverable

Script output saved to `eval-decisions/runs/sample_multi_question.txt` for one ticket, three answers.

## Done when

Three names echoed in the response; types parsed correctly.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 05](05-first-api-call.md) · **Next:** [Assignment 07](07-jsonl-schema.md)
