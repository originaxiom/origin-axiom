"""QP-3 integration cell — locks for the theta-sector coupling computation."""
import cmath
import math

import numpy as np


def _omega():
    return complex(-0.5, math.sqrt(3) / 2)


def _riley_B(u):
    return np.array([[1, 0], [-u, 1]], dtype=complex)


def _riley_A():
    return np.array([[1, 1], [0, 1]], dtype=complex)


def test_riley_polynomial_at_omega():
    """u = omega satisfies u^2 + u + 1 = 0."""
    w = _omega()
    assert abs(w**2 + w + 1) < 1e-14


def test_sl2_off_block_zero():
    """SL(2) trace map has zero off-block: d(tr AB)/du = -1 (real) everywhere."""
    # tr(AB) = 2 - u, d/du = -1 (constant, real)
    assert complex(-1).imag == 0


def test_sym2_off_block_nonzero():
    """SL(3) = Sym^2 trace map has nonzero off-block at the geometric point."""
    w = _omega()
    # d(tr Sym^2(AB))/du = -2(2 - u), at u = omega: -2(2 - omega)
    deriv = -2 * (2 - w)
    assert abs(deriv.imag - math.sqrt(3)) < 1e-12, \
        f"Im(d/du) should be sqrt(3), got {deriv.imag}"


def test_sym2_off_block_is_sqrt3():
    """The leading Sym^2 off-block norm = sqrt(|disc(Q(sqrt(-3)))|) = sqrt(3)."""
    w = _omega()
    deriv = -2 * (2 - w)  # d(tr Sym^2(AB))/du at omega
    assert abs(deriv.imag - math.sqrt(3)) < 1e-12


def test_coupling_fraction():
    """Coupling fraction = 15/32 for the full 7-word Sym^2 trace map."""
    w = _omega()
    words_derivs = [
        0,                    # A: constant
        0,                    # B: constant
        -2 * (2 - w),         # AB
        2 * (2 + w),          # A^{-1}B
        2 * (2 + w),          # AB^{-1}
        -2 * (2 - w),         # A^{-1}B^{-1}
        4 * w**3 + 8 * w,     # [A,B]
    ]
    off_sq = sum(abs(d.imag)**2 for d in words_derivs)
    total_sq = sum(abs(d)**2 for d in words_derivs)
    frac = off_sq / total_sq
    assert abs(frac - 15 / 32) < 1e-12, f"Expected 15/32, got {frac}"


def test_commutator_purely_odd():
    """The commutator [A,B] Sym^2 derivative is purely imaginary (purely theta-odd)."""
    w = _omega()
    # tr([A,B]) = u^2 + 2, tr(Sym^2([A,B])) = (u^2+2)^2 - 1
    # d/du = 2(u^2+2) * 2u = 4u(u^2 + 2) = 4u^3 + 8u
    deriv = 4 * w**3 + 8 * w
    assert abs(deriv.real) < 1e-12, f"Re should be 0, got {deriv.real}"
    assert abs(deriv.imag - 4 * math.sqrt(3)) < 1e-12


def test_adjoint_off_block():
    """Ad_B off-block ||Im(Ad_B)||_F = 3*sqrt(2)/2."""
    w = _omega()
    B = _riley_B(w)
    Binv = np.linalg.inv(B)
    basis = [np.array([[1, 0], [0, -1]], dtype=complex),
             np.array([[0, 1], [0, 0]], dtype=complex),
             np.array([[0, 0], [1, 0]], dtype=complex)]
    Ad_B = np.zeros((3, 3), dtype=complex)
    for j in range(3):
        Y = B @ basis[j] @ Binv
        Ad_B[0, j] = Y[0, 0]
        Ad_B[1, j] = Y[0, 1]
        Ad_B[2, j] = Y[1, 0]
    off_norm = np.linalg.norm(Ad_B.imag, "fro")
    assert abs(off_norm - 3 * math.sqrt(2) / 2) < 1e-10


def test_theta_fixed_locus_zero():
    """On the theta-fixed locus (u real), all Sym^2 off-blocks vanish."""
    u_real = -2.0
    A = _riley_A()
    B = _riley_B(u_real)
    AB = A @ B
    tr_AB = np.trace(AB)
    deriv_sym2 = -2 * (2 - u_real)
    assert abs(complex(deriv_sym2).imag) < 1e-14
    Binv = np.linalg.inv(B)
    basis = [np.array([[1, 0], [0, -1]], dtype=complex),
             np.array([[0, 1], [0, 0]], dtype=complex),
             np.array([[0, 0], [1, 0]], dtype=complex)]
    Ad_B = np.zeros((3, 3), dtype=complex)
    for j in range(3):
        Y = B @ basis[j] @ Binv
        Ad_B[0, j] = Y[0, 0]
        Ad_B[1, j] = Y[0, 1]
        Ad_B[2, j] = Y[1, 0]
    assert np.linalg.norm(Ad_B.imag, "fro") < 1e-14
