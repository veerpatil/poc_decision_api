# OpenAI Decisions API — Evaluation assignments

Thirty-minute assignments for learning and benchmarking the [OpenAI Decisions API](https://developers.openai.com/api/docs/guides/decisions) (`POST /v1/decisions`, model `gpt-6-luna`).

**Running domain:** customer support automation — route tickets, escalate to humans, gate refund tools.

**Total:** 24 assignments × 30 minutes = 12 hours seat time.

## How to use

1. Complete assignments **in order** (01 → 24).
2. Store deliverables under this tree:

```
eval-decisions/
  spec/decision_map.md
  data/dev_v1.jsonl
  data/lockbox_v1.jsonl
  questions/questions_v1.json
  runs/*.jsonl
  reports/scorecard.md
  scripts/run_eval.py
```

3. **Do not tune on the lockbox** until [Assignment 23](assignments/23-lockbox-scorecard.md).

## Suggested pace

| Track | Calendar | Assignments / day |
|-------|----------|-------------------|
| Fast | 4 × 3h | 8 |
| Standard | 6 × 2h | 4 |
| Evenings | 12 × 30m | 2 |

## Assignment index

| # | Level | File | Title |
|---|--------|------|--------|
| 01 | Basic | [assignments/01-decision-map.md](assignments/01-decision-map.md) | Decision map for your product |
| 02 | Basic | [assignments/02-playground-predicate.md](assignments/02-playground-predicate.md) | Playground: predicate probability |
| 03 | Basic | [assignments/03-playground-choice.md](assignments/03-playground-choice.md) | Playground: choice + fallback |
| 04 | Basic | [assignments/04-playground-score.md](assignments/04-playground-score.md) | Playground: score rubric |
| 05 | Basic | [assignments/05-first-api-call.md](assignments/05-first-api-call.md) | First API call (SDK or curl) |
| 06 | Basic | [assignments/06-multi-question.md](assignments/06-multi-question.md) | Multi-question, shared input |
| 07 | Intermediate | [assignments/07-jsonl-schema.md](assignments/07-jsonl-schema.md) | JSONL schema v1 |
| 08 | Intermediate | [assignments/08-strata-rare-classes.md](assignments/08-strata-rare-classes.md) | Strata and rare classes |
| 09 | Intermediate | [assignments/09-version-questions.md](assignments/09-version-questions.md) | Version question wording |
| 10 | Intermediate | [assignments/10-batch-runner.md](assignments/10-batch-runner.md) | Batch runner |
| 11 | Intermediate | [assignments/11-confusion-matrix.md](assignments/11-confusion-matrix.md) | Accuracy + confusion matrix |
| 12 | Intermediate | [assignments/12-macro-f1.md](assignments/12-macro-f1.md) | Macro-F1 + per-class recall |
| 13 | Intermediate | [assignments/13-wilson-interval.md](assignments/13-wilson-interval.md) | Wilson interval on lockbox |
| 14 | Intermediate | [assignments/14-calibration.md](assignments/14-calibration.md) | Calibration buckets |
| 15 | Intermediate | [assignments/15-threshold-sweep.md](assignments/15-threshold-sweep.md) | Threshold sweep (dev only) |
| 16 | Intermediate | [assignments/16-responses-baseline.md](assignments/16-responses-baseline.md) | Responses API baseline |
| 17 | Intermediate | [assignments/17-latency-benchmark.md](assignments/17-latency-benchmark.md) | Latency micro-benchmark |
| 18 | Advanced | [assignments/18-robustness.md](assignments/18-robustness.md) | Option order + paraphrase |
| 19 | Advanced | [assignments/19-input-json.md](assignments/19-input-json.md) | Structured input_json evidence |
| 20 | Advanced | [assignments/20-conversation-eval.md](assignments/20-conversation-eval.md) | Conversation slice eval |
| 21 | Advanced | [assignments/21-refusal-policy.md](assignments/21-refusal-policy.md) | Refusal and safety policy |
| 22 | Advanced | [assignments/22-prompt-caching.md](assignments/22-prompt-caching.md) | Prompt caching experiment |
| 23 | Advanced | [assignments/23-lockbox-scorecard.md](assignments/23-lockbox-scorecard.md) | Lockbox scorecard |
| 24 | Advanced | [assignments/24-ci-monitoring.md](assignments/24-ci-monitoring.md) | CI regression + monitoring |

## Decisions vs OpenAI Evals

The hosted [Evals](https://developers.openai.com/api/docs/guides/evals) product grades general model output. This course benchmarks **Decisions** with your own labeled data. Evals becomes read-only **31 Oct 2026** and shuts down **30 Nov 2026** — use this harness for Decisions; migrate other LLM tests to tools such as Promptfoo or pytest.

## References

- [Decisions guide](https://developers.openai.com/api/docs/guides/decisions)
- [Create decision API reference](https://developers.openai.com/api/reference/resources/decisions/methods/create)
- [Decisions API announcement](https://openai.com/index/decisions-api)

## Sample code

Runnable examples live under [`scripts/`](scripts/README.md) and [`examples/`](examples/).

```bash
cd eval-decisions
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/decide_once.py --dry-run
python scripts/decide_once.py   # requires OPENAI_API_KEY
```

| Path | Purpose |
|------|---------|
| `scripts/decide_once.py` | Single `choice` call |
| `scripts/decide_multi_question.py` | `choice` + `predicate` + `score` |
| `scripts/run_eval.py` | JSONL batch runner |
| `scripts/compute_metrics.py` | Accuracy / F1 / calibration |
| `examples/decide_once.sh` | curl sample |
| `examples/decide_once.ts` | TypeScript SDK sample |
