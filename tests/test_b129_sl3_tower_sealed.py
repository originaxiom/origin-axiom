"""Locks for B129 -- the SL(3) tower is sealed in Q(sqrt-3).

S1a (exact sympy) always runs: the principal Sym^2 metallic SL(3) rep is irreducible yet every trace in Q(sqrt-3).
The inQ3 detector regression (method bug B1) always runs. The off-sublocus search (S1b) is scipy-guarded; the silver
covers (S2) are SnapPy-guarded. The numeric test asserts only the ROBUST invariants (no escape), not the
seed/threshold-dependent reducible/finite split.
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b129_probe", _ROOT / "frontier/B129_sl3_tower_sealed/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B129 = _load()


# ---------------------------------------------------------------------------------------------------------------
# S1a -- exact symbolic: irreducible rep, all traces in Q(sqrt-3). Always runs.
# ---------------------------------------------------------------------------------------------------------------
def test_principal_rep_irreducible_and_in_Q3():
    r = B129.principal_sl3_rep()
    assert r["det_A"] == 1 and r["det_B"] == 1
    assert r["irreducible"] and r["algebra_dim"] == 9    # generates M_3 -> irreducible as a rep
    assert r["all_traces_in_Q3"]                          # ... yet sealed in Q(sqrt-3)


def test_principal_traces_match_handoff():
    import sympy as sp
    r = B129.principal_sl3_rep()
    # (re, im/sqrt3) for each trace -- the exact handoff values
    expect = {"trA": (3, 0), "trB": (3, 0),
              "trAB": (sp.Rational(1, 2), sp.Rational(-3, 2)),
              "trAinvB": (sp.Rational(9, 2), sp.Rational(5, 2)),
              "trComm": (sp.Rational(1, 2), sp.Rational(3, 2))}
    for name, (ok, re, ratio) in r["traces"].items():
        assert ok
        assert (sp.nsimplify(re), sp.nsimplify(ratio)) == expect[name]


# ---------------------------------------------------------------------------------------------------------------
# Method bug B1 regression: the corrected inQ3 detector accepts pure rationals, rejects a genuine escape.
# ---------------------------------------------------------------------------------------------------------------
def test_inQ3_accepts_rationals_rejects_escape():
    import math
    assert B129.inQ3(complex(1.0, 0.0))                       # 1 = 1 + 0*sqrt-3 IS in Q(sqrt-3) (B1 fix)
    assert B129.inQ3(complex(0.5, -1.5 * math.sqrt(3)))       # 1/2 - (3/2) sqrt-3
    assert not B129.inQ3(complex(math.sqrt(2), 0.0))          # sqrt2 is a genuine escape
    assert not B129.inQ3(complex(0.0, math.sqrt(5)))          # sqrt5 i: Im/sqrt3 irrational -> escape


# ---------------------------------------------------------------------------------------------------------------
# S1b -- off-sublocus search (scipy-guarded). Assert ONLY the robust invariant: no genuine escape.
# ---------------------------------------------------------------------------------------------------------------
def test_offsublocus_no_escape():
    pytest.importorskip("scipy")
    pytest.importorskip("numpy")
    r = B129.offsublocus_search(starts=24)                    # smaller deterministic run for the suite
    assert r is not None
    assert r["converged"] >= 12                               # the search does converge to fixed classes
    assert r["max_dist_to_Q3"] < 1e-4                         # every converged point within ~1e-6 of Q(sqrt-3)
    assert r["genuine_escapes"] == 0                          # ROBUST (polished, threshold 1e-4): 0 escapes
    assert r["no_escape"]


# ---------------------------------------------------------------------------------------------------------------
# S2 -- the covers correction (SnapPy-guarded).
# ---------------------------------------------------------------------------------------------------------------
def test_silver_covers_reach_rank_two():
    pytest.importorskip("snappy")
    c = B129.silver_covers()
    assert c is not None
    assert c["base_cusps"] == 1                               # base is one-cusped
    assert c["reaches_2_2"]                                   # degree-2 cover reaches (2 cusps, free rank 2)
