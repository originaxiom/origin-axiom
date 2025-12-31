from __future__ import annotations

import json
import os
import subprocess
import sys
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


def git_commit_hash() -> str:
    """
    Best-effort git commit hash. Returns "UNKNOWN" if unavailable.

    Note: This does not guarantee a clean working tree; see git_is_dirty().
    """
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "UNKNOWN"


def git_is_dirty() -> Optional[bool]:
    """
    Returns True/False if git is available, otherwise None.
    """
    try:
        # exit code 0 => clean; 1 => dirty; other => error
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return bool(out.stdout.strip())
    except Exception:
        return None


def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def make_run_id(prefix: str) -> str:
    """
    Unique run id for filesystem folders.

    We include:
    - UTC timestamp (human sortable)
    - short random suffix (prevents collisions under parallel runs)
    """
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    suffix = uuid.uuid4().hex[:8]
    return f"{prefix}_{ts}_{suffix}"


def pip_freeze_text() -> str:
    """
    Best-effort dependency snapshot. Works if pip is available.
    If it fails, we still proceed.
    """
    try:
        return subprocess.check_output([sys.executable, "-m", "pip", "freeze"], text=True)
    except Exception:
        return ""


@dataclass
class RunMeta:
    run_id: str
    created_utc: str
    git_commit: str
    python: str
    platform: str
    params: Dict[str, Any]
    notes: Optional[str] = None


def write_meta(run_dir: Path, meta: RunMeta) -> None:
    """
    Write run metadata + optional pip freeze.

    Always writes:
      - meta.json

    Writes additionally (if available):
      - pip_freeze.txt
    """
    safe_mkdir(run_dir)

    payload = asdict(meta)
    # Add extra provenance without changing call sites
    payload.setdefault("git_dirty", git_is_dirty())
    payload.setdefault("python_executable", sys.executable)
    payload.setdefault("cwd", os.getcwd())

    meta_path = run_dir / "meta.json"
    meta_path.write_text(json.dumps(payload, indent=2, sort_keys=False), encoding="utf-8")

    freeze = pip_freeze_text().strip()
    if freeze:
        (run_dir / "pip_freeze.txt").write_text(freeze + "\n", encoding="utf-8")