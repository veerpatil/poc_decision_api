# Sample scripts (Decisions API)

Python samples use **`gpt-6-luna`** and `POST /v1/decisions` via the OpenAI SDK.

## Setup

```bash
cd eval-decisions
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

Every script supports **`--dry-run`** to print the request payload without calling the API.

## Script map

| Script | Assignment | What it demonstrates |
|--------|------------|----------------------|
| `decide_once.py` | 05 | Single `choice` question |
| `decide_multi_question.py` | 06 | Shared `input`, multiple question types |
| `decide_predicate.py` | 02 | `predicate` + `probability` |
| `decide_score.py` | 04 | `score` + rubric `levels` |
| `decide_input_json.py` | 19 | `input_json` structured evidence |
| `decide_conversation.py` | 20 | Multi-turn message `input` |
| `decide_caching_demo.py` | 22 | Repeated prefix + `cached_tokens` |
| `run_eval.py` | 10 | Batch eval over JSONL |
| `compute_metrics.py` | 11–15 | Accuracy, F1, Wilson, calibration |
| `latency_benchmark.py` | 17 | p50/p95 latency |
| `baseline_responses.py` | 16 | Responses JSON vs Decisions |

## Examples (non-Python)

| File | Notes |
|------|--------|
| `../examples/decide_once.sh` | curl one-liner |
| `../examples/decide_once.ts` | Node SDK (`npx tsx`) |

## Quick start

```bash
# Preview request body
python scripts/decide_once.py --dry-run

# Live call
python scripts/decide_once.py

# Batch dev split (writes runs/dev_run_001.jsonl)
python scripts/run_eval.py --limit 2

# Metrics (after a run file exists)
python scripts/compute_metrics.py --run runs/dev_run_001.jsonl
```

Shared helpers: `_common.py`  
Question definitions: `../questions/questions_v1.json`  
Sample labeled rows: `../data/dev_sample.jsonl`
