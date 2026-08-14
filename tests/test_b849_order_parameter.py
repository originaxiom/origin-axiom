"""Locks B849 -- the order-parameter test for the claimed beta=1 SSB.

The locks that matter here are the ones that keep the arc HONEST rather than the ones that
record its numbers: the positive control (without it the object's zero means nothing), and the
sealed form of the Cell 3 lemma (zero OR half-period), which the arc's first implementation got
narrower than its own preregistration.
"""
import importlib.util
import math
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b849", _ROOT / "frontier" / "B849_order_parameter" / "order_parameter.py")
b9 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(b9)

HALF = math.pi ** 2 / 2


@pytest.fixture(scope="module")
def rows():
    return b9.cell1_and_2()


@pytest.fixture(scope="module")
def c3(rows):
    return b9.cell3(rows)


# ---------------------------------------------------------------------------------------
# The positive control -- the clause that makes the object's zero interpretable
# ---------------------------------------------------------------------------------------
def test_positive_control_passes(c3):
    """Without a chiral member returning CS != 0, the arc is INSTRUMENT VOID by its own seal."""
    assert c3["positive_control_passes"], "instrument returns zero for everything: nothing measured"
    assert len(c3["chiral_with_nonzero_CS"]) >= 5


def test_the_instrument_can_report_a_free_CS_class(c3):
    """It must be able to land OUTSIDE {0, pi^2/2}, else '2-torsion' is unfalsifiable."""
    assert c3["chiral_with_FREE_CS"], "no manifold with free CS: the 2-torsion test cannot fail"


# ---------------------------------------------------------------------------------------
# Cell 3: the lemma AS SEALED, not as first coded
# ---------------------------------------------------------------------------------------
def test_cell3_lemma_holds_in_its_sealed_form(c3):
    """Amphichiral => CS is 2-torsion, i.e. 0 OR the half-period pi^2/2."""
    assert c3["amphichiral_all_two_torsion"], c3["amphichiral_violations"]
    assert c3["amphichiral_violations"] == []
    assert c3["n_amphichiral"] >= 5


def test_the_narrower_test_would_have_failed(c3):
    """Locks the defect itself: 'all CS == 0' is FALSE, and it is what the code first checked.

    This test exists so the correction cannot be quietly lost. If someone later 'simplifies'
    the check back to CS == 0, this fails and says why.
    """
    assert not c3["amphichiral_all_zero"], (
        "m003 sits at pi^2/2, so the narrow test is false -- that is the whole point")


def test_m003_is_at_the_half_period_not_at_zero(rows):
    m003 = next(r for r in rows if r["name"] == "m003")
    assert m003["amphichiral"] is True
    assert abs(m003["CS"] - HALF) < 1e-8, "the lemma's OTHER permitted value, not a violation"
    assert m003["CS_class"].startswith("pi^2/2")


# ---------------------------------------------------------------------------------------
# Cell 2: the object, and the sister separation
# ---------------------------------------------------------------------------------------
def test_the_object_has_CS_zero_and_is_amphichiral(rows):
    m004 = next(r for r in rows if r["name"] == "m004")
    assert m004["amphichiral"] is True, "the Z/2 must EXIST -- it is SSB's precondition"
    assert abs(m004["CS"]) < 1e-9
    assert m004["CS_class"] == "0"


def test_object_and_sister_share_volume_but_differ_in_CS_class(rows):
    """A discriminating invariant separating m004 from m003. Flagged, not claimed as new."""
    m004 = next(r for r in rows if r["name"] == "m004")
    m003 = next(r for r in rows if r["name"] == "m003")
    assert abs(m004["volume"] - m003["volume"]) < 1e-6, "same volume"
    assert m004["amphichiral"] == m003["amphichiral"] is True, "both amphichiral"
    assert m004["CS_class"] != m003["CS_class"], "yet different 2-torsion CS class"


def test_the_two_routes_to_the_figure_eight_agree(rows):
    """m004 and 4_1 are the same manifold reached differently; disagreement would void the panel."""
    a = next(r for r in rows if r["name"] == "m004")
    b = next(r for r in rows if r["name"] == "4_1")
    assert abs(a["volume"] - b["volume"]) < 1e-9
    assert a["CS_class"] == b["CS_class"]


# ---------------------------------------------------------------------------------------
# Cell 4: the level test, and the honesty of its conditional
# ---------------------------------------------------------------------------------------
def test_complex_conjugation_is_in_Gal_K_over_Q_and_not_Gal_Kab_over_K():
    c4 = b9.cell4()
    assert c4["complex_conjugation_fixes_K"] is False, "conj sends sqrt(-3) -> -sqrt(-3)"
    assert c4["complex_conjugation_has_order_2"] is True
    assert c4["conjugation_in_Gal_K_over_Q"] is True
    assert c4["conjugation_in_Gal_Kab_over_K"] is False


def test_the_acting_group_step_is_declared_a_citation_not_a_computation():
    """The load-bearing half of Cell 4 must stay labelled. P5 died from an unrun gate."""
    c4 = b9.cell4()
    assert c4["CITED_acting_group_is_Gal_Kab_over_K"] is None, "must NOT be asserted as computed"
    assert "NOT VERIFIED" in c4["citation_status"]
    assert "CONDITIONAL" in c4["citation_status"]


def test_the_findings_do_not_claim_a_refutation():
    """The seal forbids reporting Cells 1-3 as a refutation; lock the prose to it."""
    txt = (_ROOT / "frontier" / "B849_order_parameter" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "is **not** refuted" in txt or "not refuted" in txt.lower()
    assert "CONDITIONAL" in txt
    assert "positive control" in txt.lower()


def test_the_prereg_is_sealed_and_its_hash_is_recorded():
    import hashlib
    p = _ROOT / "frontier" / "B849_order_parameter" / "PREREGISTRATION.md"
    h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    ledger = (_ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    assert h in ledger, f"prereg hash {h} not in the seal ledger -- the seal is void"
