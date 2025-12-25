from __future__ import annotations

import argparse
import platform
import shutil
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
    Sum of unit phasors with a controlled 'twist' subgroup:

      - (1 - twist_fraction) of phases are random uniform [0, 2π)
      - twist_fraction of phases are (random + twist) mod 2π

    Phase-1 θ-agnostic:
      'twist' is a generic misalignment knob (not θ★). We probe behavior
      near π (near-maximal cancellation) without privileging a specific
      irrational constant.
    """
    if n_modes < 2:
        raise ValueError("n_modes must be >= 2")

    k = int(round(n_modes * twist_fraction))
    k = max(1, min(k, n_modes - 1))

    base = rng.uniform(0.0, 2.0 * np.pi, size=n_modes)

    # NOTE: since base phases are i.i.d. uniform, twisting the first k entries
    # is equivalent (in distribution) to twisting a random subset of size k.
    base[:k] = (base[:k] + twist) % (2.0 * np.pi)

    return np.exp(1j * base).sum()


def run_trials(
    seed: int,
    n_trials: int,
    n_modes: int,
    twist: float,
    eps: float,
    twist_fraction: float,
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
        floored[i] = max(r, eps)

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

    safe_mkdir(out_path.parent)

    runs_root = Path(cfg["outputs"]["run_dir"])
    safe_mkdir(runs_root)

    run_id = make_run_id("figA")
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
            )
            results.append(
                {
                    "n_modes": n_modes,
                    "twist": tw,
                    "raw": summarize(raw),
                    "floored": summarize(floored),
                }
            )

    (run_dir / "results.yaml").write_text(yaml.safe_dump(results, sort_keys=False), encoding="utf-8")

    # Build an index for clean lookups: (N, twist) -> stats
    idx = {(r["n_modes"], r["twist"]): r for r in results}

    plt.figure(figsize=(10, 4))

    ax1 = plt.subplot(1, 2, 1)
    for n_modes in n_modes_list:
        xs = list(twists)
        ys = [idx[(n_modes, tw)]["raw"]["mean"] for tw in twists]
        ax1.plot(xs, ys, marker="o", label=f"N={n_modes}")
    ax1.set_xlabel(r"twist $\theta$ (rad)")
    ax1.set_ylabel(r"$\mathbb{E}[|S|]$ (raw)")
    ax1.set_title("Random phasor sum residual (raw)")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=8)

    ax2 = plt.subplot(1, 2, 2)
    for n_modes in n_modes_list:
        xs = list(twists)
        ys = [idx[(n_modes, tw)]["floored"]["mean"] for tw in twists]
        ax2.plot(xs, ys, marker="o", label=f"N={n_modes}")
    ax2.axhline(eps, linestyle="--", linewidth=1.0, label=r"$\varepsilon$")
    ax2.set_xlabel(r"twist $\theta$ (rad)")
    ax2.set_ylabel(r"$\mathbb{E}[\max(|S|,\varepsilon)]$")
    ax2.set_title("Residual with non-cancellation floor")
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8)

    plt.suptitle(
        f"Phase 1 Fig A — phasor ensemble + floor (trials={n_trials}, eps={eps}, seed={seed}, frac={twist_fraction})",
        fontsize=10,
    )

    plt.tight_layout()
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()

    shutil.copy2(out_path, run_dir / "figA_phasor_toy.pdf")

    meta = RunMeta(
        run_id=run_id,
        created_utc=utc_now_iso(),
        git_commit=git_commit_hash(),
        python=sys.version.replace("\n", " "),
        platform=platform.platform(),
        params={
            "seed": seed,
            "n_trials": n_trials,
            "n_modes_list": n_modes_list,
            "twist_angles": twists,
            "eps": eps,
            "twist_fraction": twist_fraction,
            "mode": "figA",
        },
        notes="Fig A: random phasor ensemble residual vs twist; floored variant applies max(|S|, eps).",
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
    twists = list(map(float, cfg["phasor_toy"]["twist_angles"]))
    twist_fraction = float(cfg["phasor_toy"].get("twist_fraction", 0.5))

    eps_list = cfg["phasor_toy"].get("eps_list", None)
    if not eps_list:
        raise ValueError("phasor_toy.eps_list is required for --mode eps_sweep")

    eps_vals = np.array([float(e) for e in eps_list], dtype=float)

    # Representative twist selection policy: closest to π if available.
    tw = min(twists, key=lambda x: abs(x - np.pi)) if twists else float(np.pi)

    safe_mkdir(out_path.parent)

    runs_root = Path(cfg["outputs"]["run_dir"])
    safe_mkdir(runs_root)

    run_id = make_run_id("figD")
    run_dir = runs_root / run_id
    safe_mkdir(run_dir)

    series = []
    for n_modes in n_modes_list:
        raw_means: List[float] = []
        floor_means: List[float] = []
        for eps in eps_vals:
            raw, floored = run_trials(
                seed=seed,
                n_trials=n_trials,
                n_modes=n_modes,
                twist=tw,
                eps=float(eps),
                twist_fraction=twist_fraction,
            )
            raw_means.append(float(np.mean(raw)))
            floor_means.append(float(np.mean(floored)))

        series.append(
            {
                "n_modes": int(n_modes),
                "twist_used": float(tw),
                "twist_selection_policy": "closest_to_pi",
                "eps_list": [float(e) for e in eps_vals],
                "raw_mean": raw_means,
                "floored_mean": floor_means,
                "seed_reused_across_eps": True,
            }
        )

    (run_dir / "results.yaml").write_text(yaml.safe_dump(series, sort_keys=False), encoding="utf-8")

    plt.figure(figsize=(6.5, 4.2))
    for s in series:
        plt.plot(s["eps_list"], s["floored_mean"], marker="o", label=f"N={s['n_modes']}")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel(r"$\varepsilon$")
    plt.ylabel(r"$\mathbb{E}[\max(|S|,\varepsilon)]$")
    plt.title(
        f"Phase 1 Fig D — floor scaling vs ε (twist={tw:.3f}, trials={n_trials}, seed={seed}, frac={twist_fraction})"
    )
    plt.grid(True, which="both", alpha=0.3)
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches="tight")
    plt.close()

    shutil.copy2(out_path, run_dir / "figD_eps_scaling.pdf")

    meta = RunMeta(
        run_id=run_id,
        created_utc=utc_now_iso(),
        git_commit=git_commit_hash(),
        python=sys.version.replace("\n", " "),
        platform=platform.platform(),
        params={
            "seed": seed,
            "n_trials": n_trials,
            "n_modes_list": n_modes_list,
            "twist_used": float(tw),
            "twist_selection_policy": "closest_to_pi",
            "eps_list": [float(e) for e in eps_vals],
            "twist_fraction": twist_fraction,
            "seed_reused_across_eps": True,
            "mode": "eps_sweep",
        },
        notes=(
            "Fig D: eps sweep; plots E[max(|S|, eps)] vs eps at a representative twist near pi. "
            "Same RNG seed reused across eps values to isolate the floor effect."
        ),
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