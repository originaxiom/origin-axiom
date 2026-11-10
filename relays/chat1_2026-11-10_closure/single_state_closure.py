#!/usr/bin/env python3
"""
IS "A SINGLE STATE" CLOSED UNDER COMPOSITION?
The web seat (chat1), 2026-11-10, at the owner's choice on fork 2 of the A-all relay (a711bd189): "Test closure first".
Data-free. This header is the sealed rule: it was committed, with this script's sha256, before any run on the card's
family. Before the seal the functions were exercised once on two unrelated departures, (3) and (3,1,3), to see that the
code runs; that output is not kept and nothing of the family was computed.

THE QUESTION. Under the joint action, "all allowed histories together" holds every composite of allowed histories
(a711bd189, section 3). The advisor seat's design of back-edge A allows a history only if its lightest state is single:
"one state, one place". Is that condition closed under composition: if W1 and W2 are single, is W1 W2?

KIND. A weave question: it is about a condition on all allowed histories at once. The instrument is the record's own
and is a thread instrument on a chosen clock: B1857's flat-fibre (Sol) model, where "the lightest state sits at the
deepest class (the apex)" and "it is unique if and only if the deepest run is unique" (B1857; the record counts that
clock as CHOSEN, B1815). Nothing is computed on the hyperbolic metric; H1 and H2 say what symmetry alone gives there.
No coupling, no frame output, no data. No value of tau is read: the heights below are the instrument's own.

THE INSTRUMENT (B1857's criterion, in exact form).
 - A history is a closed positive word, written by its runs r_1 ... r_n (n even; the letters alternate, L first).
   Its matrix is W. The golden background has every run equal to 1.
 - The height of run i is H_i = (r_i + x_i + y_i)/2, with x_i = [0; r_(i+1), r_(i+2), ...] read forward round the
   cycle and y_i = [0; r_(i-1), r_(i-2), ...] read backward. The apex is the greatest H_i.
 - The history is SINGLE when the apex is attained by exactly one run in one period of the word as written. A word
   written twice is read over its whole length.
 - Heights are computed at 60 digits (300 continued-fraction terms). Two heights count as equal when they differ by
   less than 1e-45. Equality is also decided exactly: H_i = H_j whenever r_i = r_j and the forward and backward run
   sequences at i equal those at j, in the same order or exchanged.

THE FAMILY (fixed now).
 - The single histories: the departures (6) and (2,1,2,1,2), each closed by k golden periods, k = 1, 2, 3. As runs:
   [6] + [1]*(2k + 1) and [2,1,2,1,2] + [1]*(2k + 1); as words L^6 R (LR)^k and (L^2 R)^3 (LR)^k. These are B1857's
   two departures with a unique apex, and the design's own examples.
 - The composites: W1 W2 for every ordered pair of the six, 36 in all, the six squares among them.
 - The generators: the four histories of a711bd189's fact F8, L^6 R (LR)^k and L R^6 (LR)^k for k = 1, 2, which
   generate, as a group, the stabiliser of the marked line up to sign in PSL(2, Z).

HAND WORK BEFORE THIS CARD (disclosed).
 H0 Heights by hand in a long golden background: (6) gives (6 + 1/phi + 1/phi)/2 = 3 + 1/phi = 3.618034, B1857's
    apex; the middle 2 of (2,1,2,1,2) gives 1.7236 and each 2 of (2,1,1,1,2) gives 1.6254, both B1857's.
 H1 Powers. The bundle of W^n is an n-fold cyclic cover of the bundle of W. Its deck move is an isometry of order n,
    for the flat-fibre metric by construction and for the hyperbolic metric of the punctured-torus bundle by rigidity
    (Mostow, Prasad). It carries each fibre one period on and acts on the fibre by W, so it keeps a line W keeps up
    to sign. An operator built from the metric and that line commutes with it (up to complex conjugation when the
    sign is minus), so the density of each eigenspace is invariant under it, whatever the eigenspace's dimension.
    The profile along the base then repeats n times and has no mode carrying more than 1/n of the total. So W^n is
    not single for n >= 2, in either metric, for any share of one half or more. [theorem, given a lowest state]
 H2 Two copies of one palindromic departure, with different golden gaps between them. The cyclic word has exactly one
    reversal; it exchanges the two copies and fixes the centres of the two gaps. Reading a word backward is
    conjugation of W^-1 by g0 = diag(1, -1), so the reversal is a g in GL(2, Z) with det g = -1 and
    g W^-1 g^-1 = W: a map of the bundle that reverses the fibre and the base and keeps the 3-manifold's orientation,
    hence an isometry up to homotopy in either metric. Mod 5, by hand: (L^2 R)^3 = I, so every word of the family
    is a power of LR mod 5 and keeps LR's line v = (1, 3); g is C g0 with C = (LR)^(k1+1) L for (6) and
    C = (LR)^k1 R^-1 for (2,1,2,1,2); in both cases g v = +-v and v^T g = +-v^T. So g keeps the line and the density
    of each eigenspace is invariant under it. The profile is then symmetric about the gap centres: whatever sits at
    one departure sits equally at the other. In the flat-fibre model the state sits at the apex, which is at the
    departures, so there are two places. On the hyperbolic metric the same symmetry forbids one place at a departure;
    it does not forbid one place at the centre of a golden gap, and where the state sits there is open (P-744).
    B1733's census agrees in kind: over its classes, every symmetry g with e det g = +1 fixes the pair of lines.
 H3 Two different departures. No symmetry exchanges them. In the flat-fibre model the deeper run is the apex alone
    (C3). On the hyperbolic metric nothing is proved here.

CELLS, PREDICTIONS, PRIORS (pass rules).
 C0 The instrument against the record. With a long golden background (k = 40), the departures (6), (2,1,2,1,2),
    (2,1,1,1,2) and (2,1^8,2) have apex heights within 1e-6 of B1857's 3.618034, 1.723607, 1.625437 and 1.617974,
    with multiplicities 1, 1, 2 and 2. 95%.
 C1 The six single histories each have a unique apex, and each keeps the line: W v = +-v and v^T W = +-v^T mod 5.
    97%.
 C2 All 18 composites of two histories with the same departure, squares included: the apex is attained exactly
    twice, and the two heights are equal by the exact criterion. So none is single. 97%.
 C3 All 18 composites of two histories with different departures: the apex is unique, at the run of 6, and exceeds
    every other height by more than 1. So each is single. 97%.
 C4 For each of the 18 same-departure composites there is a symmetry of the cyclic word that exchanges the two
    departures: for a square, the rotation by half the word; otherwise a reversal, with g in GL(2, Z), det g = -1,
    g W^-1 g^-1 = W in integers, and g v = +-v and v^T g = +-v^T mod 5. 93%.
 C5 The four generators each have a unique apex. 97%.

WHAT THE OUTCOMES MEAN (fixed now).
 - C2 holds: in the record's own instrument "a single state" is not closed under composition. Two single histories
   with the same deepest run compose to a history whose apex sits in two places. By H1 and H2 the same holds on the
   hyperbolic metric for powers, and for the other same-departure composites unless the state leaves the
   departures. So the single histories are not the histories of any subweave.
 - C5 holds as well: the subweave the single histories generate is the whole allowed subweave of a711bd189, so as a
   condition on what is allowed "single" removes nothing. Under the joint action it is then not an admission rule.
   Whether it is a read-out on the whole or a selection on one thread is the owner's fork, not this card's.
 - C2 fails (some same-departure composite is single): H2 is wrong for it, and that is diagnosed first.
 - C3 fails: mixed composites are not single either, and closure fails more widely.
 - C4 fails with C2 holding: the heights are equal without the symmetry H2 names, and H2's argument for the
   hyperbolic metric is withdrawn for those words.
 - C5 fails: the sentence on the generated subweave is not made.
 - Any cell fails: the failure is the finding, and it is diagnosed before anything else is said.

STAYS OUT: any eigenvalue computation on the hyperbolic metric (the design's tests A1 to A7); any value of tau; three
or more factors; departures other than those named.

0 of 19.
"""
import hashlib
import json
import os
import sys

import mpmath as mp

mp.mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))
TOL = mp.mpf(10) ** (-45)
TERMS = 300


def runs_single(dep, k):
    return list(dep) + [1] * (2 * k + 1)


def cf_tail(seq_iter):
    """[0; a1, a2, ...] from the first TERMS terms of an iterator."""
    a = [next(seq_iter) for _ in range(TERMS)]
    v = mp.mpf(a[-1])
    for x in reversed(a[:-1]):
        v = x + 1 / v
    return 1 / v


def fwd(r, i):
    n = len(r)
    j = i
    while True:
        j = (j + 1) % n
        yield r[j]


def bwd(r, i):
    n = len(r)
    j = i
    while True:
        j = (j - 1) % n
        yield r[j]


def heights(r):
    return [(r[i] + cf_tail(fwd(r, i)) + cf_tail(bwd(r, i))) / 2 for i in range(len(r))]


def seq_at(r, i, direction):
    n = len(r)
    return tuple(r[(i + direction * s) % n] for s in range(1, n))


def exactly_equal(r, i, j):
    if r[i] != r[j]:
        return False
    fi, bi, fj, bj = seq_at(r, i, 1), seq_at(r, i, -1), seq_at(r, j, 1), seq_at(r, j, -1)
    return (fi == fj and bi == bj) or (fi == bj and bi == fj)


def apex_info(r):
    H = heights(r)
    top = max(H)
    at = [i for i, h in enumerate(H) if abs(h - top) < TOL]
    rest = [h for i, h in enumerate(H) if i not in at]
    gap = float(top - max(rest)) if rest else None
    exact = all(exactly_equal(r, at[0], j) for j in at[1:])
    return {'apex': mp.nstr(top, 12), 'multiplicity': len(at), 'at_runs': at, 'run_lengths_at_apex': [r[i] for i in at],
            'gap_to_next': gap, 'equal_by_exact_criterion': exact}


# ---------------------------------------------------------------- integers: words and symmetries
Lm, Rm = (1, 0, 1, 1), (1, 1, 0, 1)
V = (1, 3)                      # LR's line mod 5 (LR is symmetric, so the same line for columns and for rows)


def mul(A, B):
    return (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])


def inv(A):
    d = A[0] * A[3] - A[1] * A[2]
    assert d in (1, -1)
    return (A[3] * d, -A[1] * d, -A[2] * d, A[0] * d)


def word_of(r):
    return ''.join(('L' if i % 2 == 0 else 'R') * a for i, a in enumerate(r))


def mat(w):
    M = (1, 0, 0, 1)
    for ch in w:
        M = mul(M, Lm if ch == 'L' else Rm)
    return M


def on_line(x):
    """Is the pair x, read mod 5, +-V?"""
    x = (x[0] % 5, x[1] % 5)
    return x in ((V[0] % 5, V[1] % 5), ((-V[0]) % 5, (-V[1]) % 5))


def keeps_line(g):
    col = (g[0] * V[0] + g[1] * V[1], g[2] * V[0] + g[3] * V[1])        # g v
    row = (V[0] * g[0] + V[1] * g[2], V[0] * g[1] + V[1] * g[3])        # v^T g
    return {'g v mod 5': [col[0] % 5, col[1] % 5], 'v^T g mod 5': [row[0] % 5, row[1] % 5],
            'column': on_line(col), 'row': on_line(row)}


def departure_letters(r):
    """How many letters the departure takes: the runs up to the last run that is not 1."""
    last = max(i for i, a in enumerate(r) if a != 1)
    return sum(r[:last + 1])


def symmetry_exchanging(r1, r2):
    """A symmetry of the cyclic word of r1 + r2 that carries the first departure's letters onto the second's."""
    w1, w2 = word_of(r1), word_of(r2)
    w = w1 + w2
    n = len(w)
    d1 = set(range(0, departure_letters(r1)))
    d2 = set(range(len(w1), len(w1) + departure_letters(r2)))
    res = {'word': w}
    if r1 == r2:
        half = n // 2
        ok = w == w[half:] + w[:half]
        res.update({'kind': 'rotation by half the word', 'exchanges_departures': {(p + half) % n for p in d1} == d2,
                    'holds': ok and {(p + half) % n for p in d1} == d2})
        return res
    W = mat(w)
    g0 = (1, 0, 0, -1)
    found = []
    wrev = w[::-1]
    for i in range(n):
        if wrev != w[i:] + w[:i]:
            continue
        # position p of w sits at n-1-p in the reversed word, which is position (n-1-p+i) mod n of w
        image = {(n - 1 - p + i) % n for p in d1}
        g = mul(mat(w[:i]), g0)
        line = keeps_line(g)
        found.append({'rotation': i, 'det_g': g[0] * g[3] - g[1] * g[2],
                      'g W^-1 g^-1 = W': mul(mul(g, inv(W)), inv(g)) == W, 'line': line,
                      'exchanges_departures': image == d2})
    res.update({'kind': 'reversal', 'reversals': found,
                'holds': any(f['exchanges_departures'] and f['g W^-1 g^-1 = W'] and f['det_g'] == -1
                             and f['line']['column'] and f['line']['row'] for f in found)})
    return res


# ---------------------------------------------------------------- the card
FAMILY = {
    'departures': {'(6)': [6], '(2,1,2,1,2)': [2, 1, 2, 1, 2]},
    'ks': (1, 2, 3),
    'controls': {'(6)': ([6], '3.618034', 1), '(2,1,2,1,2)': ([2, 1, 2, 1, 2], '1.723607', 1),
                 '(2,1,1,1,2)': ([2, 1, 1, 1, 2], '1.625437', 2), '(2,1^8,2)': ([2] + [1] * 8 + [2], '1.617974', 2)},
    'generators': {'L^6 R (LR)^1': [6, 1] + [1, 1], 'L^6 R (LR)^2': [6, 1] + [1, 1] * 2,
                   'L R^6 (LR)^1': [1, 6] + [1, 1], 'L R^6 (LR)^2': [1, 6] + [1, 1] * 2},
    'deepest': 6,
}


def card(F):
    R = {}
    c0 = {}
    for name, (dep, want, mult) in F['controls'].items():
        info = apex_info(runs_single(dep, 40))
        info['record'] = want
        info['within_1e-6'] = bool(abs(mp.mpf(info['apex']) - mp.mpf(want)) < mp.mpf('1e-6'))
        info['multiplicity_as_recorded'] = info['multiplicity'] == mult
        c0[name] = info
    R['C0'] = c0
    singles = {f'{name}+(LR)^{k}': runs_single(dep, k) for name, dep in F['departures'].items() for k in F['ks']}
    c1 = {}
    for name, r in singles.items():
        info = apex_info(r)
        info['word'] = word_of(r)
        info['line'] = keeps_line(mat(word_of(r)))
        c1[name] = info
    R['C1'] = c1
    same, mixed, sym = {}, {}, {}
    for n1, r1 in singles.items():
        for n2, r2 in singles.items():
            key = f'{n1} . {n2}'
            info = apex_info(r1 + r2)
            if n1.split('+')[0] == n2.split('+')[0]:
                same[key] = info
                sym[key] = symmetry_exchanging(r1, r2)
            else:
                mixed[key] = info
    R['C2_same_departure'] = same
    R['C3_different_departures'] = mixed
    R['C4_symmetries'] = sym
    R['C5_generators'] = {name: dict(apex_info(r), word=word_of(r)) for name, r in F['generators'].items()}
    half = len(singles) ** 2 // 2
    R['cells'] = {
        'C0': all(v['within_1e-6'] and v['multiplicity_as_recorded'] for v in c0.values()),
        'C1': all(v['multiplicity'] == 1 and v['line']['column'] and v['line']['row'] for v in c1.values()),
        'C2': len(same) == half and all(v['multiplicity'] == 2 and v['equal_by_exact_criterion']
                                        for v in same.values()),
        'C3': len(mixed) == half and all(v['multiplicity'] == 1 and v['run_lengths_at_apex'] == [F['deepest']]
                                         and v['gap_to_next'] > 1 for v in mixed.values()),
        'C4': len(sym) == half and all(v['holds'] for v in sym.values()),
        'C5': all(v['multiplicity'] == 1 for v in R['C5_generators'].values()),
    }
    both = list(same.values()) + list(mixed.values())
    R['counts'] = {'composites': len(both), 'single': sum(1 for v in both if v['multiplicity'] == 1),
                   'not_single': sum(1 for v in both if v['multiplicity'] != 1)}
    return R


def main():
    R = {'script_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()}
    R.update(card(FAMILY))
    out = os.path.join(HERE, 'out_single_state_closure.json')
    with open(out, 'w') as fh:
        json.dump(R, fh, indent=1)
    print('written', os.path.basename(out))


if __name__ == '__main__':
    main()
