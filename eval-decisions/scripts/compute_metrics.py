#!/usr/bin/env python3
"""Assignments 11–15: metrics from gold JSONL + run JSONL."""

from __future__ import annotations

import argparse
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import DEFAULT_DATA, load_jsonl, repo_root


def wilson_interval(successes: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    if n == 0:
        return 0.0, 0.0, 0.0
    p = successes / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    half = z * math.sqrt((p * (1 - p) / n) + (z**2 / (4 * n**2))) / denom
    return p, center - half, center + half


def macro_f1(per_class: dict[str, dict[str, float]]) -> float:
    f1s = [v["f1"] for v in per_class.values() if v["support"] > 0]
    return sum(f1s) / len(f1s) if f1s else 0.0


def prf1(gold: list[str], pred: list[str], labels: list[str]) -> dict[str, dict[str, float]]:
    stats: dict[str, dict[str, float]] = {}
    for label in labels:
        tp = sum(1 for g, p in zip(gold, pred) if g == label and p == label)
        fp = sum(1 for g, p in zip(gold, pred) if g != label and p == label)
        fn = sum(1 for g, p in zip(gold, pred) if g == label and p != label)
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        stats[label] = {"precision": prec, "recall": rec, "f1": f1, "support": tp + fn}
    return stats


def answer_by_name(answers: list[dict], name: str) -> dict | None:
    for a in answers:
        if a.get("name") == name:
            return a
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument(
        "--run",
        type=Path,
        default=repo_root() / "runs" / "dev_run_001.jsonl",
    )
    parser.add_argument("--confidence-threshold", type=float, default=0.8)
    args = parser.parse_args()

    gold_rows = {r["id"]: r for r in load_jsonl(args.data)}
    run_rows = load_jsonl(args.run)

    dept_gold: list[str] = []
    dept_pred: list[str] = []
    esc_gold: list[bool] = []
    esc_pred: list[bool] = []
    confidences: list[float] = []
    correct_flags: list[bool] = []

    for run in run_rows:
        ex = gold_rows.get(run["id"])
        if not ex:
            continue
        dept_a = answer_by_name(run["answers"], "department")
        esc_a = answer_by_name(run["answers"], "escalate_now")
        if dept_a and dept_a.get("type") == "choice":
            g = ex["gold_department"]
            p = dept_a.get("choice", "other")
            dept_gold.append(g)
            dept_pred.append(p)
            conf = float(dept_a.get("confidence") or 0)
            confidences.append(conf)
            ok = g == p
            correct_flags.append(ok)
        if esc_a and esc_a.get("type") == "predicate":
            esc_gold.append(bool(ex["gold_escalate"]))
            esc_pred.append(float(esc_a.get("probability") or 0) >= 0.5)

    # Department accuracy + confusion
    labels = sorted(set(dept_gold) | set(dept_pred))
    matrix: dict[str, Counter] = {g: Counter() for g in labels}
    for g, p in zip(dept_gold, dept_pred):
        matrix[g][p] += 1
    acc = sum(1 for g, p in zip(dept_gold, dept_pred) if g == p) / len(dept_gold) if dept_gold else 0
    per_class = prf1(dept_gold, dept_pred, labels)
    mf1 = macro_f1(per_class)

    print("=== Department ===")
    print(f"accuracy={acc:.3f} macro_f1={mf1:.3f} n={len(dept_gold)}")
    print("confusion (gold -> pred counts):")
    for g in labels:
        print(f"  {g}: {dict(matrix[g])}")
    print("per-class:")
    for label, s in per_class.items():
        print(
            f"  {label}: P={s['precision']:.2f} R={s['recall']:.2f} "
            f"F1={s['f1']:.2f} support={int(s['support'])}"
        )

    if dept_gold:
        p_hat, lo, hi = wilson_interval(int(acc * len(dept_gold)), len(dept_gold))
        print(f"Wilson 95% CI on accuracy: [{lo:.3f}, {hi:.3f}] (p_hat={p_hat:.3f})")

    # Escalate recall
    if esc_gold:
        tp = sum(1 for g, p in zip(esc_gold, esc_pred) if g and p)
        fn = sum(1 for g, p in zip(esc_gold, esc_pred) if g and not p)
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        print("\n=== Escalate (predicate @ 0.5) ===")
        print(f"recall={recall:.3f} n={len(esc_gold)}")

    # Calibration (choice confidence vs correct)
    if confidences:
        bins: dict[int, list[tuple[float, bool]]] = defaultdict(list)
        for conf, ok in zip(confidences, correct_flags):
            b = min(int(conf * 10), 9)
            bins[b].append((conf, ok))
        print("\n=== Calibration bins (confidence decile) ===")
        ece = 0.0
        total = len(confidences)
        for b in range(10):
            items = bins[b]
            if not items:
                continue
            mean_conf = sum(c for c, _ in items) / len(items)
            acc_b = sum(1 for _, ok in items if ok) / len(items)
            ece += len(items) / total * abs(acc_b - mean_conf)
            print(f"  bin {b}: n={len(items)} mean_conf={mean_conf:.2f} acc={acc_b:.2f}")
        print(f"approx_ECE={ece:.3f}")

    # Threshold sweep on confidence vs auto-route
    if confidences:
        print(f"\n=== Coverage @ confidence >= {args.confidence_threshold} ===")
        auto = [c for c in confidences if c >= args.confidence_threshold]
        print(f"auto_route_pct={100 * len(auto) / len(confidences):.1f}%")


if __name__ == "__main__":
    main()
