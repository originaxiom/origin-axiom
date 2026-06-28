"""B271 locks -- walls #3 (chirality) & #4 (4d-lift) made precise. Wall #3: the amphichiral tau (E6 outer aut)
tau-broken locus = the 26 (exponents {4,8}) = B265's E6-Zariski-dense directions => chirality locus = E6-density
locus. Wall #4: input-required (no canonical 2-/4-manifold). FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B271_walls_3_4" / "walls_3_4.py"
_spec = importlib.util.spec_from_file_location("b271", _PATH)
b271 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b271)


def test_chirality_locus_is_e6_density_locus():
    # the tau-broken (chiral) directions are exactly B265's E6-Zariski-dense {4,8}
    assert b271.chirality_locus_equals_e6_density_locus()
    assert sorted(b271.TAU_BROKEN_EXPONENTS) == [4, 8]
    assert sorted(b271.TAU_FIXED_EXPONENTS) == [1, 5, 7, 11]


def test_tau_dimension_split():
    # f4 (vector-like) = 52, 26 (chiral) = 26, sum = dim E6 = 78
    assert b271.dimension_checks()
    assert b271.DIM_F4 == 52 and b271.DIM_26 == 26


def test_wall4_lift_candidates_enumerated():
    # all three candidate 3d->4d lifts recorded with why-not-canonical (no silent drop)
    assert set(b271.LIFT_CANDIDATES) == {"M x S^1", "class-S (2-manifold)", "4-manifold filling W"}
