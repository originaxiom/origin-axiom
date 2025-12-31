from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


# -----------------------------
# Time / IDs
# -----------------------------

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_now_runstamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def assert_run_id_format(run_id: str) -> None:
    # Required: <task>_YYYYMMDDTHHMMSSZ
    # Minimal validation without regex obsession.
    if "_" not in run_id:
        raise ValueError(f"run_id must contain '_' separator: {run_id}")
    suffix = run_id.split("_")[-1]
    if not (suffix.endswith("Z") and len(suffix) == 16):
        raise ValueError(f"run_id suffix must look like YYYYMMDDTHHMMSSZ: {run_id}")


# -----------------------------
# Git provenance
# -----------------------------

def _run_cmd(cmd: list[str], cwd: Optional[Path] = None) -> Optional[str]:
    try:
        out = subprocess.check_output(cmd, cwd=str(cwd) if cwd else None, stderr=subprocess.STDOUT)
        return out.decode("utf-8", errors="replace").strip()
    except Exception:
        return None


def git_commit_hash(repo_root: Path) -> Optional[str]:
    return _run_cmd(["git", "rev-parse", "HEAD"], cwd=repo_root)


def git_is_dirty(repo_root: Path) -> Optional[bool]:
    out = _run_cmd(["git", "status", "--porcelain"], cwd=repo_root)
    if out is None:
        return None
    return len(out.strip()) > 0


# -----------------------------
# Config loading
# -----------------------------

def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def deep_get(d: Dict[str, Any], dotted: str) -> Any:
    cur: Any = d
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(f"Missing config key: {dotted}")
        cur = cur[part]
    return cur


def resolve_references(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """
    Resolve simple references of the form '@a.b.c' into values from cfg.
    Keeps the rest identical. This is deliberately conservative.

    Example:
      lattice.constraint.epsilon: "@model.epsilon.value"
    """
    def _resolve(obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: _resolve(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_resolve(v) for v in obj]
        if isinstance(obj, str) and obj.startswith("@"):
            return deep_get(cfg, obj[1:])
        return obj

    # resolve references using the original cfg as source of truth
    return _resolve(cfg)


# -----------------------------
# Run directory contract
# -----------------------------

@dataclass(frozen=True)
class RunPaths:
    run_dir: Path
    raw_dir: Path
    fig_dir: Path
    meta_json: Path
    params_json: Path
    summary_json: Path
    pip_freeze_txt: Path


def init_run_dir(
    *,
    run_base: Path,
    run_id: str,
    overwrite: bool = False,
) -> RunPaths:
    assert_run_id_format(run_id)

    run_dir = run_base / run_id
    if run_dir.exists():
        if not overwrite:
            raise FileExistsError(f"Run directory already exists: {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)

    raw_dir = run_dir / "raw"
    fig_dir = run_dir / "figures"
    raw_dir.mkdir(exist_ok=True)
    fig_dir.mkdir(exist_ok=True)

    return RunPaths(
        run_dir=run_dir,
        raw_dir=raw_dir,
        fig_dir=fig_dir,
        meta_json=run_dir / "meta.json",
        params_json=run_dir / "params_resolved.json",
        summary_json=run_dir / "summary.json",
        pip_freeze_txt=run_dir / "pip_freeze.txt",
    )


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")


def capture_pip_freeze(path: Path) -> None:
    """
    Best-effort: if pip isn't available, we still proceed.
    """
    txt = _run_cmd([sys.executable, "-m", "pip", "freeze"])
    if txt is None:
        txt = "pip freeze unavailable\n"
    path.write_text(txt + ("\n" if not txt.endswith("\n") else ""), encoding="utf-8")


def make_meta(
    *,
    repo_root: Path,
    run_id: str,
    task: str,
    cfg_resolved: Dict[str, Any],
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    meta: Dict[str, Any] = {
        "run_id": run_id,
        "task": task,
        "timestamp_utc": utc_now_iso(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": sys.version.replace("\n", " "),
            "python_executable": sys.executable,
        },
        "git": {
            "commit": git_commit_hash(repo_root),
            "dirty": git_is_dirty(repo_root),
        },
        "config": cfg_resolved,  # full resolved config snapshot
        "cwd": os.getcwd(),
    }
    if extra:
        meta["extra"] = extra
    return meta


def repo_root_from_phase2_file(current_file: Path) -> Path:
    """
    This file lives at: <repo>/phase2/src/phase2/utils_meta.py
    parents:
      0 utils_meta.py
      1 phase2/            (package dir)
      2 src/
      3 phase2/            (phase directory)
      4 <repo>/
    """
    return current_file.resolve().parents[4]


def setup_run(
    *,
    config_path: Path,
    run_id: str,
    task: str,
) -> tuple[Dict[str, Any], RunPaths, Dict[str, Any], Path]:
    """
    Returns:
      cfg_raw, paths, meta, repo_root
    """
    cfg_raw = load_yaml(config_path)
    cfg_resolved = resolve_references(cfg_raw)

    run_base = (config_path.parent.parent / cfg_resolved["outputs"]["run_dir"]).resolve()
    overwrite = bool(cfg_resolved["outputs"].get("overwrite_existing", False))

    paths = init_run_dir(run_base=run_base, run_id=run_id, overwrite=overwrite)

    repo_root = repo_root_from_phase2_file(Path(__file__))

    meta = make_meta(
        repo_root=repo_root,
        run_id=run_id,
        task=task,
        cfg_resolved=cfg_resolved,
    )

    write_json(paths.params_json, cfg_resolved)
    write_json(paths.meta_json, meta)
    capture_pip_freeze(paths.pip_freeze_txt)

    return cfg_raw, paths, meta, repo_root