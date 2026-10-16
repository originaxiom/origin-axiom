"""LIVE actual arena/source map and global shrinking tube safeguards."""
# BANKED IDENTITY: both producers fresh. PRIOR ART: packet DESIGN/PROOF.
import json
import os
import subprocess
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT/'reports/physical_bridge_2026_09_05/surface_arena_boundary_2026_10_16'

@pytest.fixture(scope='module')
def cert():
    values = []
    for name in ('probe', 'reference'):
        run = subprocess.run([sys.executable, '-B', str(HERE/(name+'.py'))], cwd=ROOT,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'), capture_output=True, text=True, timeout=1800)
        assert run.returncode == 0, run.stderr+run.stdout
        values.append(json.loads(run.stdout))
    assert values[0] == values[1] and values[0]['all_passed']
    return values[0]

def test_actual_normal_arena_map_and_both_fresh_antecedents(cert):
    for name in ('fresh geometric329 and32 controls with complete records',
        'fresh complete actual source tensor and spin R dictionary',
        'normal direction homogeneous map has determinant one',
        'exact S normal direction map including phase sign', 'exact T normal direction map',
        'wrong normal phase sign is rejected', 'central minus I acts by half normal rotation not identity',
        'double tangent angle descends but single angle does not'):
        assert cert['checks'][name]

def test_actual_total_normal_and_variable_tube_characteristic(cert):
    for name in ('actual Chern circle connection inhomogeneous S law',
        'actual coframe and radius gradient not a vertical approximation',
        'actual source characteristic form equals normal circle connection',
        'full total complex structure gives varying tube characteristic',
        'dropping radius variation loses boundary characteristic'):
        assert cert['checks'][name]

def test_global_lattice_and_strict_contact_certificate(cert):
    for name in ('entire lattice summand PDE and log gradient norm',
        'T and S reindex entire lattice without a finite census',
        'both lattice index substitutions are bijective and retain origin',
        'two positive lattice summands have distinct gradients everywhere',
        'actual varying Levi coefficient equals weighted gradient deficit',
        'strictness uses exact positive variance identity',
        'nonautomorphic finite pair controls strictness but not global invariance',
        'global radius minorant and fixed radius cusp control retained'):
        assert cert['checks'][name]
    assert not cert['records']['global_tube']['infinite_series_interval_evaluated']

def test_strict_contact_is_not_uniform_cusp_control(cert):
    for name in ('naive inverse sqrt y tube is Levi flat',
        'exact two term cusp Levi asymptotic not a uniform bound',
        'cusp constant integral from rational kernel'):
        assert cert['checks'][name]
    assert cert['records']['global_tube']['not_uniform_at_cusp']

def test_no_unearned_identification_of_contact_flows(cert):
    for name in ('Hilbert geodesic Reeb is verified not named by analogy',
        'normal connection Reeb differs and flow does not preserve it',
        'two contact forms have opposite orientation under actual map',
        'Hilbert form descends under exact normal S transition',
        'Hilbert form descends under T and minus I'):
        assert cert['checks'][name]

def test_actual_central_lifts_every_gauge_class_and_both_meridians(cert):
    for name in ('actual half frame squares to fibre puncture inner action',
        'half frame is not a pure fibre puncture loop',
        'normal and trefoil meridians distinguished by discriminant winding',
        'actual SU6 half frame unitary involution with wrong standalone centre'):
        assert cert['checks'][name]
    rows = cert['records']['central_lifts']['all_classes']
    assert [row['weak_class'] for row in rows] == [1, 3, 5, 7, 9, 11]
    for row in rows:
        assert cert['checks']['full E8 half frame square equals puncture and all sectors retained '+str(row['weak_class'])]
        assert sum(row['even']) == 136 and sum(row['odd']) == 112

def test_source_connection_curvature_and_physical_scope(cert):
    for name in ('actual source leading connection equals full weight generator',
        'tautological source frame has minus W alpha not zero',
        'global tube beta is not a free source connection substitution',
        'source full central rotation and real conjugate slots retained'):
        assert cert['checks'][name]
    meaning = cert['records']['meaning']
    assert meaning['arena_is_normal_boundary_under_explicit_map']
    assert meaning['smooth_global_embedded_strict_contact_tube_constructed']
    for name in ('uniform_positive_cusp_Levi_constant',
        'geodesic_flow_identified_as_physical_time_or_boundary_Reeb',
        'true_end_action_or_state_selected', 'global_stationary_Higgs_derived',
        'physical_SM_three_parameters_gravity_derived'):
        assert not meaning[name]
