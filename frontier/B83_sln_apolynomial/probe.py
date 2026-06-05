"""B83 (Phase A) -- the SL(n) figure-eight Dehn-filling A-polynomial family L = (-1)^(n-1) M^n.

degree=rank (B73/V54, B77/V60) is the matrix law [A,B]=(-1)^(n-1) mu^n on the principal Dehn-filling
component. Its PERIPHERAL EIGENVALUE shadow is an A-polynomial: co-diagonalizing the commuting meridian
mu=A^-1 t and longitude lam=[A,B], each (M,L)=(eig mu, eig lam) pair satisfies
    L = (-1)^(n-1) M^n        (the eigenvalue A-variety of the principal component),
with prod(M)=det(mu)=1. This is the rank-n analogue of B67 (SL(2)=Cooper-Long) and B71 (SL(3)=Falbel
W1=D2: M^3=L), now extended to SL(4) and unified into one family:
    n=3:  L = +M^3   (Falbel, B71)
    n=4:  L = -M^4   (NEW -- the SL(4) figure-eight Dehn-filling A-polynomial from the trace map)
    n=5:  L = +M^5   (predicted; the principal SL(5) component is not numerically locatable -- B78)
(SL(2) is degenerate -- no Dehn-filling component, A0/B73 -- so the family starts at n=3.)

MECHANISM (the "why n", as far as this establishes it): the exponent is the RANK n -- structurally the
Falbel filling slope of the PRINCIPAL Dehn-filling component (the component is exactly the one whose
A-polynomial degree equals the rank); the sign (-1)^(n-1) is fixed by the determinant/orientation (it is
the scalar c in B77's [A,B]=c*mu^n, forced to c^n=1 by det). The meridian eigenvalues M are GENERIC
(vary across the component, |M| spread O(1)) -- NOT fixed roots of unity (B77) -- so the A-variety is the
1-parameter (per eigenvalue) curve L=(-1)^(n-1)M^n, not a finite set of points.

This is the SL(4) figure-eight A-polynomial (the first from the trace map at rank 4) + the Aₙ family.
Standalone low-dim topology; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np

_FRONTIER = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_FRONTIER / "B71_sl3_apoly"))
sys.path.insert(0, str(_FRONTIER / "B73_sl4_apoly"))
import peripheral as P3          # noqa: E402
import dehn_filling as D4        # noqa: E402


def codiag_eig_pairs(mu, lam):
    """mu, lam commute -> co-diagonalize: return (eig(mu), eig(lam)) pairs in the common eigenbasis."""
    w, V = np.linalg.eig(mu)
    lam_diag = np.linalg.inv(V) @ lam @ V
    return list(zip(w, np.diag(lam_diag)))


def avariety_dev(mu, lam, n):
    """max |L - (-1)^(n-1) M^n| over the co-diagonalized eigenvalue pairs."""
    sign = (-1) ** (n - 1)
    return max(abs(L - sign * M ** n) for M, L in codiag_eig_pairs(mu, lam))


def sl4_principal_reps(n_reps=5, budget=40):
    out = []
    for sd in range(budget):
        if len(out) >= n_reps:
            break
        r = D4.realize_bundle_rep(D4.SPEC_W1, seed=sd, tries=60)
        if r is None:
            continue
        A, B, t = r
        mu = np.linalg.inv(A) @ t
        lam = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        if np.max(np.abs(mu @ lam - lam @ mu)) < 1e-6:
            out.append((mu, lam))
    return out


def sl3_W1_reps(n_reps=5, seed=11, budget=200):
    """SL(3) principal Dehn-filling W1 reps -> (mu, lam), using the B71 peripheral pipeline."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(budget):
        if len(out) >= n_reps:
            break
        p = complex(*rng.standard_normal(2)); q = complex(*rng.standard_normal(2))
        res = P3.realize(P3.W1(p, q))
        if res is None:
            continue
        A, B = res
        mu, cdev = P3.meridian(A, B)
        if mu is None or cdev is None or cdev > 1e-6:
            continue
        lam = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        out.append((mu, lam))
    return out


def family_dev(n):
    """Median A-variety deviation |L-(-1)^(n-1)M^n| over reps at rank n. Returns (median, n_reps)."""
    reps = sl3_W1_reps() if n == 3 else sl4_principal_reps()
    devs = [avariety_dev(mu, lam, n) for mu, lam in reps]
    return (float(np.median(devs)) if devs else float("nan")), len(devs)


def main():
    print("B83 (Phase A) -- the SL(n) figure-eight Dehn-filling A-polynomial family L=(-1)^(n-1) M^n\n")
    print("  on the principal Dehn-filling component, co-diagonalize meridian mu=A^-1 t & longitude [A,B];")
    print("  each eigenvalue pair (M,L) satisfies the A-variety L = (-1)^(n-1) M^n.\n")
    for n in (3, 4):
        sign = "+" if (-1) ** (n - 1) > 0 else "-"
        dev, k = family_dev(n)
        print(f"  n={n}: L = {sign}M^{n}   median |L-(-1)^(n-1)M^n| = {dev:.1e}  ({k} reps)")
    print("\n  Aₙ family:  n=3 -> L=+M^3 (Falbel),  n=4 -> L=-M^4 (NEW),  n=5 -> L=+M^5 (predicted).")
    print("  SL(2) is degenerate (no Dehn-filling component); the family is n>=3.")
    print("  MECHANISM: exponent = rank (the principal component's filling slope); sign (-1)^(n-1) by det.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
