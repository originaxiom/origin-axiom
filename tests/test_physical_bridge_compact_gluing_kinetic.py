from pathlib import Path
import importlib.util

BASE=Path(__file__).resolve().parents[1]/'reports'/'physical_bridge_2026_09_05'
def load(name,file):
    spec=importlib.util.spec_from_file_location(name,BASE/file)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

N=load('test_r88_native','compact_gluing_kinetic.py')
R=load('test_r88_reference','compact_gluing_kinetic_reference.py')

def test_actual_noncommuting_jacobi_identity_and_wrong_sign():
    cs=N.V.jacobi_controls()
    assert len(cs)==9 and all(cs.values())
    assert cs['dropping_background_moment_rejected'] and cs['wrong_adjoint_sign_rejected']

def test_harmonic_projection_and_exact_direction_control():
    cs=N.V.projection_controls()
    assert len(cs)==10 and all(cs.values())
    assert cs['exact_tangent_zero_norm_control'] and cs['singular_J_has_unforced_direction']

def test_full_parent_trace_gram_not_dimension_matching():
    d=N.trace_controls(); r=R.root_trace()
    assert all(d['checks'].values()) and all(r['checks'].values())
    assert d['gram']==r['gram']==[[60*(1+int(i==j)) for j in range(4)] for i in range(4)]

def test_real_kinetic_normalization_and_parent_kernel_control():
    d=N.kinetic_controls()
    assert len(d['checks'])==5 and all(d['checks'].values())

def test_actual_three_character_bending_velocities():
    for ab in N.N.CHARS:
        d=N.case(ab)
        assert all(d['checks'].values()) and d['coboundary_rank']==24 and d['augmented_rank']==25

def test_separate_modular_actual_relators_ranks_and_parent_derivative():
    assert all(R.controls()['checks'].values())
    for p,r in R.R.PRIME_ROOTS:
        for ab in N.N.CHARS:
            d=R.verify(N.case(ab),p,r)
            assert len(d['checks'])==10 and all(d['checks'].values())
