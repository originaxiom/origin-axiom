"""The source-C3 group action must act, not merely have the right order."""
import importlib.util
from pathlib import Path
import sympy as sp

PATH=Path(__file__).resolve().parents[1]/'reports/physical_bridge_2026_09_05/resolved_fermion_c3_control.py'
SPEC=importlib.util.spec_from_file_location('physical_bridge_resolved_fermion_c3',PATH)
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def test_full_source_fixed_torus_comes_from_the_actual_word_action():
    d=M.run()
    assert d['checks']['actual_order_three']
    assert d['checks']['full_fixed_torus']
    assert {tuple(r['h']) for r in d['rows']}=={(0,0),(sp.Rational(1,3),sp.Rational(2,3)),(sp.Rational(2,3),sp.Rational(1,3))}


def test_original_cube_root_sample_is_rejected_as_source_fixed():
    d=M.run()
    assert d['checks']['original_order_three_character_not_fixed']
    assert any(not x.is_Integer for x in d['original_fixed_residual'])


def test_true_source_compatible_characters_have_the_resolved_and_split_counts():
    d=M.run()
    assert d['checks']['fixed_nontrivial_resolved']
    assert d['checks']['fixed_trivial_resolved']
    assert len([r for r in d['rows'] if r['P']==-2])==2
