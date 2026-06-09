"""B139 -- firewall cartography. Item 1's load-bearing check (mirror trace-equality) + the SnapPy CS-flip control.

The trace-level facts run unconditionally (pure sympy); the CS-flip / volume / homology control is SnapPy-gated.
"""
import pytest

from frontier.B139_firewall_cartography.probe import (
    CHIRAL_WORDS,
    cs_flip_live,
    mirror_trace_equality,
    mirror_word,
    monodromy,
)


def test_mirror_is_transpose_and_traces_equal():
    """The geometric mirror sends M -> M^T, so the trace (hence char poly, Perron field) is invariant."""
    r = mirror_trace_equality()
    assert r["all_traces_equal"] is True
    assert r["all_mirror_is_transpose"] is True
    for row in r["rows"]:
        assert row["tr"] == row["tr_mirror"]
        assert row["mirror_is_transpose"] is True


def test_mirror_word_involution():
    """swap_{R<->L} o reverse is an involution; and L = R^T makes the monodromy mirror a transpose."""
    for w in CHIRAL_WORDS:
        assert mirror_word(mirror_word(w)) == w
        assert monodromy(mirror_word(w)) == monodromy(w).T


def test_trace_equality_holds_for_achiral_words_too():
    """The trace equality is UNIVERSAL (achiral words too) -- which is exactly why chirality is invisible here."""
    achiral = ["RL", "RRLL", "RLRRLL", "RRRLLL"]
    r = mirror_trace_equality(achiral)
    assert r["all_traces_equal"] is True
    assert r["all_mirror_is_transpose"] is True


def test_cs_flips_sign_snappy():
    """SnapPy control: volume mirror-invariant, CS flips sign, H1 mirror-invariant (the standard invariants all symmetrize)."""
    res = cs_flip_live()
    if res is None:
        pytest.skip("SnapPy not available")
    assert res["all_vol_invariant_cs_flips_homology_invariant"] is True
