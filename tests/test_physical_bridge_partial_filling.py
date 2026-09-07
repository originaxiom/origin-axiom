"""Reproduce finite witnesses; no inference from CS to physical matter."""
import importlib.util
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

import pytest

_PATH = Path(__file__).resolve().parents[1] / 'reports/physical_bridge_2026_09_05/partial_filling_audit.py'
_SPEC = importlib.util.spec_from_file_location('partial_filling_audit', _PATH)
pf = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(pf)


@pytest.fixture(scope='module')
def result():
    return pf.run()


def test_mirror_criterion_knows_the_period_and_two_torsion():
    assert all(pf.mirror_compatible_exact(Fraction(x, 4)) for x in range(-4, 5))
    assert not pf.mirror_compatible_exact(Fraction(1, 24))
    assert not pf.mirror_compatible_exact(Fraction(-1, 24))
    assert pf.modulo_half_distance(0.25) > 0
    assert pf.modulo_half_distance(2*0.25) == 0


def test_named_triangulation_is_combinatorially_a_degree_five_cover(result):
    assert result['cover']['cusps'] == 3 and all(result['cover']['complete'])
    assert result['covering_maps']
    assert all(row['degree'] == 5 and row['isomorphisms'] for row in result['covering_maps'])


def test_two_complete_cusps_survive_a_geometric_partial_filling(result):
    assert result['partial']['complete'] == [False, True, True]
    assert result['partial']['solution'] == 'all tetrahedra positively oriented'
    F = result['filled']
    assert F['cusps'] == 2 and all(F['complete'])
    assert F['solution'] == 'all tetrahedra positively oriented'
    assert float(F['volume']) > 0.3
    assert not result['symmetry_amphichiral']['value']


def test_cs_agrees_with_given_witness_and_reverses_with_orientation(result):
    x = result['partial_high']['cs']['value']['approximate']
    assert x == pytest.approx(0.157590041, abs=1e-9)
    assert min(pf.modulo_half_distance(x, target) for target in (0, 0.25)) > 0.09
    for key in ('filled', 'rebuilt'):
        assert pf.modulo_half_distance(x, result[key]['cs']['value']['approximate']) < 1e-10
    assert pf.modulo_half_distance(x, -result['reverse']['cs']['value']['approximate']) < 1e-10
    assert abs(result['references']['m004']['cs']['value']['approximate']) < 1e-10
