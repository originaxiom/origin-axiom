"""Finite exact domain controls; no global analytic or physical certification."""
import pytest
import sympy as s

from reports.physical_bridge_2026_09_05 import flat_domain_audit as a
from reports.physical_bridge_2026_09_05 import flat_domain_reference as r


def test_actual_fox_row_and_missing_term_control():
    f,end = a.fox()
    v = s.Matrix([a.X-1,a.Y-1])
    assert end == 1 and a.zero(f*v)
    assert not a.zero((f+s.Matrix([[1,0]]))*v)
    for x,y in ((1,1),(-1,1),(1,-1),(-1,-1)):
        assert list(f.subs({a.X:x,a.Y:y})) == [r.derivative(x,y,"a"),r.derivative(x,y,"b")]


def test_flat_relative_count_and_complement_are_domain_dependent():
    d0,d1 = a.data(-1,1,3)
    b = a.betti(d0,d1)
    assert b == [0,3,0,0] and a.index(b) == 3
    assert a.complementary(d0,d1) == [0,0,3,0]
    assert a.index(a.complementary(d0,d1)) == -3
    assert a.betti(*a.data(s.conjugate(-1),s.conjugate(1),3)) == b
    assert a.hodge_nullities(d0,d1) == b


def test_even_core_states_cannot_be_discarded_as_lossless():
    relative = a.betti(*a.data(-1,1,3))
    detached = a.betti(*a.data(-1,1,3,s.zeros(3)))
    attached = a.betti(*a.data(-1,1,3,s.eye(3)))
    assert relative == [0,3,0,0]
    assert detached == [3,3,0,0] and attached == [0,0,0,0]
    assert a.index(relative) != a.index(detached) == a.index(attached)


def test_singular_attachments_retain_pairs_not_unpaired_index():
    for n in range(4):
        b = a.betti(*a.data(-1,1,3,s.diag(*([1]*n+[0]*(3-n)))))
        assert b == [3-n,3-n,0,0] and a.index(b) == 0


def test_trivial_character_keeps_degree_zero_in_index():
    base = a.betti(*a.data(1,1,0))
    assert base == [1,2,1,0] and a.index(base) == 0
    assert base[1]-base[2] == 1  # Omitting h0 would be a different index.
    assert a.betti(*a.data(1,1,3)) == [0,4,1,0]


def test_exact_exception_is_not_generic_three_zero():
    z = (-3+s.I*s.sqrt(7))/4
    assert s.simplify(z*s.conjugate(z)) == 1
    assert a.betti(*a.data(z,z,3)) == [0,4,1,0]


def test_whole_form_green_transmission_and_opposite_control():
    g = a.green_control()
    assert g["full_match_zero"] and g["rank"] == g["annihilator"] == 8
    assert g["normal_jump_pairing"] != 0


def test_fraction_reference_agrees_without_sympy_rank():
    for x,y in ((1,1),(-1,1),(1,-1),(-1,-1)):
        for k in range(6):
            assert a.betti(*a.data(x,y,k)) == r.cohomology(x,y,k)
            for t in (0,1,-1):
                assert a.betti(*a.data(x,y,k,t*s.eye(k))) == r.cohomology(x,y,k,t)


def test_invalid_inputs_do_not_silently_change_class():
    with pytest.raises(ValueError):
        a.data(2,1,3)
    with pytest.raises(ValueError):
        a.data(-1,1,3.0)
    with pytest.raises(ValueError):
        a.data(-1,1,3,s.eye(2))
    with pytest.raises(ValueError):
        a.betti(s.Matrix([1,0]),s.Matrix([[1,0]]))


def test_foreign_synthetic_diagnostic_credits_fix_and_preserves_gap():
    p = a.foreign_probe()
    assert p["missing_named_cover_P9"] is None and p["missing_named_cover_P10"] is None
    assert p["empty_F_P8"] is True and p["empty_F_readings"] == 0
    assert p["incomplete_every_cover"] is False
    assert p["incomplete_P5"] is True and p["incomplete_P6"] is True
