"""B957 locks — L124 closed negative, and the two clauses rhyme."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B957_l124_torsor"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def _n(p):
    txt = p.read_text(encoding="utf-8")
    txt = re.sub(r"(?m)^\s*>\s?", "", txt).replace("*", "")
    return " ".join(txt.split())


def test_every_B700_torsor_has_group_Z2():
    r = _res()
    assert r["every_B700_torsor_has_group_Z2"] is True
    for t in r["B700_torsors"]:
        assert t["order"] == 2 and t["field_degree"] == 2


def test_the_CMR_group_is_infinite_so_they_cannot_match():
    r = _res()
    assert r["CMR_torsor"]["finite"] is False
    assert r["orders_match"] is False and r["fields_match"] is False
    assert r["verdict"].startswith("NO")


def test_the_fields_are_mutually_blind_computed_not_cited():
    r = _res()
    assert r["five_inert_in_Q_sqrt_minus3"] is True
    assert r["three_inert_in_Q_sqrt5"] is True
    assert r["fields_are_mutually_blind"] is True


def test_both_clauses_land_on_Z2():
    """The convergence: B723 was one level too high in BOTH clauses."""
    r = _res()
    assert r["B942_relocated_chirality_to"]["order"] == 2
    assert r["both_clauses_land_on_Z2"] is True
    assert r["B723_was_one_level_too_high_in_BOTH_clauses"] is True


def test_the_unsealed_status_is_declared_not_hidden():
    t = _n(CELL / "FINDINGS.md")
    assert "no preregistration, deliberately" in t.lower()
    assert "open-and-shut reading" in t.lower()


def test_it_refutes_an_identification_not_B700():
    t = _n(CELL / "FINDINGS.md")
    assert "B700 stands entirely" in t
    assert "not rehabilitated" in t
