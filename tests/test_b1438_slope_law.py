"""B1438 lock -- the slope law.

The index of every sector module and every coupling of the Standard-Model frame are read off the slope s(chi), the
value on the meridian of the class of H^1(M; chi) normalised on the longitude. Live: the architecture census from the
slope alone against B1434's record (the levels up to 60 characters; all 68 recorded), the firing law module by module
against main's index code, exact slopes, the coupling law on the own-level state, and the bites.
"""
import json
import pathlib
import sys
from fractions import Fraction

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1438_the_slope_law" / "verification"
sys.path.insert(0, str(V))
B1434 = ROOT / "frontier" / "B1434_the_architecture_census" / "verification" / "architecture_census.json"


def _record():
    return [o for o in json.loads(B1434.read_text()) if "candidates" in o]


def _same(r, o, fields):
    norm = lambda v: {str(a): b for a, b in v.items()} if isinstance(v, dict) else v
    return [f for f in fields if norm(r[f]) != norm(o[f])]


def test_the_census_from_the_slope_alone_small_levels_live():
    import slope_census as sc
    n = 0
    for o in _record():
        if o["characters"] > 60:
            continue
        r, _, _ = sc.slope_census(1 if o["state"][0] == "+" else -1, o["state"][1:], o["k"])
        assert _same(r, o, sc.FIELDS) == [], (o["state"], o["k"])
        n += 1
    assert n >= 25


def test_the_census_from_the_slope_alone_all_68_recorded():
    res = json.loads((V / "slope_census.json").read_text())
    assert len(res) == 68 and all(r["agrees_with_B1434"] for r in res)
    assert sum(r["generation_backgrounds"] for r in res) == 8800
    assert sum(o["candidates"] for o in _record()) == 942268


@pytest.mark.slow
def test_the_census_from_the_slope_alone_all_68_live():
    import slope_census as sc
    for o in _record():
        r, _, _ = sc.slope_census(1 if o["state"][0] == "+" else -1, o["state"][1:], o["k"])
        assert _same(r, o, sc.FIELDS) == [], (o["state"], o["k"])


def test_the_bite_a_wrong_slope_does_not_reproduce_the_census():
    """merge two slope classes on s961: the firing count changes, so the agreement above is not vacuous"""
    import slope_census as sc
    r, bgs, cls = sc.slope_census(1, "LR", 3)
    assert r["firing"] == 72 and r["generation_backgrounds"] == 48
    classes = sorted(set(cls.values()))
    assert len(classes) == 3
    merged = {c: (classes[0] if v == classes[1] else v) for c, v in cls.items()}
    N = r["N"]
    add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N)
    neg = lambda x: ((-x[0]) % N, (-x[1]) % N)
    fire = lambda C: sum(1 for l in C for a in C if a != l and int(C[a] == C[l]) - int(C[neg(add(a, neg(l)))] == C[l]) != 0)
    assert fire(cls) == 72 and fire(merged) != 72


def test_exact_slopes_of_the_roots_three_fold_cover():
    import slope_law as sl
    N, F, S = sl.exact_slopes(1, "LR", 3)
    assert N == 4 and len(S) == 16
    order = lambda c: 1 if not any(c) else (2 if all(2 * v % 4 == 0 for v in c) else 4)
    for c, s in S.items():
        if isinstance(s, str):
            assert c == (0, 0, 0)
        elif order(c) == 2:
            assert s == 0
        else:
            assert s == 1 or s == -1
    assert sum(1 for s in S.values() if not isinstance(s, str) and s == 1) == 6
    assert sum(1 for s in S.values() if not isinstance(s, str) and s == -1) == 6


def test_exact_slopes_of_the_own_level_state_and_of_the_double_cover():
    import slope_law as sl
    N, F, S = sl.exact_slopes(-1, "LLRLR", 1)
    vals = sorted(Fraction(s.c[0]) for s in S.values() if not isinstance(s, str))
    assert all(not any(s.c[1:]) for s in S.values() if not isinstance(s, str))
    assert vals == sorted([Fraction(0)] * 6 + [Fraction(-4, 3)] * 2 + [Fraction(-3, 2)] * 2 + [Fraction(-3, 4)])
    N, F, S = sl.exact_slopes(1, "LR", 2)
    for s in S.values():
        if not isinstance(s, str):
            assert (s * s) == F.const(Fraction(1, 5))          # +-1/sqrt 5


def test_the_firing_law_module_by_module_against_the_index_code():
    import slope_law as sl
    for eps, word, k in [(1, "LR", 3), (-1, "LLRLR", 1), (1, "LR", 2)]:
        r = sl.verify_level(eps, word, k)
        assert r["firing_mismatches"] == 0 and r["degenerate_modules_firing"] == 0 and r["deck_invariant"]
        assert any(key.startswith("I=1,") for key in r["firing_table"])     # the law is tested where it fires
        if r["backgrounds"]:
            assert r["value_law_pairs"] == r["value_law_holds"] > 0


def test_the_value_law_on_every_background_recorded():
    res = json.loads((V / "value_law.json").read_text())
    assert len(res) == 30 and sum(r["backgrounds"] for r in res) == 8800
    assert all(r["pairs"] == r["value_law_holds"] for r in res)
    assert sum(r["zero_couplings"] for r in res) > 0 and sum(r["pairs"] - r["zero_couplings"] for r in res) > 0


def test_the_pull_back_law_and_reality():
    import slope_law as sl
    from cot_formula import numeric, orbit_sum_general, letters
    N1, F1, S1 = sl.exact_slopes(1, "LR", 3)
    N2, F2, S2 = sl.exact_slopes(1, "LR", 6)
    for c, s in S1.items():
        if isinstance(s, str):
            continue
        c2 = tuple(v * (N2 // N1) % N2 for v in c)
        assert abs(numeric(S2[c2]) - 2 * numeric(s)) < 1e-9
    steps = letters(-1, "LLRLR", 1)
    N, F, S = sl.exact_slopes(-1, "LLRLR", 1)
    for (i, j, _), s in S.items():
        if isinstance(s, str):
            continue
        v = orbit_sum_general(i, j, N, steps)
        assert abs(v - numeric(s)) < 1e-9 and abs(v.imag) < 1e-9


def test_no_coupling_between_backgrounds_with_different_extension_characters():
    """Theorem E, live on the own-level state: every invariant functional is found by linear algebra; between
    different extension characters it is quotient.quotient and its triple product is zero; within one, eps couples"""
    import cross_couplings as xc
    r = xc.run(-1, "LLRLR", 1)
    t = r["table"]
    assert t["different l | dim 1 | quotient.quotient | Y = 0"] > 0
    assert not any(k.startswith("different l") and "Y != 0" in k for k in t)
    assert not any(k.startswith("different l") and "| other |" in k for k in t)
    assert t["same l | dim 1 | other | Y != 0"] > 0                      # the bite: the instrument does see couplings


def test_theorem_e_recorded():
    res = json.loads((V / "cross_couplings.json").read_text())
    assert {(r["state"], r["k"]) for r in res} == {("+LR", 3), ("-LLRLR", 1), ("-LR", 3), ("+LR", 4)}
    zero = 0
    for r in res:
        for k, v in r["table"].items():
            if k.startswith("different l") and "dim" in k:
                assert "quotient.quotient | Y = 0" in k, k
                zero += v
    assert zero == 11724
