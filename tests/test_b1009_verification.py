"""B1009 — locks for the post-model-switch verification pass.

The load-bearing lock is test_the_endpoint_overreach_stays_withdrawn. A synthesis claim that
reached FIVE reader-facing documents is the hardest kind to retract, because it gets re-read as
settled by every later seat. This asserts the withdrawal survives.
"""
from __future__ import annotations

import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
VIEWS = ["ROADMAP.md", "docs/MASTERPLAN.md", "docs/OPEN_PROBLEMS.md",
         "docs/PRICED_DOORS.md", "README.md"]


def test_the_endpoint_overreach_stays_withdrawn():
    """The claim 'matching the SM could never have confirmed the axioms' is withdrawn everywhere.

    B996/B993 establish genericity at the E6 WAYPOINT. Neither computes the downstream cascade
    for a non-golden grammar, so the SM-match's discriminating power is UNCOMPUTED, not zero.
    """
    for rel in VIEWS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "could never have confirmed the axioms — even if it had\n> worked.**" not in text, (
            f"{rel} still asserts the withdrawn endpoint claim as live (B1009)")
        assert "CORRECTED 2026-08-10 by the verification seat" in text, (
            f"{rel} lost B1009's withdrawal note")


def test_no_arc_runs_the_cascade_on_a_non_golden_grammar():
    """The measured absence L149 rests on — so the lead closes only when the work is done.

    If this ever fails, someone RAN the test: L149 must then be closed with that arc cited, and
    the withdrawn sentence re-adjudicated on its result.
    """
    hits = []
    for f in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")):
        try:
            c = json.loads(pathlib.Path(f).read_text(encoding="utf-8")).get("claim_one_line", "")
        except (OSError, ValueError):
            continue
        low = c.lower()
        if re.search(r"silver|bronze|m *= *2", low) and re.search(
                r"cascade.*(z6|z_6|hypercharge|generation)|"
                r"(z6|z_6|hypercharge|generation).*cascade", low):
            hits.append(c[:80])
    assert not hits, (
        f"an arc may now run the cascade on a non-golden grammar: {hits} -- close L149 and "
        "re-adjudicate B1009's withdrawn sentence against it")


def test_theta_qcd_is_not_claimed_as_delivered():
    """cc3's 'theta_QCD = 0, parameter-free' was REFUSED, not merged (B1009).

    The repo says the opposite twice, and the likely mechanism is the named recurring conflation
    between the object's theta (a reversal/contragredient involution on the character variety)
    and theta_QCD (the QCD vacuum angle) -- already B780 retracted and cc3's own B784 refuted.
    """
    verdict = (ROOT / "docs" / "THE_SM_VERDICT.md").read_text(encoding="utf-8")
    assert "strong CP" in verdict and "never addressed" in verdict, (
        "THE_SM_VERDICT no longer records strong CP as never addressed -- if it was DERIVED, "
        "that needs a banked arc, and B1009's refusal must be revisited explicitly")
    for f in glob.glob(str(ROOT / "frontier" / "*" / "arc_verdict.json")):
        try:
            c = json.loads(pathlib.Path(f).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if c["id"] == "B1009":
            continue
        assert not re.search(r"theta_?QCD *= *0.*parameter.free", c.get("claim_one_line", ""), re.I), (
            f"{c['id']} claims theta_QCD = 0 parameter-free; B1009 refused this pending a banked "
            "derivation that does not rest on the theta conflation")


def test_the_owner_standing_rule_is_repo_resident():
    """B1009's handoff finding: it lived only in machine-local agent memory.

    A fresh clone on another bench would not have had it, which is exactly the loss mode the
    programme already paid for once (B999: branch protection preserves FILES, not FINDINGS).
    """
    rules = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    assert "STANDING EPISTEMIC RULE" in rules
    assert "HYPOTHESIS REQUIRING A SEARCH" in rules, (
        "the rule's operative clause must stay stated, not merely referenced")
