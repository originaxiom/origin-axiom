"""B903 locks: the sign-law reduction (anti-palindromy + root parity)."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B903_sign_law")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_all_six_blocks_antipalindromic_and_formula_holds():
    r = _res()
    assert set(r) == {"1", "4", "5", "7", "8", "11"}
    for m, e in r.items():
        assert e["antipalindromic"] is True
        assert e["sign_formula_holds"] is True
        assert e["parity_matches_m"] is True


def test_root_parity_law_counts():
    r = _res()
    assert {m: e["pos_real_pairs"] for m, e in r.items()} == {
        "1": 1, "4": 2, "5": 3, "7": 3, "8": 4, "11": 5}


def test_spot_recheck_m4_exact():
    # independent exact recheck of the m = 4 block from the banked quotient
    R = json.load(open(os.path.join(
        os.path.dirname(ARC), "B581_six_torsions", "six_torsions_results.json")))
    t = sp.Symbol("t")
    cs = [sp.Rational(c[0]) for c in R["4"]["quotient"]]
    d = len(cs) - 1
    assert all(cs[i] == -cs[d - i] for i in range(d + 1))     # anti-palindromic
    P, rem = sp.div(sp.Poly(cs, t), sp.Poly(t - 1, t), domain="QQ")
    assert rem.is_zero
    tau = P.eval(1)
    assert sp.sign(tau) == 1                                   # theta-odd: +
    npos = sum(mult * sp.Poly(f, t).count_roots(0, sp.oo)
               for f, mult in P.factor_list()[1])
    assert npos == 4                                           # 2 pairs
