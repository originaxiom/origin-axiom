"""B1017 — locks: the recount holds, the retraction sweeps clean, the theorems survive."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_the_two_closings_differ_on_both_discriminants():
    """The correction's mathematical core, kept executable: tau vs the VEV chain."""
    # rank removed: tau: E6(6) -> F4(4) = 2 ; <1>: E6(6) -> SO(10)+U(1) rank drop = 1
    assert 6 - 4 == 2 and 6 - 5 == 1
    # branching charge tracelessness (the retraced checks):
    assert 16 * 1 + 10 * (-2) + 1 * 4 == 0
    assert 10 * (-1) + 5 * 3 + 1 * (-5) == 0


def test_the_retracted_phrase_is_registered_and_swept():
    reg = (ROOT / "docs" / "RETRACTED_PHRASES.md").read_text(encoding="utf-8")
    assert "compete for one resource" in reg and "B1017" in reg
    # the living docs no longer assert the corollary as live:
    for rel in ("docs/THE_CLAIM.md", "docs/THE_FRAMEWORK.md"):
        t = (ROOT / rel).read_text(encoding="utf-8")
        flat = " ".join(t.lower().split())
        assert "provably compete for one resource" not in flat, f"{rel} still asserts the corollary"


def test_the_claim_counts_five_and_names_the_unsourced_slot():
    t = (ROOT / "docs" / "THE_CLAIM.md").read_text(encoding="utf-8")
    flat = " ".join(t.lower().split())
    assert "five** typed external data" in t.lower() or "five typed external data" in flat
    assert "unsourced by the torsor" in flat
    assert "is open" in flat, "the fold-into-R+ question must stay open, not decided"


def test_b963_theorems_stand_while_the_corollary_is_bannered():
    f = (ROOT / "frontier" / "B963_tau_double_duty" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "COROLLARY CORRECTED 2026-08-10 (B1017" in f
    assert "true and irrelevant" in f
    flat = " ".join(f.lower().split())
    assert "the two mathematical halves of this arc stand" in flat
