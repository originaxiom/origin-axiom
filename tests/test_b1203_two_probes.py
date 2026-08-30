"""B1203 lock -- two probes, both negative; the identity credited to B148."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1203_two_probes"


def test_the_climb_preserves_kappa_and_controls_bite():
    x, y, z = sp.symbols("x y z")
    kappa = x**2 + y**2 + z**2 - x*y*z - 2
    kap = lambda t: sp.expand(t[0]**2 + t[1]**2 + t[2]**2 - t[0]*t[1]*t[2] - 2)
    cur = (x, y, z)
    for _ in range(6):                                  # (X,Y) -> (XY, X)
        a, b, c = cur
        cur = (c, a, sp.expand(a*c - b))
        assert sp.simplify(kap(cur) - kappa) == 0
    assert sp.simplify(kap((x**2 - 2, y, x*z - y)) - kappa) != 0   # bite
    assert sp.simplify(kap((z, z, x)) - kappa) != 0                # bite


def test_verdict_credits_b148_and_records_the_catch():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "NEGATIVE"
    c = d["claim_one_line"]
    assert "THIS IS NOT NEW" in c and "B148" in c
    assert "FIRST LIVE CATCH" in c
    assert "CUT OF EXACTLY ZERO" in c
    assert "MUST BREAK A SYMMETRY" in c
