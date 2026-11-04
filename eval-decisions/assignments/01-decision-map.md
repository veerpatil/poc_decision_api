# Assignment 01: Decision map for your product

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Basic |
| **Module** | Foundations |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Name three bounded decisions you will benchmark end-to-end in this course.

## Steps

1. List decision A: department routing (choice, 4–6 values incl. `other`).
2. List decision B: escalate to human now (predicate or binary choice).
3. List decision C: allow refund tool (predicate: safe to call `issue_refund`).
4. For each: write when it fires, evidence at that moment, cost of wrong auto-action.
5. Skim the Decisions guide sections **Choose a question type** and **Interpret the answers**.

## Deliverable

`eval-decisions/spec/decision_map.md` — one-page decision spec (3 rows in a table).

## Done when

Each decision has type, options/levels, and a note on false-positive vs false-negative cost.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Next:** [Assignment 02](02-playground-predicate.md)
