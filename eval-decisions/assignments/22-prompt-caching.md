# Assignment 22: Prompt caching experiment

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Production |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Reduce cost when evidence prefix repeats.

## Steps

1. Fixed 1,024+ token policy doc in shared `input` prefix.
2. 50 calls: vary only the `questions` array.
3. Read `usage.input_tokens_details.cached_tokens`.
4. Estimate savings vs uncached using guide pricing.

## Deliverable

`eval-decisions/reports/prompt_caching.md` with average cached tokens.

## Done when

Prefix identical across calls; numbers recorded.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 21](21-refusal-policy.md) · **Next:** [Assignment 23](23-lockbox-scorecard.md)
