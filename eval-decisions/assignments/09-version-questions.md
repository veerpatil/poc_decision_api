# Assignment 09: Version question wording

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Intermediate |
| **Module** | Dataset |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Freeze instructions tied to dataset version.

## Steps

1. Create `eval-decisions/questions/questions_v1.json` with all three production questions.
2. Bump a version comment when you change any instruction word.
3. Set `eval_set_version: v1` on every JSONL row.
4. Diff instructions against Playground text from Assignment 03.

## Deliverable

`questions_v1.json` + consistent `eval_set_version` in JSONL.

## Done when

Harness can load questions by version string.



---

**Previous:** [Assignment 08](08-strata-rare-classes.md) · **Next:** [Assignment 10](10-batch-runner.md)
