from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import yaml
import matplotlib.pyplot as plt

from .utils_meta import (
    RunMeta,
    git_commit_hash,
    make_run_id,
    safe_mkdir,
    utc_now_iso,
    write_meta,
)


def _import_upstream_toy_universe():
    """
    Import upstream lattice implementation from repo's /src without modifying it.

    Assumes repo layout:
        <repo-root>/src/toy_universe_lattice/...

    NOTE:
    This Phase-1 driver intentionally treats upstream as a black box and
    only applies configuration + logging + plotting.
    """
    root = Path(__file__).resolve().parents[2]  # phase1/src -> phase1 -> repo-root
    upstream_src = root / "src"
    if str(upstream_src) not in sys.path:
        sys.path.insert(0, str(upstream_src))

    from toy_universe_lattice import ScalarToyUniverse  # noqa
    from toy_universe_lattice.origin_axiom_constraint import hard_constraint_factory  # noqa

    return ScalarToyUniverse, hard_constraint_factory


def make_initial_conditions(
    seed: int, n_sites: int, init_sigma: float, init_phi_dot_sigma: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Deterministic complex Gaussian initial conditions for phi and phi_dot.

    Using the same seed ensures constrained/unconstrained runs start from the
    identical initial state, so differences are attributable to the constraint.
    """
    rng = np.random.default_rng(seed)

    # Complex Gaussian field, iid per site
    re = rng.normal(0.0, init_sigma, size=n_sites)
    im = rng.normal(0.0, init_sigma, size=n_sites)
    phi0 = re + 1j * im

    if init_phi_dot_sigma > 0:
        re_d = rng.normal(0.0, init_phi_dot_sigma, size=n_sites)
        im_d = rng.normal(0.0, init_phi_dot_sigma, size=n_sites)
        phi_dot0 = re_d + 1j * im_d
    else:
        phi_dot0 = np.zeros(n_sites, dtype=np.complex128)

    return phi0.astype(np.complex128), phi_dot0.astype(np.complex128)


def run_lattice_once(
    *,
    size: int,
    steps: int,
    dt: float,
    c: float,
    m: float,
    lam: float,
    seed: int,
    eps_mean: float,
    init_sigma: float,
    init_phi_dot_sigma: float,
    with_constraint: bool,
) -> Dict[str, np.ndarray]:
    """
    Run a single lattice simulation and return time series arrays.

    IMPORTANT INTERPRETATION NOTE:
    - The upstream universe is instantiated as a cubic lattice: (size, size, size).
    - The constraint is defined upstream on the SUM amplitude A_sum.
      Phase 1 constrains the MEAN amplitude A_mean = A_sum / N_sites.
      Therefore: eps_sum = eps_mean * N_sites.
    """
    ScalarToyUniverse, hard_constraint_factory = _import_upstream_toy_universe()

    nx = ny = nz = int(size)
    uni = ScalarToyUniverse(nx, ny, nz, c=c, m=m, lam=lam, dt=dt)

    n_sites = uni.phi.size
    phi0, phi_dot0 = make_initial_conditions(seed, n_sites, init_sigma, init_phi_dot_sigma)

    # Upstream lattice expects phi shaped like (nx, ny, nz), not flattened.
    phi0 = phi0.reshape(uni.phi.shape)
    phi_dot0 = phi_dot0.reshape(uni.phi.shape)

    uni.set_initial_conditions(phi0, phi_dot0)

    # Convert mean-floor -> sum-floor for upstream constraint
    eps_sum = float(eps_mean) * float(n_sites)

    constraint = None
    if with_constraint:
        # A_ref=0: forbidden disk centered at A=0 (θ-agnostic in Phase 1)
        constraint = hard_constraint_factory(theta_star=0.0, epsilon=eps_sum, A_ref=0.0)

    t = np.arange(steps + 1, dtype=float) * dt
    A_mean = np.empty(steps + 1, dtype=np.complex128)
    E = np.empty(steps + 1, dtype=float)

    # Record initial state
    A_mean[0] = uni.global_amplitude() / n_sites
    E[0] = float(uni.energy())

    for k in range(1, steps + 1):
        uni.step(constraint=constraint)
        A_mean[k] = uni.global_amplitude() / n_sites
        E[k] = float(uni.energy())

    return {
        "t": t,
        "A_mean": A_mean,
        "A_abs": np.abs(A_mean).astype(float),
        "E": E,
        # If upstream exposes constraint hit counters, capture them. Otherwise 0.
        "constraint_hits": np.array([int(getattr(uni, "constraint_hits", 0))], dtype=int),
        "n_sites": np.array([int(n_sites)], dtype=int),
        "eps_mean": np.array([float(eps_mean)], dtype=float),
        "eps_sum": np.array([float(eps_sum)], dtype=float),
    }


def compute_final_stat(A_abs: np.ndarray, burn_in_frac: float) -> Dict[str, float]:
    """
    Compute tail statistics of |A_mean| after discarding burn-in fraction.
    """
    n = len(A_abs)
    start = int(np.floor(n * burn_in_frac))
    tail = A_abs[start:] if start < n else A_abs
    return {
        "mean_tail": float(np.mean(tail)),
        "median_tail": float(np.median(tail)),
        "p05_tail": float(np.quantile(tail, 0.05)),
        "p95_tail": float(np.quantile(tail, 0.95)),
    }


def _read_eps_mean(lat_cfg: dict) -> float:
    """
    Phase 1 canonical lattice floor key is `eps` (config/phase1.yaml).
    Backward-compatible alias: `eps_mean`.
    """
    if "eps" in lat_cfg:
        return float(lat_cfg["eps"])
    if "eps_mean" in lat_cfg:
        return float(lat_cfg["eps_mean"])
    raise KeyError("lattice.eps (canonical) or lattice.eps_mean (legacy) is required in config")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--mode", choices=["amplitude", "scaling"], required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    seed = int(cfg["phase1"]["seed"])

    lat = cfg["lattice"]
    eps_mean = _read_eps_mean(lat)
    sizes = list(map(int, lat["sizes"]))
    steps = int(lat["steps"])
    dt = float(lat["dt"])
    c = float(lat.get("c", 1.0))
    m = float(lat.get("m", 0.0))
    lam = float(lat.get("lam", 0.0))
    init_sigma = float(lat.get("init_sigma", 1.0))
    init_phi_dot_sigma = float(lat.get("init_phi_dot_sigma", 0.0))
    burn_in_frac = float(lat.get("burn_in_frac", 0.25))

    out_path = Path(args.out)
    safe_mkdir(out_path.parent)

    runs_root = Path(cfg["outputs"]["run_dir"])
    safe_mkdir(runs_root)

    if args.mode == "amplitude":
        # Use the first size for Fig B
        size = sizes[0]

        run_id = make_run_id("figB")
        run_dir = runs_root / run_id
        safe_mkdir(run_dir)

        unc = run_lattice_once(
            size=size,
            steps=steps,
            dt=dt,
            c=c,
            m=m,
            lam=lam,
            seed=seed,
            eps_mean=eps_mean,
            init_sigma=init_sigma,
            init_phi_dot_sigma=init_phi_dot_sigma,
            with_constraint=False,
        )
        con = run_lattice_once(
            size=size,
            steps=steps,
            dt=dt,
            c=c,
            m=m,
            lam=lam,
            seed=seed,
            eps_mean=eps_mean,
            init_sigma=init_sigma,
            init_phi_dot_sigma=init_phi_dot_sigma,
            with_constraint=True,
        )

        # Save raw artifacts
        np.savez_compressed(run_dir / "unconstrained.npz", **unc)
        np.savez_compressed(run_dir / "constrained.npz", **con)

        # Plot |A_mean(t)|
        plt.figure()
        plt.plot(unc["t"], unc["A_abs"], label="unconstrained")
        plt.plot(con["t"], con["A_abs"], label="constrained")
        plt.axhline(eps_mean, linestyle="--", linewidth=1.0, label=r"$\varepsilon$ (mean floor)")
        plt.xlabel("t")
        plt.ylabel(r"$|A_{\mathrm{mean}}(t)|$")
        plt.title(f"Phase 1 Fig B — lattice mean amplitude (L={size}, steps={steps}, dt={dt}, seed={seed})")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.savefig(out_path, bbox_inches="tight")
        plt.close()

        # Copy figure into run folder
        import shutil
        shutil.copy2(out_path, run_dir / out_path.name)

        # Meta
        meta = RunMeta(
            run_id=run_id,
            created_utc=utc_now_iso(),
            git_commit=git_commit_hash(),
            python=sys.version.replace("\n", " "),
            platform=sys.platform,
            params={
                "mode": "amplitude",
                "size": size,
                "interpreted_as": "cubic lattice (L,L,L)",
                "steps": steps,
                "dt": dt,
                "c": c,
                "m": m,
                "lam": lam,
                "seed": seed,
                "eps_mean": eps_mean,
                "init_sigma": init_sigma,
                "init_phi_dot_sigma": init_phi_dot_sigma,
                "burn_in_frac": burn_in_frac,
                "constraint_definition": (
                    "forbid |A_mean| < eps_mean implemented via upstream sum constraint "
                    "with eps_sum = eps_mean * N_sites"
                ),
            },
            notes="Fig B: compare |A_mean(t)| constrained vs unconstrained using identical initial conditions.",
        )
        write_meta(run_dir, meta)

    elif args.mode == "scaling":
        run_id = make_run_id("figC")
        run_dir = runs_root / run_id
        safe_mkdir(run_dir)

        rows = []
        for size in sizes:
            unc = run_lattice_once(
                size=size,
                steps=steps,
                dt=dt,
                c=c,
                m=m,
                lam=lam,
                seed=seed,
                eps_mean=eps_mean,
                init_sigma=init_sigma,
                init_phi_dot_sigma=init_phi_dot_sigma,
                with_constraint=False,
            )
            con = run_lattice_once(
                size=size,
                steps=steps,
                dt=dt,
                c=c,
                m=m,
                lam=lam,
                seed=seed,
                eps_mean=eps_mean,
                init_sigma=init_sigma,
                init_phi_dot_sigma=init_phi_dot_sigma,
                with_constraint=True,
            )

            n_sites = int(unc["n_sites"][0])
            unc_stat = compute_final_stat(unc["A_abs"], burn_in_frac=burn_in_frac)
            con_stat = compute_final_stat(con["A_abs"], burn_in_frac=burn_in_frac)

            rows.append(
                {
                    "L": int(size),
                    "n_sites": n_sites,
                    "unc": unc_stat,
                    "con": con_stat,
                    "constraint_hits": int(con["constraint_hits"][0]),
                }
            )

            # Save each run pair
            np.savez_compressed(run_dir / f"L{size}_unconstrained.npz", **unc)
            np.savez_compressed(run_dir / f"L{size}_constrained.npz", **con)

        # Write summary table
        (run_dir / "scaling_summary.yaml").write_text(
            yaml.safe_dump(rows, sort_keys=False),
            encoding="utf-8",
        )

        # Plot: mean_tail vs N_sites
        nsites = np.array([r["n_sites"] for r in rows], dtype=float)
        unc_y = np.array([r["unc"]["mean_tail"] for r in rows], dtype=float)
        con_y = np.array([r["con"]["mean_tail"] for r in rows], dtype=float)

        plt.figure()
        plt.plot(nsites, unc_y, marker="o", label="unconstrained (tail mean)")
        plt.plot(nsites, con_y, marker="o", label="constrained (tail mean)")
        plt.axhline(eps_mean, linestyle="--", linewidth=1.0, label=r"$\varepsilon$ (mean floor)")
        plt.xscale("log")
        plt.xlabel(r"$N_{\mathrm{sites}}$")
        plt.ylabel(r"$\langle |A_{\mathrm{mean}}|\rangle_{\mathrm{tail}}$")
        plt.title(f"Phase 1 Fig C — scaling of mean residual vs size (steps={steps}, seed={seed})")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.savefig(out_path, bbox_inches="tight")
        plt.close()

        import shutil
        shutil.copy2(out_path, run_dir / out_path.name)

        meta = RunMeta(
            run_id=run_id,
            created_utc=utc_now_iso(),
            git_commit=git_commit_hash(),
            python=sys.version.replace("\n", " "),
            platform=sys.platform,
            params={
                "mode": "scaling",
                "sizes": sizes,
                "interpreted_as": "cubic lattices (L,L,L)",
                "steps": steps,
                "dt": dt,
                "c": c,
                "m": m,
                "lam": lam,
                "seed": seed,
                "eps_mean": eps_mean,
                "init_sigma": init_sigma,
                "init_phi_dot_sigma": init_phi_dot_sigma,
                "burn_in_frac": burn_in_frac,
                "constraint_definition": "mean floor via upstream sum constraint eps_sum = eps_mean * N_sites",
            },
            notes="Fig C: scaling of tail-averaged |A_mean| with/without constraint; expects unconstrained decay ~1/sqrt(N).",
        )
        write_meta(run_dir, meta)


if __name__ == "__main__":
    main()