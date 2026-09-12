"""B1346 - the chat1 handoff intake: the metallic generalisation and the refuted nesting.

Arithmetic-only locks (no SnapPy) so they run everywhere; the geometric checks live in the arc's
verification scripts.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1346_the_chat1_handoff_intake"
x = sp.symbols("x")
L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]]); S = sp.Matrix([[0, 1], [1, 0]])


def test_arc_is_banked():
    assert (ARC / "FINDINGS.md").exists()
    assert json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["id"] == "B1346"


def test_the_tick_is_twist_times_swap():
    M = S * R
    assert M == sp.Matrix([[1, 1], [1, 0]]) and M.det() == -1
    assert sp.expand(M.charpoly(x).as_expr()) == x ** 2 - x - 1
    assert S * R * S == L and S * L * S == R, "the swap exchanges the two shears"


def test_the_double_tick_is_a_word_times_its_own_mirror():
    """M^2 = X . swap(X) for every det -1 element M = X.S -- so amphichirality is by construction."""
    import itertools
    n = 0
    for a, b, c, d in itertools.product(range(-2, 3), repeat=4):
        X = sp.Matrix([[a, b], [c, d]])
        if X.det() != 1:
            continue
        n += 1
        assert sp.simplify((X * S) ** 2 - X * (S * X * S)) == sp.zeros(2, 2)
    assert n > 20, f"the check must range over real content, got {n} matrices"


def test_every_metallic_unit_has_norm_minus_one():
    """THE GENERALISATION: norm -1 <=> det -1 <=> the swap, for the WHOLE family, not just phi."""
    for m in range(1, 9):
        roots = list(sp.roots(x ** 2 - m * x - 1, x).keys())
        assert sp.simplify(sp.prod(roots) + 1) == 0, f"lambda_{m} must have norm -1"
        assert sp.Matrix([[m, 1], [1, 0]]).det() == -1
    # the escape is outside the family, and that is why it escapes
    assert sp.simplify(sp.prod(list(sp.roots(x ** 2 - 4 * x + 1, x).keys())) - 1) == 0
    assert all(sp.expand(x ** 2 - 4 * x + 1 - (x ** 2 - m * x - 1)) != 0 for m in range(1, 20)), (
        "2+sqrt3 solves x^2-4x+1, which is NOT of the metallic form x^2 - m x - 1")


def test_the_nesting_refutation_is_recorded_with_its_reason():
    """Chat-2's 3a: volume matched, manifold differs. The cusp count settles it without SnapPy."""
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "REFUTED" in t and "m129" in t and "Whitehead" in t
    assert "two cusps" in t and "one cusp" in t, (
        "the decisive reason is the cusp count, not the isometry call")


def test_b1330s_protection_clause_is_recorded():
    t = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "v2873" in t and "PROTECTED" in t
    assert "952" in t, "B1330's headline number must be named where the clause attaches"
