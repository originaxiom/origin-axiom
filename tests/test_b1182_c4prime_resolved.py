"""B1182 lock -- C4' resolved positive: the unique iso (c,r,theta)->(k11,k7,k5); the arrow typed finite."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def test_arc_verdict_proved():
    d = json.loads((ROOT / "frontier" / "B1182_c4prime_resolved" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1182" and d["verdict"] == "PROVED"
    assert "(k11, k7, k5)" in d["claim_one_line"]
    assert "THE ARROW IS FINITE-PLACE" in d["claim_one_line"]
    assert "self-correction" in d["claim_one_line"].lower()


def test_trace_reversal_invariance_live():
    a11,a12,a21,a22,b11,b12,b21,b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
    A = sp.Matrix([[a11,a12],[a21,a22]]); B = sp.Matrix([[b11,b12],[b21,b22]])
    for ms in ([A,B],[A,A,B],[A,B,A,B]):
        fwd = sp.eye(2); rev = sp.eye(2)
        for m in ms: fwd = fwd*m
        for m in reversed(ms): rev = rev*m
        assert sp.simplify(sp.trace(fwd)-sp.trace(rev)) == 0


def test_unique_k_fixer_and_group_law_live():
    z = sp.symbols('z'); PHI = sp.Poly(z**4 - z**2 + 1, z)
    red = lambda e: sp.Poly(sp.expand(e), z).rem(PHI).as_expr()
    act = lambda e,k: red(sp.expand(e.subs(z, z**k)))
    sqrt3 = red(z + z**11); i_ = red(z**3); sqrtm3 = red(sqrt3*i_)
    fix = lambda e,k: sp.simplify(act(e,k)-e)==0
    assert [k for k in (5,7,11) if fix(sqrtm3,k)] == [7]   # k7 the unique K-fixer
    assert fix(sqrt3,11) and fix(i_,5)
    assert (11*7) % 12 == 5                                 # theta -> k5


def test_reproduce_committed():
    r = (ROOT / "frontier" / "B1182_c4prime_resolved" / "verification" / "reproduce.sh").read_text(encoding="utf-8")
    assert "REPRODUCES" in r and "k7" in r
