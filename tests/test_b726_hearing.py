"""B726 lock — the hearing face and the Born content: the WEIGHTS are the hearing's, the PHASE
needs the cyclotomic upgrade; the bare two faces don't close the gap; A^2=M ~ |psi|^2 is rejected.

Structural/operator-algebra/TQFT only; no SM value (Gate 5). Locks the field-ownership of the Born
ingredients + the two rejected base-rate hooks.
"""
import numpy as np
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
D2 = 2 + phi                     # total quantum dim^2 for Fibonacci MTC
x = sp.symbols('x')


def test_weights_are_the_bare_hearing_Q_sqrt5():
    # NON-UNIFORM Born-like weights d_a^2/D^2 = 1:phi^2 live in Q(sqrt5) (deg 2) -- the hearing owns them.
    p0 = sp.simplify(1 / D2)
    p1 = sp.simplify(phi**2 / D2)
    assert sp.simplify(p0 + p1 - 1) == 0                       # a probability vector
    assert abs(float(p0) - 0.2763932) < 1e-6                   # non-uniform (!= 1/2)
    mp = sp.minimal_polynomial(p0, x)
    assert sp.degree(mp, x) == 2                               # deg 2 => Q(sqrt5) = the bare hearing field
    assert mp == 5*x**2 - 5*x + 1


def test_amplitudes_need_a_real_quartic_not_bare_hearing():
    # S-entries 1/D, phi/D and the F-symbol phi^{-1/2} live in a REAL QUARTIC -- neither bare quadratic face.
    D = sp.sqrt(D2)
    mpa = sp.minimal_polynomial(sp.simplify(1 / D), x)
    assert sp.degree(mpa, x) == 4                              # quartic, NOT bare Q(sqrt5)
    assert mpa == 5*x**4 - 5*x**2 + 1
    mpf = sp.minimal_polynomial(sp.simplify(phi**sp.Rational(-1, 2)), x)
    assert sp.degree(mpf, x) == 4
    assert mpf == x**4 + x**2 - 1


def test_interference_phase_needs_Q_zeta5_not_either_bare_face():
    # the twist theta_tau = e^{4 pi i/5} = zeta5^2 is genuinely COMPLEX -> the interference phase is in Q(zeta5),
    # the hearing's cyclotomic UPGRADE; Q(sqrt5) is totally real (no phase); the being's phases are zeta3 (order 3).
    z5 = sp.exp(4 * sp.pi * sp.I / 5)
    assert abs(float(sp.im(z5)) - 0.5877852523) < 1e-6        # complex: nonzero imaginary part
    assert sp.simplify(z5**5 - 1) == 0                         # a 5th root of unity (in Q(zeta5))
    # Q(sqrt5) is totally real: sqrt5 has a real minimal polynomial, no complex embedding forced
    assert sp.minimal_polynomial(sp.sqrt(5), x) == x**2 - 5
    # the being's field Q(sqrt-3)=Q(zeta3): its root of unity is order 3, NOT 5
    z3 = sp.exp(2 * sp.pi * sp.I / 3)
    assert sp.simplify(z3**3 - 1) == 0 and sp.simplify(z3**5 - 1) != 0


def test_hook_A2M_is_not_amplitude_squared():
    # A^2=M ~ |psi|^2 REJECTED: |psi|^2 = psi*c(psi) is the golden Galois NORM = -1 (a unit);
    # A^2=M's positive eigenvalue is the LITERAL square phi^2 = +2.618. Different operations.
    A = np.array([[1, 1], [1, 0]], dtype=float)
    M = np.array([[2, 1], [1, 1]], dtype=float)
    assert np.allclose(A @ A, M)                              # A^2 = M (the cat map)
    # A is hyperbolic/Anosov: eigenvalues off the unit circle -> NOT unitary, not conjugate to unitary
    evals = np.linalg.eigvals(A)
    assert not np.allclose(np.abs(evals), 1.0)               # |eig| != 1
    assert not np.allclose(A.T @ A, np.eye(2))              # A^T A != I -> not orthogonal/unitary
    # golden Galois norm of phi vs literal square
    phibar = (1 - sp.sqrt(5)) / 2
    assert sp.simplify(phi * phibar) == -1                    # N(phi) = phi*conj(phi) = -1
    assert abs(float(phi**2) - 2.618033989) < 1e-6           # phi^2 = +2.618  != -1
    # so the conjugation-norm and the literal square disagree: the analogy is false


def test_being_diagonal_vs_MTC_offdiagonal_dichotomy():
    # being thermal KMS state: commutes with H -> diagonal, zero off-diagonal coherence.
    E = np.array([0.0, 1.0, 2.5]); beta = 0.7
    rho = np.diag(np.exp(-beta * E) / np.exp(-beta * E).sum())
    H = np.diag(E)
    assert np.allclose(rho @ H - H @ rho, 0)                 # [rho,H]=0 -> diagonal/decohered
    assert np.allclose(rho - np.diag(np.diag(rho)), 0)       # zero off-diagonal

    # Fibonacci braid rep: sigma1 diagonal phases, sigma2 = F sigma1 F is UNITARY and OFF-DIAGONAL.
    inv = float(1 / phi)                                      # phi^{-1} ~ 0.618  (F diagonal)
    off = float(phi**sp.Rational(-1, 2))                     # phi^{-1/2} ~ 0.786 (F off-diagonal)
    F = np.array([[inv, off], [off, -inv]])                   # Fibonacci F-matrix, real symmetric, F^2=I
    assert np.allclose(F @ F, np.eye(2), atol=1e-12)
    s1 = np.diag([np.exp(-4j*np.pi/5), np.exp(3j*np.pi/5)])   # R-eigenvalue phases
    s2 = F @ s1 @ F
    assert np.allclose(s2 @ s2.conj().T, np.eye(2), atol=1e-12)   # sigma2 unitary
    assert abs(s2[0, 1]) > 0.5                                # genuinely OFF-DIAGONAL (channel mixing)
    assert np.linalg.norm(s1 @ s2 - s2 @ s1) > 0.1           # non-abelian: [sigma1,sigma2] != 0
    # Yang-Baxter certifies these are the true braid generators
    assert np.allclose(s1 @ s2 @ s1, s2 @ s1 @ s2, atol=1e-12)
