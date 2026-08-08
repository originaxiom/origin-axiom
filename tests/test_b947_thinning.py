"""B947 locks — L130, the thinning law. Seal integrity first."""
import hashlib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B947_thinning_law"
SEAL_SHA = "610fa7119c6a4fa8b55fe3155eebf5de0527ab4ac85f460a2f473eb69c51807c"


def test_seal_integrity_prereg_hash_unchanged():
    assert hashlib.sha256((CELL / "PREREGISTRATION.md").read_bytes()).hexdigest() == SEAL_SHA


def test_the_seal_carries_its_provenance_fields():
    """The first seal under the seal-provenance gate must actually carry them."""
    txt = (CELL / "PREREGISTRATION.md").read_text(encoding="utf-8")
    assert "BANKED IDENTITY:" in txt and "PRIOR ART:" in txt


def test_the_vacuity_exclusion_was_declared_in_advance():
    txt = " ".join((CELL / "PREREGISTRATION.md").read_text(encoding="utf-8").split())
    assert "Pre-declared vacuity exclusion" in txt
    assert "cannot be chosen after seeing results" in txt


def test_the_normalisation_defect_is_named_not_inherited():
    txt = " ".join((CELL / "PREREGISTRATION.md").read_text(encoding="utf-8").split())
    assert "if the normaliser is free" in txt
    assert "nearly vacuous" in txt


def test_the_convenient_answer_is_named():
    txt = " ".join((CELL / "PREREGISTRATION.md").read_text(encoding="utf-8").split())
    assert "LAW is the convenient answer and must clear the higher bar" in txt
