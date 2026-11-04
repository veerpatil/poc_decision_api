#!/usr/bin/env python3
"""Assignment 04: score rubric example (urgency)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import create_decision, ensure_api_key_or_exit, load_questions, make_client, print_answer

DEFAULT_TEXT = "Export fails in Safari but works in Chrome; I cannot finish payroll today."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", default=DEFAULT_TEXT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    questions = load_questions()
    urgency = next(q for q in questions if q["name"] == "urgency")
    payload = {"model": "gpt-6-luna", "input": args.text, "questions": [urgency]}
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    decision, latency_ms = create_decision(
        make_client(), input_payload=args.text, questions=[urgency]
    )
    print(f"latency_ms={latency_ms:.1f}")
    print_answer(decision.answers[0])


if __name__ == "__main__":
    main()
