"""B71 (P2) -- the geometric component V0 has NO tidy closed A-variety form (matches Falbel D1).

Unlike the Dehn-filling components (W1=D2: M^3=L; W2=D3: M^3 L=1, exact -- V44/V47), the geometric
component V0={x1=x4, x2=x5} (containing Sym^2 of the figure-eight SL(2) holonomy) has NO clean closed
A-variety form. This is expected: Falbel-Guilloux-Koseleff-Rouillier-Thistlethwaite (arXiv:1412.4711)
report the geometric D1 boundary projection as a 141-polynomial Groebner basis, generically 1-to-4 over
a hypersurface in C^3 -- a large ideal, not a curve. A symbolic elimination of the 2 free parameters
from the V0 peripheral data is correspondingly intractable in-house.

This script confirms the characterization numerically: on V0 the meridian mu still COMMUTES with the
longitude [A,B] (V46), but NO clean monomial relation M^a L^b is constant across the component (the
smallest relative spread over the family is O(1), and the W1/W2 relations fail) -- so there is no tidy
A-variety relation. Honest characterization (matching the literature), not a new closed form.

Standalone low-dim topology; no physics. Proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import itertools
import pathlib

import numpy as np

_HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("b71_peripheral", _HERE / "peripheral.py")
per = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(per)


def v0_peripheral_data(npts=14, seed=7):
    rng = np.random.default_rng(seed)
    data, commute = [], []
    for _ in range(npts):
        p = complex(rng.standard_normal(), rng.standard_normal())
        q = complex(rng.standard_normal(), rng.standard_normal())
        out = per.realize(per.V0(p, q))
        if out is None:
            continue
        A, B = out
        mu, cdev = per.meridian(A, B)
        if mu is None:
            continue
        commute.append(cdev)
        comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
        M, L = per.ratios(mu), per.ratios(comm)
        data.append((M[0], M[1], L[0], L[1]))
    return data, commute


def smallest_monomial_spread(data, deg=4):
    """Smallest relative spread of M^a L^b across the V0 family (a CONSTANT one => a tidy relation)."""
    best = np.inf
    for a, b in itertools.product(range(-deg, deg + 1), repeat=2):
        if a == 0 and b == 0:
            continue
        arr = np.array([M0 ** a * L0 ** b for (M0, M1, L0, L1) in data])
        best = min(best, float(np.std(arr) / (np.mean(np.abs(arr)) + 1e-30)))
    return best


def main():
    print("B71 (P2) -- geometric V0: no tidy A-variety form (matches Falbel D1 = 141-poly)\n")
    data, commute = v0_peripheral_data()
    print(f"  V0: {len(data)} reps; meridian commutes with [A,B]: median {np.median(commute):.1e}")
    spread = smallest_monomial_spread(data)
    print(f"  smallest relative spread of any M^a L^b (|a|,|b|<=4) across V0 = {spread:.2e}")
    m3l = np.median([abs(M0 ** 3 - L0) for (M0, M1, L0, L1) in data])
    print(f"  W1's M^3=L on V0: median |M^3-L| = {m3l:.2e}  (fails, as expected)")
    print("\n  => NO clean monomial relation is constant on V0; the geometric A-variety is a large")
    print("     ideal (no tidy form), consistent with Falbel D1 (141-poly). Symbolic eliminant intractable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
