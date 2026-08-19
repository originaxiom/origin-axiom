"""B8088 — one W×Galois orbit per row; W alone gives 25. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8088_row_homogeneity", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_sweep_is_exhaustive(r):
    assert r["n_elements"] == 5**6 - 1 == 15624

def test_every_row_is_a_single_W_times_galois_orbit(r):
    """The owner's claim, which B8086 did NOT establish."""
    assert r["n_W_galois_orbits"] == 9
    assert r["W_galois_orbit_sizes"] == r["b8086_row_counts"]
    assert r["every_row_is_one_W_galois_orbit"] is True

def test_the_homogeneity_is_arithmetic_not_geometric(r):
    """The sharpening: W alone splits 8 of the 9 rows, so uniqueness needs Galois."""
    assert r["n_W_orbits"] == 25
    assert r["W_alone_rows_that_are_single_orbits"] == 1

def test_the_d5_row_is_four_galois_conjugate_orbits_of_27(r):
    """Explains the external proposal's 108 = 27 x 4."""
    row = [s for s in r["splits"] if s["row"] == 108]
    assert len(row) == 1 and row[0]["n_W_orbits"] == 4 and row[0]["W_orbit_size"] == [27]

def test_orbit_sizes_partition_the_whole_sweep(r):
    assert sum(r["W_galois_orbit_sizes"]) == r["n_elements"]
    assert sum(r["W_orbit_sizes"]) == r["n_elements"]

def test_scope_disclaims_the_manifold(r):
    assert "NOT" in r["scope"] and "torsion-free" in r["scope"]
