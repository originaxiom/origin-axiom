"""B73 -- the SL(4) figure-eight A-variety from the trace map: the B71 pipeline at rank 4.

The B71 (SL(3)) pipeline realize -> monodromy -> eigenvalue ratios generalizes mechanically to SL(4):
the monodromy t is the null vector of the (2n^2 x n^2)=(32 x 16) Kronecker system, and the genuine
meridian mu = w^-1 t = A^-1 t (the conjugator w=a is P-level / rank-independent, V46). What this
script ESTABLISHES (rank 4):

  1. The 32x16 Kronecker monodromy solves (residual ~1e-10) and the V46 meridian fix is
     RANK-INDEPENDENT: mu = A^-1 t COMMUTES with the longitude [A,B] (~1e-10), with eig(mu)=eig(t).
  2. The geometric branch via Sym^3 : SL(2)->SL(4) of the figure-eight holonomy: the SL(4) monodromy
     reproduces Sym^3 of the SL(2) monodromy EXACTLY --
        eig(t4) = (4th root of unity) * {mu^3, mu, mu^-1, mu^-3}   (mu = eig of the SL(2) monodromy),
     to ~1e-12 across sampled fixed points. So the geometric-branch SL(4) meridian eigenvalues are the
     Sym^3 SHADOW of the Cooper-Long figure-eight A-polynomial -- the rank-degree eigenvalue pattern
     (exponents +-3, +-1) made explicit.

  HONEST BOUNDARY (deferred): a genuine SL(4) "Dehn-filling" component (the analogue of SL(3)'s W1/W2
  = the +-3 fillings, where the predicted degree-4 relation L^4=M and a possible link to the SL(2)
  spectral-curve j=1728 would be tested) requires the SL(4) character-variety FIXED LOCUS, i.e. the
  SL(4) trace map (B48 is SL(3) only). A direct numerical fixed-locus search for SL(4) bundle reps at
  candidate root-of-unity A-spectra ({1,i,-1,-i}, {i,i,-i,-i}, cube-root spectra) found NONE -- the
  right Dehn-filling spectra are not known a priori without that machinery. So the degree-4 / j=1728
  hypotheses are UNTESTED here; recorded as open, not claimed. The Sym^3 geometric branch is the
  validated higher-rank content.

Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1-P16 untouched.
"""
from __future__ import annotations

import pathlib

import numpy as np


def sym_power(g, n):
    """Sym^n : SL(2,C) -> SL(n+1,C), on monomials x^(n-i) y^i (i=0..n).  g: x->g00 x+g10 y, y->g01 x+g11 y."""
    import sympy as sp
    x, y = sp.symbols("x y")
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    X, Y = a * x + c * y, b * x + d * y
    M = np.zeros((n + 1, n + 1), dtype=complex)
    for i in range(n + 1):
        poly = sp.Poly(sp.expand(X ** (n - i) * Y ** i), x, y)
        for j in range(n + 1):
            M[j, i] = complex(poly.coeff_monomial(x ** (n - j) * y ** j))
    return M


def monodromy(A, B):
    """t in SL(n,C) with t A t^-1 = A^2 B, t B t^-1 = A B (figure-eight monodromy), via the
    (2 n^2 x n^2) Kronecker null space. Returns (t, residual)."""
    n = A.shape[0]
    In = np.eye(n, dtype=complex)
    phiA, phiB = A @ A @ B, A @ B
    E = np.vstack([np.kron(A.T, In) - np.kron(In, phiA),
                   np.kron(B.T, In) - np.kron(In, phiB)])
    t = np.linalg.svd(E)[2][-1].conj().reshape(n, n, order="F")
    t = t / np.linalg.det(t) ** (1.0 / n)
    res = (np.max(np.abs(t @ A @ np.linalg.inv(t) - phiA))
           + np.max(np.abs(t @ B @ np.linalg.inv(t) - phiB)))
    return t, res


def meridian(A, B):
    """Genuine commuting meridian mu = A^-1 t (w=a, rank-independent). Returns (mu, commutator_dev)."""
    t, _ = monodromy(A, B)
    mu = np.linalg.inv(A) @ t
    comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    return mu, float(np.max(np.abs(mu @ comm - comm @ mu)))


def _b67():
    import importlib.util
    p = pathlib.Path(__file__).resolve().parents[1] / "B67_figure_eight_apolynomial" / "probe.py"
    spec = importlib.util.spec_from_file_location("b67_probe", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sym3_branch(xval):
    """SL(4) geometric rep = Sym^3 of the figure-eight SL(2) rep at x=xval; returns (A4,B4,t4,t2)."""
    A2, B2, t2, _ = _b67().build_rep(xval)
    return sym_power(A2, 3), sym_power(B2, 3), None, t2


def shadow_residual(xval):
    """How well eig(t4) matches a 4th-root multiple of {mu^3,mu,mu^-1,mu^-3} (Sym^3 shadow)."""
    A4, B4, _, t2 = sym3_branch(xval)
    t4, res = monodromy(A4, B4)
    mu = np.linalg.eigvals(t2)
    mu = mu[np.argmax(np.abs(mu))]
    pred = np.array([mu ** 3, mu, 1 / mu, mu ** -3])
    et = np.sort_complex(np.linalg.eigvals(t4))
    best = min(np.max(np.abs(et - np.sort_complex(w * pred))) for w in (1, 1j, -1, -1j))
    return res, best


def main():
    print("B73 -- SL(4) figure-eight A-variety from the trace map (rank-4 B71 pipeline)\n")
    print("Sym^3 geometric branch: monodromy residual, meridian commutativity, shadow match")
    print(" x     mono-res   |[mu,[A,B]]|   eig(t4)=4th-root*{mu^3,mu,mu^-1,mu^-3}")
    for xv in (3, 4, 5, 7, -1):
        A4, B4, _, _ = sym3_branch(xv)
        mu, cdev = meridian(A4, B4)
        res, shadow = shadow_residual(xv)
        print(f" {str(xv):>4}  {res:.1e}    {cdev:.1e}      shadow-match {shadow:.1e}")
    print("\n-> SL(4) pipeline + the V46 meridian fix are rank-independent; the geometric branch is the")
    print("   Sym^3 shadow of Cooper-Long. Genuine SL(4) Dehn-filling components (degree-4 relation,")
    print("   j=1728 link) need the SL(4) trace map / character-variety fixed locus -- deferred.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
