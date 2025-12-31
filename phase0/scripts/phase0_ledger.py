#!/usr/bin/env python3
"""
phase0_ledger.py — deterministic theta corridor ledger

Reads per-phase JSON artifacts:
  phase_outputs/phase_XX_theta_filter.json

Computes the running intersection corridor and writes:
  phase_outputs/theta_corridor_current.json
  phase_outputs/theta_corridor_history.jsonl
  phase_outputs/phase0_dashboard.md

Design goals:
- deterministic: no wall-clock timestamps required
- functional: outputs depend only on input JSON files
- auditable: history records exactly which filter files were applied
"""

from __future__ import annotations

import argparse
import glob
import json
import math
from dataclasses import dataclass
from pathlib import Path
from statistics import median
from typing import Any, Dict, Iterable, List, Tuple, Optional

TAU = 2.0 * math.pi


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_jsonl(path: Path, obj: Any) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, sort_keys=True) + "\n")


def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def normalize_domain(domain: List[float]) -> Tuple[float, float]:
    if not (isinstance(domain, list) and len(domain) == 2):
        raise ValueError("theta_domain must be [lo, hi]")
    lo, hi = float(domain[0]), float(domain[1])
    if hi <= lo:
        raise ValueError("theta_domain must satisfy hi > lo")
    return lo, hi


def interval_length(intervals: List[List[float]]) -> float:
    total = 0.0
    for a, b in intervals:
        total += max(0.0, float(b) - float(a))
    return total


def sort_merge_intervals(intervals: List[List[float]], *, tol: float = 1e-12) -> List[List[float]]:
    """Sort and merge overlapping/adjacent intervals."""
    if not intervals:
        return []
    ints = [[float(a), float(b)] for a, b in intervals if float(b) > float(a)]
    ints.sort(key=lambda x: x[0])
    merged: List[List[float]] = []
    cur_a, cur_b = ints[0]
    for a, b in ints[1:]:
        if a <= cur_b + tol:
            cur_b = max(cur_b, b)
        else:
            merged.append([cur_a, cur_b])
            cur_a, cur_b = a, b
    merged.append([cur_a, cur_b])
    return merged


def intersect_intervals(A: List[List[float]], B: List[List[float]], *, tol: float = 1e-12) -> List[List[float]]:
    """Intersection of two unions of intervals (both assumed sorted/merged)."""
    A = sort_merge_intervals(A, tol=tol)
    B = sort_merge_intervals(B, tol=tol)
    i = j = 0
    out: List[List[float]] = []
    while i < len(A) and j < len(B):
        a1, a2 = A[i]
        b1, b2 = B[j]
        lo = max(a1, b1)
        hi = min(a2, b2)
        if hi > lo + tol:
            out.append([lo, hi])
        if a2 < b2:
            i += 1
        else:
            j += 1
    return sort_merge_intervals(out, tol=tol)


def split_wrap_interval(a: float, b: float, lo: float, hi: float) -> List[List[float]]:
    """
    If interval wraps (a > b) under modular interpretation, split into [a, hi] and [lo, b].
    Here we assume callers already mapped to [lo, hi). For safety, we clamp.
    """
    a = clamp(a, lo, hi)
    b = clamp(b, lo, hi)
    if b >= a:
        return [[a, b]]
    return [[a, hi], [lo, b]]


def ensure_in_domain(intervals: List[List[float]], lo: float, hi: float) -> List[List[float]]:
    out: List[List[float]] = []
    for a, b in intervals:
        a = clamp(float(a), lo, hi)
        b = clamp(float(b), lo, hi)
        if b > a:
            out.append([a, b])
    return sort_merge_intervals(out)


def pass_mask_to_intervals(theta_grid: List[float], passed: List[bool], lo: float, hi: float) -> List[List[float]]:
    """
    Convert pass mask on a (roughly uniform) grid to a union of intervals.
    We treat each grid point as a bin centered at theta with width ~ step,
    then merge contiguous passing bins.
    """
    if len(theta_grid) != len(passed):
        raise ValueError("theta_grid and pass must have same length")

    if len(theta_grid) == 0:
        return []

    # Estimate step size robustly
    diffs = [theta_grid[i + 1] - theta_grid[i] for i in range(len(theta_grid) - 1)]
    diffs = [d for d in diffs if d > 0]
    step = median(diffs) if diffs else (hi - lo)
    half = 0.5 * step

    # Build candidate intervals per passing point
    bins: List[List[float]] = []
    for t, ok in zip(theta_grid, passed):
        if not ok:
            continue
        a = float(t) - half
        b = float(t) + half
        # Clamp bins to domain
        a = clamp(a, lo, hi)
        b = clamp(b, lo, hi)
        if b > a:
            bins.append([a, b])

    return sort_merge_intervals(bins)


def extract_pass_intervals(filter_obj: Dict[str, Any]) -> Tuple[Tuple[float, float], List[List[float]]]:
    lo, hi = normalize_domain(filter_obj.get("theta_domain", [0.0, TAU]))

    # Prefer explicit theta_pass intervals
    theta_pass = filter_obj.get("theta_pass")
    if isinstance(theta_pass, dict) and theta_pass.get("type") == "intervals":
        intervals = theta_pass.get("intervals", [])
        intervals = ensure_in_domain(intervals, lo, hi)
        return (lo, hi), intervals

    # Otherwise use grid + mask
    grid = filter_obj.get("theta_grid")
    pmask = filter_obj.get("pass")
    if not (isinstance(grid, list) and isinstance(pmask, list)):
        raise ValueError("Filter missing theta_pass and missing theta_grid/pass")
    theta_grid = [float(x) for x in grid]
    passed = [bool(x) for x in pmask]
    intervals = pass_mask_to_intervals(theta_grid, passed, lo, hi)
    return (lo, hi), intervals


def list_phase_filters(phase_outputs_dir: Path) -> List[Path]:
    """
    Deterministic order:
      - by phase number parsed from filename phase_XX_theta_filter.json
      - then by filename lexical (covers subphases if you encode them)
    """
    paths = sorted(phase_outputs_dir.glob("phase_*_theta_filter.json"))
    def key(p: Path):
        name = p.name
        # phase_02_theta_filter.json
        parts = name.split("_")
        phase_num = 10**9
        if len(parts) >= 2 and parts[0] == "phase":
            try:
                phase_num = int(parts[1])
            except Exception:
                pass
        return (phase_num, name)
    return sorted(paths, key=key)


def format_intervals(intervals: List[List[float]], *, digits: int = 6) -> str:
    if not intervals:
        return "∅"
    return ", ".join([f"[{a:.{digits}f}, {b:.{digits}f}]" for a, b in intervals])


def write_dashboard(
    out_path: Path,
    domain: Tuple[float, float],
    history_rows: List[Dict[str, Any]],
    final_intervals: List[List[float]],
) -> None:
    lo, hi = domain
    total = hi - lo
    final_len = interval_length(final_intervals)

    lines: List[str] = []
    lines.append("# Phase 0 θ Corridor Dashboard")
    lines.append("")
    lines.append(f"- Domain: [{lo:.12f}, {hi:.12f})  (length = {total:.12f})")
    lines.append(f"- Current corridor length: {final_len:.12f}")
    lines.append(f"- Current corridor intervals ({len(final_intervals)}): {format_intervals(final_intervals, digits=6)}")
    lines.append("")
    lines.append("## Applied filters")
    lines.append("")
    lines.append("| Order | Phase file | Pass intervals | Corridor length after | Narrowed? | git_commit | config_hash |")
    lines.append("|---:|---|---|---:|:---:|---|---|")

    for r in history_rows:
        lines.append(
            f"| {r['order']} | {r['file']} | {r['pass_intervals_str']} | {r['corridor_len_after']:.12f} | "
            f"{'✅' if r['narrowed'] else '—'} | {r.get('git_commit','')} | {r.get('config_hash','')} |"
        )

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_update(root: Path) -> int:
    phase_outputs = root / "phase_outputs"
    phase_outputs.mkdir(exist_ok=True)

    current_path = phase_outputs / "theta_corridor_current.json"
    history_path = phase_outputs / "theta_corridor_history.jsonl"
    dashboard_path = phase_outputs / "phase0_dashboard.md"

    # Start from full domain unless current exists
    if current_path.exists() and current_path.stat().st_size > 0:
        current = load_json(current_path)
        lo, hi = normalize_domain(current.get("theta_domain", [0.0, TAU]))
        corridor = ensure_in_domain(current.get("intervals", []), lo, hi)
    else:
        lo, hi = 0.0, TAU
        corridor = [[lo, hi]]
        save_json(current_path, {"theta_domain": [lo, hi], "intervals": corridor, "meta": {"source": "init_full_domain"}})

    filters = list_phase_filters(phase_outputs)

    # Read existing history to avoid re-applying (deterministic)
    applied_files = set()
    history_rows: List[Dict[str, Any]] = []
    if history_path.exists() and history_path.stat().st_size > 0:
        with history_path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                rec = json.loads(line)
                applied_files.add(rec.get("file"))
                # We'll rebuild dashboard rows fresh below; keep a minimal record list if desired.
        # We rebuild rows from scratch each update for determinism.

    # Recompute from scratch deterministically (simpler + safer)
    lo, hi = 0.0, TAU
    corridor = [[lo, hi]]
    history_rows = []

    # Clear history and rewrite from scratch deterministically
    history_path.write_text("", encoding="utf-8")

    order = 0
    for fp in filters:
        order += 1
        obj = load_json(fp)
        (dlo, dhi), pass_intervals = extract_pass_intervals(obj)
        if abs(dlo - lo) > 1e-9 or abs(dhi - hi) > 1e-9:
            raise ValueError(f"{fp.name}: theta_domain mismatch. Expected [{lo},{hi}), got [{dlo},{dhi})")

        before_len = interval_length(corridor)
        new_corridor = intersect_intervals(corridor, pass_intervals)
        after_len = interval_length(new_corridor)
        narrowed = after_len < before_len - 1e-15

        prov = obj.get("provenance", {}) if isinstance(obj.get("provenance"), dict) else {}
        git_commit = str(prov.get("git_commit", ""))
        config_hash = str(prov.get("config_hash", ""))

        rec = {
            "order": order,
            "file": fp.name,
            "pass_intervals": pass_intervals,
            "corridor_after": new_corridor,
            "corridor_len_after": after_len,
            "narrowed": narrowed,
            "git_commit": git_commit,
            "config_hash": config_hash,
        }
        append_jsonl(history_path, rec)

        history_rows.append({
            "order": order,
            "file": fp.name,
            "pass_intervals_str": format_intervals(pass_intervals, digits=4),
            "corridor_len_after": after_len,
            "narrowed": narrowed,
            "git_commit": git_commit,
            "config_hash": config_hash,
        })

        corridor = new_corridor

        if not corridor:
            # Still write current + dashboard so failure is explicit.
            break

    save_json(current_path, {"theta_domain": [lo, hi], "intervals": corridor, "meta": {"source": "ledger_update"}})
    write_dashboard(dashboard_path, (lo, hi), history_rows, corridor)
    return 0


def cmd_status(root: Path) -> int:
    phase_outputs = root / "phase_outputs"
    current_path = phase_outputs / "theta_corridor_current.json"
    if not current_path.exists() or current_path.stat().st_size == 0:
        print("No current corridor found. Run: python3 scripts/phase0_ledger.py update")
        return 1
    cur = load_json(current_path)
    lo, hi = normalize_domain(cur.get("theta_domain", [0.0, TAU]))
    intervals = ensure_in_domain(cur.get("intervals", []), lo, hi)
    print(f"Domain: [{lo:.12f}, {hi:.12f})")
    print(f"Intervals ({len(intervals)}): {format_intervals(intervals, digits=6)}")
    print(f"Total length: {interval_length(intervals):.12f}")
    return 0


def cmd_report(root: Path) -> int:
    phase_outputs = root / "phase_outputs"
    dashboard_path = phase_outputs / "phase0_dashboard.md"
    if not dashboard_path.exists() or dashboard_path.stat().st_size == 0:
        print("No dashboard found. Run: python3 scripts/phase0_ledger.py update")
        return 1
    print(dashboard_path.read_text(encoding="utf-8"))
    return 0


def main() -> int:
    here = Path(__file__).resolve()
    root = here.parent.parent  # scripts/ -> root

    p = argparse.ArgumentParser(description="Phase 0 theta corridor ledger")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("update", help="Recompute corridor intersection and dashboard")
    sub.add_parser("status", help="Print current corridor summary")
    sub.add_parser("report", help="Print dashboard markdown")

    args = p.parse_args()

    if args.cmd == "update":
        return cmd_update(root)
    if args.cmd == "status":
        return cmd_status(root)
    if args.cmd == "report":
        return cmd_report(root)

    raise RuntimeError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())