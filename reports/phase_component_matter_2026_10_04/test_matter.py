import pytest
import verify_matter as m


@pytest.mark.parametrize("seed",[0,1])
@pytest.mark.parametrize("component",[1,2])
@pytest.mark.parametrize("t",[-1,1,2])
def test_actual_coupled_coefficients_and_dual_domains(seed,component,t):
    row=m.point(seed,component,t)
    for x in row["coefficients"].values():
        assert x["n"]-x["n_dual"]==x["ordinary"]["I"]
        assert x["n"]==x["relative_n"] and x["n_dual"]==x["relative_dual_n"]


def test_old_positive_and_instrument_controls():
    x=m.controls()
    assert x["old_component_zero_at2_recovered"] and x["phase_input_changes_both_coefficients"]
