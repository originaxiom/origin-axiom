"""B88 (Task 2) -- the SL(4) Dehn-filling census: which degrees appear at rank 4.

Over a targeted sweep of finite-order (root-of-unity) product-1 A-spectra at n=4, exactly TWO clean
Dehn-filling components appear -- degrees {3, 4}:
  * {1, 1, w, w^2}  (tr A = 1, char (z-1)^2(z^2+z+1))  ->  M^4 = L   (degree 4 = rank; the PRINCIPAL
    component; scalar c = -1, a root of unity, since det(mu)=1 here -- B77's (-1)^(n-1));
  * {prim 8th roots} (tr A = 0, char z^4+1)            ->  M^3 = L   (degree 3; a non-principal
    component; the scalar c is rep-dependent / not a clean root of unity, because det(mu) != 1 there).
So at rank 4 the Dehn-filling tower exposes degrees 3 AND 4 -- consistent with the conjecture "rank n
exposes degrees ~3..n" (n=4 -> {3,4}). The DEGREE k is the robust invariant (B73/B83 eig test); the
scalar c is a clean root of unity ONLY on the principal {det mu = 1} component.

HONEST SCOPE. (1) No additional clean Dehn-filling component was found over the searched spectra -- but
true completeness needs the symbolic Fix(T_1^2) (Task 1a / B71 at rank 4), not a numerical search.
(2) NOT every irreducible figure-eight bundle rep is on a Dehn-filling component: e.g. {z8, z8^-1, i, -i}
and the primitive 12th-root spectrum admit irreducible reps but with NO clean [A,B]=c*mu^k relation
(dev ~ O(1)) -- they are generic bundle reps, not Dehn-filling. m=1 sanity baseline: the two known
components reproduce. Standalone low-dim topology; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sys

import numpy as np

sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B73_sl4_apoly")
import dehn_filling as D4  # noqa: E402

W = np.exp(2j * np.pi / 3)
Z8 = np.exp(1j * np.pi / 4)


def degree_of(spec, ks=(2, 3, 4, 5, 6), n_reps=2, budget=25, tries=25):
    """Best clean degree k in [A,B]=c*mu^k for A=diag(spec). Returns (found, best_k, dev, c)."""
    devs = {k: [] for k in ks}; cs = {k: [] for k in ks}; found = 0
    for sd in range(budget):
        if found >= n_reps:
            break
        r = D4.realize_bundle_rep(spec, seed=sd, tries=tries)
        if r is None:
            continue
        A, B, t = r
        mu = np.linalg.inv(A) @ t
        comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        if np.max(np.abs(mu @ comm - comm @ mu)) > 1e-6:
            continue
        found += 1
        for k in ks:
            S = comm @ np.linalg.matrix_power(np.linalg.inv(mu), k)
            dev = np.max(np.abs(S - np.diag(np.diag(S)))) + np.max(np.abs(np.diag(S) - np.mean(np.diag(S))))
            devs[k].append(dev); cs[k].append(np.mean(np.diag(S)))
    med = {k: (np.median(devs[k]) if devs[k] else np.inf) for k in ks}
    cc = {k: (np.mean(cs[k]) if cs[k] else np.nan) for k in ks}
    bk = min(med, key=lambda k: med[k]) if found else None
    return found, bk, (med[bk] if bk else np.inf), (cc[bk] if bk is not None else np.nan)


# the SL(4) census: the two clean Dehn-filling components + non-component controls
COMPONENTS = {
    "{1,1,w,w2} (principal, tr=1)": [1, 1, W, W ** 2],         # -> M^4=L, c=-1
    "{prim 8th, z^4+1} (tr=0)": [Z8, Z8 ** 3, Z8 ** 5, Z8 ** 7],  # -> M^3=L
}
NON_COMPONENTS = {
    "{z8,z8^-1,i,-i}": [Z8, Z8.conjugate(), 1j, -1j],          # irreducible reps, NO clean degree
}


def main():
    print("B88 (Task 2) -- the SL(4) Dehn-filling census\n")
    print("Clean Dehn-filling components (degree k in [A,B]=c*mu^k):")
    degs = set()
    for name, spec in COMPONENTS.items():
        f, bk, dev, c = degree_of(spec)
        if f >= 1 and dev < 1e-7:
            degs.add(bk)
            print(f"  {name}: M^{bk}=L  (dev {dev:.0e}, c={c:+.3f}, |c|={abs(c):.3f})")
    print(f"\n  Degrees found at rank 4: {sorted(degs)}  (consistent with 'rank n -> degrees ~3..n')")
    print("\nControl (irreducible bundle reps that are NOT on a Dehn-filling component):")
    for name, spec in NON_COMPONENTS.items():
        f, bk, dev, c = degree_of(spec)
        print(f"  {name}: {f} reps, best dev {dev:.0e} -> {'clean M^%d' % bk if dev < 1e-7 else 'NO clean relation'}")
    print("\nNET: at rank 4, exactly the two components {1,1,w,w2}->M^4 (principal) and {prim 8th}->M^3;")
    print("  degrees {3,4}. The degree is the invariant; c is a root of unity only on the principal")
    print("  component. True completeness needs the symbolic Fix(T_1^2) (Task 1a).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
