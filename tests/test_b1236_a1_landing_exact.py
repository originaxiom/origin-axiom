"""B1236 -- the A1 landing at exact multiplet grade (codex R035 verified here).

The lock runs the independent implementation and pins the six cells: the exact hit, uniqueness within
support, and the three controls that TYPE the result (histogram false positive; the external reading
excluded by type not content; the diagonal rescue's triplet), plus the exhibited extra u(1).
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1236_a1_landing_exact"


def _run():
    r = subprocess.run([sys.executable, str(ARC / "verification" / "a1_su6_branching.py")],
                       capture_output=True, text=True, cwd=str(ARC / "verification"))
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout


def test_the_hit_and_uniqueness():
    out = _run()
    assert "27 -> the SM-shaped 27 EXACTLY (multiset of irreps)" in out
    assert "exactly 1 reproduces the target: [(Fraction(-1, 3), Fraction(1, 2), Fraction(0, 1))]" in out


def test_the_three_controls_type_the_result():
    out = _run()
    assert "reproduces the CHARGE HISTOGRAM but not the multiplets" in out
    assert "EXTERNAL reading (2_E = weak) also matches abstractly -- excluded by type" in out
    assert "diagonal weak su(2) turns (2_W,2_E) into 1+3" in out
    assert "commutant rank 2" in out
    assert out.strip().splitlines()[-1].startswith("VERDICT: the A1 landing reproduces the SM-shaped 27 EXACTLY")


def test_declares_no_identification_and_stays_a_compatibility_theorem():
    d = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert d["verdict"] == "PROVED" and d["creates_law"] is False
    assert d["identifications"] == []
    assert "COMPATIBILITY THEOREM" in d["claim_one_line"]
    assert "OPEN" in d["claim_one_line"]


def test_the_two_addenda_point_here():
    a = (ROOT / "frontier" / "B1098_nonabelian_hatch" /
         "ADDENDUM_2026-09-02_a1_row_exact_grade_B1236.md").read_text(encoding="utf-8")
    b = (ROOT / "frontier" / "B1100_landing_content" /
         "ADDENDUM_2026-09-02_the_a1_has_no_residual_B1236.md").read_text(encoding="utf-8")
    assert "B1236" in a and "multiplet" in a
    assert "B1236" in b and "residual" in b
