#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
POST HOC, after the first check's output was read (loop_phase1_out.txt).  The web seat (chat1), 2026-11-11.
Data-free, integers.  It imports the first check's functions and changes nothing in it.  Three questions the
output raised; no expectation is sealed, and each answer is labelled post hoc.

  H1  The run of 6 with k = 1..8 golden periods: in each twisted sector, how many classes attain the least |Q| and
      where.  (The first check found the pattern changes with k.)
  H2  The same with the other twin taken as the mark, 2.v0 in place of v0.  (It should exchange the two sectors.)
  H3  The word the lane's sealed specification declares for (2,2,2), L^2 R^2 L^2 (L R)^k: its runs as a cyclic
      word; whether it keeps +-v0 with rows or with columns; whether it keeps any line of order 5 up to sign
      (the Smith invariants of M - I and M + I).  The same for L^2 R^2 L^2 R (L R)^k, which has the runs
      2, 2, 2 followed by ones.
"""
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from loop_phase1_check import word, rowact, smith, least_classes, position, frac_diff  # noqa: E402


def runs_cyclic(w):
    k = 0
    while k < len(w) and w[k] == w[0]:
        k += 1
    if k == len(w):
        return [len(w)]
    w = w[k:] + w[:k]
    out = []
    cur, n = w[0], 0
    for ch in w:
        if ch == cur:
            n += 1
        else:
            out.append(n)
            cur, n = ch, 1
    out.append(n)
    return out


def sectors(m, mark, box=60):
    un = least_classes(m, None, 1, box)
    s_apex = position(un[0][1][0], m)
    res_out = []
    for qc in (1, 2):
        res = set(((sg * qc * mark[0]) % 5, (sg * qc * mark[1]) % 5) for sg in (1, -1))
        tw = least_classes(m, res, 5, 5 * box)
        pos = sorted(frac_diff(position(r, m), s_apex) for r in tw[0][1])
        res_out.append((qc, tw[0][0], len(tw[0][1]), [mp.nstr(p, 6) for p in pos]))
    return res_out


def main():
    v0 = (1, 3)
    print('H1, H2  the run of 6: sectors by the number of golden periods k (post hoc)')
    for k in range(1, 9):
        m = word('LLLLLLR' + 'LR' * k)
        img = rowact(v0, m)
        sign = '+' if (img[0] % 5, img[1] % 5) == v0 else '-'
        a = sectors(m, v0)
        b = sectors(m, (2, 1))
        print('    k = %d  v0.M = %sv0   mark v0:   %s' % (k, sign, a))
        print('                        mark 2.v0: %s' % (b,))
    print()
    print('H3  the declared word for (2,2,2) (post hoc)')
    for label, dep in (("the specification's string L^2 R^2 L^2", 'LLRRLL'), ('L^2 R^2 L^2 R', 'LLRRLLR')):
        for k in (1, 2, 3):
            w = dep + 'LR' * k
            m = word(w)
            mt = ((m[0][0], m[1][0]), (m[0][1], m[1][1]))
            def keeps(mm):
                img = rowact(v0, mm)
                return (img[0] % 5, img[1] % 5) in ((1, 3), (4, 2))
            sm = smith(((m[0][0] - 1, m[0][1]), (m[1][0], m[1][1] - 1)))
            sp = smith(((m[0][0] + 1, m[0][1]), (m[1][0], m[1][1] + 1)))
            any5 = (sm[1] % 5 == 0) or (sp[1] % 5 == 0)
            print('    %s, k = %d: word %s  runs %s  trace %d  keeps +-v0 by rows: %s, by columns: %s;  M - I: %s  M + I: %s;  keeps some line of order 5 up to sign: %s'
                  % (label, k, w, runs_cyclic(w), m[0][0] + m[1][1], keeps(m), keeps(mt), sm, sp, any5))
    return 0


if __name__ == '__main__':
    sys.exit(main())
