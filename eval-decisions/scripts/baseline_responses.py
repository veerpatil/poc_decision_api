#!/usr/bin/env python3
"""Assignment 16: compare Decisions to Responses + JSON parsing (baseline)."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    DEFAULT_DATA,
    create_decision,
    ensure_api_key_or_exit,
    load_jsonl,
    load_questions,
    make_client,
)

SYSTEM = (
    "Classify the support message. Reply with JSON only: "
    '{"department":"billing|technical|shipping|other",'
    '"escalate":boolean,"refund_safe":boolean}'
)


def parse_json(text: str) -> dict | None:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                return None
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--split", default="dev")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--responses-model", default="gpt-4.1-mini")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rows = [r for r in load_jsonl(args.data) if r.get("split") == args.split][: args.limit]
    if args.dry_run:
        print(f"Would compare {len(rows)} rows")
        return

    ensure_api_key_or_exit(dry_run=False)
    client = make_client()
    dept_q = next(q for q in load_questions() if q["name"] == "department")

    parse_errors = 0
    latencies: list[float] = []
    for row in rows:
        start = time.perf_counter()
        resp = client.responses.create(
            model=args.responses_model,
            input=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": row["state"]},
            ],
        )
        latencies.append((time.perf_counter() - start) * 1000)
        text = resp.output_text
        if parse_json(text) is None:
            parse_errors += 1

    print(f"responses_model={args.responses_model} rows={len(rows)}")
    print(f"parse_errors={parse_errors} median_latency_ms={sorted(latencies)[len(latencies)//2]:.1f}")

    # Decisions reference on same rows
    d_lat: list[float] = []
    for row in rows:
        _, ms = create_decision(
            client, input_payload=row["state"], questions=[dept_q]
        )
        d_lat.append(ms)
    print(f"decisions median_latency_ms={sorted(d_lat)[len(d_lat)//2]:.1f}")


if __name__ == "__main__":
    main()
