#!/usr/bin/env python3
"""Assignment 19: evaluate structured ticket + order with input_json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import create_decision, ensure_api_key_or_exit, make_client, print_answer

SAMPLE = {
    "ticket": {"body": "Please refund the duplicate charge on my card."},
    "order": {"id": "8821", "charges": [49, 49], "currency": "USD"},
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    input_messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Evaluate the ticket using the order evidence.",
                },
                {"type": "input_json", "data": SAMPLE},
            ],
        }
    ]

    question = {
        "type": "predicate",
        "name": "duplicate_charge",
        "instructions": "Does the ticket describe a duplicate charge supported by the order record?",
    }

    payload = {
        "model": "gpt-6-luna",
        "input": input_messages,
        "questions": [question],
    }
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    decision, latency_ms = create_decision(
        make_client(), input_payload=input_messages, questions=[question]
    )
    print(f"latency_ms={latency_ms:.1f}")
    print_answer(decision.answers[0])


if __name__ == "__main__":
    main()
