"""B8099 — the 2+1 completeness audit. Reads results.json, never prose."""
import json, os, pytest
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontier",
                   "B8099_3d_completeness", "results.json")
@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)

def test_the_classical_datum(r):
    assert r["n_tetrahedra"] == 2 and r["n_cusps"] == 1
    assert r["regular_ideal_shape"] is True
    assert r["vol_equals_two_regular_ideal_tetrahedra"] is True

def test_the_complex_volume_is_purely_real(r):
    """CS = 0 by amphichirality -- the whole classical action is the volume."""
    assert r["complex_volume_purely_real"] is True
    assert abs(r["chern_simons"]) < 1e-12

def test_six_of_eleven_present(r):
    assert r["n_present"] == 6 and r["n_total"] == 11

def test_the_two_theories_are_distinguished(r):
    """The headline: 'complete the 3d theory' is ambiguous until one is named."""
    assert "ABELIAN" in r["two_theories"]["A"] and "E6" in r["two_theories"]["B"]
    assert "AMBIGUOUS" in r["headline"]

def test_3d3d_is_not_a_4d_lift(r):
    assert "Riemann surface" in r["3d3d_is_not_a_4d_lift"]

def test_scope_is_an_audit_not_a_construction(r):
    assert "An AUDIT, not a construction" in r["scope"]
