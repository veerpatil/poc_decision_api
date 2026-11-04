#!/usr/bin/env bash
# Assignment 05 (curl): single choice decision.
# Usage: OPENAI_API_KEY=sk-... ./examples/decide_once.sh

set -euo pipefail

: "${OPENAI_API_KEY:?Set OPENAI_API_KEY}"

curl -sS https://api.openai.com/v1/decisions \
  -H "Authorization: Bearer ${OPENAI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6-luna",
    "input": "Customer: I was charged twice for order #8821. Please refund the duplicate $49 charge.",
    "questions": [{
      "type": "choice",
      "name": "department",
      "instructions": "Which team should handle this message?",
      "choices": [
        {"value": "billing"},
        {"value": "technical"},
        {"value": "shipping"},
        {"value": "other"}
      ]
    }]
  }' | python3 -m json.tool
