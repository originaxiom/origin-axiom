"""B1343 - the elliptic bridge is closed, and 'derivable' is not 'enriching'.

These recompute the no-go rather than reading it from the arc, so the test fails if the mathematics
is ever wrong. The load-bearing fact: Kodaira fibre monodromies are quasi-unipotent (|trace| <= 2)
and the object's monodromy is hyperbolic (trace 3), so no conjugacy is possible.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1343_deriving_the_other_faces"
M = lambda a, b, c, d: sp.Matrix([[a, b], [c, d]])

# Kodaira's classification, local monodromy representatives
KODAIRA = {"I_n": M(1, 1, 0, 1), "I_0*": M(-1, 0, 0, -1), "I_n*": M(-1, -1, 0, -1),
           "II": M(1, 1, -1, 0), "III": M(0, 1, -1, 0), "IV": M(0, 1, -1, -1),
           "IV*": M(-1, -1, 1, 0), "III*": M(0, -1, 1, 0), "II*": M(0, -1, 1, 1)}
L, R, P = M(1, 1, 0, 1), M(1, 0, 1, 1), M(0, 1, 1, 0)
MONO, HALF = L * R, L * P


def test_arc_is_banked():
    assert (ARC / "FINDINGS.md").exists()
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1343" and v["verdict"] == "PROVED"


def test_every_kodaira_monodromy_is_quasi_unipotent():
    for name, A in KODAIRA.items():
        assert A.det() == 1, f"{name}: a fibre monodromy lies in SL2(Z)"
        assert abs(A.trace()) <= 2, f"{name}: the monodromy theorem forbids |trace| > 2"


def test_ivstar_is_order_three_over_the_objects_own_field():
    """IV* is E6~, and its eigenvalue field is Q(zeta_3) = Q(sqrt-3) -- the object's 'being' face."""
    lam = sp.symbols("lam")
    A = KODAIRA["IV*"]
    assert sp.simplify(sp.expand(A.charpoly(lam).as_expr()) - (lam ** 2 + lam + 1)) == 0
    assert A ** 3 == sp.eye(2) and A != sp.eye(2), "IV* monodromy has order 3"


def test_the_objects_monodromy_is_hyperbolic_so_no_bridge():
    """trace and det are conjugacy invariants; trace 3 > 2 matches nothing in the classification."""
    assert MONO.trace() == 3 and MONO.det() == 1
    assert not [n for n, A in KODAIRA.items()
                if A.trace() == MONO.trace() and A.det() == MONO.det()], (
        "the object's monodromy must be conjugate to NO Kodaira fibre monodromy")


def test_no_iterate_escapes():
    """powers of a hyperbolic element stay hyperbolic -- the even Lucas numbers."""
    Pw, traces = sp.eye(2), []
    for _ in range(8):
        Pw = Pw * MONO
        traces.append(int(Pw.trace()))
    assert traces == [3, 7, 18, 47, 123, 322, 843, 2207], traces
    assert all(abs(t) > 2 for t in traces)


def test_the_near_miss_is_killed_on_determinant():
    """the half step's trace 1 coincides with II*, but det -1 vs +1 -- and II* is E8~, not E6~."""
    assert HALF.trace() == 1 and HALF.det() == -1
    assert KODAIRA["II*"].trace() == 1 and KODAIRA["II*"].det() == 1
    assert HALF.det() != KODAIRA["II*"].det(), "not conjugate; the coincidence is the trace alone"


def test_the_fence_is_written_down():
    """B727's point must survive: derivable is not evidence."""
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "derivable and cannot enrich" in t.lower()
    assert "no new physics" in t.lower() or "claims no new physics" in t.lower()
