"""B1205 lock -- the dimension ledger; the codimension count re-derived in the test."""
import json, random
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1205_the_dimension_ledger"


def test_the_cubic_exists_and_cuts_only_one_dimension():
    h = sp.symbols("h0 h1 h2 h3")
    random.seed(20260829)
    T = [[[random.randint(-3, 3) for _ in range(3)] for _ in range(3)] for _ in range(4)]
    M = sp.zeros(3, 3)
    for k in range(4):
        M += h[k] * sp.Matrix(T[k])
    C = sp.expand(M.det())
    assert C != 0 and sp.Poly(C, *h).total_degree() == 3      # a genuine failable cubic
    sols = sp.solve([sp.diff(C, v) for v in h], list(h), dict=True)
    assert [s for s in sols if any(s.get(v, v) != 0 for v in h)] == []   # smooth: selects nothing


def test_verdict_states_the_inversion():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "NEGATIVE"
    c = d["claim_one_line"]
    assert "IT IS THE LINEAR CUTS" in c or "THE LINEAR CUTS" in c
    assert "LOCK TOGETHER" in c
    assert "amended not discarded" in c
    assert "named, not run" in c
