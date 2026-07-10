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


def test_forcing_theorem_exhaustive_uv():
    # the (u,v) Pisot box is exhaustive; unique irreducible quartic Pisot unit is (1,2)=F^3
    t, u, v = sp.symbols('t u v')
    chi = ((t*sp.eye(2) - F)**2 - (u*sp.eye(2) + v*F)).det()
    hits = []
    for uu in range(0, 9):
        for vv in range(0, 7):
            q = sp.Poly(sp.expand(chi.subs({u: uu, v: vv})), t)
            if not q.is_irreducible or abs(q.as_expr().subs(t, 0)) != 1:
                continue
            mags = sorted(abs(complex(sp.N(r, 15))) for r in q.all_roots())
            if mags[-1] > 1.0001 and all(m < 0.9999 for m in mags[:-1]):
                hits.append((uu, vv))
    assert hits == [(1, 2)]


def test_perron_nesting():
    phi = (1 + sp.sqrt(5))/2; sq = sp.sqrt(phi); beta = phi*(1 + sq)
    Ms = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])
    v = sp.Matrix([phi, 1, phi*sq, sq])
    assert sp.simplify(Ms*v - beta*v) == sp.zeros(4, 1)


def test_oneway_coupling_reducible():
    # grounding for assumption (3): an identity cross-channel (one-way) bootstrap is reducible
    Mtri = sp.Matrix(sp.BlockMatrix([[F, F], [sp.zeros(2), F]]))
    cp = sp.factor(Mtri.charpoly(x).as_expr())
    assert cp == (x**2 - x - 1)**2   # reducible: two separate Fibonacci copies, not a new object


def test_reading_double_uniquely_coherent():
    # among candidate 'self-reference' readings, only the coupled double is new(irreducible)+coherent(Pisot)
    def new_and_coherent(M):
        cp = M.charpoly(x).as_expr()
        irred = sp.Poly(cp, x).is_irreducible
        mags = sorted(abs(complex(sp.N(r, 15))) for r in sp.Poly(cp, x).all_roots())
        pis = mags[-1] > 1.0001 and all(m < 0.9999 for m in mags[:-1])
        return irred and pis
    tensor = sp.Matrix(sp.kronecker_product(F, F))
    summ = sp.Matrix(sp.BlockMatrix([[F, sp.zeros(2)], [sp.zeros(2), F]]))
    double = sp.Matrix(sp.BlockMatrix([[F, F], [F**2, F]]))
    assert not new_and_coherent(tensor)      # reducible
    assert not new_and_coherent(summ)        # reducible
    assert new_and_coherent(double)          # the unique new coherent object


def test_lorentzian_signature_is_generic():
    # trace-form signature (r1+r2, r2): golden beta AND controls all give (3,1) => generic, not object-forced
    def sig(poly):
        K = sp.Poly(poly, x); n = K.degree()
        roots = K.all_roots()
        r1 = sum(1 for r in roots if abs(complex(sp.N(r, 25)).imag) < 1e-12)
        return (r1 + (n - r1)//2, (n - r1)//2)
    assert sig(x**4 - 2*x**3 - 5*x**2 - 4*x - 1) == (3, 1)   # golden beta: Lorentzian
    assert sig(x**4 - x - 1) == (3, 1)                        # child field -283: ALSO (3,1) => generic
    assert sig(x**4 - x**3 - x**2 - x - 1) == (3, 1)          # tetranacci: ALSO (3,1) => generic
    assert sig(x**4 - 4*x**2 + 1) == (4, 0)                   # totally real => Euclidean (splitting-type dependent)
    assert sig(x**4 + 1) == (2, 2)                            # totally complex => (2,2); so (3,1) is the (2,1)-class, generic
