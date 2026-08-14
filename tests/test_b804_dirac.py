"""B804 — locks the cobordism computation and the pre-registered Weyl caveat."""
import importlib.util
from pathlib import Path

ARC = Path(__file__).resolve().parents[1] / "frontier" / "B804_dirac_spectrum"
VOL = 2.0298832128          # vol(m003) = vol(m004), snappy-verified in B803


def _m():
    spec = importlib.util.spec_from_file_location("b804", ARC / "dirac.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_omega_spin_2_is_z2_with_exactly_one_non_bounding_class():
    m = _m()
    structs = m.spin_structures_on_torus()
    assert len(structs) == 4
    assert m.bordism_group_order() == 2                       # Z/2
    non_bounding = [s for s in structs if not m.bounding(*s)]
    assert non_bounding == [(1, 1)]                           # the Lie structure generates


def test_arf_is_the_product_and_detects_the_generator():
    m = _m()
    assert m.arf(1, 1) == 1
    assert all(m.arf(a, b) == 0 for a, b in [(0, 0), (0, 1), (1, 0)])


def test_cusp_structure_is_forced_bounding_for_every_spin_structure():
    """The step the campaign turns on: T^2 bounds the compact core => Arf = 0."""
    ok, why = _m().cusp_structure_is_forced_bounding()
    assert ok and "Omega^spin_2" in why


def test_weyl_caveat_is_binding_equal_volume_gives_identical_leading_order():
    """Pre-registered: leading-order agreement is NOT a result -- it is an identity."""
    m = _m()
    diffs = m.weyl_caveat_is_binding(VOL, VOL)
    assert all(d == 0.0 for _, d in diffs), f"equal volumes must give identical leading order: {diffs}"
    # and the leading term is volume-driven: different volume => different count
    assert m.dirac_weyl_leading(VOL, 40) != m.dirac_weyl_leading(VOL * 1.01, 40)
