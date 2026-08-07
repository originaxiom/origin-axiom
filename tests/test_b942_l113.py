"""B942 locks — L113, the BC/CMR falsifier.

Seal integrity first, per the preregistration. The remaining locks (one per
cell, plus the kill-condition-execution lock) are added when the cells run;
until then this file holds the seal, which is the part that must be
untamperable while the computation is still ahead of us.
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B942_l113_bc_falsifier"
SEAL_SHA = "48cd1ea291277f8c85637a9c817a554edc7bc4370bf7ec893bec223428ebc5a2"


def test_seal_integrity_prereg_hash_unchanged():
    got = hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert got == SEAL_SHA


def test_seal_integrity_ledger_row_matches():
    ledger = (ROOT / "docs" / "SEAL_LEDGER.md").read_text(encoding="utf-8")
    rows = [r for r in ledger.splitlines() if "B942" in r and SEAL_SHA in r]
    assert len(rows) == 1


def test_the_kill_condition_is_quoted_in_the_seal():
    """The prereg must carry the locked kill condition verbatim, so the seat
    cannot soften it on contact with the answer."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "L113 YES" in txt
    assert "the observer construction's foundation fails" in txt


def test_the_criterion_forbids_a_third_outcome():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "There is no third outcome" in txt
    assert "does **not** default to the programme's favour" in txt


def test_the_prior_was_disclosed_against_the_programme():
    """The disclosed prior must be the inconvenient one, stated before compute."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*OUTCOME YES, high\.\*\*", txt)
    assert m, "the prior must be disclosed as OUTCOME YES"
    assert "executes a kill condition against the programme's own construction" in txt
