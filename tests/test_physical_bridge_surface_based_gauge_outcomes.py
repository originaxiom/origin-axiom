"""Explicit POST-RESULT outcome guards; not an unseen prediction."""
import importlib.util
from pathlib import Path

P=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/surface_based_gauge_2026_10_14/probe.py'
sp=importlib.util.spec_from_file_location('based_gauge_postresult',P)
M=importlib.util.module_from_spec(sp);sp.loader.exec_module(M)

def test_computed_complete_parallel_gauge_cost_not_only_range():
    r=M.run()['records']
    assert r['family_adjoint_invariants']==0
    assert r['family_symmetric_invariants']==1
    assert r['diagonal_block_hypercharge_invariants']==0
    assert r['complete_based_gauge_invariant_dimension']==15

def test_actual_new_phase_gap_and_even_zero_rank():
    r=M.run()['records']
    assert r['minimum_nonzero_phase']=='1/12'
    assert r['even_x_growth_pi_squared_coefficient']=='1/72'
    assert r['odd_P_growth_pi_squared_coefficient']=='1/144'
    assert r['even_phase_populations'][0][1][0]==[0,32]
    assert r['even_phase_populations'][1][1][0]==[0,16]
