# Evaluation data

Place labeled JSONL files here.

## Row schema (v1)

| Field | Description |
|-------|-------------|
| `id` | Unique example id |
| `state` | Evidence at decision time only (no future transcript) |
| `gold_department` | Human label for routing |
| `gold_escalate` | Boolean: should escalate to human |
| `gold_refund_safe` | Boolean: safe to call refund tool |
| `stratum` | Object: channel, language, week, noisy_stt, etc. |
| `split` | `dev` or `lockbox` |
| `eval_set_version` | e.g. `v1` — pairs with `questions/questions_v1.json` |

See [Assignment 07](../assignments/07-jsonl-schema.md).
