"""B978 locks — Phase A: dispositions, the V5 mechanism, and the third-instance record."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B978_phaseA_bank"
VERDICT = ROOT / "docs" / "THE_SM_VERDICT.md"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_all_four_leads_closed():
    d = _res()["dispositions"]
    assert set(d) == {"L134", "L132", "L137", "L135"}
    assert "CLOSED" in d["L134"]["verdict"]
    assert "VACUOUS" in d["L132"]["verdict"]
    assert "REFUTED" in d["L137"]["verdict"]
    assert "DISCHARGED" in d["L135"]["verdict"]


def test_L132_independently_corroborates_B976():
    d = _res()["dispositions"]["L132"]
    assert "B864" in d["why"] and "B976" in d["why"]


def test_V5_was_verified_by_lattice_membership_not_accepted():
    v = _res()["V5_VERIFIED_HERE"]
    assert "LATTICE MEMBERSHIP" in v["how_verified"]
    assert "ORDER 3" in v["how_verified"]
    assert "NO ADJOINT VEV CAN GIVE ANY 27 FERMION A MASS" in v["consequence"]


def test_the_verdict_carries_the_scope_and_the_mechanism():
    assert contains(VERDICT, "the path", "not the landing site",
                    "18 of 27 states change side",
                    "no adjoint vev can give any 27 fermion a mass")


def test_the_third_instance_is_recorded_not_softened():
    r = _res()["THIRD_INSTANCE_OF_THE_SAME_FAILURE"]
    assert len(r["so_today_has_three"]) == 3
    assert "DECLARING ABSENT WHAT EXISTS" in r["reading"]
    assert "exhaustion, measured" in r["reading"]


def test_the_instrument_caveat_is_in_the_source():
    src = (ROOT / "frontier" / "B961_frame_instrument" / "frame.py").read_text(encoding="utf-8")
    assert "CONSISTENT WITH" in src and "not PROVED BY" in src
