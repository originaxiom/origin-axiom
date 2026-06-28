"""B262 locks -- Rung 1 of the T[4_1] build: from the figure-eight triangulation (2 tetra, 1 cusp), the DGG
dictionary gives T[4_1] = U(1) gauge, 2 chirals, flavor U(1)_meridian x Weyl Z/2 -- abelian (gauge rank confirmed
two ways). FIREWALLED (3d-3d, not physics); nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B262_t41_theory" / "t41_theory.py"
_spec = importlib.util.spec_from_file_location("b262", _PATH)
b262 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b262)


def test_gauge_rank_confirmed_two_ways():
    # symplectic count and edge-equation rank must agree, both = 1 (-> U(1))
    assert b262.gauge_rank() == 1
    assert b262.independent_edge_constraints() == 1
    assert b262.gauge_rank() == b262.independent_edge_constraints()


def test_theory_is_abelian_no_e6():
    t = b262.theory()
    assert t["gauge_group"] == "U(1)" and t["gauge_rank"] == 1
    assert t["n_chirals"] == 2                      # one per tetrahedron <-> 2 quantum dilogs
    assert t["abelian"] is True
    assert t["has_E6_gauge_factor"] is False        # McKay-E6 stays arithmetic-only


def test_two_tetrahedra_one_cusp():
    assert b262.N_TET == 2 and b262.N_CUSP == 1
