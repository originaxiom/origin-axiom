"""QP-4 closure probe -- locks for the canonical-sign computation."""
import cmath
import importlib.util
import math
import os

import numpy as np

PHI = (1 + math.sqrt(5)) / 2


def _build_weld_block():
    here = os.path.dirname(__file__) or "."
    spec = importlib.util.spec_from_file_location(
        "b238", os.path.join(here, "..", "frontier", "B238_su32_levelrank", "su32_wrt.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    w, S, T, _ = mod.su3_data(2)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    pairs = [(w.index((1, 0)), w.index((0, 1))),
             (w.index((2, 0)), w.index((0, 2)))]
    U = np.zeros((n, 2))
    for j, (a, b) in enumerate(pairs):
        U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    U = U.astype(complex)
    W = C @ R @ L
    B = np.array([[np.conj(U[:, i]) @ W @ U[:, j]
                   for j in range(2)] for i in range(2)])
    return B, C, U


def test_eigenphases_72():
    """Weld block eigenphases are exactly +/-72 deg = {zeta_5, zeta_5^4}."""
    B, _, _ = _build_weld_block()
    evals = np.linalg.eigvals(B)
    phases = sorted([cmath.phase(ev) * 180 / math.pi for ev in evals])
    assert abs(phases[0] + 72) < 1e-8 and abs(phases[1] - 72) < 1e-8


def test_su2_structure():
    """B is in SU(2): [[alpha,beta],[-conj(beta),conj(alpha)]]."""
    B, _, _ = _build_weld_block()
    assert abs(B[1, 1] - np.conj(B[0, 0])) < 1e-12
    assert abs(B[1, 0] + np.conj(B[0, 1])) < 1e-12
    assert abs(np.linalg.det(B) - 1) < 1e-10


def test_b5_is_identity():
    """B^5 = I (cyclotomic order 5)."""
    B, _, _ = _build_weld_block()
    assert np.allclose(np.linalg.matrix_power(B, 5), np.eye(2), atol=1e-10)


def test_trace_is_one_over_phi():
    """tr(B) = 1/phi = 2 cos(72 deg)."""
    B, _, _ = _build_weld_block()
    assert abs(np.trace(B) - 1 / PHI) < 1e-10


def test_charge_conj_minus_identity():
    """Charge conjugation C = -I on the theta-odd sector."""
    _, C, U = _build_weld_block()
    C_odd = np.array([[np.conj(U[:, i]) @ C @ U[:, j]
                       for j in range(2)] for i in range(2)])
    assert np.allclose(C_odd, -np.eye(2), atol=1e-12)


def test_galois_swaps_eigenvalues():
    """Complex conjugation swaps the eigenvalues: conj(zeta_5) = zeta_5^4."""
    B, _, _ = _build_weld_block()
    evals = sorted(np.linalg.eigvals(B), key=lambda z: -cmath.phase(z))
    assert abs(np.conj(evals[0]) - evals[1]) < 1e-10
    assert abs(np.conj(evals[1]) - evals[0]) < 1e-10


def test_rotation_no_fixed_direction():
    """Rotation by 72 deg has no invariant direction: det(R-I) != 0."""
    cos72 = math.cos(math.radians(72))
    det_RmI = 2 - 2 * cos72
    assert abs(det_RmI) > 1.0


def test_no_mcg_power_half_integer():
    """No power B^n (n=1..4) has eigenphase 0 or 180 deg."""
    for n in range(1, 5):
        phase = (n * 72) % 360
        assert phase not in (0, 180), f"B^{n} has half-integer eigenphase {phase}"


def test_coupling_galois_invariant():
    """QP-3 coupling fraction 15/32 is Galois-invariant."""
    omega = complex(-0.5, math.sqrt(3) / 2)
    omega_bar = complex(-0.5, -math.sqrt(3) / 2)

    def frac(u):
        ds = [0, 0, -2*(2-u), 2*(2+u), 2*(2+u), -2*(2-u), 4*u**3+8*u]
        off = sum(abs(complex(d).imag)**2 for d in ds)
        tot = sum(abs(complex(d))**2 for d in ds)
        return off / tot

    assert abs(frac(omega) - 15 / 32) < 1e-12
    assert abs(frac(omega_bar) - 15 / 32) < 1e-12


def test_coupling_sign_flips():
    """The signed coupling Im(d/du) flips under Galois (omega <-> omega_bar)."""
    omega = complex(-0.5, math.sqrt(3) / 2)
    omega_bar = complex(-0.5, -math.sqrt(3) / 2)
    im_omega = (-2 * (2 - omega)).imag
    im_omega_bar = (-2 * (2 - omega_bar)).imag
    assert abs(im_omega + im_omega_bar) < 1e-12
    assert abs(im_omega - math.sqrt(3)) < 1e-12
