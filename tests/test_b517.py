"""B517 locks — the intertwining theorem + golden-specificity of the canonical coupling."""
import sympy as sp
x = sp.symbols('x')
F = sp.Matrix([[1, 1], [1, 0]])
GOLD = x**4 - 2*x**3 - 5*x**2 - 4*x - 1


def test_commutant_is_ZF():
    a, b, c, d = sp.symbols('a b c d')
    G = sp.Matrix([[a, b], [c, d]])
    sol = sp.solve([e for e in (F*G - G*F)], [a, b, c, d], dict=True)[0]
    # forced a=c+d, b=c  => G = d*I + c*F  (span{I,F})
    assert sol[a] == c + d and sol[b] == c


def test_CD_equals_Fcubed_gives_golden():
    M = (F - x*sp.eye(2))**2 - F**3
    assert sp.expand(M.det() - GOLD) == 0


def test_unique_factorization_FF2():
    I = sp.eye(2); F3 = F**3
    sols = []
    for av in range(3):
        for bv in range(3):
            for cv in range(3):
                for dv in range(3):
                    C = av*I + bv*F; D = cv*I + dv*F
                    if C == I or D == I:
                        continue
                    if C*D == F3:
                        sols.append((C == F, D == F**2, C == F**2, D == F))
    # only (F,F^2) and (F^2,F)
    assert all((s[0] and s[1]) or (s[2] and s[3]) for s in sols) and len(sols) == 2


def test_canonical_coupling_golden_specific():
    def pisot(m):
        S = sp.Matrix([[m, 1], [1, 0]])
        M = sp.Matrix(sp.BlockMatrix([[S, S], [S**2, S]]))
        mags = sorted(abs(complex(sp.N(r, 18))) for r in sp.Poly(M.charpoly(x).as_expr(), x).all_roots())
        return mags[-1] > 1.0001 and all(v < 0.9999 for v in mags[:-1])
    assert pisot(1) and not pisot(2) and not pisot(3)


def test_forcing_unique_pisot_bootstrap():
    # among F-equivariant two-way bootstraps (entries {0,1,2}), the ONLY Pisot irreducible
    # quartic is the golden one
    F2 = sp.Matrix([[1, 1], [1, 0]]); I2 = sp.eye(2)
    polys = set()
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    C = a*I2 + b*F2; D = c*I2 + d*F2
                    if C in (sp.zeros(2), I2) or D in (sp.zeros(2), I2):
                        continue
                    M = sp.Matrix(sp.BlockMatrix([[F2, C], [D, F2]]))
                    cp = M.charpoly(x).as_expr()
                    if not sp.Poly(cp, x).is_irreducible:
                        continue
                    mags = sorted(abs(complex(sp.N(r, 16))) for r in sp.Poly(cp, x).all_roots())
                    if mags[-1] > 1.0001 and all(v < 0.9999 for v in mags[:-1]):
                        polys.add(sp.expand(cp))
    assert polys == {sp.expand(GOLD)}
