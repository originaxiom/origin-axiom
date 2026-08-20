"""B8100 — the one-loop geodesic factor. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8100_oneloop_geodesic", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_systole_is_the_known_value(r):
    assert abs(r["systole"] - 1.087070144995739) < 1e-9

def test_the_estimate_carries_its_cutoff_error(r):
    """Oscillatory convergence: the uncertainty is the last delta, not the last digit."""
    assert r["convergence_is_oscillatory"] is True
    assert r["cutoff_uncertainty"] > 0
    assert abs(r["logZ_geodesic_estimate"] + 0.273) < 0.01

def test_it_is_explicitly_NOT_a_partition_function(r):
    assert r["is_full_one_loop_partition_function"] is False
    assert "cusp" in r["why_not"]

def test_the_missing_piece_is_located(r):
    """The finding: B739's scattering determinant supplies what the product omits."""
    assert "B739" in r["missing_piece_governed_by"]
    assert "Lambda_K" in r["missing_piece_governed_by"]

def test_the_next_rung_is_named(r):
    assert "combine" in r["next_rung"]
