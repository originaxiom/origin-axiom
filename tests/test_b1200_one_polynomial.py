"""B1200 lock -- one polynomial, three faces."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1200_one_polynomial"


def test_the_identity_is_exact():
    """Re-derive the load-bearing identity in the test itself, not from a cache."""
    u = sp.symbols("u")
    Phi3 = u**2 + u + 1
    # Phi3(kappa-2) = 0 identically mod Phi3, with kappa = u^2 + 2
    assert sp.rem(((u**2 + 2) - 2)**2 + ((u**2 + 2) - 2) + 1, Phi3, u) == 0
    roots = sp.solve(Phi3, u)
    # the saddle set IS {kappa-2, conj}, and u -> u^2 is the swap (= c)
    assert {sp.expand(r**2) for r in roots} == set(roots)
    assert sp.expand(roots[0]**2) == roots[1]
    # face 3: the same polynomial on the boundary companion
    M = sp.Matrix([[0, -1], [1, -1]])
    assert M * M + M + sp.eye(2) == sp.zeros(2, 2) and M**3 == sp.eye(2)


def test_arc_verdict():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["id"] == "B1200" and d["verdict"] == "PROVED"
    c = d["claim_one_line"]
    assert "THE MAP BETWEEN THEM IS THE PROGRAM'S ONE INVOLUTION" in c
    assert "ONE INVARIANT" in c
    assert "CITED, their certificate not re-run here" in c    # the quine stays cited
    assert "nothing weakens a negative" in c
