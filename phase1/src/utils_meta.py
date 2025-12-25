from __future__ import annotations

import json
import platform
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

def git_commit_hash() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "UNKNOWN"

def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def make_run_id(prefix: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{prefix}_{ts}"

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
    safe_mkdir(run_dir)
    meta_path = run_dir / "meta.json"
    meta_path.write_text(json.dumps(asdict(meta), indent=2), encoding="utf-8")

    freeze = pip_freeze_text().strip()
    if freeze:
        (run_dir / "pip_freeze.txt").write_text(freeze + "\n", encoding="utf-8")
