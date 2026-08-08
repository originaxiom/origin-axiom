"""B961 locks — the frame instrument reproduces banked numbers from scratch."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B961_frame_instrument"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_killing_form_is_exact_and_nondegenerate():
    r = _res()
    assert r["killing_symmetric"] is True
    assert r["killing_rank"] == 78
    assert r["killing_nondegenerate"] is True


def test_it_reproduces_B958s_colour_centralizer():
    r = _res()
    assert r["dim_Z_su3_colour"] == 16 and r["matches_B958"] is True


def test_it_reproduces_B892s_three_numbers_from_scratch():
    """dim 14, derived 11, centre 3 -- the first independent derivation here."""
    r = _res()
    assert r["levi_dim"] == 14
    assert r["levi_derived_dim"] == 11
    assert r["levi_centre_dim"] == 3
    assert r["matches_B892_numbers"] is True


def test_the_killing_perp_complements():
    r = _res()
    assert r["dim_killing_perp_of_cartan"] == 72
    assert r["perp_complements_cartan"] is True


def test_the_rref_trap_is_documented_in_the_source():
    """The bug the self-test caught must stay documented so it cannot recur."""
    src = (CELL / "frame.py").read_text(encoding="utf-8")
    assert "PIVOT COLUMNS, not row indices" in src
    assert "rowspace()" in src


def test_the_presence_side_is_still_recorded_as_owed():
    assert contains(CELL / "FINDINGS.md",
                    "still not verified",
                    "does not supply solo's frame definitions",
                    "this is an instrument, not a result")
