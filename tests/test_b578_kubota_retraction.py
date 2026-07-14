"""B578-D5 lock -- exact, deterministic, sympy-only (~0.4s).

The Kubota-Leopoldt retraction + the 432*e3 identity. See
frontier/B578_debt_clearing/D5_KUBOTA_RETRACTION.md.
"""
from sympy import Matrix, Poly, Rational as R, bernoulli as bern, div, symbols

x = symbols('x')
Phi9 = Poly(x**6 + x**3 + 1, x, domain='QQ')


def red(p):
    if not isinstance(p, Poly):
        p = Poly(p, x, domain='QQ')
    _, r = div(p, Phi9, domain='QQ')
    return r


def add(*ps):
    out = Poly(0, x, domain='QQ')
    for p in ps:
        out = red(out + (p if isinstance(p, Poly) else Poly(p, x, domain='QQ')))
    return out


def mul(a, b):
    return red((a if isinstance(a, Poly) else Poly(a, x, domain='QQ')) *
               (b if isinstance(b, Poly) else Poly(b, x, domain='QQ')))


def scal(c, p):
    return red(Poly(c, x, domain='QQ') * (p if isinstance(p, Poly) else Poly(p, x, domain='QQ')))


def zp(k):
    return Poly(x**(k % 9), x, domain='QQ')


def vec(p):
    p = red(p)
    c = p.all_coeffs()[::-1]
    c = list(c) + [0] * (6 - len(c))
    return [R(v) for v in c[:6]]


def test_kubota_retraction_and_432e3():
    ms = [1, 2, 4]
    c = [add(zp(m), zp(-m)) for m in ms]
    zeta3 = zp(3)

    def Lchi(j):
        total = Poly(0, x, domain='QQ')
        for idx in range(3):
            w = Poly(1, x, domain='QQ')
            for _ in range((j * idx) % 3):
                w = mul(w, zeta3)
            total = add(total, mul(w, add(Poly(1, x, domain='QQ'), c[idx])))
        return scal(R(1, 12), total)

    L0, L1, L2 = Lchi(0), Lchi(1), Lchi(2)
    assert L0 == Poly(R(1, 4), x, domain='QQ')
    L1_12, L2_12 = scal(12, L1), scal(12, L2)
    assert L1_12 == Poly(3 * x, x, domain='QQ')                    # = tau(chi), exact
    assert L2_12 == Poly(-3 * x**5 - 3 * x**2, x, domain='QQ')     # = conj tau(chi)

    powers = {}
    gk = 1
    for k in range(6):
        powers[gk % 9] = k
        gk = (gk * 2) % 9

    def chi_of(a):
        a = a % 9
        if a == 0 or a not in powers:
            return None
        w = Poly(1, x, domain='QQ')
        for _ in range(powers[a] % 3):
            w = mul(w, zeta3)
        return w

    def gen_bernoulli(n):
        tot = Poly(0, x, domain='QQ')
        for a in range(1, 10):
            cv = chi_of(a % 9)
            if cv is None:
                continue
            tot = add(tot, scal(bern(n, R(a, 9)), cv))
        return scal(R(9)**(n - 1), tot)

    assert gen_bernoulli(1) == Poly(0, x, domain='QQ')             # chi even
    B2chi = gen_bernoulli(2)
    assert B2chi == Poly(R(4, 3) * x**3 + R(8, 3), x, domain='QQ')  # cross-checked vs Sage
    assert chi_of(3) is None                                        # KL Euler factor = 1
    L3m1 = scal(R(-1, 2), B2chi)
    co = B2chi.all_coeffs()[::-1]
    co = list(co) + [0] * (6 - len(co))
    assert all(co[i] == 0 for i in range(6) if i % 3 != 0)          # lives in Q(zeta3)

    def conj(p):
        coeffs = p.all_coeffs()[::-1]
        out = Poly(0, x, domain='QQ')
        for i, cf in enumerate(coeffs):
            if cf != 0:
                out = add(out, scal(cf, zp(-i)))
        return out

    assert mul(L1_12, conj(L1_12)) == Poly(9, x, domain='QQ')        # |tau|^2 = 9
    assert mul(B2chi, conj(B2chi)) == Poly(R(16, 3), x, domain='QQ')  # 16/3 != 9
    M = Matrix([vec(Poly(1, x, domain='QQ')), vec(L1_12), vec(L2_12), vec(L3m1)])
    assert M.rank() == 4          # KL value Q-independent of the Gauss sums: RETRACTION

    e3_numerator = add(zp(1), zp(-1))                                # = 1728*e3
    assert red(scal(4, add(L1, L2)) - e3_numerator) == Poly(0, x, domain='QQ')  # L1+L2 = 432*e3
