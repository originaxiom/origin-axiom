"""B1136 lock -- the genericity control turned on the wins: of 7 elementary properties, exactly
one separates m004 from its Q(sqrt-3) shape-field family (H_1 = Z); everything else (Vol,
amphichirality, CS=0, torsion-freeness) is the family's. Verified two-bench; results pinned in
b1136_results.json; a SnapPy spot-check + full census run when snappy/OA_SLOW are available."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1136_genericity_on_the_wins"
RESULTS = ARC / "b1136_results.json"


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


def _has_snappy():
    try:
        import snappy  # noqa: F401
        return True
    except Exception:
        return False


def test_family_is_the_14():
    d = _load()
    assert d["family_size"] == 14
    assert d["matches_cc3_14"] is True
    assert "m004" in d["family"]


def test_exactly_one_separator_h1_Z():
    d = _load()
    assert d["separators"] == ["h1_is_Z"]        # exactly one
    assert d["unique_separator_is_h1_Z"] is True
    assert d["h1_Z_members"] == ["m004"]         # m004 alone


def test_the_wins_are_family_level():
    d = _load()
    assert d["vol_m004_eq_m003"] is True                       # Vol identity (B680) family-level
    assert d["all_amphichiral"] is True                        # amphichirality family-level
    assert set(d["cs_zero_members"]) >= {"m004", "m203"}       # CS=0 shared, not a separator
    assert set(d["torsion_free_members"]) >= {"m004", "m202"}  # torsion-free shared


def test_findings_states_the_control_and_scope_notes():
    f = " ".join((ARC / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "H₁ = ℤ" in f and "family" in f.lower()
    assert "B955" in f
    assert "B680" in f and "family-level" in f
    assert "Gate 5 untouched" in f


@pytest.mark.skipif(not _has_snappy(), reason="snappy not installed in this env")
def test_snappy_spotcheck_h1_separator():
    import snappy
    assert str(snappy.Manifold("m004").homology()) == "Z"     # the separator holds
    assert str(snappy.Manifold("m003").homology()) != "Z"     # m003 differs
    assert abs(float(snappy.Manifold("m004").volume())
               - float(snappy.Manifold("m003").volume())) < 1e-9   # vol shared


@pytest.mark.skipif(not (os.environ.get("OA_SLOW") and _has_snappy()),
                    reason="full census scan ~60s; set OA_SLOW=1 with snappy installed")
def test_full_census_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(ARC / "verify_genericity.py")],
                       cwd=str(ARC), capture_output=True, text=True, timeout=1200)
    assert r.returncode == 0, r.stderr[-3000:]
    d = _load()
    assert d["separators"] == ["h1_is_Z"] and d["matches_cc3_14"] is True
