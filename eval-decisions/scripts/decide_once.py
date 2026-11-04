#!/usr/bin/env python3
"""Assignment 05: single choice decision on one ticket string."""

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

SAMPLE_TICKET = (
    "Customer: I was charged twice for the same order #8821. "
    "Please refund the duplicate $49 charge."
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one department choice decision.")
    parser.add_argument("--text", default=SAMPLE_TICKET, help="Ticket / message text")
    parser.add_argument("--dry-run", action="store_true", help="Print payload only")
    args = parser.parse_args()

    questions = load_questions()
    department_q = next(q for q in questions if q["name"] == "department")

    payload = {
        "model": "gpt-6-luna",
        "input": args.text,
        "questions": [department_q],
    }

    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    client = make_client()
    decision, latency_ms = create_decision(
        client, input_payload=args.text, questions=[department_q]
    )
    print(f"latency_ms={latency_ms:.1f}")
    for answer in decision.answers:
        print_answer(answer)


if __name__ == "__main__":
    main()
