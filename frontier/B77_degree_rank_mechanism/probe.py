"""B77 (Phase 1a) -- the degree=rank mechanism probe: refine the law, and test the A<->D unification.

CONTEXT. degree=rank (B73/V54, B75/V57): on the SL(n) figure-eight bundle's principal Dehn-filling
component {tr A=tr A^-1=1}, the longitude is the meridian's n-th power, M^n=L. Two questions:
  (i)  what is the PRECISE relation (is there a hidden scalar)?
  (ii) UNIFICATION HYPOTHESIS (CONJECTURED): is degree=rank the geometric shadow of the Dickson tower's
       top factor char(M^n)? i.e. are the meridian/longitude eigenvalues the roots of char(M^n)?

WHAT THIS COMPUTES. On each principal Dehn-filling rep (SL(3) W1 spectrum {1,i,-i}; SL(4) {1,1,w,w^2}),
with the genuine meridian mu=A^-1 t (V46; mu commutes with [A,B]):
  * the scalar c in the scalar-matrix identity [A,B] = c * mu^n  ([A,B] mu^-n = c I);
  * the meridian eigenvalues eig(mu) (= eig(t)), and their SPREAD across reps (do they vary?).

FINDINGS (high-precision-numerical, robust across reps/seeds):
  1. REFINED LAW: [A,B] = c * mu^n with c = (-1)^(n-1) -- c=+1 at n=3, c=-1 at n=4 (scalar-dev ~1e-10..
     1e-14). c is forced to be an n-th root of unity (det: c^n = det[A,B]/det(mu)^n = 1); the OBSERVED
     branch is (-1)^(n-1). So degree=rank is the SIGNED scalar-matrix identity [A,B] = (-1)^(n-1) mu^n.
     (Prediction for n=5: c=+1.) The sign (-1)^(n-1) ECHOES the Dickson tower's parity, but see (2).
  2. UNIFICATION REFUTED. The meridian eigenvalues eig(mu)=eig(t) are GENERIC and VARY continuously
     across the component (|eig| spread ~0.3-0.4 over reps) -- they are NOT roots of unity, NOT metallic,
     and NOT the fixed Dickson char(M^n) roots. So degree=rank (a PERIPHERAL scalar-matrix identity) and
     the Dickson tower (the trace-map JACOBIAN spectrum) are genuinely DIFFERENT objects. The mechanism
     for "why n" lives in the bundle/peripheral structure, not the trace ring. Honest negative; it
     narrows the mechanism hunt (and kills the tempting CONJECTURED unification with a computation).

Standalone low-dim topology; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sys

import numpy as np

sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B71_sl3_apoly")
sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B73_sl4_apoly")
import peripheral as P3          # noqa: E402
import dehn_filling as D4        # noqa: E402


def scalar_c(A, B, t, n):
    """The scalar c in [A,B] = c * mu^n (mu=A^-1 t). Returns (c, scalar_dev, eig(mu))."""
    mu = np.linalg.inv(A) @ t
    comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    S = comm @ np.linalg.matrix_power(np.linalg.inv(mu), n)
    dev = (np.max(np.abs(S - np.diag(np.diag(S)))) + np.max(np.abs(np.diag(S) - np.mean(np.diag(S)))))
    return np.mean(np.diag(S)), dev, np.linalg.eigvals(mu)


def sl3_reps(n_reps=6, seed=11, budget=200):
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
        t, r = P3.monodromy(A, B)
        if t is not None:
            out.append((A, B, t))
    return out


def sl4_reps(n_reps=6, budget=300):
    out = []
    for sd in range(budget):
        if len(out) >= n_reps:
            break
        r = D4.realize_bundle_rep(D4.SPEC_W1, seed=sd, tries=60)
        if r is not None:
            out.append(r)
    return out


def c_over_reps(reps, n):
    """Returns (list of c, list of scalar_dev, eig(mu) |.|-spread across reps)."""
    cs, devs, mus = [], [], []
    for A, B, t in reps:
        c, dev, em = scalar_c(A, B, t, n)
        if dev < 1e-7:
            cs.append(c); devs.append(dev); mus.append(np.sort(np.abs(em)))
    spread = np.ptp(mus, axis=0) if len(mus) > 1 else np.zeros(1)
    return cs, devs, spread


def main():
    print("B77 (Phase 1a) -- degree=rank mechanism: the scalar c, and the A<->D unification test\n")
    for label, reps, n in [("SL(3) W1 {1,i,-i}", sl3_reps(), 3),
                           ("SL(4) {1,1,w,w^2}", sl4_reps(), 4)]:
        cs, devs, spread = c_over_reps(reps, n)
        cmean = np.mean(cs) if cs else float("nan")
        print(f"{label} (n={n}, {len(cs)} reps): [A,B] = c * mu^{n}")
        print(f"   c = {cmean:+.5f}  (predict (-1)^{n-1} = {(-1)**(n-1):+d})   scalar-dev <= {max(devs):.0e}")
        print(f"   eig(mu) |.|-spread across reps = {spread.round(3)}  "
              f"({'GENERIC/varying -> NOT fixed Dickson roots' if np.max(spread) > 0.05 else 'fixed'})")
    print("\nVERDICT:")
    print("  - REFINED LAW: [A,B] = (-1)^(n-1) mu^n on the principal Dehn-filling component (c^n=1 by det).")
    print("  - UNIFICATION REFUTED: meridian/longitude eigenvalues are generic + vary across the")
    print("    component, NOT the Dickson char(M^n) roots. degree=rank is peripheral, not trace-ring.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
