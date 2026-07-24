"""FORWARD doubling-orbit of {phi,psi} mod p, tracked by irreducible minpolys / F_p.

Doubling correspondence: mu -> two children = roots of x^2 - 2 mu x + (mu^2 - mu^3).
The forward orbit O = union_n S_n  (S_0 = {phi,psi} = roots of x^2 - x - 1).
Child-transform of an irreducible q(mu):
    child_q(x) = Res_mu( q(mu),  x^2 - 2 mu x + mu^2 - mu^3 )  in F_p[x],
then factor into irreducibles = minpolys of the children.

If BFS closes (finite set of irreducibles), O is finite  =>  the eigenvalue
multiset dynamics is a fixed linear map on a finite index set  =>  e_n mod p
is eventually periodic.  Divisibility p | e_{n+1} <=> S_n contains a root of
g(mu)=mu^3-mu^2+2mu-1  <=> some irreducible factor of g lies in O.
"""
import sympy as sp
from sympy import Poly, symbols, resultant
from math import gcd

x, mu = symbols('x mu')

def child_irreducibles(q_coeffs, p):
    """q given as integer coeff list high->low (monic). Return list of child
    irreducible factors (each as tuple of coeffs high->low mod p, monic)."""
    qmu = Poly(sum(c*mu**i for i, c in enumerate(reversed(q_coeffs))), mu)  # over ZZ
    child = Poly(x**2 - 2*mu*x + mu**2 - mu**3, mu)  # poly in mu, ZZ coeffs (in x)
    R = resultant(qmu, child)          # integer poly in x
    Rp = Poly(R, x, modulus=p)
    if Rp.is_zero:
        return []
    _, facs = Rp.factor_list()
    out = []
    for fac, mult in facs:
        fm = fac.monic()
        out.append(tuple(int(c) % p for c in fm.all_coeffs()))
    return out

def forward_orbit(p, cap=3000):
    seed = Poly(x**2 - x - 1, x, modulus=p).monic()
    def key(coeffs): return tuple(coeffs)
    seed_facs = [tuple(int(c)%p for c in f.monic().all_coeffs())
                 for f,_ in seed.factor_list()[1]]
    known = set(seed_facs)
    frontier = list(seed_facs)
    order = list(seed_facs)
    while frontier:
        q = frontier.pop()
        for c in child_irreducibles([int(v) for v in q], p):
            if c not in known:
                known.add(c); frontier.append(c); order.append(c)
                if len(known) > cap:
                    return order, known, False
    return order, known, True

def g_factors(p):
    g = Poly(x**3 - x**2 + 2*x - 1, x, modulus=p)
    return [tuple(int(c)%p for c in f.monic().all_coeffs()) for f,_ in g.factor_list()[1]]

if __name__ == "__main__":
    for p in (5, 7):
        order, known, finite = forward_orbit(p)
        degs = sorted(len(c)-1 for c in known)
        D = 1
        for d in degs: D = D*d//gcd(D, d)
        gf = g_factors(p)
        hit = [f for f in gf if f in known]
        print(f"p={p}: forward-orbit finite={finite}  #distinct minpolys={len(known)}")
        print(f"   minpoly degrees in orbit: {degs}  (lcm field degree D={D})")
        print(f"   g factors mod {p}: {gf}")
        print(f"   g-roots IN forward orbit? {'YES -> p DIVIDES some e_n' if hit else 'NO -> p excluded'}  hits={hit}")
        print(f"   orbit minpolys: {sorted(known)}")
