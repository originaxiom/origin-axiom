"""B1142 lock -- LANE C: the object's cusp/scattering spectrum is Λ_K = ζ·L(χ₋₃), GUE-distributed
but GENERIC (discriminates nothing), and the graviton bridge stays dead. Verified two-bench
(cloud Lane C + this bench's own mpmath/scipy re-derivation).

Fast tests pin b1142_results.json (the density discriminant, the 43+65=108 placement, the GUE
stats + the generic caveat, the graviton-bridge-dead) + assert the kill-graph routing. The full
L-function-zero re-derivation (>120s, mpmath) re-runs under OA_SLOW."""
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B1142_lane_c_cusp_spectrum"
RESULTS = ARC / "b1142_results.json"
FINDINGS = ARC / "FINDINGS.md"
VERIF = ARC / "verification"
REPO = Path(__file__).resolve().parents[1]
KILLGRAPH = REPO / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"


def _load():
    return json.loads(RESULTS.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- density: the falsifiable check
def test_density_discriminant_not_laplace():
    d = _load()["density_discriminant"]
    assert d["observed_zeros_to_t130"] == 108
    assert d["N_130"] > 70000                        # Laplace predicts ~75000
    assert d["ratio_too_sparse"] > 600               # 697x -> not the Laplace/geodesic spectrum


# ---------------------------------------------------------------- the placement (the exact match)
def test_placement_is_zeta_K():
    d = _load()["placement"]
    assert "zeta * L(chi_-3)" in d["the_108_are"]     # the full Dedekind zeta, not L(chi_-3) alone
    assert "43" in d["exact_count_match"] and "65" in d["exact_count_match"]
    assert 43 + 65 == 108
    assert "cusp" in d["side"].lower() and "NOT geodesic" in d["side"] or "not geodesic" in d["side"].lower()
    # the scattering determinant is the repo's B739
    assert "phi(s)=Lambda_K(s-1)/Lambda_K(s)" in d["scattering_determinant"]


# ---------------------------------------------------------------- the statistics + the caveat
def test_gue_generic_caveat():
    r = _load()
    g = r["gue_statistics"]["combined_108_set"]
    assert g["KS_GUE_p"] > g["KS_Poisson_p"]          # GUE fits, Poisson rejected
    assert g["KS_Poisson_p"] < 0.01
    assert "GENERIC" in r["caveat"] and ("Montgomery" in r["caveat"] or "Katz-Sarnak" in r["caveat"])
    assert "density" in r["caveat"].lower()           # the density carries the object, not the spacing


# ---------------------------------------------------------------- the graviton bridge is dead
def test_graviton_bridge_dead():
    r = _load()
    assert "DEAD" in r["graviton_bridge"]
    assert "cusp" in r["graviton_bridge"] and "geodesic" in r["graviton_bridge"]
    assert "does not hold" in r["graviton_bridge"]      # three-faces bridge does not hold
    assert "two faces" in FINDINGS.read_text(encoding="utf-8")   # the conclusion, in the FINDINGS


# ---------------------------------------------------------------- the FINDINGS + routing
def test_findings_and_kill_graph():
    t = FINDINGS.read_text(encoding="utf-8")
    assert "density (which can falsify) before statistics" in t or "density before statistics" in t.lower()
    assert "generic" in t.lower() and "discriminate" in t.lower()
    kg = json.loads(KILLGRAPH.read_text(encoding="utf-8"))
    e = [x for x in kg if x.get("id") == "B1142"]
    assert len(e) == 1, "B1142 (NEGATIVE) must be routed into the kill-graph (B836)"


# ---------------------------------------------------------------- reproduction present
def test_verification_present():
    assert (VERIF / "combined_analysis.py").exists()
    assert (VERIF / "verify_lane_c.py").exists()


# ---------------------------------------------------------------- full re-derivation (OA_SLOW, >120s)
@pytest.mark.slow
@pytest.mark.skipif(not os.environ.get("OA_SLOW"),
                    reason="L-function-zero re-derivation via mpmath >120s; set OA_SLOW=1 to run")
def test_lane_c_reproduces_OA_SLOW():
    r = subprocess.run([sys.executable, str(VERIF / "combined_analysis.py")],
                       capture_output=True, text=True, cwd=str(REPO), timeout=1800)
    assert r.returncode == 0, r.stderr[-2000:]
    assert "===COMBINED_RESULTS_JSON===" in r.stdout
