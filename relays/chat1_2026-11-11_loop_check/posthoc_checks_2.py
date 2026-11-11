#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
POST HOC 2, after the referee's first read of the relay on this check.  The web seat (chat1), 2026-11-11.
Data-free, integers.  It imports the first check's functions, changes nothing in it and seals no expectation.
The referee found two things the seat had not looked at; this file lets the seat's own code say them.

  K1  The word the lane's sealed specification declares for the history it calls (2,1^8,2):
      L^2 (R L)^4 R L^2 R (L R)^k.  Its cyclic runs; whether it keeps +-v0 by rows and by columns; the Smith
      invariants of M - I and M + I.  The same for L^2 (R L)^4 R^2 (L R)^k, whose two runs of 2 are an L-run
      and an R-run, as the record's B1857 has that history.
  K2  The reversal of the run of 6 in integers: g = rows (1, 0), (6, -1).  Whether g M g^-1 = M^-1 for
      M = L^6 R (L R)^k, k = 1, 2, 3; det g; g.g; and v0.g modulo 5.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from loop_phase1_check import word, rowact, smith, mul, inv  # noqa: E402
from posthoc_checks import runs_cyclic  # noqa: E402


def main():
    v0 = (1, 3)
    print('K1  the declared word for (2,1^8,2) (post hoc)')
    for label, dep in (("the specification's string", 'LL' + 'RL' * 4 + 'R' + 'LL' + 'R'), ('L^2 (R L)^4 R^2', 'LL' + 'RL' * 4 + 'RR')):
        for k in (1, 2, 3):
            w = dep + 'LR' * k
            m = word(w)
            mt = ((m[0][0], m[1][0]), (m[0][1], m[1][1]))

            def keeps(mm):
                img = rowact(v0, mm)
                return (img[0] % 5, img[1] % 5) in ((1, 3), (4, 2))
            sm = smith(((m[0][0] - 1, m[0][1]), (m[1][0], m[1][1] - 1)))
            sp = smith(((m[0][0] + 1, m[0][1]), (m[1][0], m[1][1] + 1)))
            print('    %s, k = %d: word %s  runs %s  trace %d  keeps +-v0 by rows: %s, by columns: %s;  M - I: %s  M + I: %s'
                  % (label, k, w, runs_cyclic(w), m[0][0] + m[1][1], keeps(m), keeps(mt), sm, sp))
    print()
    print('K2  the reversal of the run of 6 (post hoc)')
    g = ((1, 0), (6, -1))
    det_g = g[0][0] * g[1][1] - g[0][1] * g[1][0]
    gg = mul(g, g)
    ginv = ((g[1][1] * det_g, -g[0][1] * det_g), (-g[1][0] * det_g, g[0][0] * det_g))
    img = rowact(v0, g)
    print('    det g = %d;  g.g = %s;  v0.g modulo 5 = %s' % (det_g, gg, (img[0] % 5, img[1] % 5)))
    for k in (1, 2, 3):
        m = word('LLLLLLR' + 'LR' * k)
        conj = mul(mul(g, m), ginv)
        print('    k = %d: g M g^-1 = M^-1: %s' % (k, conj == inv(m)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
