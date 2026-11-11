#!/usr/bin/env python3
"""
THE SEAT'S CHECKS AFTER THE REVIEW OF THE VALUE CARD, KEPT (data-free; post hoc; not a sealed card)
The web seat (chat1), 2026-11-11. Written and run after the referee's report, to reproduce with the closure card's own
functions what that report found. The sealed card and its output are unchanged.

What it checks:
 - the referee's pair with close own values, A = (2,1,1,4,4) and B = (2,1,2,4,4): their own values; that both keep
   LR's line when closed; and where the apex of "A closed by g periods, then B closed by g + 1" sits, for g = 1, 2, 4, 8;
 - the reading with one golden period on both sides: L^6 R L R and L^11 R L R against the own values;
 - that (6) closed by 1 then (6) closed by 2 reads below (6) closed by 1 alone;
 - the step ratios of the distance for two copies of (6), against phi^4.

0 of 19.
"""
import os
import sys

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'chat1_2026-11-10_closure'))
import single_state_closure as card  # noqa: E402

mp.mp.dps = 60
PHI = (1 + mp.sqrt(5)) / 2
A, B = [2, 1, 1, 4, 4], [2, 1, 2, 4, 4]


def own(dep):
    return max(card.heights(card.runs_single(dep, 60)))


def closed(dep, g):
    # a departure with an odd number of runs is closed by an odd number of golden runs
    return list(dep) + [1] * (2 * g + 1)


print('own values: A', mp.nstr(own(A), 10), ' B', mp.nstr(own(B), 10))
for name, dep in (('A', A), ('B', B)):
    w = card.word_of(closed(dep, 1))
    print(name, 'closed by 1 period keeps the line:', card.keeps_line(card.mat(w)))
for g in (1, 2, 4, 8):
    r = closed(A, g) + closed(B, g + 1)
    H = card.heights(r)
    i = max(range(len(r)), key=lambda j: H[j])
    where = 'A' if i < len(closed(A, g)) else 'B'
    bestA = max(H[:len(closed(A, g))])
    bestB = max(H[len(closed(A, g)):])
    print('A closed by', g, 'then B closed by', g + 1, ': apex', mp.nstr(H[i], 10), 'in', where,
          '| best of A', mp.nstr(bestA, 10), '| best of B', mp.nstr(bestB, 10),
          '| the composite keeps the line:', card.keeps_line(card.mat(card.word_of(r)))['column'])
for n in (6, 11):
    one = max(card.heights(closed([n], 1)))
    o = own([n])
    print('run of', n, 'with one period on both sides:', mp.nstr(one, 10), 'own', mp.nstr(o, 10),
          'off by', mp.nstr(100 * (one - o) / o, 4), 'percent')
h1 = max(card.heights(closed([6], 1)))
h12 = max(card.heights(closed([6], 1) + closed([6], 2)))
print('(6) closed by 1:', mp.nstr(h1, 10), '| (6) closed by 1 then by 2:', mp.nstr(h12, 10), '| below:', bool(h12 < h1))
d = []
for k in (1, 2, 3, 4, 5, 6):
    r = closed([6], k) + closed([6], k + 1)
    d.append(max(card.heights(r)) - own([6]))
print('step ratios of the distance, two copies of (6), k to k + 1:', [mp.nstr(d[i] / d[i + 1], 6) for i in range(5)],
      '| phi^4 =', mp.nstr(PHI ** 4, 6))
