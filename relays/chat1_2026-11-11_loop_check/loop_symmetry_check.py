#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
THE AGY LANE'S LOOP, PHASES 2 AND 3: THE SYMMETRY FACTS THEIR CLAIMS REST ON.   Data-free; SnapPy and integers.

The web seat (chat1), 2026-11-11, at the owner's word to the seat ("verify it please"; then "continue as u
recomend", on the seat's proposal to check exact claims with SnapPy and to compute no value of the lane's third
gate of Phase 3; relayed, not confirmed to main).  Kind: thread.  The lane was read at 2cc5bf4e5 through the mask;
none of its code was run and none of its output files was opened.

WHAT THE LANE SAYS, AS THE SEAT READ IT (its reports' openings)
  Phase 2: the bundle of the run of 6 has a palindrome symmetry that keeps a tie; a history and its mirror image
  tie in volume.  Phase 3: on the run of 6, with a symmetry group it calls Klein-four, a coupled spin and flux
  cannot break the tie; a history it writes [5,1,2,2] and calls irreversible has a smaller symmetry group and does
  break it.  Its third gate says a reversible history gives no CP violation in its construct and an irreversible
  one, with a twist, does.

WHAT IS CHECKED HERE: only the facts about the manifolds and the words.
  S1  For each history: is the cyclic word its own reverse (a palindrome); is it its own mirror (L and R
      exchanged) up to rotation or reversal.
  S2  With SnapPy, for the once-punctured-torus bundle of each word: the volume, the order of the symmetry group
      and whether it is abelian, whether the manifold is amphicheiral, and the Chern-Simons invariant.
  S3  For each word and its mirror word: equal volume, isometric as unoriented manifolds, and Chern-Simons
      invariants that add to zero modulo one half.
  S4  Whether each history keeps the mark +-v0 modulo 5 (rows; v0 = (1, 3)), and the Smith invariants of M - I
      and M + I.
  NOT COMPUTED: any spectrum, any overlap, any mixing matrix, and no value of the lane's CP invariant.  The seat's
  reading of the lane's third gate is an argument from symmetry and is given in the seat's report, not here.

EXPECTATIONS (written before the run)
  X1  The run of 6 closed by k = 1, 2, 3 golden periods is a palindrome and is not its own mirror; its bundle
      has a symmetry group of order 4, abelian and not cyclic; it is not amphicheiral, and its Chern-Simons
      invariant is not zero.
  X2  L^5 R L^2 R^2, read as a closed word, is not a palindrome; its bundle has a symmetry group of order 2 and
      is not amphicheiral.
  X3  For every word listed, the mirror word has the same volume, is isometric as an unoriented manifold, and has
      the opposite Chern-Simons invariant modulo one half.
  X4  The golden ground is a palindrome and its own mirror, and its bundle is amphicheiral.
  Disclosed: main's B1875 and B1876 already hold that each bundle of the seat's closure card has twice as many
  isometries as its word has symmetries, that the run of 6 has a hand, and Chern-Simons values for it.  X1 and
  X3 are expected from them.  Which word the lane means by [5,1,2,2] is the seat's guess: the closed word with
  those runs; the same runs followed by one golden period are listed beside it.  Nothing was run before this
  file was committed; it was parsed for syntax.
"""
import sys
from math import gcd

import snappy

L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
I2 = ((1, 0), (0, 1))


def mul(a, b):
    return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
            (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]))


def word(s):
    m = I2
    for ch in s:
        m = mul(m, L if ch == 'L' else R)
    return m


def smith(m):
    g = gcd(gcd(abs(m[0][0]), abs(m[0][1])), gcd(abs(m[1][0]), abs(m[1][1])))
    d = abs(m[0][0] * m[1][1] - m[0][1] * m[1][0])
    return (g, d // g if g else 0)


def rotations(w):
    return set(w[i:] + w[:i] for i in range(len(w)))


def swap(w):
    return ''.join('R' if c == 'L' else 'L' for c in w)


def half(x):
    """reduce modulo one half to the interval (-1/4, 1/4]"""
    x = float(x)
    x = x - 0.5 * round(x / 0.5)
    return x


def facts(w):
    out = {}
    rot = rotations(w)
    out['palindrome'] = w[::-1] in rot
    out['own mirror'] = (swap(w) in rot) or (swap(w)[::-1] in rot)
    m = word(w)
    v0 = (1, 3)
    img = ((v0[0] * m[0][0] + v0[1] * m[1][0]) % 5, (v0[0] * m[0][1] + v0[1] * m[1][1]) % 5)
    out['keeps +-v0'] = img in ((1, 3), (4, 2))
    out['trace'] = m[0][0] + m[1][1]
    out['M - I'] = smith(((m[0][0] - 1, m[0][1]), (m[1][0], m[1][1] - 1)))
    out['M + I'] = smith(((m[0][0] + 1, m[0][1]), (m[1][0], m[1][1] + 1)))
    man = snappy.Manifold('b++' + w)
    out['volume'] = float(man.volume())
    try:
        g = man.symmetry_group()
        out['symmetries'] = g.order()
        out['abelian'] = g.is_abelian()
        out['amphicheiral'] = g.is_amphicheiral()
        out['group'] = str(g)
    except Exception as exc:  # reported, not hidden
        out['symmetries'] = 'failed: %s' % type(exc).__name__
        out['abelian'] = None
        out['amphicheiral'] = None
        out['group'] = None
    try:
        out['cs'] = float(man.chern_simons())
    except Exception as exc:
        out['cs'] = None
        out['cs_error'] = type(exc).__name__
    return out, man


def main():
    print('THE AGY LANE\'S LOOP, PHASES 2 AND 3: SYMMETRY FACTS   (SnapPy %s)' % snappy.__version__)
    print()
    hist = [('(6), k = 1', 'LLLLLLR' + 'LR'), ('(6), k = 2', 'LLLLLLR' + 'LR' * 2), ('(6), k = 3', 'LLLLLLR' + 'LR' * 3),
            ('[5,1,2,2] as a closed word', 'LLLLLRLLRR'), ('[5,1,2,2] then one golden period', 'LLLLLRLLRR' + 'LR'),
            ('(2,1,2,1,2), k = 1', 'LLRLLRLLR' + 'LR'), ('(2,1,1,1,2), k = 1', 'LLRLRLLR' + 'LR'),
            ('golden ground, two periods', 'LRLR')]
    res = {}
    x3 = True
    for name, w in hist:
        f, man = facts(w)
        fm, mirror = facts(swap(w))
        res[name] = f
        same_vol = abs(f['volume'] - fm['volume']) < 1e-9
        try:
            iso = bool(man.is_isometric_to(mirror))
        except Exception as exc:
            iso = 'failed: %s' % type(exc).__name__
        cs_sum = None if (f['cs'] is None or fm['cs'] is None) else half(f['cs'] + fm['cs'])
        ok3 = same_vol and iso is True and cs_sum is not None and abs(cs_sum) < 1e-8
        x3 = x3 and ok3
        print('%s   word %s' % (name, w))
        print('    palindrome: %s   own mirror: %s   trace %d   keeps +-v0: %s   M - I: %s   M + I: %s'
              % (f['palindrome'], f['own mirror'], f['trace'], f['keeps +-v0'], f['M - I'], f['M + I']))
        print('    volume %.10f   symmetry group: order %s, abelian %s, %s   amphicheiral: %s   Chern-Simons modulo 1/2: %s'
              % (f['volume'], f['symmetries'], f['abelian'], f['group'], f['amphicheiral'],
                 'not computed' if f['cs'] is None else '%.8f' % half(f['cs'])))
        print('    mirror word %s: same volume %s; isometric unoriented %s; sum of the two Chern-Simons invariants modulo 1/2: %s'
              % (swap(w), same_vol, iso, 'not computed' if cs_sum is None else '%.2e' % cs_sum))
    print()

    def six_ok(f):
        return (f['palindrome'] and not f['own mirror'] and f['symmetries'] == 4 and f['abelian'] is True
                and f['group'] is not None and 'Z/2 + Z/2' in f['group'] and f['amphicheiral'] is False
                and f['cs'] is not None and abs(half(f['cs'])) > 1e-6)
    x1 = all(six_ok(res['(6), k = %d' % k]) for k in (1, 2, 3))
    f5 = res['[5,1,2,2] as a closed word']
    x2 = (not f5['palindrome']) and f5['symmetries'] == 2 and f5['amphicheiral'] is False
    fg = res['golden ground, two periods']
    x4 = fg['palindrome'] and fg['own mirror'] and fg['amphicheiral'] is True
    for nm, ok in (('X1', x1), ('X2', x2), ('X3', x3), ('X4', x4)):
        print('%s: %s' % (nm, 'HOLDS' if ok else 'FAILS'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
