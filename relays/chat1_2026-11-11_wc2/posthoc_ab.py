#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C2, POST HOC to w2_ab.py and posthoc_c3.py.  The web seat (chat1), 2026-11-11.  Seals no expectation.

  Q1  The eight bundles of the census on which A2' failed: for each, H^1(M; F_5)'s dimension, whether the monodromy is
      +-I modulo 5 (the lane's hypothesis "the golden eigenline has multiplicity one modulo 5" excludes that case), and
      what failed.
  Q2  The A4 count with each coordinate bounded by 3 in absolute value, (1/2)|h|^2 <= 12: whether it is 1020.
"""
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import w2_ab as w  # noqa: E402

EIGHT = ['b++LLLLLRRRRR', 'b++LLLRLRLLLRR', 'b++LLRLRLRLLRR', 'b++LLRRLRLRLRR', 'b++LLRRRLRLRRR', 'b++LLLLRLRRRRLR', 'b+-LLLRRLLRLLRR', 'b+-LLRRLRRLLRRR']


def main():
    print('Q1  the eight (post hoc)')
    for name in EIGHT:
        word = name[3:]
        sign = 1 if name[2] == '+' else -1
        m = w.mat(word, False)
        mm = tuple(tuple((sign * x) % 5 for x in row) for row in m)
        scalar = mm in (((1, 0), (0, 1)), ((4, 0), (0, 4)))
        M, dim, info = w.analyse(name)
        ok1, ok2 = w.check_a(name, info, dim)
        kinds = sorted(k for _, k, _, _, _ in info)
        print('    %-16s H_1 = %-12s dim H^1(F_5) = %d; monodromy +-I mod 5: %s; lines %d (%s); A1 %s, A2 %s'
              % (name, M.homology(), dim, scalar, len(info), ', '.join('%s %d' % (k, kinds.count(k)) for k in sorted(set(kinds))), ok1, ok2))
    print('Q2  the A4 count in a box (post hoc)')
    for b in (3, 4):
        n = sum(1 for h in itertools.product(range(-b, b + 1), repeat=5) if sum(h) == 0 and any(h) and sum(x * x for x in h) <= 24)
        print('    |h_i| <= %d, (1/2)|h|^2 <= 12: %d' % (b, n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
