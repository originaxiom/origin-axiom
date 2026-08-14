"""B958 locks — the presence side stays owed; one necessary condition met."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B958_presence_scope"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def _n(p):
    t = re.sub(r"(?m)^\s*>\s?", "", p.read_text(encoding="utf-8")).replace("*", "")
    return " ".join(t.split())


def test_the_colour_centralizer_was_computed_here():
    c = _res()["consistency_test_run"]
    assert c["dim_e6"] == 78 and c["stacked_ad_rank"] == 62
    assert c["dim_centralizer"] == 78 - 62 == 16
    assert c["passed"] is True


def test_the_test_is_labelled_necessary_not_sufficient():
    c = _res()["consistency_test_run"]
    assert "NOT a verification" in c["strength"]
    t = _n(CELL / "FINDINGS.md")
    assert "necessary, not sufficient" in t


def test_the_repo_lacks_an_independent_M12_construction():
    r = _res()
    assert r["repo_has_independent_M12_construction"] is False
    assert "not by rebuilding" in r["how_B909_verified_LVIII"]


def test_the_debt_is_recorded_as_still_owed():
    t = _n(CELL / "FINDINGS.md")
    assert "remains OWED" in t or "stays owed" in t.lower()
    assert "this arc does not either" in t
    assert "L135" in t


def test_the_deferral_reason_is_on_the_record():
    r = _res()
    assert "FALSE verification" in r["why_not_done_here"]
