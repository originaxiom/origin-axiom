"""Locks B851 -- the lit-gate B849 owed.

These are DISCIPLINE locks, not numeric ones. A lit-gate's failure mode is not a wrong number,
it is an unstated question, a one-directional search, or a conditional that silently disappears.
P5 died from the first of those.
"""
import re
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[1]
_F = (_ROOT / "frontier" / "B851_bc_litgate" / "FINDINGS.md").read_text(encoding="utf-8")
_B849 = (_ROOT / "frontier" / "B849_order_parameter" / "FINDINGS.md").read_text(encoding="utf-8")


def test_the_question_is_stated_before_the_answer():
    """The P5 failure was a gate that named the right person and asked the wrong question."""
    q = _F.index("## 1.")
    a = _F.index("## 2.")
    assert q < a, "the question section must precede the result section"
    seg = _F[q:a]
    assert "CONFIRMS the mismatch" in seg and "REFUTES the mismatch" in seg, (
        "both outcomes must be specified BEFORE the result")


def test_the_search_ran_in_both_directions():
    """A prior-art call that checks only the confirming half is half a check."""
    assert "Both directions were searched" in _F
    assert "Counter-evidence searched for and not found" in _F
    assert "zero times" in _F, "the measured absence must be stated, not assumed"


def test_the_load_bearing_quote_is_present_and_attributed():
    assert "free and transitive" in _F
    assert "Idele class group as group of symmetries" in _F
    assert "math/0501424" in _F, "the primary source must be identified"
    assert "maximal abelian quotient" in _F, "why Gal(K^ab/K) fixes K must be quoted, not asserted"


def test_the_conditional_relocates_rather_than_disappears():
    """The dangerous outcome of a confirming gate is a conditional quietly dropped."""
    assert "RELOCATES" in _F or "relocates" in _F
    assert "Is the programme's β=1 system actually a BC/CMR-type system" in _F
    assert "IN-REPO question" in _F or "in-repo" in _F.lower()


def _norm(t):
    """Lowercase AND normalise typographic apostrophes -- matching one but not the other is how
    a prose lock fails on text that says exactly what it should."""
    return t.lower().replace("\u2019", "'")


def test_the_gate_does_not_claim_a_refutation():
    f = _norm(_F)
    assert _norm("does not refute the reframe") in f
    assert _norm("does not show the programme's system is CMR's") in f


def test_no_third_party_source_text_was_vendored():
    """Quotes with line refs are fine; shipping someone else's paper into the repo is not."""
    d = _ROOT / "frontier" / "B851_bc_litgate"
    for p in d.iterdir():
        assert p.suffix in {".md", ".json"}, f"unexpected artifact in the arc: {p.name}"
        assert p.stat().st_size < 60_000, f"{p.name} is too large to be quotes-only"


# ---------------------------------------------------------------------------------------
# The mathematical content the gate turns on -- computed, so the prose cannot drift from it
# ---------------------------------------------------------------------------------------
def test_complex_conjugation_does_not_fix_the_trace_field():
    """Membership in Gal(K^ab/K) requires fixing K. This is why the mismatch exists."""
    s = sp.sqrt(-3)
    assert sp.simplify(sp.conjugate(s) - s) != 0
    assert sp.simplify(sp.conjugate(sp.conjugate(s)) - s) == 0, "conjugation has order 2"


def test_the_Q_case_DOES_contain_complex_conjugation():
    """The asymmetry that explains the error: for Q^ab, conjugation is -1 in Zhat*.

    Complex conjugation sends zeta_n -> zeta_n^{-1}, i.e. acts as -1 under the cyclotomic
    character. So it IS in Gal(Q^ab/Q) -- and is NOT in Gal(K^ab/K). Checked on roots of unity.
    """
    for n in (3, 4, 5, 7, 12):
        z = sp.exp(2 * sp.pi * sp.I / n)
        assert sp.simplify(sp.conjugate(z) - z**(n - 1)) == 0, n
    # and conjugation fixes Q itself, which is why it is a legitimate element of Gal(Q^ab/Q)
    assert sp.conjugate(sp.Rational(5, 7)) == sp.Rational(5, 7)


def test_b849_is_updated_to_point_at_this_gate():
    """A confirming gate that never reaches the arc it was owed to has not been paid."""
    assert "B851" in _B849, "B849 must record that its owed gate ran"
