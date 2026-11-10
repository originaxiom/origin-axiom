#!/usr/bin/env python3
"""
THE SEAT'S CHECKS AFTER THE REVIEW OF THE CLOSURE CARD, KEPT (data-free; post hoc; not a sealed card)
The web seat (chat1), 2026-11-10. Written and run after the referee's first report, to reproduce with the card's own
functions what that report found; committed after the second read asked that it be kept. Only the import path differs
from the scratch script. The card, its amendment and their outputs are unchanged.

What it checks:
 - the referee's two apex ties with no symmetry behind them: runs (1,3,1,3,4,3) and (2,2,1,3,3,1,1,3);
 - the integer form of the height, H_i = sqrt(tr^2 - 4)/(2 c_i), on five words;
 - (2,1,1,1,2) closed once is -I mod 5 and LLRLR does not keep LR's line;
 - LR itself is not single;
 - (2,1^8,2) closed by an even number of golden runs (k = 1, 2, 3) keeps its tie, by a reversal at an odd index;
 - the square of (6) closed once followed by the square of (6) closed three times is single;
 - how many of the card's 36 composites are +-I mod 5.

0 of 19.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import single_state_closure as m
import posthoc_three_factors as ph
import mpmath as mp

def show(r, tag):
    H = m.heights(r); info = m.apex_info(r); rot, rev = ph.symmetries(r)
    print(tag, r, 'letters', sum(r), 'apex', info['apex'], 'mult', info['multiplicity'], 'at', info['at_runs'],
          'runs there', info['run_lengths_at_apex'], 'exact-crit', info['equal_by_exact_criterion'], 'rot', rot, 'rev', rev)
    return H

# E1: the referee's two ties without a symmetry
H = show([1, 3, 1, 3, 4, 3], 'E1a'); print('   ', [mp.nstr(h, 30) for h in H])
H = show([2, 2, 1, 3, 3, 1, 1, 3], 'E1b'); print('   ', [mp.nstr(h, 30) for h in H])
w = m.word_of([2, 2, 1, 3, 3, 1, 1, 3]); print('   word', w, 'keeps line', m.keeps_line(m.mat(w)))

# the integer form: H_i = sqrt(tr^2 - 4) / (2 c_i)
def int_heights(r):
    n = len(r); out = []
    for i in range(n):
        # the word started at run i, the run's letter taken as the parabolic fixing infinity: T^a = [[1,a],[0,1]], then
        # alternate with its transpose
        M = (1, 0, 0, 1)
        for s in range(n):
            a = r[(i + s) % n]
            M = m.mul(M, (1, a, 0, 1) if s % 2 == 0 else (1, 0, a, 1))
        tr = M[0] + M[3]
        out.append((tr, M[2]))
    return out
for r in ([6, 1, 1, 1], [2, 1, 2, 1, 2, 1, 1, 1], [1, 3, 1, 3, 4, 3], [2, 2, 1, 3, 3, 1, 1, 3], [6, 1, 1, 1, 6, 1, 1, 1, 1, 1]):
    H = m.heights(r); ih = int_heights(r)
    print(r, 'max |H - sqrt(tr^2-4)/(2c)| =', mp.nstr(max(abs(h - mp.sqrt(mp.mpf(t) ** 2 - 4) / (2 * c)) for h, (t, c) in zip(H, ih)), 5), 'c:', [c for _, c in ih])

# (2,1,1,1,2) closed once: -I mod 5? does LLRLR keep v?
w = m.word_of([2, 1, 1, 1, 2, 1, 1, 1]); M = m.mat(w); print(w, [x % 5 for x in M], 'LLRLR keeps', m.keeps_line(m.mat('LLRLR')))
# LR itself
show([1, 1], 'LR')
# (2,1^8,2) with an even golden closure: the symmetry and the line
for k in (1, 2, 3):
    r = [2] + [1] * 8 + [2] + [1] * (2 * k)
    show(r, '(2,1^8,2) k=%d' % k)
# the referee's E3 example: the square of (6)_1 followed by the square of (6)_3
r = [6, 1, 1, 1] * 2 + [6] + [1] * 7 + [6] + [1] * 7
show(r, 'E3'); info = m.apex_info(r); print('   margin', info['gap_to_next'])
# how many of the 36 composites are +-I mod 5
F = m.FAMILY
S = {(n, k): m.runs_single(d, k) for n, d in F['departures'].items() for k in F['ks']}
cnt = 0; cnt_same = 0
for a, ra in S.items():
    for b, rb in S.items():
        M = [x % 5 for x in m.mat(m.word_of(ra + rb))]
        if M in ([1, 0, 0, 1], [4, 0, 0, 4]):
            cnt += 1
            if a[0] == b[0] and a != b: cnt_same += 1
print('composites +-I mod 5:', cnt, 'of 36; non-square same-departure among them:', cnt_same)
