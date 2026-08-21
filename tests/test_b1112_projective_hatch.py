"""B1112 lock -- the projective-hatch selection theorem (stored parity facts +
the A2/B1100 exact cross-check, which is independently locked)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SWEEP = json.loads((ROOT / "frontier/B1112_projective_hatch/parity_sweep.json")
                   .read_text(encoding="utf-8"))


def _by_dim(d):
    return [r for r in SWEEP if r["dim_c"] == d]


def test_twenty_strata_swept():
    assert len(SWEEP) == 20
    assert sum(1 for r in SWEEP if r["parity"] == "EVEN") == 9


def test_A2_projective_and_is_the_banked_multiset():
    a2 = _by_dim(16)
    assert len(a2) == 1 and a2[0]["parity"] == "EVEN"
    # THE load-bearing fact: A2's parity is exact because its spectrum IS
    # B1100's banked branching multiset (independently locked in test_b1100).
    assert a2[0]["weights27"] == {"-2": 6, "0": 15, "2": 6}


def test_A1_needs_the_lift():
    a1 = _by_dim(35)
    assert len(a1) == 1 and a1[0]["parity"] == "ODD"
    assert a1[0]["weights27"].get("1") == 6  # odd-weight witness


def test_principal_is_projective():
    prin = [r for r in SWEEP if "1, 2, 3, 4, 5)-reg" in r["label"]]
    assert prin and all(r["parity"] == "EVEN" for r in prin)


def test_selection_theorem_unique_SM_projective():
    # exactly one of the two SM-compatible landings (A2 rank4, A1 rank5) is projective
    a2_even = _by_dim(16)[0]["parity"] == "EVEN"
    a1_even = _by_dim(35)[0]["parity"] == "EVEN"
    assert a2_even and not a1_even, "the SM-facing selection must be unique (A2 only)"


def test_findings_carry_the_repricing():
    f = " ".join((ROOT / "frontier/B1112_projective_hatch/FINDINGS.md")
                 .read_text(encoding="utf-8").split())
    assert "0 bits of SM-facing ambiguity" in f
    assert "three-way convergence" in f.lower() or "THREE-WAY convergence" in f
