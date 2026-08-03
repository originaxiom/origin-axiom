"""Locks B873 -- gate P5: menu completeness, with citation-free winner-safety."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B873_p5_gate"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_p5_gated():
    assert RES["p5_gated"] is True
    assert RES["undisposed_total"] == 0


def test_every_above_winner_match_is_disposed_by_a_computed_kill():
    for g in ("E6", "D5", "A4"):
        for row in RES["impostors"][g]["rows"]:
            assert not row["disposal"].startswith("UNKILLED"), row
            if row["dim"] > RES["impostors"][g]["winner_dim"]:
                assert row["disposal"].startswith("KILL") or \
                       row["disposal"] == "IN-MENU", row


def test_the_derived_fit_kill_closes_the_scratch_gaps():
    """The three impostors the full-rank bound alone misses."""
    labs = {r["label"]: r["disposal"] for g in ("D5", "A4")
            for r in RES["impostors"][g]["rows"]}
    for lab in ("A1_1+A4_1", "A2_1+A2_1", "A1_1+A1_1+A2_1"):
        assert "derived-fit" in labs[lab], (lab, labs[lab])


def test_no_winner_dim_ties_survive():
    for g in ("E6", "D5", "A4"):
        assert RES["impostors"][g]["winner_ties_outside_menu"] == 0


def test_winners_unchanged_and_unique():
    w = {k: (v["winner"], v["winner_dim"], v["unique"])
         for k, v in RES["steps"].items()}
    assert w["step1 (E6)_1"] == ("SO(10)xU(1)", 46, True)
    assert w["step2 SO(10)_1"] == ("SU(5)xU(1)", 25, True)
    assert w["step3 SU(5)_1"] == ("SM", 12, True)


def test_a1_cap_is_theorem_backed():
    assert RES["a1_cap_justification"] == {"E6": 156, "D5": 60, "A4": 20}


def test_t_arithmetic_cross_checks_pass():
    assert RES["t_checks"] and all(ok for _, ok in RES["t_checks"])


def test_registerability_kills_and_the_one_survivor():
    assert all(RES["registerability"].values())
    assert RES["a2g2_registerable_but_small"] is True


def test_findings_state_the_citation_status_and_provenance():
    assert "winner-safety needs no citation" in _F
    assert "zero load-bearing imports" in _F
    assert "hardened here" in _F
