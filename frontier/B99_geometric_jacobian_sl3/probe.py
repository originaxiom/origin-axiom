"""B99 (Probe 1c) -- the SL(3) trace-map Jacobian at the GEOMETRIC representation.

Strengthens B98 (Probe 1) to SL(3): does the geometric rep again give a torsion-type spectrum rather than
the Dickson tower? Neutral low-dim topology; the 3d-3d / Daly framework is cited, not claimed.

The SL(3) geometric rep is Sym^2 of the SL(2) geometric figure-eight rep, on the V0 component (B71). The
SL(3) figure-eight trace map T_1 acts on the 8 trace coordinates by
    T_1(x1..x8) = (x3, x1, x1 x3 - x4 x2 + x6, x8, x4, x5, x2, x4 x8 - x1 x5 + x7).
At the geometric Sym^2 point c0 = sym2_groundtruth_coords(x_geom), x_geom=(3+sqrt(-3))/2:

RESULT. char(D T_1^2)|_geom = (t-1)^2 * [3 reciprocal pairs (t^2 - c_i t + 1)]:
  * 2 eigenvalues = 1  (tangent to the 2-dimensional fixed component V0);
  * 6 transverse eigenvalues forming 3 pairs {mu, 1/mu} (product 1), with pair-sums c_i = mu + 1/mu:
        c = 5            (the SL(2) torsion pair {(5+-sqrt 21)/2} carried up by Sym^2 -- B98),
        c = 4.5 +- 4.664 i  (two complex pairs from the Sym^2 deformation).
This is NOT the trivial-point Dickson SL(3) tower char(M^-1) char(M^2) char(M^3) (t-1)(t+1), whose
pair-sums are c in {-1, 3, 4} (real). So at SL(3) too, the geometric rep carries a TORSION-type
(twisted-Alexander) spectrum, NOT the tower -- consistent with B98 and with Daly (arXiv:2411.04431).

VERDICT (with B98). The Dickson tower is a TRIVIAL-rep phenomenon at SL(2) AND SL(3); the GEOMETRIC rep
carries the adjoint-torsion / twisted-Alexander spectrum (the SL(2) torsion pair c=5 appears at SL(3) via
Sym^2). The two trace-map fixed points are genuinely different objects. (3d-3d / Daly: cited, not claimed.)

Standalone low-dim topology / Lie theory; no physics claim; no Origin-core claim; P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _b71():
    spec = importlib.util.spec_from_file_location("b71_probe", _ROOT / "frontier" / "B71_sl3_apoly" / "probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _T1(c):
    x1, x2, x3, x4, x5, x6, x7, x8 = c
    return np.array([x3, x1, x1 * x3 - x4 * x2 + x6, x8, x4, x5, x2, x4 * x8 - x1 * x5 + x7], dtype=complex)


def _T1sq(c):
    return _T1(_T1(c))


def geometric_sl3_point():
    """The geometric SL(3) rep = Sym^2 of the SL(2) geometric figure-eight rep (x_geom=(3+sqrt-3)/2)."""
    xg = 1.5 + 0.5j * np.sqrt(3)
    return np.array(_b71().sym2_groundtruth_coords(xg), dtype=complex)


def jacobian_eigenvalues():
    """Eigenvalues of D(T_1^2) at the geometric SL(3) point (finite-difference, deterministic)."""
    c0 = geometric_sl3_point()
    h = 1e-7
    J = np.zeros((8, 8), complex)
    for j in range(8):
        e = np.zeros(8, complex)
        e[j] = h
        J[:, j] = (_T1sq(c0 + e) - _T1sq(c0 - e)) / (2 * h)
    return np.linalg.eigvals(J)


def reciprocal_pair_sums():
    """Return (num eigenvalue-1, list of pair-sums c_i = mu+1/mu of the transverse reciprocal pairs)."""
    ev = jacobian_eigenvalues()
    ev = ev[np.argsort(np.abs(ev - 1))]
    n1 = int(np.sum(np.abs(ev - 1) < 1e-4))
    trans = list(ev[np.abs(ev - 1) >= 1e-4])
    used, sums = set(), []
    for i in range(len(trans)):
        if i in used:
            continue
        for k in range(i + 1, len(trans)):
            if k not in used and abs(trans[i] * trans[k] - 1) < 1e-3:
                sums.append(trans[i] + trans[k])
                used |= {i, k}
                break
    return n1, sums


def main():
    print("B99 (Probe 1c) -- the SL(3) trace-map Jacobian at the GEOMETRIC rep\n")
    c0 = geometric_sl3_point()
    print(f"  geometric Sym^2 point fixed by T_1^2?  {np.max(np.abs(_T1sq(c0) - c0)):.1e}")
    n1, sums = reciprocal_pair_sums()
    print(f"  eigenvalue-1 multiplicity (tangent to V0): {n1}")
    print(f"  transverse reciprocal-pair sums c=mu+1/mu: {[f'{c:.3f}' for c in sums]}")
    print("  one pair has c=5 (the SL(2) torsion pair, B98, carried by Sym^2); the others complex.")
    print("  trivial-point SL(3) tower pair-sums are {-1, 3, 4} (real) -> DIFFERENT.")
    print("  => geometric rep carries the torsion/twisted-Alexander spectrum, NOT the tower (cf. Daly).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
