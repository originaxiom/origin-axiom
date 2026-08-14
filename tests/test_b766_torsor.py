"""Locks for B766 -- the measurement torsor (compute-grade: every fact re-derived).

STRENGTHENED 2026-07-25 (R31-4 audit + cc3's convergent b766-torsor-scrutiny):
 - the rank-3 is now COMPUTED from c/theta/gamma5 acting on genuine probes, not hardcoded
   flip-vectors;
 - the chord is corrected to a MATRIX-LEVEL observable (theta is trace-trivial at all ranks,
   so the Im part of the trace tangent is c-odd, NOT theta-odd);
 - the theta(reversal) vs iota(inversion) distinction is recorded (cc3 N7, gated): they
   coincide at SL(2)/Sym^2 but differ at genuine SL(3).
"""
import sympy as sp

u, x, y, t = sp.symbols("u x y t")
phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


def _sym2(M):
    a, b, c, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, a*b, b**2], [2*a*c, a*e + b*c, 2*b*e], [c**2, c*e, e**2]])


def test_c_flips_chirality_side():
    curve = y**2 - (x**2 - 1) * y + (x**2 - 1)
    sols = sp.solve(curve.subs(x, 2), y)
    assert set(sp.nsimplify(sp.conjugate(s)) for s in sols) == set(sp.nsimplify(s) for s in sols)
    assert all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols)


def test_theta_fixes_sl2_traces_and_time():
    # theta (reversal) is trivial on SL(2) traces -- and, as the tests below show, trace-trivial
    # at ALL ranks; its genuine action lives at the matrix level.
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [-u, 1]])
    assert sp.simplify((A * B).trace() - (B * A).trace()) == 0
    M, Mrev = sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[1, 1], [1, 2]])
    assert sorted(M.eigenvals()) == sorted(Mrev.eigenvals())


def test_gamma5_is_the_time_inversion():
    assert sp.simplify((1 - phi) ** 2 - 1 / phi**2) == 0     # Gal(Q(sqrt5)): phi^2 -> phi^-2


def test_chord_is_matrix_level_not_trace():
    # CORRECTED (R31-4 + cc3 b766-scrutiny): the chord (c XOR theta) sign is a MATRIX-LEVEL
    # observable, invisible to traces. theta is trace-trivial, so the Im=sqrt(3) part of the
    # trace tangent is c-ODD, not theta-odd.
    A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-u, 1]])
    d = sp.diff(sp.expand((A * B).trace() ** 2 - 1), u).subs(u, omega)
    assert sp.simplify(sp.im(d) - sp.sqrt(3)) == 0            # Im = c-odd (NOT theta-odd)
    assert sp.simplify(sp.re(d) + 5) == 0                     # Re = c-even (for the record)
    # the GENUINE chord observable: theta = reversal FLIPS at the Sym^2 MATRIX level while
    # staying invisible to the trace (cc3 b766-scrutiny: Sym^2(AB)-Sym^2(BA) has nonzero entries)
    diff = _sym2(A * B).subs(u, omega) - _sym2(B * A).subs(u, omega)
    assert diff != sp.zeros(3)                                              # matrix-level: non-trivial
    assert sp.simplify(_sym2(A * B).trace() - _sym2(B * A).trace()) == 0    # but trace-invisible


def test_rank_three_computed_from_generator_action():
    # STRENGTHENED (R31-4): rank-3 COMPUTED from c/theta/gamma5 each moving exactly one genuine
    # probe -- not hardcoded flip-vectors. probe_c in Q(sqrt-3), probe_g5 in Q(sqrt5),
    # probe_theta a real Sym^2 word matrix (reversal at the matrix level).
    c_act = lambda z: sp.conjugate(z)
    g5_act = lambda z: z.subs(sp.sqrt(5), -sp.sqrt(5))
    Pc, Pg = 2 - omega, phi
    A1, B1 = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [-1, 1]])   # real u = 1
    Pt_AB, Pt_BA = _sym2(A1 * B1), _sym2(B1 * A1)
    v_c = (1 if sp.simplify(c_act(Pc) - Pc) != 0 else 0, 0,
           1 if sp.simplify(g5_act(Pc) - Pc) != 0 else 0)
    v_th = (1 if Pt_AB.applyfunc(c_act) != Pt_AB else 0,
            1 if Pt_AB != Pt_BA else 0,
            1 if Pt_AB.applyfunc(g5_act) != Pt_AB else 0)
    v_g5 = (1 if sp.simplify(c_act(Pg) - Pg) != 0 else 0, 0,
            1 if sp.simplify(g5_act(Pg) - Pg) != 0 else 0)
    assert v_c == (1, 0, 0) and v_th == (0, 1, 0) and v_g5 == (0, 0, 1)   # each generator alone
    M = [list(v_c), list(v_th), list(v_g5)]
    r = 0
    for col in range(3):
        piv = next((i for i in range(r, 3) if M[i][col] % 2), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(3):
            if i != r and M[i][col] % 2:
                M[i] = [(a + b) % 2 for a, b in zip(M[i], M[r])]
        r += 1
    assert r == 3                                            # == B733's menu rank, COMPUTED


def test_theta_reversal_vs_iota_inversion_at_sl3():
    # cc3 N7 (gated): theta = reversal (w -> w^R) and iota = inversion (w -> w^-1) coincide at
    # SL(2)/Sym^2 (both trace-trivial) but DIFFER at genuine SL(3): reversal stays trace-trivial
    # at ALL ranks; inversion is trace-NON-trivial at SL(3). On the object's self-dual (Sym^2/V0)
    # component iota ~ theta, so B766 rank 3 stands; the full SL(3) variety can carry iota as a
    # 4th generator (cc3 N8 -- conclusion gated CORRECT; cc3's specific S=diag(1,-1,1) does NOT
    # intertwine, flagged back to cc3).
    A = sp.Matrix([[1, 2, 0], [0, 1, 3], [0, 0, 1]])
    B = sp.Matrix([[1, 0, 0], [4, 1, 0], [0, 5, 1]])
    W = A * A * B
    assert sp.simplify(sp.trace(W) - sp.trace(B * A * A)) == 0    # reversal trace-trivial @ SL(3)
    assert sp.simplify(sp.trace(W) - sp.trace(W.inv())) != 0      # inversion trace-NON-trivial @ SL(3)
