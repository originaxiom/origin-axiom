#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C2, POST HOC to w2_cd.py's cell C3, which did not reproduce on two counts.  The web seat (chat1), 2026-11-11.
It seals no expectation; each line is post hoc.

  P1  Rademacher's function.  w2_cd.py computed Phi(A) = (a + d)/c - 12 sign(c) s(a, |c|), which is not invariant
      under conjugation.  The function of a hyperbolic conjugacy class is Psi(A) = Phi(A) - 3 sign(c (a + d)) (Barge
      and Ghys), which for a positive word in L and R is the number of R's minus the number of L's (up to the sign of
      the convention).  Both are printed for the two words, with the letter counts, and for every rotation of each word
      (Psi must not change; Phi may).
  P2  The count 1020.  The number of nonzero vectors of the A4 lattice with (1/2)|h|^2 <= K, for K = 1..14; and with
      the bound read strictly; and the count up to sign; to see whether 1020 is one of them.
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from w2_cd import rademacher, matw  # noqa: E402


def psi(m):
    a, b = m[0]
    c, d = m[1]
    ph = rademacher(m)
    if c == 0:
        return ph
    sg = (1 if c * (a + d) > 0 else -1)
    return ph - 3 * sg


def main():
    print('P1  Rademacher (post hoc)')
    for w in ('LLLLLLRLR', 'LLLLLRLLRR'):
        rots = [w[i:] + w[:i] for i in range(len(w))]
        phis = [rademacher(matw(r)) for r in rots]
        psis = [psi(matw(r)) for r in rots]
        print('    %s: #L = %d, #R = %d; Phi over the rotations %s; Psi over the rotations %s'
              % (w, w.count('L'), w.count('R'), sorted({str(x) for x in phis}), sorted({str(x) for x in psis})))
    print('P2  the count of A4 vectors (post hoc)')
    norms = {}
    for h in itertools.product(range(-6, 7), repeat=5):
        if sum(h) == 0 and any(h):
            k = Fr(sum(x * x for x in h), 2)
            if k <= 14:
                norms[k] = norms.get(k, 0) + 1
    cum = 0
    for k in sorted(norms):
        cum += norms[k]
        print('    k = %s: %d vectors; cumulative %d; cumulative up to sign %d' % (k, norms[k], cum, cum // 2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
