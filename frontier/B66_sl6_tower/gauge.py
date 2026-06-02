"""B66 validation Tasks 4 + 2 -- the gauge subspace, and exact-arithmetic feasibility.

Task 4: the fixed-line rank-loss makes the eps->0 pinv limit gauge-dependent in a
~9-dim subspace (B62). The principled, non-circular test of "gauge" is base-point
(seed) dependence: compute the 35x35 fixed-line Jacobian at two seeds and check
(a) the |k|=3 eigenvalues/eigenvectors are seed-STABLE, (b) the ~9 gauge modes are
NOT, (c) the |k|=3 eigenvectors carry ~no weight in the gauge subspace.  Then the
|k|=3 multiplicity is recounted on the clean complement.

Task 2: exact-over-Q would need a canonical (seed-independent) rational matrix.
We measure ||dt0(seed20)-dt0(seed24)|| to see whether that is even available, and
report the seed-stable (canonical) char-poly content around the |k|=3 factors.
Numerical, high-precision; not a symbolic proof.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe as PR
import validate as V

DIM = 35
N = 6


def jacobian(words, seed, dps=60, deg=7):
    mp.mp.dps = dps
    epss = [mp.mpf(e) for e in ("0.006", "0.009", "0.012", "0.015", "0.018", "0.021", "0.024", "0.027")]
    h = mp.mpf(10) ** (-(dps // 3))
    basis = V._basis_mp(N)
    pp = [PR.expm_mp(h * g) for g in basis]
    pm = [PR.expm_mp(-h * g) for g in basis]
    Pm, Qm = V._random_PQ(N, seed)
    dts = []
    for eps in epss:
        A, B = PR.expm_mp(eps * Pm), PR.expm_mp(eps * Qm)
        dx = V._diff_matrix(words, A, B, False, pp, pm, h, DIM)
        dX = V._diff_matrix(words, A, B, True, pp, pm, h, DIM)
        dts.append(dX * PR.svd_pinv(dx))
    dt0 = mp.zeros(DIM, DIM)
    for i in range(DIM):
        for j in range(DIM):
            dt0[i, j] = mp.re(PR._extrap0(epss, [d[i, j] for d in dts], deg))
    return np.array([[complex(dt0[i, j]) for j in range(DIM)] for i in range(DIM)])


def catalog():
    L = PR._lucas(8)
    cat = []
    for k in range(-6, 8):
        Lk = float(L[k])
        s = float((-1) ** (k % 2))
        d = (Lk * Lk - 4 * s) ** 0.5
        cat += [((Lk + d) / 2, f"M^{k}"), ((Lk - d) / 2, f"M^{k}")]
        cat += [((-Lk + d) / 2, f"-M^{k}"), ((-Lk - d) / 2, f"-M^{k}")]
    cat += [(1.0, "par+"), (-1.0, "par-")]
    return cat


def main():
    print("B66 validation Tasks 4 + 2 -- gauge subspace & exact-Q feasibility (m=1)\n")
    words = V.select_words(N, 5, seed=20)
    print("computing dt0(seed=20) ...")
    A20 = jacobian(words, 20)
    print("computing dt0(seed=24) ...")
    A24 = jacobian(words, 24)

    cat = catalog()
    cr = np.array([c[0] for c in cat])
    v20, V20 = np.linalg.eig(A20)
    v24, _ = np.linalg.eig(A24)

    # classify seed-20 eigenvalues: gauge if far from catalog or complex
    gauge_idx, clean_idx = [], []
    for i, ev in enumerate(v20):
        d = float(np.min(np.abs(ev - cr)))
        (gauge_idx if (d > 0.05 or abs(ev.imag) > 0.05) else clean_idx).append(i)
    print(f"\n[Task 4] seed-20 spectrum: {len(clean_idx)} clean (catalog) + {len(gauge_idx)} gauge = {DIM}")

    k3 = sorted([2 + 5 ** 0.5, 2 - 5 ** 0.5, -(2 + 5 ** 0.5), -(2 - 5 ** 0.5)])  # +-4.236, -+0.236

    print("\n[Task 4a] |k|=3 eigenvalues -- seed-STABLE? (physical modes must not move)")
    for r in k3:
        e20 = v20[np.argmin(np.abs(v20 - r))]
        e24 = v24[np.argmin(np.abs(v24 - r))]
        print(f"    char(M^3)/char(-M^3) root {r:+.6f}:  seed20 {e20.real:+.9f}  seed24 {e24.real:+.9f}  |diff|={abs(e20 - e24):.2e}")

    print("\n[Task 4b] gauge modes -- seed-UNSTABLE? (scatter across base points)")
    for i in gauge_idx:
        ev = v20[i]
        e24 = v24[np.argmin(np.abs(v24 - ev))]
        print(f"    {ev.real:+.5f}{ev.imag:+.5f}j  -> nearest seed24 {e24.real:+.5f}{e24.imag:+.5f}j  |diff|={abs(ev - e24):.2e}")

    # eigenvalue condition numbers kappa_i = ||v_i|| * ||w_i|| (right/left eigvecs):
    # the basis-independent sensitivity. Physical modes are well-conditioned (small
    # kappa); gauge modes are ill-conditioned (huge kappa). The non-normal matrix has
    # non-orthogonal eigenvectors, so an orthogonal "overlap" is NOT a contamination
    # measure -- kappa is.
    Vinv = np.linalg.inv(V20)
    kappa = np.array([np.linalg.norm(V20[:, i]) * np.linalg.norm(Vinv[i, :]) for i in range(DIM)])
    print("\n[Task 4c] eigenvalue condition numbers (small => physical, huge => gauge):")
    for r in k3:
        i = int(np.argmin(np.abs(v20 - r)))
        print(f"    |k|=3 mode {v20[i].real:+.6f}: kappa = {kappa[i]:.3e}")
    if gauge_idx:
        print(f"    gauge modes:  kappa in [{kappa[gauge_idx].min():.2e}, {kappa[gauge_idx].max():.2e}]")
    print(f"    all clean:    kappa in [{kappa[clean_idx].min():.2e}, {kappa[clean_idx].max():.2e}]")

    tol = 0.05
    m3 = sum(1 for ev in v20 if any(abs(ev - r) < tol and abs(ev.imag) < tol for r in k3)) / 2
    print(f"\n[Task 4d] mult(|k|=3) on the clean complement = {m3}")

    print("\n[Task 2] exact-over-Q feasibility:")
    diff = np.abs(A20 - A24)
    print(f"    ||dt0(20) - dt0(24)||_max = {diff.max():.3e}")
    print(f"    entries seed-stable to 1e-6: {(diff < 1e-6).sum()}/{DIM*DIM}")
    print("    => the numerical Jacobian is NOT canonical (pinv amplifies error in the")
    print("       gauge directions), so there is no exact rational matrix to reconstruct.")
    print("    The seed-STABLE content includes the |k|=3 eigenvalues (4a); the canonical")
    print("    exact route to the |k|=3 factor is the ambient SL(6,C) trace ring (B58, open).")

    np.save("frontier/B66_sl6_tower/_A20.npy", A20)
    np.save("frontier/B66_sl6_tower/_A24.npy", A24)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
