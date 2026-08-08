"""B959 locks — L133's decisive cell. Seal integrity first."""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B959_nontoral_rank4"
SEAL_SHA = "6c5d76e695ff7958ab3e15d079e5676e594f61b753648e82f0b1363cec0723aa"


def _n(p):
    t = re.sub(r"(?m)^\s*>\s?", "", p.read_text(encoding="utf-8")).replace("*", "")
    return " ".join(t.split())


def test_seal_integrity_prereg_hash_unchanged():
    assert hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_the_seal_carries_its_provenance_fields():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt


def test_the_hinge_is_stated_before_computing():
    t = _n(CELL / "PREREGISTRATION.md")
    assert "non-toral" in t
    assert "The hinge, stated before computing" in t


def test_the_prior_is_disclosed_as_NO_GO():
    t = _n(CELL / "PREREGISTRATION.md")
    assert "NO-GO, moderately favoured" in t
    assert "FOUND is the convenient answer and must clear the higher bar" in t


def test_the_valuable_outcome_is_named_as_the_negative():
    t = _n(CELL / "PREREGISTRATION.md")
    assert "convert the programme's four independent negatives into one" in t
