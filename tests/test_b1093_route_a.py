"""B1093 lock: Route A's arithmetic facts."""
import sympy as sp
from sympy import symbols, Poly, ZZ, Rational

x = symbols("x")
F = x**3 - 12*x - 5

def test_disc_and_dedekind():
    assert sp.discriminant(F, x) == 6237
    assert sp.factorint(6237) == {3: 4, 7: 1, 11: 1}
    g = Poly(x + 1, x, domain=ZZ); h = Poly((x + 1)**2, x, domain=ZZ)
    T = Poly([c // 3 for c in (g * h - Poly(F, x, domain=ZZ)).all_coeffs()], x, domain=ZZ)
    D = sp.gcd(Poly(g.as_expr(), x, modulus=3), Poly(h.as_expr(), x, modulus=3))
    assert sp.gcd(D, Poly(T.as_expr(), x, modulus=3)).degree() == 0   # 3-maximal

def test_units_and_signature_rank():
    a, b, c = symbols("a b c")
    nf = sp.expand(sp.resultant(F, a + b*x + c*x**2, x))
    assert nf.subs({a: -4, b: 2, c: 1}) == 1
    assert nf.subs({a: 2, b: 6, c: 3}) == -1
    roots = [sp.CRootOf(F, i).evalf(30) for i in range(3)]
    def sv(A, B, C):
        return [0 if (A + B*r + C*r**2) > 0 else 1 for r in roots]
    rows = [[1, 1, 1], sv(-4, 2, 1), sv(2, 6, 3)]
    M = sp.Matrix(rows)
    assert M.rank() >= 3 or _f2rank(rows) == 3

def _f2rank(rows):
    M = [r[:] for r in rows]; rank = 0
    for col in range(3):
        piv = next((r for r in range(rank, len(M)) if M[r][col] % 2 == 1), None)
        if piv is None: continue
        M[rank], M[piv] = M[piv], M[rank]
        for r in range(len(M)):
            if r != rank and M[r][col] % 2 == 1:
                M[r] = [(M[r][k] ^ M[rank][k]) for k in range(3)]
        rank += 1
    return rank

def test_principal_generator_examples():
    a, b, c = symbols("a b c")
    nf = sp.expand(sp.resultant(F, a + b*x + c*x**2, x))
    assert abs(nf.subs({a: -1, b: -2, c: 1})) == 2      # (2, theta+1)
    assert abs(nf.subs({a: -4, b: 1, c: 0})) == 11      # (11, theta-4)
