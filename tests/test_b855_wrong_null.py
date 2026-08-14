"""Locks B855 -- the wrong-null audit.

The point of these locks is that a genericity verdict is only as good as its null, and this repo's
nulls were family members. They also lock the bug this arc nearly shipped: volumes must be COMPUTED,
never keyed on the field, or every row lands at index 12 by construction and the audit is vacuous.
"""
import json
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B855_wrong_null_audit"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = (_D / "FINDINGS.md").read_text(encoding="utf-8")
_SRC = (_D / "wrong_null.py").read_text(encoding="utf-8")

mp.mp.dps = 30
BY = {r["name"]: r for r in RES["panel"]}


def test_humbert_covolumes_are_right():
    """If these are wrong every index below is wrong."""
    assert abs(mp.mpf(RES["covolumes"]["-3"]) - mp.mpf("0.169156934401608938")) < mp.mpf("1e-15")
    assert abs(mp.mpf(RES["covolumes"]["-4"]) - mp.mpf("0.305321864725739672")) < mp.mpf("1e-15")


def test_the_family_has_two_rows_both_at_index_12():
    for n in ("m004", "m003"):
        assert BY[n]["field_disc"] == -3 and BY[n]["index_is_12"], n
    for n in ("m136", "m135"):
        assert BY[n]["field_disc"] == -4 and BY[n]["index_is_12"], n


def test_the_proposed_null_m129_is_the_SILVERS_classmate():
    """THE CATCH. cc proposed m129 as a non-commensurable null; it is index 12 in PSL(2,O_-1),
    the same class as m136, the family's second row."""
    assert BY["m129"]["field_disc"] == -4
    assert BY["m129"]["index_is_12"] is True
    assert BY["m129"]["volume"] == BY["m136"]["volume"], "same covolume class as the silver"


def test_m206_is_index_24_not_12():
    """The bug check with teeth: if volumes were keyed on the field, m206 would read 12."""
    idx = mp.mpf(BY["m206"]["index"])
    assert abs(idx - 24) < mp.mpf("1e-9"), f"m206 index {idx}"
    assert BY["m206"]["index_is_12"] is False


def test_the_volume_is_computed_not_keyed_on_the_field():
    """Locks the fix. The first version hardcoded a class volume per field, which would have
    forced every row to index 12 BY CONSTRUCTION and made the audit vacuous."""
    assert "USE THE COMPUTED VOLUME" in _SRC
    assert "vacuous" in _SRC, "the reason must stay documented where the fix lives"
    assert '2.029883212819307250042405108549' not in _SRC, "no hardcoded class volume"


def test_m003_is_amphichiral():
    """B296 calls it a 'non-amphichiral control' in the verdict line that turns on that axis."""
    assert RES["amphichiral"]["m003"] is True
    assert RES["amphichiral"]["m004"] is True


def test_the_candidate_nulls_are_not_amphichiral_and_differ_in_field():
    """A null for an orientation-odd verdict must be matched on amphichirality, or it confounds."""
    assert RES["amphichiral"]["m015"] is False
    assert RES["amphichiral"]["m009"] is False


def test_reid_forbids_any_knot_complement_commensurable_with_4_1():
    r = RES["reid"]
    assert "unique arithmetic knot complement" in r
    assert "NOT commensurable" in r


def test_the_repo_has_no_null_valid_for_both_rows():
    assert RES["family_rows"] == 2
    assert RES["repo_has_null_noncommensurable_with_both_rows"] is False


# ---------------------------------------------------------------------------------------
# Honesty locks
# ---------------------------------------------------------------------------------------
def test_the_arc_records_ccs_own_error():
    assert "and was wrong" in _F or "was wrong" in _F
    assert "the null I proposed" in _F


def test_unverified_items_are_marked_as_such():
    """The scan's three further claims must not be readable as computed in this arc."""
    assert "NOT verified here" in _F
    assert "reportedly" in _F


def test_the_arc_does_not_invert_the_direction_to_be_agreeable():
    """These corrections deflate. Saying so is the point."""
    assert "mostly deflate" in _F
    assert "not inverted here to be agreeable" in _F
