import numpy as np
from pathlib import Path

from theta_star_config import load_theta_star_config
from toy_universe_1d import vacuum_energy_1d
from toy_universe_1d.defected_chain import defected_vacuum_energy


def main() -> None:
    """
    Minimal θ★-aware 1D vacuum check.

    - Reads the frozen Act II theta★ config (fiducial + band).
    - Chooses a handful of sample θ★ values inside that band.
    - Evaluates uniform-ring and defected-chain vacuum energies.
    - Saves a small structured NPZ for later plots / paper figures.
    """

    # ------------------------------------------------------------------
    # 1. Load theta★ configuration from Act II
    # ------------------------------------------------------------------
    cfg = load_theta_star_config()
    theta_fid = float(cfg.theta_star_fid_rad)
    theta_lo, theta_hi = map(float, cfg.theta_star_band_rad)

    print("=== θ★ prior from Act II ===")
    print(f"  fiducial θ★  = {theta_fid:.6f} rad")
    print(f"  band θ★      = [{theta_lo:.6f}, {theta_hi:.6f}] rad")
    print()

    # ------------------------------------------------------------------
    # 2. Choose sample θ★ values inside that band
    # ------------------------------------------------------------------
    # Simple, transparent choice:
    #   - lower edge
    #   - midpoint between lower and fiducial
    #   - fiducial
    #   - midpoint between fiducial and upper
    #   - upper edge
    theta_samples = np.array(
        [
            theta_lo,
            0.5 * (theta_lo + theta_fid),
            theta_fid,
            0.5 * (theta_fid + theta_hi),
            theta_hi,
        ],
        dtype=float,
    )

    # Index of the sample closest to the fiducial value (for reference)
    idx_fid = int(np.argmin(np.abs(theta_samples - theta_fid)))

    # ------------------------------------------------------------------
    # 3. 1D vacuum parameters (match existing twisted/defected scans)
    # ------------------------------------------------------------------
    N = 256           # lattice sites
    c = 1.0           # "speed of light" parameter
    m0 = 0.1          # small but nonzero mass
    defect_strength = 0.5  # as in run_1d_defected_vacuum_scan.py

    print("=== 1D vacuum model parameters ===")
    print(f"  N               = {N}")
    print(f"  c               = {c}")
    print(f"  m0              = {m0}")
    print(f"  defect_strength = {defect_strength}")
    print()

    # ------------------------------------------------------------------
    # 4. Evaluate uniform and defected vacuum energies at each θ★
    # ------------------------------------------------------------------
    E_uniform = np.zeros_like(theta_samples)
    E_defected = np.zeros_like(theta_samples)

    print("=== θ★ samples and vacuum energies ===")
    print("  idx  θ★ [rad]    E0_uniform       E0_defected")
    for i, th in enumerate(theta_samples):
        E_uniform[i] = vacuum_energy_1d(N, c, m0, th)
        E_defected[i] = defected_vacuum_energy(
            N,
            c,
            m0,
            th,
            defect_strength=defect_strength,
        )
        print(
            f"  {i:3d}  {th:8.4f}  "
            f"{E_uniform[i]:12.6e}  {E_defected[i]:12.6e}"
        )

    # ------------------------------------------------------------------
    # 5. Define a reference at (nearest) fiducial θ★ and compute deltas
    # ------------------------------------------------------------------
    E0_ref_uniform = float(E_uniform[idx_fid])
    E0_ref_defected = float(E_defected[idx_fid])

    delta_uniform = E_uniform - E0_ref_uniform
    delta_defected = E_defected - E0_ref_defected

    print()
    print("=== Reference (nearest fiducial) sample ===")
    print(f"  idx_fid      = {idx_fid}")
    print(f"  θ★_fid_used  = {theta_samples[idx_fid]:.6f} rad")
    print(f"  E0_uniform   = {E0_ref_uniform:.6e}")
    print(f"  E0_defected  = {E0_ref_defected:.6e}")
    print()

    # ------------------------------------------------------------------
    # 6. Save a compact NPZ for later analysis / plotting
    # ------------------------------------------------------------------
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "theta_star_prior_1d_vacuum_samples.npz"

    np.savez(
        out_path,
        theta_samples=theta_samples,
        E_uniform=E_uniform,
        E_defected=E_defected,
        delta_uniform=delta_uniform,
        delta_defected=delta_defected,
        params=dict(
            N=int(N),
            c=float(c),
            m0=float(m0),
            defect_strength=float(defect_strength),
            theta_star_fid_rad=theta_fid,
            theta_star_band_lo=theta_lo,
            theta_star_band_hi=theta_hi,
            idx_fid=int(idx_fid),
            # Note: full cfg.raw is *not* stored to avoid pickling;
            # we only keep the essential scalars here.
        ),
    )

    print(f"Saved θ★-prior 1D vacuum samples to {out_path}")
    print("You can inspect it later with, e.g.:")
    print("  PYTHONPATH=src python3 -c 'import numpy as np; d=np.load(")
    print("    \"data/processed/theta_star_prior_1d_vacuum_samples.npz\",")
    print("    allow_pickle=True); print(d.files); print(d[\"theta_samples\"])'")


if __name__ == "__main__":
    main()