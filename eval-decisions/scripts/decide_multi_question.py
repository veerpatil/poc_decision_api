#!/usr/bin/env python3
"""Assignment 06: department + predicate + score in one request."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    create_decision,
    ensure_api_key_or_exit,
    load_questions,
    make_client,
    print_answer,
)

SAMPLE_INPUT = (
    "Customer: Export fails in Safari but works in Chrome. Also, I see two $49 "
    "charges for order #8821 — please remove the duplicate."
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Multi-question Decisions call.")
    parser.add_argument("--text", default=SAMPLE_INPUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    all_q = load_questions()
    names = ["department", "duplicate_charge", "urgency"]
    questions = [q for q in all_q if q["name"] in names]

    payload = {"model": "gpt-6-luna", "input": args.text, "questions": questions}
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    client = make_client()
    decision, latency_ms = create_decision(
        client, input_payload=args.text, questions=questions
    )
    print(f"latency_ms={latency_ms:.1f}")
    by_name = {a.name: a for a in decision.answers}
    for name in names:
        print(f"\n--- {name} ---")
        print_answer(by_name[name])


if __name__ == "__main__":
    main()
