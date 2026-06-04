"""B69 extension: cusp polynomial = leading-z coefficient of the fixed-locus polynomial P(x,z)
(the ideal points / cusps are where z -> infinity). No solve/groebner -> fast. Verify cusp-torsion
law (cusps at x=2cos(pi/k)) for m=1..6, extending the chat's m<=4."""
import sympy as sp
x, y, z = sp.symbols("x y z")


def pseq(m, X, Y, Z):
    p = [Y, Z]
    for _ in range(2, m + 2):
        p.append(sp.expand(X * p[-1] - p[-2]))
    return p


def Tm(m, v):
    X, Y, Z = v; p = pseq(m, X, Y, Z); return (p[m], X, p[m + 1])


def cusp_poly(m):
    F = Tm(m, Tm(m, (x, y, z)))                 # T_m^2
    yb = sp.solve(sp.Eq(pseq(m, x, y, z)[m], y), y)[0]   # branch y=f(x,z) (linear in y)
    P = sp.numer(sp.together(sp.expand((F[0] - x).subs(y, yb))))   # fixed-locus poly in (x,z)
    Pz = sp.Poly(sp.expand(P), z)
    return sp.factor(Pz.LC())                    # leading-z coefficient = cusp polynomial


tor = {k: sp.nsimplify(2 * sp.cos(sp.pi / k)) for k in range(3, 11)}
minpoly = {k: sp.minimal_polynomial(2 * sp.cos(sp.pi / k), x) for k in range(3, 11)}


def kset(poly):
    """which 2cos(pi/k) appear as roots (via min-poly divisibility)."""
    ks = []
    P = sp.Poly(sp.expand(poly), x)
    for k in range(3, 11):
        if sp.rem(P, sp.Poly(minpoly[k], x)) == 0 or sp.gcd(P, sp.Poly(minpoly[k], x)).degree() >= 1:
            ks.append(k)
    return sorted(set(ks))


pred = {1: [3], 2: [4], 3: [3, 5], 4: [4, 6], 5: [3, 5, 7], 6: [4, 6, 8]}
for m in range(1, 7):
    cp = cusp_poly(m)
    ks = kset(cp)
    ok = ks == pred[m]
    print(f"m={m}: cusp poly = {cp}")
    print(f"      k-set = {ks}   predicted {pred[m]}   {'OK' if ok else 'MISMATCH'}")
