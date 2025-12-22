#!/usr/bin/env python3
"""
Gate 0 reproducibility entrypoint for origin-axiom.

This script is intentionally thin:
- It orchestrates existing, committed scripts.
- It validates expected canonical outputs exist after execution.
- It fails loudly (non-zero exit) on any failure.

No new physics. No parameter scans. No silent overwrites.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone


REPO_ROOT = Path(__file__).resolve().parents[1]

# Canonical scripts (relative to repo root)
PIPELINE = [
    ("effective_vacuum", "scripts/effective_vacuum_mass_scale_pivot.py"),
    ("frw_background", "scripts/plot_theta_star_lcdm_background_corridor.py"),
    ("lcdm_compare_growth", "scripts/compare_theta_star_to_lcdm_growth.py"),
]

# Canonical expected outputs (relative to repo root)
EXPECTED_OUTPUTS = [
    "data/processed/effective_vacuum_mass_scale_pivot.json",
    "data/processed/theta_star_lcdm_background_corridor_plot_summary.json",
    "data/processed/theta_star_lcdm_growth_comparison.json",
    "figures/theta_star_lcdm_background_corridor.png",
    "figures/theta_star_lcdm_background_corridor.pdf",
]


def _git_head(repo_root: Path) -> str:
    try:
        cp = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return cp.stdout.strip()
    except Exception:
        return "UNKNOWN_GIT_HEAD"


def _run_script(repo_root: Path, rel_path: str) -> None:
    script_path = repo_root / rel_path
    if not script_path.exists():
        raise FileNotFoundError(f"Missing script: {rel_path}")

    env = os.environ.copy()
    # Ensure src/ is importable if scripts assume PYTHONPATH=src
    env["PYTHONPATH"] = str(repo_root / "src") + (
        os.pathsep + env["PYTHONPATH"] if "PYTHONPATH" in env else ""
    )

    cmd = [sys.executable, str(script_path)]
    print(f"\n==> RUN: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=repo_root, env=env, check=True)


def _assert_outputs(repo_root: Path) -> None:
    missing = []
    for rel in EXPECTED_OUTPUTS:
        p = repo_root / rel
        if not p.exists():
            missing.append(rel)

    if missing:
        msg = "\n".join(["Missing expected canonical outputs:"] + [f"  - {m}" for m in missing])
        raise RuntimeError(msg)


def main() -> int:
    started = datetime.now(timezone.utc).isoformat()
    head = _git_head(REPO_ROOT)

    print("=== origin-axiom Gate 0 reproducibility entrypoint ===")
    print(f"Repo root: {REPO_ROOT}")
    print(f"git head:  {head}")
    print(f"started:   {started}")

    try:
        for stage, rel_script in PIPELINE:
            print(f"\n--- Stage: {stage} ---")
            _run_script(REPO_ROOT, rel_script)

        print("\n--- Validate canonical outputs ---")
        _assert_outputs(REPO_ROOT)

    except subprocess.CalledProcessError as e:
        print("\nERROR: A pipeline stage failed.")
        print(f"Command: {e.cmd}")
        print(f"Exit code: {e.returncode}")
        return e.returncode or 1
    except Exception as e:
        print("\nERROR:", str(e))
        return 1

    finished = datetime.now(timezone.utc).isoformat()
    print("\n✅ Reproducibility entrypoint completed successfully.")
    print(f"finished: {finished}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())