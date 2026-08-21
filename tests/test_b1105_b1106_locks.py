"""B1105 + B1106 locks — the scope audit's corrections and the edge seal."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


# ---- B1105: the corrections stay landed, the overstatement stays dead ----

def test_scope_correction_landed():
    t = _read("TERMINOLOGY.md")
    assert "scope correction 2026-08-21, B1105" in t
    assert "FOUR INDEPENDENT THEOREMS, ONE CONCLUSION" in t
    l = _read("docs/THE_LADDER.md")
    assert "B1105 scope audit, 2026-08-21" in l


def test_overstatement_stays_dead():
    for rel in ("TERMINOLOGY.md", "docs/THE_LADDER.md", "docs/THE_FRAMEWORK.md"):
        assert "shown to be one fact" not in _read(rel), rel


def test_b1105_findings_table():
    f = _read("frontier/B1105_wall_scope/FINDINGS.md")
    assert "pairwise different" in f
    assert "E-PD↔AW" in f and "named opens" in f


# ---- B1106: the seal and its control ----

def test_prereg_sealed_and_differential_first():
    p = _read("docs/EDGE_PREREG_SPEC.md")
    assert "WHAT STANDARD THEORY ALREADY FORCES" in p.split("THE PREDICTION")[0], (
        "differential-first: the concession section must precede the prediction")
    assert "KILL CONDITIONS" in p and "K3" in p
    assert "PINS the convention" in p
    s = _read("docs/SEAL_LEDGER.md")
    assert "THE EDGE SEAL" in s and "docs/EDGE_PREREG_SPEC.md" in s


def test_gen_control_results():
    r = json.loads(_read("frontier/B1106_edge_seal/b1106_gen_control.json"))
    assert r["positive_control_golden_law"] is True
    assert r["silver_strict_never_closes"] is True
    assert r["verdict"].startswith("C-GEN PASS")
    assert r["golden"]["987"] == [] and r["golden"]["2584"] == []
    assert r["golden"]["1597"] == [0, 1] and r["golden"]["4181"] == [0, 1]


def test_gen_control_live():
    p = subprocess.run(
        [sys.executable, str(ROOT / "frontier/B1106_edge_seal/b1106_gen_control.py")],
        capture_output=True, text=True, cwd=str(ROOT), timeout=300)
    assert p.returncode == 0
    assert "C-GEN PASS" in p.stdout
