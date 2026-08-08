"""B951 + B954 locks — the L132 scouting result and the both-branches answer."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCOUT = ROOT / "frontier" / "B951_l132_scout"
BR = ROOT / "frontier" / "B954_both_branches"


def _n(p):
    return " ".join(p.read_text(encoding="utf-8").split())


# ---------------------------------------------------------------- B951
def test_the_anomaly_check_is_flagged_as_probably_vacuous():
    t = _n(SCOUT / "FINDINGS.md")
    assert "CANNOT FAIL" in t
    assert "MB12" in t
    assert "establishing non-vacuity is the prerequisite" in t.lower()


def test_the_target_algebra_is_recorded_as_a_classified_Levi():
    t = _n(SCOUT / "FINDINGS.md")
    assert "A₂+A₁ Levi subalgebra of e₆" in t
    assert "Borel–de Siebenthal (1949)" in t
    assert "not a discovery" in t
    # and the arithmetic was re-derived here, not accepted
    assert "6 + 8 = **14**" in t


def test_the_centralizer_argument_does_not_transplant():
    t = _n(SCOUT / "FINDINGS.md")
    assert "1-dimensional" in t and "9-dimensional" in t
    assert "does not single out Y" in t


def test_the_nearest_prior_art_is_recorded():
    t = _n(SCOUT / "FINDINGS.md")
    assert "Todorov" in t and "JHEP 04 (2021) 164" in t
    assert "u(2) ⊕ u(3)" in t
    assert "occupied literature" in t


def test_the_null_is_explicitly_NOT_certified():
    t = _n(SCOUT / "FINDINGS.md")
    assert "MathSciNet NOT reached" in t
    assert "not found by this sweep" in t


# ---------------------------------------------------------------- B954
def _res():
    return json.loads((BR / "results.json").read_text(encoding="utf-8"))


def test_the_odd_part_is_not_an_algebra():
    r = _res()
    assert r["even_part_is_a_subalgebra"] is True
    assert r["odd_part_is_a_subalgebra"] is False
    assert r["can_restrict_to_odd_branch"] is False
    assert r["bracket_rules"]["[odd,odd]"] == "even"
    assert r["dim_check"] is True


def test_theta_is_a_rank_reducer_that_destroys_what_it_is_needed_for():
    r = _res()
    assert r["theta_is_itself_a_rank_reducer"]["from"] == 6
    assert r["theta_is_itself_a_rank_reducer"]["to"] == 4
    assert "kills chirality" in r["theta_is_itself_a_rank_reducer"]["cost"]
    assert r["therefore_chirality_requires_the_whole"] is True


def test_B954_corrects_B953_framing_without_refuting_it():
    t = _n(BR / "FINDINGS.md")
    assert "there is no second seed to switch to" in t
    assert "This refutes nothing" in t
    assert "SU(5) is exactly such a thing" in t
