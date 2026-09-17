"""xB010 — the lock on THE RE-DERIVATION RULE.

The rule: a banked result is a HYPOTHESIS, not an answer. These assert the MATHEMATICS OF
THE INSTRUMENT — that silence is impossible, that an honest refusal is cheap, that citing
is not re-deriving, and that the rule binds its own author.
"""
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
_s = importlib.util.spec_from_file_location("_rd", ROOT / "scripts" / "checks" / "rederivation.py")
RD = importlib.util.module_from_spec(_s)
_s.loader.exec_module(RD)


def test_selftest_both_directions():
    assert RD.selftest_quiet() == []


def test_silence_is_impossible():
    """the whole point: an arc that declares nothing must be caught."""
    problems, bound = RD.check()
    assert not problems, problems
    assert bound, "no arc is bound -- the rule binds nothing and is decorative"


def test_an_honest_refusal_is_cheap():
    """a rule that forbade 'I did not re-run this' would produce FALSE DECLARATIONS, not
    re-derivation (the B1222 shape, turned on ourselves)."""
    assert RD.validate({"arc": "B9", "outcome": "NOT_RERUN", "why": "needs Sage"}) is None


def test_a_bare_refusal_is_not():
    assert RD.validate({"arc": "B9", "outcome": "NOT_RERUN"}) is not None


def test_citing_is_not_rederiving():
    """CONFIRMED with nothing recomputed is a citation wearing a re-derivation's label."""
    assert RD.validate({"arc": "B425", "outcome": "CONFIRMED"}) is not None
    assert RD.validate({"arc": "B425", "outcome": "CONFIRMED",
                        "what": "recomputed the adjoint torsion, got -3"}) is None


def test_the_outcome_vocabulary_is_closed():
    assert RD.validate({"arc": "B425", "outcome": "LOOKED_AT_IT"}) is not None
    for o in ("CONFIRMED", "CORRECTED", "SCOPED"):
        assert RD.validate({"arc": "B425", "outcome": o, "what": "x"}) is None


def test_the_rule_binds_its_own_author():
    """a NUMERIC cutoff could never bind this seat: 'xB009' parses to 9. The roster binds by
    identity, so the arc that wrote the rule is subject to it."""
    ros = json.loads((ROOT / "docs" / "REDERIVATION_ROSTER.json").read_text(encoding="utf-8"))
    assert "xB010_the_rederivation_rule" not in ros["exempt"]
    d = json.loads((ROOT / "frontier" / "xB010_the_rederivation_rule" /
                    "arc_verdict.json").read_text(encoding="utf-8"))
    assert d.get("rederived"), "the rule's own arc declares nothing"
    assert any(e["arc"].startswith("B742") for e in d["rederived"]), \
        "xB010 argues from B742's numbers; it must declare re-deriving them"


def test_the_rule_is_written_where_rules_live():
    for f in ("WORKING_RULES.md", "docs/PRACTICES.md"):
        t = (ROOT / f).read_text(encoding="utf-8")
        assert "THE RE-DERIVATION RULE" in t
        assert "CITE" in t and "RE-DERIVE" in t
