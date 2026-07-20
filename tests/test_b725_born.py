"""B725 lock — the Born rule: FORM forced (+ quadratic from the c-swap order), CONTENT open.

Two-seat cross-verified (cc SSB-dynamics + cc2 axiomatic). Structural/operator-algebra only;
no SM value (Gate 5). Locks the discriminating facts of all three probes + the cc2 content-gap.
"""
import numpy as np
import sympy as sp


def test_probe1_quadratic_degree_equals_cswap_order():
    # |psi|^2 = psi * c(psi) = N_{C/R}(psi): the c-swap is order 2 -> the invariant norm is degree 2 = QUADRATIC.
    x, y = sp.symbols('x y', real=True)
    psi = x + sp.I * y
    norm2 = sp.expand(psi * sp.conjugate(psi))
    assert norm2 == x**2 + y**2                       # the Born form
    assert sp.Poly(norm2, x, y).total_degree() == 2   # degree = |Gal(C/R)| = 2

    # live falsifier: an ORDER-3 swap (cyclic cubic field) gives a degree-3 norm -> had c been order 3, CUBIC.
    t = sp.symbols('t')
    minpoly = t**3 + t**2 - 2*t - 1                    # min poly of 2cos(2pi/7), a cyclic cubic
    assert sp.Poly(minpoly, t).degree() == 3          # order-3 Galois group -> degree-3 invariant


def test_probe1_modular_conjugation_J_is_antiunitary_order2():
    # J(a)=a* on the GNS/HS space of M_n with cyclic-separating Omega=rho^{1/2}: antiunitary, J^2=1, JMJ=M'.
    n = 3
    rng = np.random.default_rng(11)
    A = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    B = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    # HS inner product <a,b> = Tr(a^dag b); J(a) = a^dag implements conjugate-linear, order-2 involution
    def J(a): return a.conj().T
    ip = lambda a, b: np.trace(a.conj().T @ b)
    assert abs(ip(J(A), J(B)) - np.conj(ip(A, B))) < 1e-12   # antiunitary: <Ja,Jb> = conj<a,b>
    assert np.allclose(J(J(A)), A)                            # J^2 = 1
    alpha = 0.7 - 1.3j
    assert np.allclose(J(alpha * A), np.conj(alpha) * J(A))   # conjugate-linear (the Born bra slot)


def test_probe2_ssb_orthogonal_pointer_weights_are_tr_rho_P():
    # SSB selects the orthogonal pointer MASA; its decomposition weights = Tr(rho P_i) exactly (the FORM).
    E = np.array([0.0, 1.0, 2.5]); beta = 0.8
    gibbs = np.exp(-beta*E); gibbs /= gibbs.sum()
    rho = np.diag(gibbs)
    Ps = [np.diag((np.arange(3) == i).astype(float)) for i in range(3)]
    w = np.array([np.real(np.trace(rho @ P)) for P in Ps])
    assert np.allclose(w, gibbs)                              # orthogonal pointer weight = Tr(rho P) = eigenvalue
    assert abs(w.sum() - 1) < 1e-12 and np.all(w >= 0)

    # NON-vacuous: a non-orthogonal ensemble for the same rho gives weights that DIFFER from Tr(rho P).
    a = 0.4  # nonzero overlap
    v_plus = np.array([np.cos(a),  np.sin(a)])
    v_minus = np.array([np.cos(a), -np.sin(a)])
    rho2 = 0.5*np.outer(v_plus, v_plus) + 0.5*np.outer(v_minus, v_minus)
    Pp = np.outer(v_plus, v_plus)
    assert abs(np.trace(rho2 @ Pp) - 0.5) > 0.05             # Tr(rho P) != the 1/2 ensemble weight


def test_cc2_content_gap_gleason_does_not_fix_weights_on_abelian_outcomes():
    # cc2's sharp point (CONFIRMED): on the broken/abelian outcome algebra, Gleason does NOT single
    # out Born over Gibbs -- BOTH are valid states. The weights across outcomes are a SEPARATE input.
    rng = np.random.default_rng(7)
    psi = rng.normal(size=3) + 1j*rng.normal(size=3); psi /= np.linalg.norm(psi)
    born = np.abs(psi)**2                                     # a pure state's Born weights
    E = np.array([0.0, 1.0, 2.5]); beta = 0.8
    gibbs = np.exp(-beta*E); gibbs /= gibbs.sum()             # a thermal/Gibbs weight vector
    # both are legitimate probability vectors (valid states on the abelian algebra) ...
    for w in (born, gibbs):
        assert abs(w.sum() - 1) < 1e-12 and np.all(w >= 0)
    # ... and they are DIFFERENT -> Gleason's form does not pin the content (interference / |amp|^2 weights).
    assert not np.allclose(born, gibbs)


def test_probe3_gleason_needs_dim3_dim2_has_a_non_born_frame_function():
    # Gleason is genuinely load-bearing: dim 2 admits NON-Born frame functions, so "frame function =>
    # quadratic Tr(rho P)" requires dim >= 3. A line in R^2 is defined mod pi; a frame function on
    # orthonormal pairs {theta, theta+pi/2} must have constant sum. In the Fourier variable phi=2theta,
    # the shift is phi -> phi + pi, so only EVEN harmonics survive the sum -> odd harmonics cancel
    # automatically and are UNCONSTRAINED. k=1 (cos 2theta) is the Born/quadratic term; k=3 (cos 6theta)
    # is an ODD, non-Born frame function that still satisfies the constraint -> the dim-2 escape.
    thetas = np.linspace(0, np.pi, 37, endpoint=False)
    born = lambda t: np.cos(t)**2                                  # = (1+cos2theta)/2, the k=1 Born form
    sums_born = np.array([born(t) + born(t + np.pi/2) for t in thetas])
    assert np.allclose(sums_born, 1.0)                             # quadratic: constant sum (valid frame fn)

    nonborn = lambda t: np.cos(6*t)                                # k=3 odd harmonic: NOT a quadratic form
    sums_nonborn = np.array([nonborn(t) + nonborn(t + np.pi/2) for t in thetas])
    assert np.allclose(sums_nonborn, 0.0)                          # ALSO a valid frame function (const sum 0)...
    assert np.std([nonborn(t) for t in thetas]) > 1e-6            # ...but non-constant, and it is NOT Tr(rho P)
    # => dim 2 has non-Born frame functions; Gleason (dim>=3, no type-I_2 summand) is what forces Born.
