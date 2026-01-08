#!/usr/bin/env python3
"""
Phase 3: toy 'instability penalty' functional near A0 ≈ 0.

This script reads the diagnostics JSON produced by phase3_measure_v1.py
and constructs a purely toy, non-binding functional that up-weights
mass of the A0 distribution near zero. It is intended only as a
diagnostic of the cancellation basin; it does not feed into any corridor
constraints or physical claims at this rung.
"""

import json
from pathlib import Path
from typing import Dict, Any

def resolve_paths() -> Dict[str, Path]:
    script_path = Path(__file__).resolve()
    # repo_root/.../phase3/src/phase3_mech/instability_penalty_v1.py
    repo_root = script_path.parents[3]
    phase3_root = repo_root / "phase3"
    table_dir = phase3_root / "outputs" / "tables"

    stats_path = table_dir / "phase3_measure_v1_stats.json"
    out_json = table_dir / "phase3_instability_penalty_v1.json"

    return {
        "repo_root": repo_root,
        "phase3_root": phase3_root,
        "table_dir": table_dir,
        "stats_path": stats_path,
        "out_json": out_json,
    }

def main() -> None:
    paths = resolve_paths()
    stats_path = paths["stats_path"]
    out_json = paths["out_json"]

    if not stats_path.is_file():
        raise FileNotFoundError(
            f"Expected stats JSON from phase3_measure_v1 at {stats_path}"
        )

    with stats_path.open("r", encoding="utf-8") as f:
        stats = json.load(f)

    eps_info = stats.get("eps_info", {})
    if not eps_info:
        raise RuntimeError(
            "Stats JSON does not contain 'eps_info' – "
            "run phase3_measure_v1.py first."
        )

    penalty_grid = []
    total_penalty = 0.0

    # We expect eps_info to be a dict keyed by str(eps) with nested dicts.
    for key in sorted(eps_info.keys(), key=lambda k: float(k)):
        entry = eps_info[key]
        eps = float(entry.get("eps", key))
        frac = float(entry["fraction_below_eps"])

        # Toy weight: inversely proportional to eps, so smaller eps are
        # up-weighted. Any overall rescaling of the weights is irrelevant
        # for qualitative use.
        weight = 1.0 / max(eps, 1e-12)
        contribution = weight * frac

        penalty_grid.append(
            {
                "eps": eps,
                "fraction_below_eps": frac,
                "weight": weight,
                "contribution": contribution,
            }
        )
        total_penalty += contribution

    out_payload: Dict[str, Any] = {
        "description": (
            "Toy, non-binding 'instability penalty' functional for the "
            "Phase 3 baseline A0 distribution, constructed from eps_info "
            "in phase3_measure_v1_stats.json. The functional up-weights "
            "probability mass near A0 = 0 by weights proportional to 1/eps. "
            "It is intended only as a diagnostic of the cancellation basin "
            "in the current toy ensemble, not as a corridor constraint or "
            "physical scale."
        ),
        "source_stats_file": str(
            stats_path.relative_to(paths["repo_root"])
        ),
        "penalty_grid": penalty_grid,
        "total_penalty": total_penalty,
    }

    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_json.open("w", encoding="utf-8") as f:
        json.dump(out_payload, f, indent=2, sort_keys=True)

    print("[phase3_instability_penalty_v1] Repo root:", paths["repo_root"])
    print("[phase3_instability_penalty_v1] Phase 3 root:", paths["phase3_root"])
    print("[phase3_instability_penalty_v1] Read stats from", stats_path)
    print("[phase3_instability_penalty_v1] Wrote penalty JSON to", out_json)
    print(
        "[phase3_instability_penalty_v1] total_penalty = "
        f"{total_penalty:.6g}"
    )

if __name__ == "__main__":
    main()
