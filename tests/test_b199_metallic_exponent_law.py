"""B199 -- the metallic exponent: no closed-form law; sublocus correction of B198 (V192). Fast pyenv locks.

Locks the DETERMINISTIC refuters that kill every simple k(o,m) law, plus the sublocus evidence (from the
shipped grid_summary.json) for the B198 down-tier. The slow numeric grid is the reproducer (grid_driver.py),
not the test. Standalone character-variety math; nothing to CLAIMS.md.
"""
import os
import json
from math import gcd
from functools import reduce
import numpy as np

HERE = os.path.dirname(__file__)
SUMMARY = os.path.join(HERE, "..", "frontier", "B199_metallic_exponent_law", "grid_summary.json")


def _lcm(a, b):
    return a * b // gcd(a, b)


def _order(z, maxd=60):
    return next((d for d in range(1, maxd + 1) if abs(z ** d - 1) < 1e-9), None)


def _eff_o(o, exps):
    """effective/projective order = order of the eigenvalue-ratio group of A=diag(zeta_o^exps)."""
    z = np.exp(2j * np.pi / o)
    diag = [z ** e for e in exps]
    orders = [_order(diag[i] / diag[j]) for i in range(len(diag)) for j in range(len(diag))
              if i != j and abs(diag[i] - diag[j]) > 1e-9]
    return reduce(_lcm, orders)


def _Apow_diag(o, exps, m):
    z = np.exp(2j * np.pi / o)
    return np.round(np.diag(np.linalg.matrix_power(np.diag([z ** e for e in exps]), m)), 6)


def test_o4_o8_collision_invariant():
    # o=4 and o=8 share eff_o=4 -> both give k=3 at m=1 -> kills k=7-o, f(o), gcd-laws
    assert _eff_o(4, [0, 1, 3]) == 4
    assert _eff_o(8, [1, 3, 5, 7]) == 4
    assert _eff_o(3, [0, 1, 2]) == 3
    assert _eff_o(5, [0, 1, 2, 3, 4]) == 5


def test_Am_spectrum_collision():
    # A^2(o=4 {1,i,-i}) == A^3(o=6 {1,z6,z6^5}) == diag(1,-1,-1) EXACTLY, yet k=2 vs k=1
    # -> no pure-A^m-spectral / order(A^m) law can exist
    a2 = _Apow_diag(4, [0, 1, 3], 2)
    a3 = _Apow_diag(6, [0, 1, 5], 3)
    assert np.allclose(a2, [1, -1, -1])
    assert np.allclose(a3, [1, -1, -1])
    assert np.allclose(a2, a3)


def test_degeneracy_o_divides_m():
    # o|m  => A^m = I  => mu = A^-m t = t collapses (inadmissible) -- e.g. m=4, o=4
    assert np.allclose(_Apow_diag(4, [0, 1, 3], 4), [1, 1, 1])
    assert np.allclose(_Apow_diag(3, [0, 0, 1, 2], 3), [1, 1, 1, 1])


def _summary():
    return {c["id"]: c for c in json.load(open(SUMMARY))}


def test_sign_law_on_committed_cells():
    s = _summary()
    # surviving closed form: s = (-1)^(n-1) on committed cells (n=3->+1, n=4->-1, n=5->+1)
    for cid in ["m1_o3_n4", "m1_o4_n3", "m1_o5_n5", "m2_o3_n4", "m2_o4_n3", "m3_o4_n3"]:
        c = s[cid]
        assert c["geometric_s"] == (-1) ** (c["n"] - 1), cid


def test_o4_column_non_monotone():
    s = _summary()
    # the o=4 column k=(3,2,3) over m=(1,2,3) -- non-monotone, kills affine/2-param laws
    assert [s["m1_o4_n3"]["geometric_k"], s["m2_o4_n3"]["geometric_k"], s["m3_o4_n3"]["geometric_k"]] == [3, 2, 3]


def test_sublocus_phenomenon_corrects_b198():
    s = _summary()
    # B198 down-tier: clean [A,B]=mu^k is a ~1% SUBLOCUS at SL5, but the whole component at SL3
    assert s["m1_o5_n5"]["clean_frac"] < 5.0      # SL5 o5: sublocus (~0.9%)
    assert s["m1_o4_n3"]["clean_frac"] > 90.0     # SL3 o4: whole component (100%)


if __name__ == "__main__":
    for fn in [test_o4_o8_collision_invariant, test_Am_spectrum_collision, test_degeneracy_o_divides_m,
               test_sign_law_on_committed_cells, test_o4_column_non_monotone, test_sublocus_phenomenon_corrects_b198]:
        fn()
    print("ALL CHECKS PASS")
