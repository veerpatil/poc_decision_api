#!/usr/bin/env python3
"""Assignment 22: prompt caching demo — fixed prefix, varying questions."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import create_decision, ensure_api_key_or_exit, load_questions, make_client

# Repeat a policy block so shared input exceeds typical cache thresholds when reused.
POLICY_PREFIX = (
    "Company support policy (reference only):\n"
    + "- Billing handles payments, refunds, invoices.\n"
    + "- Technical handles bugs, login, app crashes.\n"
    + "- Shipping handles delivery and wrong items.\n"
) * 40

TICKET = "Customer: I was charged $49 twice for order 8821."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--calls", type=int, default=3, help="Number of requests (vary questions)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    shared_input = f"{POLICY_PREFIX}\n\nTicket:\n{TICKET}"
    all_q = load_questions()

    if args.dry_run:
        print(
            json.dumps(
                {
                    "model": "gpt-6-luna",
                    "input_chars": len(shared_input),
                    "sample_questions": [all_q[0], all_q[1]],
                },
                indent=2,
            )
        )
        return

    ensure_api_key_or_exit(dry_run=False)
    client = make_client()
    question_sets = [
        [all_q[0]],
        [all_q[1]],
        [all_q[0], all_q[1]],
    ]

    for i in range(args.calls):
        qs = question_sets[i % len(question_sets)]
        decision, latency_ms = create_decision(
            client, input_payload=shared_input, questions=qs
        )
        usage = decision.usage
        cached = None
        if usage and getattr(usage, "input_tokens_details", None):
            details = usage.input_tokens_details
            cached = getattr(details, "cached_tokens", None)
        print(
            f"call={i + 1} latency_ms={latency_ms:.1f} "
            f"input_tokens={getattr(usage, 'input_tokens', None)} cached_tokens={cached}"
        )


if __name__ == "__main__":
    main()
