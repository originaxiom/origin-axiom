import pytest
import verify_monomial_lifts as m


@pytest.mark.parametrize("seed", [0, 1])
@pytest.mark.parametrize("constraint", ["free", "mu", "both"])
def test_complete_lattice_and_failable_admission(seed, constraint):
    x = m.analyze(seed, constraint)
    assert x["all_complex_multipliers_covered"]
    assert x["obstruction_order"] in (1, 5)
    assert (x["witness"] is not None) == (x["obstruction_order"] == 5)


def test_two_sided_controls():
    assert all(m.controls().values())


def test_actual_order_five_test_cycle():
    assert list(m.obstruction_row()) == [0]*5+[8]*5+[0]*25
