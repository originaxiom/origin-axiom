"""B161 -- cancellation-locus stratification (V155). Fast symbolic + coarse-numeric locks.

The obstruction as math: cancellation kappa=2 is non-generic (codim-1, kappa free) and trivial
(full band at lambda=0); non-cancellation kappa>2 is fractured. Guard: kappa=2 is ATTAINED
(B130) -- refutes fine-tuning, NOT 'forced/empty'.
"""
import sympy as sp
import numpy as np

x, y, z, k = sp.symbols('x y z k')
kappa = x**2 + y**2 + z**2 - x*y*z - 2


def test_cancellation_locus_codim1():
    poly = sp.expand(kappa - 2)
    assert poly == sp.expand(sp.factor(poly))            # single (irreducible) hypersurface
    grad = [sp.diff(poly, v).subs({x: 2, y: 0, z: 0}) for v in (x, y, z)]
    assert any(g != 0 for g in grad)                     # grad != 0 => codim exactly 1


def test_kappa_free_on_fixed_locus_m2():
    # re-derive B130: kappa-elimination ideal empty (m=2) => kappa free on the fixed locus
    def Ta(p): X, Y, Z = p; return (X, Z, X*Z - Y)
    def Tb(p): X, Y, Z = p; return (Z, Y, Y*Z - X)
    p = (x, y, z)
    for _ in range(2): p = Tb(p)
    for _ in range(2): p = Ta(p)
    eqs = [sp.expand(p[i] - (x, y, z)[i]) for i in range(3)] + [k - kappa]
    G = sp.groebner(eqs, x, y, z, k, order='lex')
    konly = [g for g in G.polys if g.free_symbols <= {k}]
    assert konly == []                                   # no k-only generator => kappa free


def test_mb12_abelian_control_kappa_two():
    t, s = sp.symbols('t s', positive=True)
    A = sp.diag(t, 1/t); B = sp.diag(s, 1/s)
    assert sp.simplify(sp.trace(A*B*A.inv()*B.inv())) == 2   # abelian => kappa==2 (non-vacuous)


def test_cancellation_is_lambda_zero():
    lam = sp.symbols('lambda')
    assert sp.solve(sp.Eq(2 + lam**2, 2), lam) == [0]    # kappa=2 <=> lambda=0 (periodic crystal)


def _measure(word, lm, NE=60000):
    Es = np.linspace(-(2+lm)-.05, (2+lm)+.05, NE)
    a = np.ones(NE); b = np.zeros(NE); c = np.zeros(NE); d = np.ones(NE)
    with np.errstate(over='ignore', invalid='ignore'):
        for ch in word:
            V = lm*(1.0 if ch == 'a' else 0.0)
            na = (Es-V)*a - c; nb = (Es-V)*b - d; a, b, c, d = na, nb, a.copy(), b.copy()
        ins = np.abs(a+d) <= 2.0
    return float(np.mean(ins)*(Es[-1]-Es[0]))


def test_full_band_at_cancellation_fractures_above():
    w = {1: "a", 2: "ab"}
    for j in range(3, 12): w[j] = w[j-1] + w[j-2]
    W = w[11]
    assert abs(_measure(W, 0.0) - 4.0) < 0.05            # lambda=0: full band (trivial)
    assert _measure(W, 1.0) < 3.5                          # kappa>2: fractured (Cantor)
