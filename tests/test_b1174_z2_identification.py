"""B1174 lock -- the Z/2-identification cell (R50-3): NOT ONE TORSOR -- ONE SHARED INVOLUTION.
Re-runs the exact cyclotomic leg table live (fast) + pins the verdict structure. Gate 5 clean."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1174_z2_identification"


def _d():
    return json.loads((ARC / "b1174_results.json").read_text(encoding="utf-8"))


def test_arc_verdict_negative():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1174" and d["verdict"] == "NEGATIVE"
    assert d["instrument"] is False and d["creates_law"] is False
    assert "ONE SHARED INVOLUTION" in d["claim_one_line"]


def test_exact_leg_table_live():
    # the load-bearing Galois facts, re-derived exactly at test time (mod Phi_12 = z^4 - z^2 + 1)
    z = sp.symbols('z')
    PHI = sp.Poly(z**4 - z**2 + 1, z)
    red = lambda e: sp.Poly(sp.expand(e), z).rem(PHI).as_expr()
    act = lambda e, k: red(sp.expand(e.subs(z, z**k)))
    sqrt3 = red(z + z**11); i_ = red(z**3); sqrtm3 = red(sqrt3 * i_)
    # c = k11: fixes sqrt3, flips sqrt-3 (the orientation leg)
    assert sp.simplify(act(sqrt3, 11) - sqrt3) == 0
    assert sp.simplify(act(sqrtm3, 11) + sqrtm3) == 0
    # k7: fixes K pointwise (sqrt-3 fixed), flips sqrt3 (the form-class swap / bit 2)
    assert sp.simplify(act(sqrtm3, 7) - sqrtm3) == 0
    assert sp.simplify(act(sqrt3, 7) + sqrt3) == 0
    # k5 fixes i
    assert sp.simplify(act(i_, 5) - i_) == 0


def test_field_level_parity_mechanism():
    r = _d()["refutations_exact"]
    assert "TRIVIAL on Q(sqrt5)" in r["b957_value_leg"]
    assert "IFF imaginary" in r["b957_value_leg"]
    assert "MOVES sqrt-15" in r["s068_genus_leg"]


def test_shared_involution_and_census_grounding():
    d = _d()
    assert d["one_line_theorem"] == "NOT ONE TORSOR -- ONE SHARED INVOLUTION"
    p = d["proved_shared_involution"]
    assert "the mirror IS c" in p["mirror_eq_conjugation"]
    assert "k=11 = c" in p["branch_V4_leg_table_exact"] and "k=7" in p["branch_V4_leg_table_exact"]
    assert "bit 1 = c" in d["consequences"]["b1164_census"]


def test_consequences_routed():
    c = _d()["consequences"]
    assert "PARTIALLY PROMOTED" in c["b1169_s1"] and "QP-4" in c["b1169_s1"]
    assert (ROOT / "frontier" / "B1169_qualia_parity_synthesis" / "ADDENDUM_s1_partial_B1174.md").exists()
    assert "share the c-leg" in c["b1166_c4"]
    assert "SUPPORTED-CONJECTURAL" in c["b1161_label"]


def test_bug_catch_fenced():
    f = _d()["fences"]
    assert "self-caught" in f and "hand-check" in f.lower()


def test_reproduce_runner_committed():
    runners = list((ARC / "verification").glob("reproduce*.sh"))
    assert runners and "REPRODUCES" in runners[0].read_text(encoding="utf-8")


def test_gate5_clean():
    assert "Gate 5 clean" in _d()["fences"]
