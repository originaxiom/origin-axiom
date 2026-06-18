"""B174 -- the GL(2,Z) gluing-map landscape (H5; V168). Fast locks.

The cheap, decisive facts: the identity glue is a continuum for the same seed and the exact {-4,-2}
fork for (1,2) (B131); the swap glue forks the figure-eight to itself via p=f(f(p)), degree 16 (B134);
and the twist T forces a finite fork of size 9 via (2-p)(f(p)^2-(p+2))=0. The full landscape (heavier
resultants for ST/STS) lives in gluing_landscape.py.
"""
import sympy as sp

p, r = sp.symbols("p r")


def f(x):
    return x**4 - 5*x**2 + 2                       # fig-8 A-poly curve q = f(p) (B67)


def _apoly_relation(m):
    t = sp.Symbol("t")
    return {1: t**4 - 5*t**2 + 2, 2: t**2 - 6}[m]


def _identity_fork(m1, m2):
    t = sp.Symbol("t")
    diff = sp.expand(_apoly_relation(m1) - _apoly_relation(m2))
    if diff == 0:
        return "CONTINUUM"
    roots = sp.solve(diff, t)
    return {sp.nsimplify(sp.simplify(_apoly_relation(m2).subs(t, tr))) for tr in roots}


def test_identity_gluing_continuum_and_12_fork():
    assert _identity_fork(1, 1) == "CONTINUUM"            # same seed -> continuum (B131/K014)
    assert _identity_fork(1, 2) == {-4, -2}               # distinct seeds -> discrete (exact)


def test_swap_glue_is_degree16():
    cond = sp.expand(p - f(f(p)))                         # swap fig-8 self-glue: p = f(f(p)) (B134)
    assert sp.Poly(cond, p).degree() == 16
    assert not cond.has(r)


def test_twist_glue_fork_size_9():
    # T: (p,q,r)->(p,r,pr-q); curve requires r=f(p); with the r-quadratic on q=f(p):
    rquad = r**2 - p*f(p)*r + p**2 + f(p)**2 - 4
    cond = r - f(p)                                       # q' = r must equal f(p') = f(p)
    res = sp.factor(sp.resultant(sp.Poly(cond, r), sp.Poly(rquad, r), r))
    assert sp.Poly(sp.expand(res), p).degree() == 9      # (2-p)(f(p)^2-(p+2)) = 0
    # and it genuinely factors as p=2 plus a degree-8 piece
    assert sp.simplify(res - sp.expand((2 - p) * (f(p)**2 - (p + 2)))) == 0
