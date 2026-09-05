"""Recompute the conditional action/vacuum, not only its archived verdict."""
import json

import numpy as np
import pytest
import sympy as sp

from reports.physical_bridge_2026_09_05 import vacuum as v


@pytest.fixture(scope="module")
def report():
    return v.analyze()


def test_cubic_invariant_and_broken_control():
    triples, coeff, eq, _ = v.cubic()
    assert len(triples) == 45
    assert set(map(abs, coeff)) == {1}
    assert (eq*coeff).is_zero_matrix
    broken = coeff.copy()
    broken[0] *= -1
    assert not (eq*broken).is_zero_matrix


def test_compact_positive_kinetic_norm():
    generators = v.representation()[4]
    # Each i*T is anti-Hermitian for the actual identity kinetic metric.
    assert all((sp.I*t).H == -sp.I*t for t in generators)
    gram = np.array([[complex(sp.trace(a*b)).real for b in generators]
                     for a in generators])
    assert np.linalg.eigvalsh(gram).min() > 0


def test_exact_mass_blocks_and_zero_control():
    s, n = sp.symbols("s n", real=True)
    _, d, l = v.mass_blocks(s, n)
    assert sp.simplify(d*d.H-(s*s+n*n)*sp.eye(3)).is_zero_matrix
    assert sp.simplify(l*l.H-(s*s+n*n)*sp.eye(2)).is_zero_matrix
    assert v.mass_blocks(0, 0)[0].is_zero_matrix
    for ss, nn in [(1, 0), (0, 1), (1, 2), (1+2*sp.I, 3-sp.I)]:
        m, d, l = v.mass_blocks(ss, nn)
        masses = np.linalg.svd(np.array(m, complex), compute_uv=False)
        target = float(sp.sqrt(abs(ss)**2+abs(nn)**2))
        np.testing.assert_allclose(masses[:10], target, atol=1e-12)
        np.testing.assert_allclose(masses[10:], 0, atol=1e-12)
        for block in (d, l):
            assert all(sp.simplify(block*x).is_zero_matrix for x in block.nullspace())
            # Simplification cannot make an actual non-kernel vector pass.
            nonzero_col = next(i for i in range(block.cols) if any(block[:, i]))
            assert not sp.simplify(block*sp.eye(block.cols)[:, nonzero_col]).is_zero_matrix


def test_family_mixing_kernel_and_singular_values():
    mn = np.array([[1, 2j], [2j, 3]], complex)
    ms = np.array([[2j, 1], [1, -1j]], complex)
    masses, light = v.heavy_light(mn, ms)
    block = np.hstack((mn, ms))
    np.testing.assert_allclose(block@light, 0, atol=1e-13)
    np.testing.assert_allclose(light.conj().T@light, np.eye(2), atol=1e-13)
    np.testing.assert_allclose(np.sort(masses**2), np.linalg.eigvalsh(mn@mn.conj().T+ms@ms.conj().T))
    masses, light = v.heavy_light(np.zeros((2, 2)), np.zeros((2, 2)))
    assert masses.size == 0 and light.shape == (4, 4)
    with pytest.raises(ValueError):
        v.heavy_light(np.zeros((2, 3)), np.zeros((2, 3)))


def test_full_compact_stabilizers_and_sm_action(report):
    assert report["compact_stabilizer_dimensions"] == {
        "S": 45, "S_plus_2N_single_field": 45,
        "S_and_N_distinct_fields": 24, "S_N_and_Y": 12,
    }
    _, orbit = v.fluctuation_matrices()
    sm = v.sm_generator_coordinates()
    assert sm.rank() == 12
    assert (orbit*sm).is_zero_matrix


def test_potential_vacuum_hessian_and_gauge_zeros(report):
    p = report["potential"]
    assert p["value_at_candidate"] < 1e-25
    assert p["exact_hessian_rank"] == p["independent_numeric_rank"]
    assert p["gauge_goldstone_modes"] == 66
    assert p["nongauge_tree_level_zero_modes"] >= 11
    j, orbit = v.fluctuation_matrices()
    assert (j*orbit).is_zero_matrix
    # A nonzero radial fluctuation must not be called a Goldstone.
    si = report["singlet_indices"]["S"]
    assert not j[:, si].is_zero_matrix
    displacement = np.zeros(186)
    displacement[si] = 0.1
    c = v.constraints(*v.fields_at(displacement))
    assert c@c > 0


def test_directional_derivative_and_positive_potential():
    j = np.array(v.fluctuation_matrices()[0], float)
    rng = np.random.default_rng(20260905)
    for _ in range(4):
        direction = rng.normal(size=186)
        direction /= np.linalg.norm(direction)
        eps = 1e-4
        plus = v.constraints(*v.fields_at(eps*direction))
        minus = v.constraints(*v.fields_at(-eps*direction))
        np.testing.assert_allclose((plus-minus)/(2*eps), j@direction, atol=1e-10)
        measured = (plus@plus+minus@minus)/eps**2
        expected = 2*np.linalg.norm(j@direction)**2
        assert abs(measured-expected) < 1e-5


def test_output_serialization(report):
    assert json.loads(json.dumps(report, allow_nan=False)) == report
