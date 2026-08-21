"""The map-finalization wave's locks (B1109/B1110/B1111) — stored verdicts
plus live recomputes of the cheap decisive facts."""
import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _j(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_b1109_stored_and_live_projection():
    r = _j("frontier/B1109_selection_cluster/b1109_results.json")
    assert r["F1_verdict"] == "NO-MATCH"
    assert r["F4_n_orbits"] == 2 and r["F4_orbit_sizes"] == [9, 9]
    # live: the 7-class projection with the size-9 class, from B1102's data
    inter = _j("frontier/B1102_exact_hypercharge_solve/b1102_intermediate.json")
    def parse(x):
        return F(x[0], x[1]) if isinstance(x, list) else F(str(x))
    classes = [(tuple(parse(c) for c in w), int(sz)) for w, sz in inter["classes"]]
    for idxs in ([2, 3], [0, 1]):
        proj = {}
        for w, sz in classes:
            p = tuple(w[i] for i in idxs)
            proj[p] = proj.get(p, 0) + sz
        assert len(proj) == 7, "the cardinality obstruction (7 < 8)"
        assert max(proj.values()) == 9, "the multiplicity obstruction (9 > 6)"


def test_b1110_stored():
    r = _j("frontier/B1110_spectral_cluster/b1110_results.json")
    assert r["F5_verdict"] == "WORD-PROPERTY"
    assert all(v == 28 for v in r["F5_counts"].values())
    assert all(r["F5_same_as_odd_u3"].values())
    assert r["F4b_swap_in_S"] == 0 and r["F4b_orbits"] == [9, 9]


def test_b1110_center_break_live():
    # three windows exact (fast): even Pell -> center, odd -> cut
    p, q = 1, 1
    for _ in range(60):
        p, q = p + 2 * q, p + q
    a = F(3 * q - 2 * p, q)
    def diffs(N):
        b = lambda n: ((n + 1) * a + a).__floor__() - (n * a + a).__floor__()
        r_ = [b(n) for n in range(N)]
        lo = [b(-n - 1) for n in range(N)]
        rr = r_[::-1]
        return [i for i in range(N) if lo[i] != rr[i]]
    assert diffs(70) == [35, 36]
    assert diffs(169) == [0, 1]
    assert diffs(408) == [204, 205]


def test_b1111_live_exact():
    p = subprocess.run(
        [sys.executable, str(ROOT / "frontier/B1111_w5_scoping/b1111_scoping.py")],
        capture_output=True, text=True, cwd=str(ROOT), timeout=900)
    assert p.returncode == 0, p.stderr[-400:]
    assert "1656 transversal pairs" in p.stdout
    assert "(1, 42), (3, 53)" in p.stdout


def test_findings_carry_the_verification():
    for rel, needle in [
        ("frontier/B1109_selection_cluster/FINDINGS.md", "PURE-A, PURE-A,"),
        ("frontier/B1109_selection_cluster/FINDINGS.md", "DOUBLE"),
        ("frontier/B1110_spectral_cluster/FINDINGS.md", "RE-VERIFIED IN EXACT ARITHMETIC"),
        ("frontier/B1111_w5_scoping/FINDINGS.md", "positive control"),
    ]:
        flat = " ".join((ROOT / rel).read_text(encoding="utf-8").split())
        assert needle.replace("\n", " ") in flat, (rel, needle)
