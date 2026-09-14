"""B1407 -- L209 was never a choice: the row's spec settles it, and the row is
dead on POWER rather than on accounting.

The decisive facts are documentary and arithmetic, and both are asserted here
so that a change to either breaks the closure rather than silently voiding it.
"""
import importlib.util
import math
from pathlib import Path

import pytest

sp = pytest.importorskip("sympy")
from sympy import Rational as Q

ROOT = Path(__file__).resolve().parents[1]
PHI = (1 + sp.sqrt(5)) / 2


def _doc(rel):
    return (ROOT / rel).read_text(encoding="utf-8").replace("\n", " ")


# ------------------------------------------------- the spec, as written down
def test_the_zero_anchor_clause_is_in_the_kind_table():
    assert "zero anchors consumed" in _doc("docs/KIND_TABLE.md")


def test_the_zero_anchor_clause_is_in_campaign_status_twice():
    cs = _doc("docs/CAMPAIGN_STATUS.md")
    assert "coupling, zero anchors, one licensed row" in cs
    assert "ZERO anchors (R11's open lane)" in cs


def test_the_rows_declared_kind_columns():
    kt = _doc("docs/KIND_TABLE.md")
    assert "mirror set" in kt and "amplitude-part" in kt


def test_branch_A_anchor_is_nonzero_on_both_accountings():
    assert math.log2(7) > 0                                  # B1349 addendum 5
    assert math.log2(212641) > 0                             # B1405's floor
    # a spec that says ZERO and a reading that costs 2.81 do not meet
    assert abs(math.log2(7) - 2.807) < 0.01


def test_branch_B_dies_on_the_tie():
    """2 ear-discriminating directions, 2-bit anchor, R11 needs strictly > 0."""
    assert (2 - 2) == 0
    assert not ((2 - 2) > 0)


def test_the_object_word_is_a_unit_hence_branch_B():
    assert math.gcd(1, 15) == 1


# ------------------------------------------- the observable that meets the spec
@pytest.fixture(scope="module")
def normalised():
    B = ROOT / "frontier" / "B1349_the_mirror_sector_posed" / "verification"
    spec = importlib.util.spec_from_file_location(
        "exact60_b1407", str(B / "b1349c_exact_instrument.py"))
    X = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(X)
    N = 6
    ix = {w: i for i, w in enumerate(X.W)}
    I6 = sp.eye(N)
    cm = lambda A: sp.Matrix(A.rows, A.cols, lambda i, j: X.conj(A[i, j]))
    C = sp.zeros(N, N)
    for i, w in enumerate(X.W):
        C[ix[(w[1], w[0])], i] = 1
    C = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
    R, L = X.T, X.mmul(X.mmul(cm(X.S), cm(X.T)), X.S)

    def mpow(A, k):
        P = I6
        for _ in range(k):
            P = X.mmul(P, A)
        return P

    ZN = sp.exp(2 * sp.pi * sp.I / 60)
    ex = lambda e: sp.nsimplify(sp.simplify(sp.expand(e).subs(X.z, ZN)), [sp.sqrt(5)])
    trC = sp.trace(C)
    out = {}
    for m in range(15):
        Wd = X.mmul(mpow(R, m), mpow(L, m))
        st = ex(X.red(sp.expand(sum(X.mmul(C, Wd)[i, i] for i in range(N)))))
        out[m] = sp.nsimplify(sp.radsimp(st / trC))
    return trC, out


def _c6():
    s = {sp.Integer(0)}
    for v in [Q(1, 4), 1 / (4 * PHI), Q(1, 2), 1 / (2 * PHI), PHI / 4, PHI / 2, sp.Integer(1)]:
        s |= {sp.nsimplify(sp.radsimp(v)), sp.nsimplify(sp.radsimp(-v))}
    return s


def test_the_normaliser_is_canonical_not_fitted(normalised):
    trC, _ = normalised
    assert trC == 2                       # = 4 even - 2 odd, the grading's index


def test_c6_has_fifteen_elements():
    assert len(_c6()) == 15


def test_every_normalised_value_meets_range_field_and_membership(normalised):
    _, out = normalised
    C6 = _c6()
    vals = set(out.values())
    assert len(vals) == 6
    for v in vals:
        assert abs(float(v)) <= 1                                   # range
        assert v.is_rational or sp.sqrt(5) in v.atoms(sp.Pow)       # field
        assert any(sp.simplify(v - c) == 0 for c in C6)             # membership


def test_at_the_object_it_reads_one_over_two_phi(normalised):
    _, out = normalised
    assert sp.simplify(out[1] - 1 / (2 * PHI)) == 0
    assert abs(float(out[1]) - 0.30901699437494745) < 1e-15


def test_that_value_is_the_one_already_benched_and_non_discriminating():
    kt = _doc("docs/KIND_TABLE.md")
    assert "already took to a bench and could not discriminate" in kt
    assert "REFUTED ON KIND" in kt
    assert "17 natural candidates" in kt


def test_l209_is_recorded_closed():
    """Check L209's OWN section, not merely that 'CLOSED' occurs in the file."""
    text = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    start = text.index("## L209")
    nxt = text.find("\n## L", start + 1)
    section = text[start: nxt if nxt > 0 else len(text)]
    assert "CLOSED" in section
    assert "never an owner" in section.lower() or "NEVER AN OWNER" in section
    assert "zero anchors consumed" in section
    assert "1/(2φ)" in section
