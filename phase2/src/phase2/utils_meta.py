from __future__ import annotations

import json
import os
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import yaml


# ============================================================
# Origin Axiom — Phase 2
# Utilities for reproducible runs + provenance (binding)
# ============================================================


# -----------------------------
# Basic IO
# -----------------------------

def load_yaml(path: Path) -> Dict[str, Any]:
    """Load YAML into a Python dict (no side effects)."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise TypeError(f"YAML root must be a mapping/dict: {path}")
    return data


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)
        f.write("\n")


# -----------------------------
# Dict helpers
# -----------------------------

def deep_get(d: Dict[str, Any], dotted: str) -> Any:
    """Get nested dictionary value via dotted key path, e.g. 'model.epsilon.value'."""
    cur: Any = d
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(f"Missing key path '{dotted}' at '{part}'")
        cur = cur[part]
    return cur


def deep_set(d: Dict[str, Any], dotted: str, value: Any) -> None:
    """Set nested dictionary value via dotted key path, creating intermediate dicts."""
    parts = dotted.split(".")
    cur: Dict[str, Any] = d
    for p in parts[:-1]:
        if p not in cur or not isinstance(cur[p], dict):
            cur[p] = {}
        cur = cur[p]
    cur[parts[-1]] = value


def deep_copy(obj: Any) -> Any:
    """JSON-safe deep copy (sufficient for our YAML config structures)."""
    return json.loads(json.dumps(obj))


def resolve_references(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """
    Resolve simple string references of the form '@a.b.c' within the config.

    Example:
      lattice.constraint.epsilon: "@model.epsilon.value"
    becomes:
      lattice.constraint.epsilon: <value at model.epsilon.value>

    Only resolves strings starting with '@'. Resolution is repeated until stable
    (or a conservative max depth is reached).
    """
    out = deep_copy(cfg)

    def _walk(node: Any) -> Any:
        if isinstance(node, dict):
            return {k: _walk(v) for k, v in node.items()}
        if isinstance(node, list):
            return [_walk(v) for v in node]
        if isinstance(node, str) and node.startswith("@"):
            ref = node[1:]
            return deep_get(out, ref)
        return node

    # Iterate a few times in case references point to other references
    for _ in range(8):
        before = json.dumps(out, sort_keys=True)
        out = _walk(out)
        after = json.dumps(out, sort_keys=True)
        if after == before:
            break
    return out


# -----------------------------
# Repo / provenance helpers
# -----------------------------

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_commit_hash(repo_root: Path) -> Optional[str]:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            stderr=subprocess.STDOUT,
            text=True,
        ).strip()
        return out or None
    except Exception:
        return None


def repo_root_from_phase2_file(this_file: Path, *, config_path: Optional[Path] = None) -> Path:
    """
    Determine repo root reliably when called from phase2/src/phase2/utils_meta.py.

    BUG WE FIX HERE:
      There are two directories named 'phase2' on this path:
        .../phase2/src/phase2/utils_meta.py
                  ^^^        ^^^
      The inner one is the Python package dir; the outer one is the Phase 2 project dir.

    We therefore *only* accept a candidate 'phase2' directory if it looks like the real Phase 2 root,
    i.e. it contains:
      - config/phase2.yaml   (preferred), or
      - workflow/Snakefile   (fallback)

    If config_path is provided, we can anchor directly from it.
    """
    # Strong anchor: config lives in <repo_root>/phase2/config/phase2.yaml
    if config_path is not None:
        cp = Path(config_path).resolve()
        if cp.exists():
            phase2_dir = cp.parent.parent  # .../phase2
            if (phase2_dir / "src" / "phase2").exists():
                return phase2_dir.parent  # repo_root

    # Otherwise: walk upward from this file
    p = this_file.resolve()
    for _ in range(12):
        if p.name == "phase2":
            # Accept only if this is the *outer* phase2 directory (the project folder)
            if (p / "config" / "phase2.yaml").exists() or (p / "workflow" / "Snakefile").exists():
                return p.parent
        p = p.parent

    # Fallback: assume three levels up from src/phase2/utils_meta.py -> phase2 -> repo_root
    return this_file.resolve().parents[3]


def capture_pip_freeze(path: Path) -> None:
    """Best-effort pip freeze capture. If it fails, write a short note instead."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        out = subprocess.check_output(
            [sys.executable, "-m", "pip", "freeze"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        path.write_text(out, encoding="utf-8")
    except Exception as e:
        path.write_text(f"# pip freeze unavailable: {e}\n", encoding="utf-8")


# -----------------------------
# Run layout
# -----------------------------

@dataclass(frozen=True)
class RunPaths:
    run_dir: Path
    fig_dir: Path
    raw_dir: Path
    meta_json: Path
    params_json: Path
    summary_json: Path
    pip_freeze_txt: Path


def _phase2_root_from_repo(repo_root: Path) -> Path:
    p2 = repo_root / "phase2"
    if not p2.exists():
        raise FileNotFoundError(f"phase2/ not found under repo root: {repo_root}")
    return p2


def _ensure_relpath(base: Path, p: Path) -> Path:
    """Convert a config path (string) into a path under base if it is relative."""
    if p.is_absolute():
        return p
    return (base / p).resolve()


def make_run_paths(*, repo_root: Path, cfg_resolved: Dict[str, Any], run_id: str) -> RunPaths:
    phase2_root = _phase2_root_from_repo(repo_root)

    out_cfg = cfg_resolved.get("outputs", {})
    if not isinstance(out_cfg, dict):
        raise TypeError("config.outputs must be a dict")

    run_base = _ensure_relpath(phase2_root, Path(out_cfg.get("run_dir", "outputs/runs")))
    fig_base = _ensure_relpath(phase2_root, Path(out_cfg.get("fig_dir", "outputs/figures")))

    run_dir = run_base / run_id
    fig_dir = run_dir / "figures"
    raw_dir = run_dir / "raw"

    return RunPaths(
        run_dir=run_dir,
        fig_dir=fig_dir,
        raw_dir=raw_dir,
        meta_json=run_dir / "meta.json",
        params_json=run_dir / "params.json",
        summary_json=run_dir / "summary.json",
        pip_freeze_txt=run_dir / "pip_freeze.txt",
    )


def make_meta(*, repo_root: Path, run_id: str, task: str, cfg_resolved: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "run_id": run_id,
        "task": task,
        "timestamp_utc": utc_now_iso(),
        "git_commit": git_commit_hash(repo_root),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": sys.version.replace("\n", " "),
            "python_executable": sys.executable,
        },
        "config_digest": None,  # optional: filled by caller if desired
        "notes": {
            "phase": cfg_resolved.get("meta", {}).get("phase", 2),
        },
    }


def _inject_runtime_meta(cfg: Dict[str, Any], repo_root: Path) -> Dict[str, Any]:
    """
    Fill in cfg.meta.created_utc and cfg.meta.git_commit if present and set to 'AUTO'.
    This modifies a copy of cfg (not in-place).
    """
    out = deep_copy(cfg)
    meta = out.setdefault("meta", {})
    if isinstance(meta, dict):
        if meta.get("created_utc") == "AUTO":
            meta["created_utc"] = utc_now_iso()
        if meta.get("git_commit") == "AUTO":
            meta["git_commit"] = git_commit_hash(repo_root)
    return out


def setup_run(*, config_path: Path, run_id: str, task: str) -> Tuple[Dict[str, Any], RunPaths, Dict[str, Any], Path]:
    """
    Standard Phase-2 entry point. Creates run dir, records params/meta/pip_freeze, and returns:
      (cfg_raw, paths, meta, repo_root)

    cfg_raw: raw YAML dict (unresolved)
    paths: RunPaths for the created run_id
    meta: meta.json dict
    repo_root: repository root
    """
    # FIX: anchor repo root using config_path when possible (prevents writing to phase2/src/phase2/outputs)
    repo_root = repo_root_from_phase2_file(Path(__file__), config_path=config_path)
    cfg_raw = load_yaml(config_path)

    # Resolve references (e.g., '@model.epsilon.value')
    cfg_resolved = resolve_references(cfg_raw)

    # Fill runtime meta fields if declared AUTO
    cfg_resolved = _inject_runtime_meta(cfg_resolved, repo_root)

    paths = make_run_paths(repo_root=repo_root, cfg_resolved=cfg_resolved, run_id=run_id)

    # Create directories
    paths.run_dir.mkdir(parents=True, exist_ok=False)
    paths.fig_dir.mkdir(parents=True, exist_ok=True)
    paths.raw_dir.mkdir(parents=True, exist_ok=True)

    meta = make_meta(repo_root=repo_root, run_id=run_id, task=task, cfg_resolved=cfg_resolved)

    # Record configuration snapshot + meta
    write_json(paths.params_json, cfg_resolved)
    write_json(paths.meta_json, meta)
    capture_pip_freeze(paths.pip_freeze_txt)

    return cfg_raw, paths, meta, repo_root