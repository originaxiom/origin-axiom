"""B151 -- firewall confirmation (L15). Locks the unit's anchor (figure-eight complex volume; CS=0) AND the *honesty
structure* of the reading (every source row tagged, cited, with what_carries_units; no CROSSING without exhibited primary
text). It does NOT (and cannot) unit-test the papers' unit-assignment claims themselves -- those are cited prose, the
honest boundary of a reading task; the discipline this test enforces is that no scale-crossing is asserted without an
exhibited primary-text location."""
import pytest

from frontier.B151_firewall_confirmation.probe import (
    CS_FIG8,
    FIREWALL_READING,
    TAGS,
    VOL_FIG8,
    figure_eight_complex_volume,
    verdict,
)


def test_anchor_recorded_values():
    """The unit's recorded anchor: Vol = 2*V_tet (minimal cusped volume), CS = 0 (amphichiral)."""
    assert abs(VOL_FIG8 - 2.0298832128) < 1e-9
    assert CS_FIG8 == 0.0


def test_anchor_live_recompute_if_snappy():
    """When SnapPy is present, the live figure-eight complex volume matches the anchor (Vol=2.02988, CS=0)."""
    pytest.importorskip("snappy")
    vol, cs, live = figure_eight_complex_volume()
    assert live is True
    assert abs(vol - 2.0298832128) < 1e-7
    assert abs(cs) < 1e-9                     # CS = 0 (amphichiral) -- the pre-strengthening


def test_reading_rows_well_formed_and_cited():
    """Every reading row has a tag in {FIREWALL_HOLDS,CROSSING}, a primary-source citation, and a what_carries_units."""
    for r in FIREWALL_READING:
        assert r["tag"] in TAGS, r
        assert "arXiv" in r["source"], r["source"]
        assert r["what_carries_units"].strip(), r["source"]


def test_no_crossing_without_exhibited_text():
    """The binding discipline: a CROSSING tag must exhibit the exact primary-text location where a dimensionful quantity
    attaches to the invariant. No row may claim a crossing without it."""
    for r in FIREWALL_READING:
        if r["tag"] == "CROSSING":
            assert r["exhibited_text"].strip(), r["source"]


def test_verdict_is_firewall_holds():
    """All three sources locate the units in hbar/k + squashing, none in the invariant -> firewall holds (the honest
    boundary; a real result, not a crossing)."""
    assert all(r["tag"] == "FIREWALL_HOLDS" for r in FIREWALL_READING)
    v = verdict()
    assert v["verdict"] == "FIREWALL_HOLDS"
    assert "does not cross" in v["boundary"]
