"""Recompute the B915 defect; do not certify its curve from a stored verdict."""
import math

import numpy as np

from reports.physical_bridge_2026_09_05.gauge_running import (
    boundary_down, evolve, inverse_couplings)
from reports.physical_bridge_2026_09_05.run_audit import legacy_functions, vary_legacy_guess


def test_legacy_two_loop_boundary_defect_is_not_integration_noise():
    old,_ = legacy_functions()
    mu = 1.5e13
    t = math.log(mu/old["MZ"])
    observable = old["curve_point"](mu, True)
    x = inverse_couplings(old["INV_AEM"], *observable)
    endpoint = evolve(x,0,t)
    tighter = evolve(x,0,t,rtol=2e-13,atol=2e-14)
    assert max(abs(np.diff(endpoint))) > 1e-3
    assert max(abs(tighter-endpoint)) < 1e-7
    corrected = boundary_down(t,old["INV_AEM"])
    assert max(abs(np.diff(evolve(corrected.inverse_ir,0,t)))) < 1e-7


def test_sequential_guess_is_inert_at_one_loop_but_leaks_at_two():
    old,prefix = legacy_functions()
    low,high = (vary_legacy_guess(old,prefix,s) for s in (.09,.15))
    mu = 1.5e13
    assert max(abs(np.array(low(mu,False))-high(mu,False))) < 1e-11
    assert max(abs(np.array(low(mu,True))-high(mu,True))) > 1e-5
