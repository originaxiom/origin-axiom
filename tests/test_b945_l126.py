"""B945 locks — L126: one Z/2 or two? Seal integrity first, per the prereg."""
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B945_l126_one_z2"
SEAL_SHA = "4873215851b1ea76adbf7997b6795ed502dad7597d15ddb3f55bacb109d1dfdf"


def test_seal_integrity_prereg_hash_unchanged():
    got = hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert got == SEAL_SHA


def test_the_prior_is_declared_split_and_names_the_degeneracy_in_advance():
    """The scoping observation that RL has only two cyclic rotations was made
    BEFORE the seal, and cells 2-3 were pre-committed because of it."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "Split, and honestly so" in txt
    assert "two** cyclic rotations" in txt
    assert "pre-committed here rather than added after" in txt


def test_the_convenient_answer_is_named_as_such():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "The convenient answer is LOCKED" in txt


def test_instrument_failure_branch_is_defined():
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "INSTRUMENT FAILURE" in txt
