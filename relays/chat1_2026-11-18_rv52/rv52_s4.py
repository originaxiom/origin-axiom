#!/usr/bin/env python3
"""The status page's section 13, on W-A2's line 114. Data-free. Computed once.

    python3 -I -u rv52_s4.py

Two facts the section uses, checked by coset enumeration and by brute force:
  1. PSL(2, Z) = <S, R | S^2, R^3> with T = S R; adding T^4 = 1 gives a group of order 24 (the (2, 3, 4) triangle
     group), and it is S_4: it acts faithfully on its 4 cosets of a subgroup of order 6... checked here by taking the
     permutation images of S and R on the cosets of <R> and computing the order of the group they generate.
  2. Of S_4's quotients (by 1, V_4, A_4, S_4), only S_4 itself keeps an element of order 4: the image of a 4-cycle has
     order 2 modulo V_4, and order 1 or 2 in the smaller quotients.
"""
from itertools import permutations

from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.combinatorics import Permutation

F, s, r = free_group("s r")
G = FpGroup(F, [s**2, r**3, (s*r)**4])
print("order of <S, R | S^2, R^3, (SR)^4>:", G.order())
C = G.coset_enumeration([r])
C.compress(); C.standardize()
tab = C.table                                      # columns: s, s^-1, r, r^-1
ps = Permutation([row[0] for row in tab]); pr = Permutation([row[2] for row in tab])
P = PermutationGroup([ps, pr])
print("action on the %d cosets of <R>: a group of order %d (S_4 has 24): %s" % (len(tab), P.order(), P.order() == 24))
print("order of the image of T = SR there: %d" % (ps * pr).order())
# 2: S_4 modulo V_4
S4 = list(permutations(range(4)))
comp = lambda p, q: tuple(p[q[i]] for i in range(4))
V4 = {(0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)}
c4 = (1, 2, 3, 0); x = c4; k = 1
while x not in V4:
    x = comp(c4, x); k += 1
print("a 4-cycle's order modulo V_4: %d (in S_4 it is 4)" % k)
