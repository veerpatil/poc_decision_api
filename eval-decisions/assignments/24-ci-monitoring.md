# Assignment 24: CI regression + monitoring

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Sign-off |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Keep the eval alive after launch.

## Steps

1. Check in lockbox JSONL, `questions_v1`, and runner script.
2. CI job: nightly lockbox run; fail if macro-F1 drops more than 2 points.
3. Log: `name`, `type`, choice/score/probability, `confidence`, latency.
4. Dashboard slices: stratum, refusal, below-threshold queue volume.

## Deliverable

`eval-decisions/ci_eval.yml` sketch + `eval-decisions/spec/monitoring_fields.md`.

## Done when

Regression baseline matches Assignment 23 scorecard.



---

**Previous:** [Assignment 23](23-lockbox-scorecard.md)
