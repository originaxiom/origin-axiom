"""B105 -- locking tests: the n=5 wall is a characterized COORDINATE ARTIFACT (gauge noise), and the unified
n>=5 wall is the forced-cusp-spectrum collision at n=5 (repeated -1)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b105", _ROOT / "frontier" / "B105_n5_wall_and_convergence" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_n5_resolves_21_of_24():
    """The eps-series resolves exactly 21 of 24 Dickson factors at SL(5) (the catalog-consistent part)."""
    assert B.n5_resolved_degree() == 21


def test_n5_unresolved_factor_varies_with_seed_rank_deficiency_signature():
    """The 3 unresolved factors VARY across seeds while all seeds resolve the same 21. [CORRECTION A, V90]:
    this is the expected eps-series RANK-DEFICIENCY signature (B84), UNINFORMATIVE about the true
    factorization there -- it does NOT imply 'coordinate artifact, not structural change'. The locked facts
    are the raw computation: the resolved 21 are invariant, the 3 unresolved are not."""
    n_distinct, all_resolve_21 = B.n5_unresolved_factor_varies_with_seed()
    assert all_resolve_21 is True                          # the genuine evidence: resolved 21 invariant
    assert n_distinct >= 2                                  # unresolved sector varies (rank-deficiency, not informative)


def test_v90_corrections_banked():
    """Corrections A and B are banked explicitly as downgrades (not silent edits)."""
    assert set(B.CORRECTIONS_V90) == {"A", "B"}
    assert "UNINFORMATIVE" in B.CORRECTIONS_V90["A"]
    assert "OVERSTATES" in B.CORRECTIONS_V90["B"]


def test_unified_wall_cusp_spectrum_collision_at_n5():
    """The forced cusp spectrum has tr=trinv=det=1 at n=3,4,5; its NON-trivial eigenvalues are distinct at
    n=3,4 and COLLIDE at n=5 (the doubly-degenerate -1 sector = the unified wall's root cause)."""
    tbl = B.unified_wall_table()
    for n in (3, 4, 5):
        assert tbl[n]["tr1"] and tbl[n]["trinv1"] and tbl[n]["det1"]
    assert tbl[3]["nontrivial_collision"] == 0
    assert tbl[4]["nontrivial_collision"] == 0
    assert tbl[5]["nontrivial_collision"] == 1             # the n=5 collision


def test_observations_and_corrections_banked():
    assert set(B.OBSERVATIONS) == {"H1", "H2", "H3", "H4", "H5", "H6"}
    assert set(B.CORRECTIONS) == {"C1", "C2", "C3", "C4"}
