"""B155 -- the 'golden x phase' spectral bridge at n=4 (V148).

Locks the exact facts of the canonical matrix M_g: charpoly = (golden)(phase),
rational block split, nonderogatory (=> Q-conjugacy by charpoly), (Z/2)^2 glue
(class-specific vs trivial block-diagonal glue), invariant form signature (1,3)
with discriminant -15, and the Omega_4 match at a=4, m=-1/2 (half-integer).
"""
import sympy as sp

x = sp.symbols('x')
Mg = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 0, 1]])
golden = x**2 - 3*x + 1
phase = x**2 - x + 1


def test_charpoly_is_golden_times_phase():
    chi = sp.expand(Mg.charpoly(x).as_expr())
    assert sp.expand(chi - golden * phase) == 0
    assert sp.expand(chi - (x**4 - 4*x**3 + 5*x**2 - 4*x + 1)) == 0
    assert Mg.det() == 1


def test_field_discriminants():
    assert sp.discriminant(golden, x) == 5      # Q(sqrt5), real / Anosov
    assert sp.discriminant(phase, x) == -3      # Q(sqrt-3)
    assert sp.expand(phase - sp.cyclotomic_poly(6, x)) == 0   # phase = Phi_6
    assert 5 * (-3) == -15


def _invariant_factors(M):
    from sympy.matrices.normalforms import smith_normal_form
    xm = x * sp.eye(M.shape[0]) - M
    snf = smith_normal_form(xm, domain=sp.QQ[x])
    return [sp.expand(sp.factor(snf[i, i])) for i in range(M.shape[0])]


def test_rational_block_split_and_nonderogatory():
    Bdiag = sp.Matrix(sp.BlockDiagMatrix(
        sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[0, 1], [-1, 1]])))
    inv = _invariant_factors(Mg)
    assert inv == _invariant_factors(Bdiag)            # Q-similar to the block sum
    chi = sp.expand(Mg.charpoly(x).as_expr())
    assert sp.expand(inv[-1] - chi) == 0               # min poly = char poly => nonderogatory


def _primitive_int_basis(Msub):
    cols = []
    for v in Msub.nullspace():
        v = sp.Matrix(v)
        dens = [sp.Rational(c).q for c in v]
        v = v * sp.ilcm(*dens) if len(dens) > 1 else v * dens[0]
        ints = [int(c) for c in v]
        g = sp.igcd(*ints) if len(ints) > 1 else abs(ints[0])
        if g:
            v = sp.Matrix([c // g for c in ints])
        cols.append(v)
    return cols


def test_glue_is_Z2squared_and_class_specific():
    Lp = _primitive_int_basis(Mg**2 - 3*Mg + sp.eye(4))
    Lg = _primitive_int_basis(Mg**2 - Mg + sp.eye(4))
    P = sp.Matrix.hstack(*(Lp + Lg))
    assert abs(P.det()) == 4                            # glue order 4
    from sympy.matrices.normalforms import smith_normal_form
    diag = [smith_normal_form(P, domain=sp.ZZ)[i, i] for i in range(4)]
    assert sorted(abs(d) for d in diag if abs(d) != 1) == [2, 2]   # (Z/2)^2
    # the block-diagonal form with the same charpoly has TRIVIAL glue
    Bdiag = sp.Matrix(sp.BlockDiagMatrix(
        sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[0, 1], [-1, 1]])))
    P0 = sp.Matrix.hstack(*(_primitive_int_basis(Bdiag**2 - 3*Bdiag + sp.eye(4))
                            + _primitive_int_basis(Bdiag**2 - Bdiag + sp.eye(4))))
    assert abs(P0.det()) == 1


def test_invariant_form_signature_1_3_disc_minus15():
    g = sp.symbols('g0:16')
    G = sp.Matrix(4, 4, lambda i, j: g[4*i + j])
    cons = [G[i, j] - G[j, i] for i in range(4) for j in range(i+1, 4)]
    cons += list(Mg.T * G * Mg - G)
    sol = sp.solve(cons, list(g), dict=True)[0]
    free = sorted({str(s) for v in sol.values() for s in v.free_symbols}, key=str)
    import itertools
    formG = None
    for vals in itertools.product([1, -1, 2, -2, 3, 0], repeat=min(len(free), 3)):
        Gc = G.subs(sol).subs({sp.Symbol(s): v for s, v in zip(free, vals)})
        Gc = sp.Matrix(Gc.subs({r: 1 for r in Gc.free_symbols}))
        if Gc == Gc.T and Gc.det() != 0:
            formG = Gc
            break
    assert formG is not None
    ev = formG.eigenvals()
    pos = sum(m for e, m in ev.items() if e.is_real and e > 0)
    neg = sum(m for e, m in ev.items() if e.is_real and e < 0)
    assert {pos, neg} == {1, 3}                          # signature (1,3)
    assert sp.sqrt(sp.nsimplify(formG.det() / sp.Integer(-15))).is_rational is True


def test_omega4_match_is_half_integer():
    a, m = sp.symbols('a m')
    am = sp.solve([sp.Eq(a, 4), sp.Eq(2*a - 2*m - 4, 5)], [a, m], dict=True)[0]
    assert am[a] == 4
    assert am[m] == sp.Rational(-1, 2)        # half-integer: bridge is the shared object, not a lattice pt
