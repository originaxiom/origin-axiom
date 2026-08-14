"""Locks B877 -- the S1 review of the First Measurement Theorem."""
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B877_fmt_review"
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")
_OUT = (_D / "rerun_output.txt").read_text(encoding="utf-8")


def test_the_pencil_theorem_reran_green():
    assert "det == c*mu^12: True" in _OUT
    assert "det == c*mu^4: True" in _OUT


def test_restriction_of_scalars_kernels():
    assert "Q-kernel dim 36 (predict 36 = per-root 12 x deg 3)" in _OUT
    assert "Q-kernel dim 12 (predict 12 = per-root 4 x deg 3)" in _OUT


def test_sum_freeness_closed_at_both_primes_all_roots():
    assert _OUT.count("; SUM-FREE: True") == 6
    assert "q=40123: ALL ROOTS SUM-FREE: True" in _OUT
    assert "q=40493: ALL ROOTS SUM-FREE: True" in _OUT


def test_their_roots_match_this_seats_13x_values():
    for r in ("-0.001938050209720433", "0.000398221501250352", "0.005685236871735386"):
        assert r in _OUT


def test_reviewed_document_and_reproducers_are_preserved():
    assert (_D / "REVIEWED_DOCUMENT.md").exists()
    for f in ("levi6.py", "fmt_phase2b.py", "fmt_combined.py"):
        assert (_D / "reproducers_rerun" / f).exists()


def test_the_verdict_and_the_fence():
    assert "accepted." in _F
    assert "the physics reading stays inside their §5 fence" in _F
    assert "not banked: the generation reading" in _F
    assert "the decisive test is the descent" in _F


def test_review_notes_recorded():
    assert "manifest gap" in _F
    assert "request the script for the record on the next pass" in _F
