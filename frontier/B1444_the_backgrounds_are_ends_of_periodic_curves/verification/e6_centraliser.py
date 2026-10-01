#!/usr/bin/env python3
"""The centraliser of the Standard Model's gauge algebra in E6, on the root system.
E6 roots in the standard model inside E8 coordinates (8-dim, orthogonal to two vectors).  SU(5) is taken as an A4,
su(3) + su(2)_L inside it, Y the Cartan direction of A4 orthogonal to both.  A root of E6 lies in the centraliser of
su(3) + su(2) + u(1)_Y exactly when it is orthogonal to the roots of su(3), su(2) and to Y."""
import itertools
from fractions import Fraction as Fr
def e8_roots():
    R = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); R.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0: R.append(tuple(Fr(s, 2) for s in signs))
    return R
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
E8 = e8_roots(); assert len(E8) == 240
# E6 = roots orthogonal to an A2 of E8:  a1 = e7 - e8,  a2 = (1/2)(1,1,1,1,1,1,-1,-1)... take a1 = (0,..,1,-1), a2 = half(-1,-1,-1,-1,-1,-1,-1,... ) chosen with a1.a2 = -1
a1 = tuple([Fr(0)] * 6 + [Fr(1), Fr(-1)]); a2 = tuple([Fr(1, 2)] * 5 + [Fr(-1, 2), Fr(-1, 2), Fr(1, 2)])
assert a2 in E8 and dot(a1, a2) == -1
E6 = [r for r in E8 if dot(r, a1) == 0 and dot(r, a2) == 0]; assert len(E6) == 72, len(E6)
# an A4 (su(5)) inside E6: simple roots e1-e2, e2-e3, e3-e4, e4-e5
e = lambda i, j: tuple(Fr((k == i) - (k == j)) for k in range(8))
A4 = [e(0, 1), e(1, 2), e(2, 3), e(3, 4)]; assert all(r in E6 for r in A4)
su3 = [e(0, 1), e(1, 2)]; su2 = [e(3, 4)]
# Y in the span of A4's simple roots, orthogonal to su3 and su2:  diag(-2,-2,-2,3,3) on the five coordinates
Y = tuple([Fr(-2)] * 3 + [Fr(3)] * 2 + [Fr(0)] * 3)
assert all(dot(Y, r) == 0 for r in su3 + su2)
sm_roots = [r for r in E6 if all(r[k] == 0 for k in range(5, 8)) and sum(r[:5]) == 0 and ((r[3] == 0 and r[4] == 0) or (r[0] == r[1] == r[2] == 0))]
assert len(sm_roots) == 6 + 2
cent = [r for r in E6 if all(dot(r, s) == 0 for s in sm_roots) and dot(r, Y) == 0]
print("roots of E6 in the centraliser of su(3) + su(2)_L + u(1)_Y:", len(cent), cent)
beta = cent[0]
com = [r for r in E6 if dot(r, beta) == 0]
print("roots of E6 orthogonal to beta (the centraliser of su(2)_beta):", len(com), " -> su(6) has 30")
print("all Standard-Model roots commute with beta:", all(dot(r, beta) == 0 for r in sm_roots), "; Y orthogonal to beta:", dot(Y, beta) == 0)
# the SU(5) roots too?
su5 = [r for r in E6 if all(r[k] == 0 for k in range(5, 8)) and sum(r[:5]) == 0]
print("su(5) roots:", len(su5), "all orthogonal to beta:", all(dot(r, beta) == 0 for r in su5))
print("dimension of the centraliser: %d roots + rank 6 - 3 = %d" % (len(cent), len(cent) + 3))
