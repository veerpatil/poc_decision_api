#!/usr/bin/env python3
"""Assignment 20: route using conversation history + tool output."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import create_decision, ensure_api_key_or_exit, load_questions, make_client, print_answer

def build_input() -> list[dict]:
    """Multi-turn text context at routing time (see API ref for tool call items)."""
    return [
        {
            "role": "user",
            "content": "I was charged twice for order 8821. Can you fix billing?",
        },
        {
            "role": "assistant",
            "content": "I checked order 8821: two $49 charges posted the same day.",
        },
        {
            "role": "user",
            "content": "Yes, refund the duplicate charge please.",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    questions = load_questions()
    department = next(q for q in questions if q["name"] == "department")
    payload = {"model": "gpt-6-luna", "input": build_input(), "questions": [department]}
    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return

    ensure_api_key_or_exit(dry_run=False)
    decision, latency_ms = create_decision(
        make_client(), input_payload=build_input(), questions=[department]
    )
    print(f"latency_ms={latency_ms:.1f}")
    print_answer(decision.answers[0])


if __name__ == "__main__":
    main()
