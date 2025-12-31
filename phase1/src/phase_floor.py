from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, Tuple, List

import matplotlib.pyplot as plt
import numpy as np
import yaml

from .utils_meta import RunMeta, git_commit_hash, make_run_id, safe_mkdir, utc_now_iso, write_meta


def phasor_sum(
    rng: np.random.Generator,
    n_modes: int,
    twist: float,
    twist_fraction: float = 0.5,
) -> complex:
    """
    Sum of unit phasors with a controlled "twist" applied to a random subset.

    - Draw n_modes angles uniformly in [0, 2π)
    - Choose k = round(n_modes * twist_fraction) angles and add twist (mod 2π)
    - Return the complex sum Σ exp(i θ_j)

    This creates a controllable mismatch structure while preserving generic cancellation.
    """
    if n_modes <= 0:
        raise ValueError("n_modes must be positive")
    twist_fraction = float(twist_fraction)
    if not (0.0 < twist_fraction < 1.0):
        raise ValueError("twist_fraction must be in (0,1)")

    k = int(round(n_modes * twist_fraction))
    k = max(1, min(k, n_modes - 1))

    base = rng.uniform(0.0, 2.0 * np.pi, size=n_modes)
    idx = rng.choice(n_modes, size=k, replace=False)
    base[idx] = (base[idx] + twist) % (2.0 * np.pi)

    return np.exp(1j * base).sum()


def run_trials(
    seed: int,
    n_trials: int,
    n_modes: int,
    twist: float,
    eps: float,
    twist_fraction: float,
    enabled: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns:
      raw_residuals: |S| for each trial (no floor)
      floored_residuals: max(|S|, eps) for each trial
    """
    rng = np.random.default_rng(seed)
    raw = np.empty(n_trials, dtype=float)
    floored = np.empty(n_trials, dtype=float)

    for i in range(n_trials):
        s = phasor_sum(rng, n_modes=n_modes, twist=twist, twist_fraction=twist_fraction)
        r = float(np.abs(s))
        raw[i] = r
        if enabled:
            floored[i] = max(r, eps)
        else:
            floored[i] = r

    return raw, floored


def summarize(x: np.ndarray) -> Dict[str, float]:
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "p05": float(np.quantile(x, 0.05)),
        "p95": float(np.quantile(x, 0.95)),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
    }


def make_figA(*, cfg: dict, out_path: Path) -> None:
    seed = int(cfg["phase1"]["seed"])
    n_trials = int(cfg["phasor_toy"]["n_trials"])
    n_modes_list = list(map(int, cfg["phasor_toy"]["n_modes_list"]))
    twists = list(map(float, cfg["phasor_toy"]["twist_angles"]))
    eps = float(cfg["phasor_toy"]["eps"])
    twist_fraction = float(cfg["phasor_toy"].get("twist_fraction", 0.5))

    constraint_enabled = cfg.get("model", {}).get("constraint", {}).get("enabled", True)
    if not isinstance(constraint_enabled, bool):
        raise ValueError(f"model.constraint.enabled must be boolean, got {constraint_enabled!r}")

    safe_mkdir(out_path.parent)

    runs_root = Path(cfg["outputs"]["run_dir"])
    safe_mkdir(runs_root)

    run_id = make_run_id("figA_phasor")
    run_dir = runs_root / run_id
    safe_mkdir(run_dir)

    results = []
    for n_modes in n_modes_list:
        for tw in twists:
            raw, floored = run_trials(
                seed=seed,
                n_trials=n_trials,
                n_modes=n_modes,
                twist=tw,
                eps=eps,
                twist_fraction=twist_fraction,
                enabled=constraint_enabled,
            )
            results.append(
                {
                    "n_modes": int(n_modes),
                    "twist": float(tw),
                    "eps": float(eps),
                    "twist_fraction": float(twist_fraction),
                    "constraint_enabled": bool(constraint_enabled),
                    "raw": summarize(raw),
                    "floored": summarize(floored),
                }
            )

    # Save artifacts
    out_json = run_dir / "summary.json"
    out_json.write_text(yaml.safe_dump(results, sort_keys=False), encoding="utf-8")

    # Plot: bar chart style summary comparing mean raw vs mean floored for each case
    labels = []
    raw_means = []
    floor_means = []
    for r in results:
        labels.append(f"N={r['n_modes']}\nθ={r['twist']:.2f}")
        raw_means.append(r["raw"]["mean"])
        floor_means.append(r["floored"]["mean"])

    x = np.arange(len(labels))
    width = 0.38

    plt.figure(figsize=(10, 5))
    plt.bar(x - width / 2, raw_means, width, label="raw mean |S|")
    plt.bar(x + width / 2, floor_means, width, label=f"floored mean max(|S|, ε), ε={eps:g}")
    plt.xticks(x, labels, rotation=0)
    plt.ylabel("Residual proxy")
    plt.title("Phase 1 Fig A — raw vs floored residual (phasor toy)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    meta = RunMeta(
        run_id=run_id,
        created_utc=utc_now_iso(),
        git_commit=git_commit_hash(),
        python=sys.version.replace("\n", " "),
        platform=sys.platform,
        params={
            "mode": "figA",
            "seed": seed,
            "n_trials": n_trials,
            "n_modes_list": n_modes_list,
            "twists": twists,
            "eps": eps,
            "twist_fraction": twist_fraction,
            "constraint_enabled": bool(constraint_enabled),
        },
        notes="Fig A: compare raw vs floored (Origin Axiom floor) residuals over twists and N.",
    )
    write_meta(run_dir, meta)


def make_figD_eps_scaling(*, cfg: dict, out_path: Path) -> None:
    """
    Fig D: show how the floored statistic depends on eps.
    We plot E[max(|S|, eps)] versus eps (log-log), for each N.

    NOTE: For controlled comparison, we reuse the same RNG seed for each eps,
    so raw samples are identical and only the floor changes.
    """
    seed = int(cfg["phase1"]["seed"])
    n_trials = int(cfg["phasor_toy"]["n_trials"])
    n_modes_list = list(map(int, cfg["phasor_toy"]["n_modes_list"]))
    twist_fraction = float(cfg["phasor_toy"].get("twist_fraction", 0.5))

    constraint_enabled = cfg.get("model", {}).get("constraint", {}).get("enabled", True)
    if not isinstance(constraint_enabled, bool):
        raise ValueError(f"model.constraint.enabled must be boolean, got {constraint_enabled!r}")

    eps_vals = list(map(float, cfg["phasor_toy"]["eps_list"]))
    tw = float(cfg["phasor_toy"].get("eps_sweep_twist", np.pi))

    safe_mkdir(out_path.parent)

    runs_root = Path(cfg["outputs"]["run_dir"])
    safe_mkdir(runs_root)

    run_id = make_run_id("figD_eps")
    run_dir = runs_root / run_id
    safe_mkdir(run_dir)

    plt.figure(figsize=(7.5, 5))
    for n_modes in n_modes_list:
        floor_means: List[float] = []
        for eps in eps_vals:
            raw, floored = run_trials(
                seed=seed,
                n_trials=n_trials,
                n_modes=n_modes,
                twist=tw,
                eps=float(eps),
                twist_fraction=twist_fraction,
                enabled=constraint_enabled,
            )
            floor_means.append(float(np.mean(floored)))

        plt.plot(eps_vals, floor_means, marker="o", label=f"N={n_modes}")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$\varepsilon$")
    plt.ylabel(r"$\mathbb{E}[\max(|S|,\varepsilon)]$")
    plt.title(
        f"Phase 1 Fig D — floor scaling at twist={tw:.3f} (constraint_enabled={constraint_enabled})"
    )
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

    # Save a small YAML summary for reuse by Phase0 certificates
    summary = []
    for n_modes in n_modes_list:
        row = {"n_modes": int(n_modes), "twist": float(tw), "constraint_enabled": bool(constraint_enabled), "eps_list": eps_vals}
        raw_means = []
        floor_means = []
        for eps in eps_vals:
            raw, floored = run_trials(
                seed=seed,
                n_trials=n_trials,
                n_modes=n_modes,
                twist=tw,
                eps=float(eps),
                twist_fraction=twist_fraction,
                enabled=constraint_enabled,
            )
            raw_means.append(float(np.mean(raw)))
            floor_means.append(float(np.mean(floored)))

        row["raw_mean"] = raw_means
        row["floored_mean"] = floor_means
        summary.append(row)

    (run_dir / "results.yaml").write_text(yaml.safe_dump(summary, sort_keys=False), encoding="utf-8")

    meta = RunMeta(
        run_id=run_id,
        created_utc=utc_now_iso(),
        git_commit=git_commit_hash(),
        python=sys.version.replace("\n", " "),
        platform=sys.platform,
        params={
            "mode": "eps_sweep",
            "seed": seed,
            "n_trials": n_trials,
            "n_modes_list": n_modes_list,
            "twist": tw,
            "twist_fraction": twist_fraction,
            "eps_list": eps_vals,
            "constraint_enabled": bool(constraint_enabled),
        },
        notes="Fig D: eps sweep; plots E[max(|S|, eps)] vs eps at a representative twist near pi. Same RNG seed per eps for controlled comparison.",
    )
    write_meta(run_dir, meta)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True, help="Path to canonical figure PDF")
    ap.add_argument(
        "--mode",
        default="figA",
        choices=["figA", "eps_sweep"],
        help="Which plot to generate",
    )
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    out_path = Path(args.out)

    if args.mode == "figA":
        make_figA(cfg=cfg, out_path=out_path)
    elif args.mode == "eps_sweep":
        make_figD_eps_scaling(cfg=cfg, out_path=out_path)
    else:
        raise ValueError(f"Unknown mode: {args.mode}")


if __name__ == "__main__":
    main()