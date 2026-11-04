#!/usr/bin/env python3
"""Assignment 10: run Decisions on JSONL eval rows and write run results."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    DEFAULT_DATA,
    DEFAULT_QUESTIONS,
    create_decision,
    decision_record,
    ensure_api_key_or_exit,
    load_jsonl,
    load_questions,
    make_client,
    repo_root,
    write_jsonl,
)

DEFAULT_OUT = repo_root() / "runs" / "dev_run_001.jsonl"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--split", default="dev", help="Filter JSONL split field")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--question-names",
        default="department,duplicate_charge,escalate_now,refund_tool_safe",
        help="Comma-separated subset of questions_v1 names",
    )
    parser.add_argument("--limit", type=int, default=0, help="Max rows (0 = all)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rows = [r for r in load_jsonl(args.data) if r.get("split") == args.split]
    if args.limit:
        rows = rows[: args.limit]

    names = [n.strip() for n in args.question_names.split(",") if n.strip()]
    all_q = load_questions(args.questions)
    questions = [q for q in all_q if q["name"] in names]

    if args.dry_run:
        print(f"Would run {len(rows)} rows split={args.split!r} questions={names}")
        return

    ensure_api_key_or_exit(dry_run=False)
    client = make_client()
    results: list[dict] = []
    refusals = 0

    for row in rows:
        decision, latency_ms = create_decision(
            client, input_payload=row["state"], questions=questions
        )
        rec = decision_record(row["id"], decision, latency_ms)
        results.append(rec)
        for ans in rec["answers"]:
            if ans.get("type") == "refusal":
                refusals += 1
        print(f"ok id={row['id']} latency_ms={rec['latency_ms']}")

    write_jsonl(args.out, results)
    print(f"wrote {len(results)} rows to {args.out} refusals={refusals}")


if __name__ == "__main__":
    main()
