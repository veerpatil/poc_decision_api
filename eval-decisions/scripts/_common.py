"""Shared helpers for Decisions API sample scripts."""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

from openai import OpenAI
from openai import RateLimitError

DECISIONS_MODEL = "gpt-6-luna"

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUESTIONS = ROOT / "questions" / "questions_v1.json"
DEFAULT_DATA = ROOT / "data" / "dev_sample.jsonl"


def repo_root() -> Path:
    return ROOT


def load_questions(path: Path | None = None) -> list[dict[str, Any]]:
    path = path or DEFAULT_QUESTIONS
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload["questions"]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def make_client() -> OpenAI:
    # Uses OPENAI_API_KEY from the environment.
    return OpenAI()


def answer_to_dict(answer: Any) -> dict[str, Any]:
    """Convert a Decisions answer object to a JSON-serializable dict."""
    if hasattr(answer, "model_dump"):
        return answer.model_dump()
    if hasattr(answer, "to_dict"):
        return answer.to_dict()
    return dict(answer)


def print_answer(answer: Any) -> None:
    data = answer_to_dict(answer)
    print(json.dumps(data, indent=2))
    atype = data.get("type")
    name = data.get("name")
    if atype == "refusal":
        print(f"[refusal] question={name!r}")
    elif atype == "choice":
        print(f"choice={data.get('choice')!r} confidence={data.get('confidence')}")
    elif atype == "predicate":
        print(f"probability={data.get('probability')}")
    elif atype == "score":
        print(f"score={data.get('score')} confidence={data.get('confidence')}")


def create_decision(
    client: OpenAI,
    *,
    input_payload: str | list[dict[str, Any]],
    questions: list[dict[str, Any]],
    max_retries: int = 5,
) -> tuple[Any, float]:
    """Call Decisions API with simple 429 backoff. Returns (decision, latency_ms)."""
    last_err: Exception | None = None
    for attempt in range(max_retries):
        start = time.perf_counter()
        try:
            decision = client.decisions.create(
                model=DECISIONS_MODEL,
                input=input_payload,
                questions=questions,
            )
            latency_ms = (time.perf_counter() - start) * 1000
            return decision, latency_ms
        except RateLimitError as err:
            last_err = err
            sleep_s = min(2**attempt, 32)
            time.sleep(sleep_s)
    assert last_err is not None
    raise last_err


def decision_record(
    example_id: str,
    decision: Any,
    latency_ms: float,
) -> dict[str, Any]:
    answers = [answer_to_dict(a) for a in decision.answers]
    usage = None
    if getattr(decision, "usage", None) is not None:
        usage = answer_to_dict(decision.usage) if hasattr(decision.usage, "model_dump") else decision.usage
    return {
        "id": example_id,
        "latency_ms": round(latency_ms, 2),
        "answers": answers,
        "usage": usage,
    }


def ensure_api_key_or_exit(dry_run: bool) -> None:
    if dry_run:
        return
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit(
            "Set OPENAI_API_KEY or pass --dry-run to print the request without calling the API."
        )
