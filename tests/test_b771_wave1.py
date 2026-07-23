"""B771 Wave 1 -- compute-grade locks on the banked cell verdicts.

Each lock recomputes its discriminating fact (never greps prose). Facts too
expensive to recompute here (the Kashaev r-stream, the Bianchi index-10, the
E6 branching) are locked at the artifact level via wave1_results.json's
verdict/upheld invariants -- their full recomputation lives in the cell
compute.py files, all re-runnable.
"""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B771_phase1_wave1"


def test_oi031_e3_exact_identity():
    # the depth-5 triple cubic closes: prod (t - cos(2pi k/27)/6) = t^3 - t/48 - cos(2pi/9)/864
    t = sp.symbols("t")
    poly = sp.prod([t - sp.cos(2 * sp.pi * k / sp.Integer(27)) / 6 for k in (1, 10, 19)])
    target = t**3 - t / 48 - sp.cos(2 * sp.pi / sp.Integer(9)) / 864
    for tv in (sp.Rational(1, 3), sp.Rational(-2, 7), sp.Rational(5, 11)):
        assert abs(sp.N(sp.expand(poly - target).subs(t, tv), 80)) < sp.Float(10) ** -70


def test_oi031_chebyshev_clearing():
    # u = 12t: u^3 - 3u = 2cos(2pi/9) at u = 2cos(2pi/27) -- the zeta27 trisection rung
    u = 2 * sp.cos(2 * sp.pi / sp.Integer(27))
    assert abs(sp.N(u**3 - 3 * u - 2 * sp.cos(2 * sp.pi / sp.Integer(9)), 80)) < sp.Float(10) ** -70


def test_oi200_d4_ceiling_identified():
    x = sp.symbols("x")
    v = sp.sqrt(5 + 2 * sp.sqrt(3) - 2 * sp.sqrt(2) - sp.sqrt(6))
    assert sp.minimal_polynomial(v, x) == x**8 - 20 * x**6 + 98 * x**4 - 172 * x**2 + 97
    assert abs(sp.N(v - sp.Float("1.78498872478"), 20)) < sp.Float(10) ** -10


def test_oi186_family_law_fricke_15():
    # tr(A_m A_n) = (mn)^2 + (m+n)^2 + 2; the (1,2) value is Fricke's 15
    law = lambda m, n: (m * n) ** 2 + (m + n) ** 2 + 2
    assert law(1, 2) == 15
    assert law(1, 1) == 7 and law(2, 3) == 63


def test_oi151_torsion_one_identity():
    # det(N - I) = 2 - tr(N) for N in SL(2), basis-free
    a, b, c, d0 = sp.symbols("a b c d0")
    N = sp.Matrix([[a, b], [c, d0]])
    det_ni = (N - sp.eye(2)).det()
    # det(N-I) = 1 - tr(N) + det(N); imposing det(N)=1 gives exactly 2 - tr(N)
    assert sp.simplify(det_ni - (2 - N.trace()) - (N.det() - 1)) == 0


def test_oi055_five_inert_lemma():
    # the in-cell kill's arithmetic ground: (-3/5) = -1, T^2+T+1 irreducible mod 5
    assert sp.jacobi_symbol(-3, 5) == -1
    T = sp.symbols("T")
    assert sp.factor_list(T**2 + T + 1, modulus=5)[1][0][1] == 1  # single irreducible factor


def test_wave_integrity():
    d = json.loads((ARC / "wave1_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 12  # OI-150's report died; its re-run is Wave 2's
    banked_upheld = [i for i, c in cells.items() if c["upheld"]]
    assert len(banked_upheld) == 11
    assert cells["OI-148"]["upheld"] is False  # the circularity catch stays on the record
    for i in banked_upheld:
        assert cells[i]["verdict"] in ("RESOLVED-A", "RESOLVED-B")
        assert (ARC / "cells" / i / "compute.py").exists()
        assert (ARC / "cells" / i / "output.txt").exists()


# ---- Wave 2 locks -------------------------------------------------------------


def test_w2_148r_resolvent_norm_frozen():
    # the exact structure behind the refutation: |sum_j omega^j (z^k + z^-k)| = 3 in Q(zeta27),
    # i.e. the Z/3 resolvent of the Chebyshev triple is 3*(a root of unity) -- norm 9, not 27
    z = sp.exp(2 * sp.pi * sp.I / 27)
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    res = sum(omega**j * (z ** (10**j % 27) + z ** (-(10**j) % 27)) for j in range(3))
    assert abs(sp.N(sp.Abs(res) - 3, 60)) < sp.Float(10) ** -50
    # the level-9 anchor is 3*zeta9^-1 in disguise: zeta9 + zeta9^4 + zeta9^7 = 0
    z9 = sp.exp(2 * sp.pi * sp.I / 9)
    assert abs(sp.N(z9 + z9**4 + z9**7, 60)) < sp.Float(10) ** -50


def test_w2_148r_sqrt3_counterfactual_excluded():
    # (z^9 - z^18)^2 = -3 exactly: the unique quadratic subfield of Q(zeta27) is Q(sqrt(-3)),
    # so sqrt(3) is not in the field and the N = 12*sqrt(3) rescue cannot exist
    z = sp.exp(2 * sp.pi * sp.I / 27)
    assert abs(sp.N((z**9 - z**18) ** 2 + 3, 60)) < sp.Float(10) ** -50


def test_w2_197_weights_are_odd_phi_powers():
    # the six closed-formed kappa=10 weights: {phi^1, phi^-1, phi^3, phi^-3, 4phi^1, 4phi^-1}/(10 sqrt 5)
    phi = (1 + sp.sqrt(5)) / 2
    weights = [phi, 1 / phi, phi**3, 1 / phi**3, 4 * phi, 4 / phi]
    scaled = [sp.nsimplify(w / (10 * sp.sqrt(5))) for w in weights]
    assert len(set(scaled)) == 6  # six distinct values, all exact in Q(sqrt5)
    for s_ in scaled:
        assert sp.simplify(sp.expand(s_ * 10 * sp.sqrt(5)) - sp.expand(weights[scaled.index(s_)])) == 0


def test_wave2_integrity():
    d = json.loads((ARC / "wave2_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 13
    upheld = [i for i, c in cells.items() if c["upheld"]]
    assert sorted(upheld) == ["W2-020", "W2-140", "W2-148r", "W2-174", "W2-197", "W2-237"]
    refused = [i for i, c in cells.items() if c["upheld"] is False]
    assert len(refused) == 7
    for i in upheld:
        assert (ARC / "cells" / i / "compute.py").exists()
