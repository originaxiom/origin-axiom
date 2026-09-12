"""R27 follow-on controls. Original failed assertions remain visible in their own file."""
import json
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'reports/physical_bridge_2026_09_05/finite_twist_reductivity.py'


@pytest.fixture(scope='module')
def data():
    sage = shutil.which('sage')
    if sage is None:
        pytest.skip('Sage exact number-field runtime is required')
    result = subprocess.run([sage, '-python', '-u', str(SOURCE)], cwd=ROOT,
                            text=True, capture_output=True, timeout=180, check=False)
    assert result.returncode == 0, result.stdout+'\n'+result.stderr
    rows = [json.loads(line) for line in result.stdout.splitlines() if line.startswith('{')]
    return {row['part']: row.get('result', row) for row in rows}


@pytest.mark.parametrize('field', ['F13', 'Q(u)'])
def test_exact_positive_survives_both_fields_without_claiming_geometric_holonomy(data, field):
    r = data[field]['original']
    assert r['index'] == 1 and r['dimension_equalities']
    assert all(r['identities'].values())
    assert all(r['V']['checks'].values()) and all(r['dual']['checks'].values())
    assert (r['V']['n'], r['dual']['n'], r['V']['r1'], r['dual']['r1']) == (1, 0, 0, 2)


@pytest.mark.parametrize('field', ['F13', 'Q(u)'])
def test_invariant_flag_and_unsplittable_line_refute_complete_reducibility(data, field):
    r = data[field]
    assert r['invariant_full_flag'] and r['base_algebra_dimension'] == 3 and r['V_algebra_dimension'] == 9
    assert r['unipotent_ranks'] == [3, 2, 1, 0]
    for key in ('base_complement', 'V_complement'):
        assert not r[key]['invariant_complement']
        assert r[key]['augmented_rank'] > r[key]['equation_rank']


@pytest.mark.parametrize('field', ['F13', 'Q(u)'])
def test_a_nonzero_intertwiner_is_not_an_isomorphism(data, field):
    r = data[field]['dual_intertwiners']
    assert r['dimension'] == 1 and r['ranks'] == [3] and r['determinants'] == [0]
    assert r['equations']


@pytest.mark.parametrize('field', ['F13', 'Q(u)'])
def test_semisimplification_is_a_different_coefficient_system_with_zero_index(data, field):
    r = data[field]
    assert r['original']['index'] == 1 and r['semisimplification']['index'] == 0
    assert all(r['semisimplification']['identities'].values())
    assert r['coefficient_matrices'] != r['semisimplification_matrices']


def test_received_irreducibility_filter_misses_different_generator_eigenvalues(data):
    r = data['F13']
    assert r['defective_filter_accepts']
    assert r['common_line_eigenvalues'] == {'a': 4, 'b': 12}
    assert not r['base_complement']['invariant_complement']


def test_instrument_recovers_irreducible_and_reducible_semisimple_controls(data):
    r = data['instrument_controls']
    assert r['irreducible_algebra_dimension'] == 4
    assert r['semisimple_diagonal_algebra_dimension'] == 2
    assert r['semisimple_diagonal_complement']['invariant_complement']
