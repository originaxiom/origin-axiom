"""B140 -- compute-session reconciliation. The load-bearing items run unconditionally (sympy-exact); SnapPy-gated."""
import pytest
import sympy as sp

from frontier.B140_compute_reconciliation.probe import (
    bundle_trace_fields_live,
    genus_general_live,
    incidence_facts,
    phi2_fixed_is_positive_dim,
    phi_fixed_sl2,
    sym2_of_000_is_rational,
)


def test_incidence_facts():
    """det[[m,1],[1,0]] = -1; [[m,1],[1,0]]^2 = R^m L^m; tr = m^2+2 (Items 3-4)."""
    f = incidence_facts()
    assert f["all_det_minus1"] is True
    assert f["all_N2_eq_RmLm"] is True
    assert f["all_trN2"] is True


def test_phi_fixed_unique_irreducible_is_rational():
    """The unique irreducible phi-fixed point is (0,0,0), rational, kappa=-2 (Items 2-3), m=1 and m=2."""
    for m in (1, 2):
        r = phi_fixed_sl2(m)
        assert r["unique_irreducible_is_000_rational"] is True
        irr = [p for p in r["points"] if p["irreducible"]]
        assert len(irr) == 1 and tuple(irr[0]["pt"]) == (0, 0, 0)
        assert sp.simplify(irr[0]["kappa"]) == -2


def test_phi2_fixed_is_positive_dimensional():
    """phi^2-fixed locus is a positive-dim curve (the geometric bundle object), unlike phi's isolated points."""
    p2 = phi2_fixed_is_positive_dim(1)
    assert p2["has_free_parameter_curve"] is True


def test_sym2_of_000_rational():
    """SL(3): Sym^2 of the SL(2) point (0,0,0) has rational trace coords (-1,-1,-1), commutator 3 (Item 2)."""
    s = sym2_of_000_is_rational()
    assert s["coords_are_-1"] is True
    assert s["commutator_is_3"] is True
    assert s["all_rational"] is True


def test_genus_general_mirror_snappy():
    """Item 1: genus-1 bundles + chiral knots have vol invariant, CS opposite under the mirror (SnapPy-gated)."""
    g = genus_general_live()
    if g is None:
        pytest.skip("SnapPy not available")
    assert g["genus1_and_knots_vol_same_cs_opposite"] is True


def test_bundle_trace_fields_recorded():
    """Item 5 is a record of already-banked fields (B125/B129); the in-sandbox trace_field needs Sage."""
    b = bundle_trace_fields_live()
    if b is None:
        pytest.skip("SnapPy not available")
    assert set(b.keys()) == {1, 2, 3}
    assert "sqrt-3" in b[1]["banked"] and "Q(i)" in b[2]["banked"]
