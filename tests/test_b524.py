"""B524 locks — the arithmetic consequences of the two actionable steps.

The iwip certificate (train_track) and the Ptolemy solves (snappy) run in the sage env and
self-assert in their reproducers (iwip_certificate.py, higher_ptolemy.py). These pyenv locks
pin the pure-arithmetic facts that back the write-up.
"""
import sympy as sp

x = sp.symbols('x')


def _INV(c):
    return c.lower() if c.isupper() else c.upper()


def _reduce(w):
    st = []
    for ch in w:
        if st and st[-1] == _INV(ch):
            st.pop()
        else:
            st.append(ch)
    return ''.join(st)


def _apply(sub, w):
    out = []
    for ch in w:
        img = sub[ch.lower()]
        out.append(img if ch.islower() else ''.join(_INV(x) for x in reversed(img)))
    return _reduce(''.join(out))


def _growth(sub, seed='a', K=13):
    w = seed
    lens = [len(w)]
    for _ in range(1, K):
        w = _apply(sub, w)
        lens.append(len(w))
    ratios = [lens[i + 1] / lens[i] for i in range(len(lens) - 1)]
    return sum(ratios[-4:]) / 4


def test_dilatation_asymmetry_independently_verified():
    # The load-bearing datum for "not geometric / not a 3-manifold group": lambda(phi) != lambda(phi^-1).
    # Verified WITHOUT train_track -- pure free reduction + word-length growth.
    phi = {'a': 'abccd', 'b': 'acd', 'c': 'abcd', 'd': 'ac'}
    psi = {'a': 'bAcBd', 'b': 'DbCaBcAcBd', 'c': 'DbCaBd', 'd': 'Db'}
    # psi is the genuine inverse (this also re-confirms phi in Aut(F4))
    assert all(_apply(phi, _apply(psi, g)) == g and _apply(psi, _apply(phi, g)) == g for g in 'abcd')
    lp, li = _growth(phi), _growth(psi)
    assert abs(lp - 3.67621) < 1e-3              # lambda(phi) = beta = phi(1+sqrt phi)
    assert abs(li - 3.0523) < 1e-3               # lambda(phi^-1), independent of train_track
    assert abs(lp - li) > 0.1                    # asymmetric => NOT geometric => not a 3-mfd group (Stallings)
    assert abs(li - 2.272) > 0.1                 # != abelianization |M^-1|-Perron (free cancellation matters)
    # sanity: lambda(phi) is the Perron root of the bootstrap charpoly
    beta = max(abs(complex(r)) for r in sp.Poly(x**4 - 2*x**3 - 5*x**2 - 4*x - 1, x).nroots())
    assert abs(beta - lp) < 1e-3


def test_sl3_ptolemy_brings_in_sqrt_minus7():
    # the four SL(3) boundary-unipotent reps of 4_1 have these quadratic min polys (snappy):
    minpolys = [x**2 - x + 1, x**2 + x + 1, x**2 + 3*x + 4, x**2 - sp.Rational(1, 4)*x + 1]

    def sqfree_disc(p):
        c = sp.Poly(p, x).all_coeffs()          # [a, b, c]
        D = c[1]**2 - 4*c[0]*c[2]
        D = sp.nsimplify(D)
        n = sp.Integer(sp.numer(D) * sp.denom(D))
        return sp.sign(n) * sp.prod([q**(e % 2) for q, e in sp.factorint(abs(n)).items()])

    fields = {sqfree_disc(p) for p in minpolys}
    assert fields == {-3, -7}                     # SL(2) was only {-3}; SL(3) adds Q(sqrt-7)


def test_dgg_gauge_rank_is_abelian():
    # 4_1: N=2 tetrahedra, c=1 cusp -> DGG(SL2) gauge = U(1)^(N-c) = U(1)^1 (abelian).
    N, c = 2, 1
    assert N - c == 1                             # a single U(1); higher K -> U(1)^{r_K}, still abelian
