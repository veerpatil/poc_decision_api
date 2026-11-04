# Assignment 20: Conversation slice eval

| | |
|---|---|
| **Duration** | 30 minutes |
| **Level** | Advanced |
| **Module** | Inputs |
| **Domain** | Customer support — route, escalate, gate refund tool |

## Objective

Evaluate mid-thread routing with tool output.

## Steps

1. Build one `input` array: user, assistant, function_call, function_output.
2. Question: department after tool returned order lookup.
3. Match `call_id` on tool output to the call.
4. Add 3 multi-turn gold items to JSONL.

## Deliverable

3 conversation eval rows + one API trace in `eval-decisions/runs/conversation_sample.json`.

## Done when

Tool pairing correct; no post-decision messages in `input`.

## References

- https://developers.openai.com/api/docs/guides/decisions

---

**Previous:** [Assignment 19](19-input-json.md) · **Next:** [Assignment 21](21-refusal-policy.md)
