#!/usr/bin/env python3
"""Assignment 17: simple p50/p95 latency benchmark."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import create_decision, ensure_api_key_or_exit, load_questions, make_client, repo_root

SAMPLE = "Customer: wrong size shipped, need exchange for order 4412."


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    k = (len(ordered) - 1) * p
    f = int(k)
    c = min(f + 1, len(ordered) - 1)
    if f == c:
        return ordered[f]
    return ordered[f] + (ordered[c] - ordered[f]) * (k - f)


def bench(client, questions, n: int) -> dict:
    latencies: list[float] = []
    for _ in range(n):
        _, ms = create_decision(client, input_payload=SAMPLE, questions=questions)
        latencies.append(ms)
    return {
        "n": n,
        "p50_ms": round(percentile(latencies, 0.5), 2),
        "p95_ms": round(percentile(latencies, 0.95), 2),
        "mean_ms": round(statistics.mean(latencies), 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=10, help="Calls per configuration")
    parser.add_argument("--out", type=Path, default=repo_root() / "reports" / "latency_summary.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    all_q = load_questions()
    single = [next(q for q in all_q if q["name"] == "department")]
    triple = [q for q in all_q if q["name"] in ("department", "duplicate_charge", "urgency")]

    if args.dry_run:
        print(json.dumps({"single_questions": 1, "triple_questions": 3, "n": args.n}, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    client = make_client()
    report = {
        "single_question": bench(client, single, args.n),
        "three_questions": bench(client, triple, args.n),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
