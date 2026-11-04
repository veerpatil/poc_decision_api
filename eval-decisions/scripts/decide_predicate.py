#!/usr/bin/env python3
"""Assignment 02: predicate-only example (duplicate charge probability)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import create_decision, ensure_api_key_or_exit, make_client, print_answer

DEFAULT_TEXT = "Please refund the duplicate charge — I was billed $49 twice for one order."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", default=DEFAULT_TEXT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    question = {
        "type": "predicate",
        "name": "duplicate_charge",
        "instructions": "Does the message describe a duplicate charge or being billed twice for the same purchase?",
    }
    payload = {"model": "gpt-6-luna", "input": args.text, "questions": [question]}
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    decision, latency_ms = create_decision(
        make_client(), input_payload=args.text, questions=[question]
    )
    print(f"latency_ms={latency_ms:.1f}")
    print_answer(decision.answers[0])


if __name__ == "__main__":
    main()
