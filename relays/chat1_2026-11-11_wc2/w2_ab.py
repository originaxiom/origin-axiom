#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C2, THEOREMS A AND B OF THE AGY LANE'S NOTE (agy/self-consistent-loop-2026-11-11 at 8ef2df5ac), COMPUTED BY THIS
SEAT'S OWN ROUTE.   The web seat (chat1), 2026-11-11.  Data-free: SnapPy 3.3.2 for the manifolds and their
presentations, Fox calculus written here, complex arithmetic for characters of order 5.

None of the lane's code was run or opened.  The lane's statements were read through the mask.  No overlap, matrix Y,
commutator determinant, mixing or CP quantity is computed; no cusp modulus is evaluated.

THE ROUTE, convention-free where possible
  For a manifold M (SnapPy's notation b++W, b+-W), the seat takes SnapPy's own presentation (deficiency one), solves
  the homomorphisms pi_1(M) -> Z/5 from the relators' exponent sums, finds the reduction of the integral class (the
  one character that kills the torsion of H_1), and evaluates every character on SnapPy's two peripheral curves.
  Lines: the integral class's reduction ("base"); the line that vanishes on both peripheral curves ("unramified");
  the rest ("ramified").  Wada's torsion by Fox calculus: for a character rho into the fifth roots of unity, delete
  the column of a generator g with rho(g) != 1 and divide the 2x2... determinant by |rho(g) - 1|.
  The census: binary Lyndon words in L, R of length 2 to 12 with both letters; a necklace keeps the mark when one of
  its rotations W has  v.M(W) = +-v  modulo 5 for the mark v.  Four conventions are counted, because the lane's
  matrices sit on lines the mask stars: M(W) as the product of the letter matrices L = rows (1,0),(1,1),
  R = rows (1,1),(0,1) or its transpose, and the mark as the golden eigenline of M(LR) or of M(RL).  The bundle is
  b++W' or b+-W' by the sign, for the rotation W' that keeps the mark.

WHAT WOULD COUNT AS NOT REPRODUCING (written before the run)
  A1  On each of the seven bundles the lane names, H^1(M; F_5) is not two-dimensional; or the number of lines that
      vanish on the peripheral subgroup is not one; or the base line vanishes there.
  A2  On those seven: the unramified line's torsion is not zero (above 1e-9) for some charge; or on some ramified
      line a charge's modulus is neither 2 sin(pi/5) nor 2 sin(2 pi/5) (to 1e-9); or the four charges' product is not
      5 (to 1e-9).
  A2' (the lane's B.3, "independent of W across all mark-preserving bundles"): the same on every bundle of the census.
  B   Under none of the four conventions the census gives 285 necklaces; or, under the convention that gives 285, the
      oriented classes are not 228, the unoriented not 124, or the split not 20 amphicheiral, 70 chiral with symmetry
      group of order at least 4, 34 chiral with group Z/2; or the least volumes are not at b+-LR, b++LLLRLL (its class)
      and b+-LLLLLRLLRR (its class).
  CONTROLS that must come out as stated or the code is broken: b++LLRR and b+-LLRR have H^1(M; F_5) one-dimensional
      (L^2 R^2 keeps no line of order 5); the census without the mark condition has 745 necklaces (the Lyndon counts).

DISCLOSED.  The lane's numbers are known to the seat; this is a check, not a blind test.  Its matrices and mark are on
starred lines, hence the four conventions.
"""
import cmath
import itertools
import math
import sys
import warnings

warnings.filterwarnings('ignore')
import snappy  # noqa: E402

Z5 = cmath.exp(2j * cmath.pi / 5)
S1 = 2 * math.sin(math.pi / 5)
S2 = 2 * math.sin(2 * math.pi / 5)
NAMED = ['b+-LR', 'b++LLLRLL', 'b+-RRRRRLR', 'b++LLLLLLRLR', 'b+-RRRRLRRLLR', 'b++LLLLLLLRRLLR', 'b++LLLLLRLLRRLR']


# ------------------------------------------------------------------ characters and Fox calculus on SnapPy's presentation
def exps(word, gens):
    e = [0] * len(gens)
    for ch in word:
        if ch.islower():
            e[gens.index(ch)] += 1
        else:
            e[gens.index(ch.lower())] -= 1
    return e


def characters(G):
    """all homomorphisms to Z/5 as tuples over the generators"""
    gens = G.generators()
    rel = [exps(r, gens) for r in G.relators()]
    out = []
    for v in itertools.product(range(5), repeat=len(gens)):
        if all(sum(a * b for a, b in zip(r, v)) % 5 == 0 for r in rel):
            out.append(v)
    return gens, out


def ev(word, gens, v):
    return sum(c * x for c, x in zip(exps(word, gens), v)) % 5


def lines(chars):
    seen = set()
    out = []
    for v in chars:
        if not any(v):
            continue
        key = min(tuple((q * x) % 5 for x in v) for q in range(1, 5))
        if key not in seen:
            seen.add(key)
            out.append(key)
    return out


def fox_row(word, gens, rho):
    """the Fox derivatives of a relator, evaluated at the one-dimensional rep rho (values per generator)"""
    row = [0j] * len(gens)
    pref = 1 + 0j
    for ch in word:
        i = gens.index(ch.lower())
        if ch.islower():
            row[i] += pref
            pref *= rho[i]
        else:
            pref /= rho[i]
            row[i] -= pref
    return row


def torsion(G, gens, v, q):
    rho = [Z5 ** ((q * x) % 5) for x in v]
    rows = [fox_row(r, gens, rho) for r in G.relators()]
    n = len(gens)
    best = None
    for j in range(n):
        if abs(rho[j] - 1) < 1e-12:
            continue
        cols = [c for c in range(n) if c != j]
        m = [[rows[i][c] for c in cols] for i in range(len(rows))]
        d = det(m)
        val = abs(d) / abs(rho[j] - 1)
        if best is None:
            best = val
    return best


def det(m):
    n = len(m)
    if n == 0:
        return 1 + 0j
    a = [row[:] for row in m]
    d = 1 + 0j
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        if abs(a[p][i]) < 1e-300:
            return 0j
        if p != i:
            a[i], a[p] = a[p], a[i]
            d = -d
        d *= a[i][i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            for c in range(i, n):
                a[r][c] -= f * a[i][c]
    return d


def analyse(name):
    M = snappy.Manifold(name)
    G = M.fundamental_group()
    gens, chars = characters(G)
    dim = round(math.log(len(chars), 5))
    mer, lon = G.peripheral_curves()[0]
    ls = lines(chars)
    # the integral class: a character into Z that kills torsion: take H_1 free part by checking which line is the
    # reduction of a Z-valued solution; found as the line whose every multiple lifts to an integral solution
    rel = [exps(r, gens) for r in G.relators()]
    integral = None
    for L in ls:
        # search a small integral lift with entries in -10..10
        for lift in itertools.product(range(-6, 7), repeat=len(gens)):
            if all((a - b) % 5 == 0 for a, b in zip(lift, L)) and any(lift) and all(sum(a * b for a, b in zip(r, lift)) == 0 for r in rel):
                integral = L
                break
        if integral:
            break
    info = []
    for L in ls:
        hm, hl = ev(mer, gens, L), ev(lon, gens, L)
        kind = 'base' if L == integral else ('unramified' if hm == 0 and hl == 0 else 'ramified')
        taus = [torsion(G, gens, L, q) for q in range(1, 5)]
        info.append((L, kind, hm, hl, taus))
    return M, dim, info


def check_a(name, info, dim):
    kinds = [k for _, k, _, _, _ in info]
    ok1 = dim == 2 and len(info) == 6 and kinds.count('base') == 1 and kinds.count('unramified') == 1 and kinds.count('ramified') == 4
    base = [x for x in info if x[1] == 'base']
    ok1 = ok1 and base and (base[0][2], base[0][3]) != (0, 0)
    ok2 = True
    for L, k, hm, hl, taus in info:
        if k == 'unramified':
            ok2 = ok2 and all(t is not None and t < 1e-9 for t in taus)
        if k == 'ramified':
            ok2 = ok2 and all(t is not None and min(abs(t - S1), abs(t - S2)) < 1e-9 for t in taus)
            ok2 = ok2 and abs(math.prod(taus) - 5) < 1e-9
    return ok1, ok2


# ------------------------------------------------------------------ the census
Lm = ((1, 0), (1, 1))
Rm = ((1, 1), (0, 1))


def mul(a, b):
    return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
            (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]))


def mat(w, transpose):
    m = ((1, 0), (0, 1))
    for ch in w:
        m = mul(m, Lm if ch == 'L' else Rm)
    return ((m[0][0], m[1][0]), (m[0][1], m[1][1])) if transpose else m


def golden_line(transpose, word):
    m = mat(word, transpose)
    for v in ((1, x) for x in range(5)):
        w = ((v[0] * m[0][0] + v[1] * m[1][0]) % 5, (v[0] * m[0][1] + v[1] * m[1][1]) % 5)
        if w == ((-v[0]) % 5, (-v[1]) % 5):
            return v
    raise SystemExit('no golden line')


def keeps(w, transpose, mark):
    m = mat(w, transpose)
    img = ((mark[0] * m[0][0] + mark[1] * m[1][0]) % 5, (mark[0] * m[0][1] + mark[1] * m[1][1]) % 5)
    if img == (mark[0] % 5, mark[1] % 5):
        return 1
    if img == ((-mark[0]) % 5, (-mark[1]) % 5):
        return -1
    return 0


def lyndon(n):
    out = []
    for t in itertools.product('LR', repeat=n):
        w = ''.join(t)
        if 'L' in w and 'R' in w and all(w < w[i:] + w[:i] for i in range(1, n)):
            out.append(w)
    return out


def census(transpose, mark):
    res = []
    total = 0
    for n in range(2, 13):
        for w in lyndon(n):
            total += 1
            for i in range(n):
                r = w[i:] + w[:i]
                s = keeps(r, transpose, mark)
                if s:
                    res.append((w, r, s))
                    break
    return total, res


def main():
    print('W-C2, theorems A and B, by the seat\'s own route (SnapPy %s)' % snappy.__version__)
    print()
    print('CONTROLS')
    for name in ('b++LLRR', 'b+-LLRR'):
        G = snappy.Manifold(name).fundamental_group()
        gens, chars = characters(G)
        print('    %s: |Hom(pi_1, Z/5)| = %d, so H^1(M; F_5) has dimension %d' % (name, len(chars), round(math.log(len(chars), 5))))
    print()
    print('A1, A2  the seven bundles the lane names')
    a_ok = True
    for name in NAMED:
        M, dim, info = analyse(name)
        ok1, ok2 = check_a(name, info, dim)
        a_ok = a_ok and ok1 and ok2
        print('  %-18s H_1 = %-10s dim H^1(F_5) = %d   A1 %s   A2 %s' % (name, M.homology(), dim, 'holds' if ok1 else 'FAILS', 'holds' if ok2 else 'FAILS'))
        for L, k, hm, hl, taus in info:
            print('      %-10s line %s  peripheral (%d, %d)  |tau| for q = 1..4: %s  product %s'
                  % (k, L, hm, hl, ', '.join('-' if t is None else '%.12f' % t for t in taus),
                     '-' if None in taus else '%.12f' % math.prod(taus)))
    print('A1 and A2 on the seven: %s' % ('REPRODUCED' if a_ok else 'NOT REPRODUCED'))
    print()

    print('B  the census under four conventions')
    variants = []
    for transpose in (False, True):
        for ground in ('LR', 'RL'):
            mark = golden_line(transpose, ground)
            total, res = census(transpose, mark)
            variants.append((transpose, ground, mark, total, res))
            print('    matrices %s, mark the golden line of %s = %s: %d necklaces in all; %d keep the mark'
                  % ('transposed' if transpose else 'as written', ground, mark, total, len(res)))
    chosen = [v for v in variants if len(v[4]) == 285]
    print('    conventions giving 285: %d of 4' % len(chosen))
    if not chosen:
        print('B: NOT REPRODUCED at the count')
        return 0
    transpose, ground, mark, total, res = chosen[0]
    print('    taken: matrices %s, the golden line of %s' % ('transposed' if transpose else 'as written', ground))
    data = []
    a2_all = 0
    a2_fail = []
    for w, r, s in res:
        name = ('b++' if s == 1 else 'b+-') + r
        M = snappy.Manifold(name)
        sym = M.symmetry_group()
        un = M.isometry_signature()
        orsig = M.isometry_signature(ignore_orientation=False)
        vol = float(M.volume())
        data.append((name, un, orsig, sym.order(), sym.is_amphicheiral(), vol, str(M.homology())))
        _, dim, info = analyse(name)
        ok1, ok2 = check_a(name, info, dim)
        if ok1 and ok2:
            a2_all += 1
        else:
            a2_fail.append(name)
    un_classes = {}
    for d in data:
        un_classes.setdefault(d[1], []).append(d)
    or_classes = {d[2] for d in data}
    amph = [c for c in un_classes.values() if c[0][4]]
    chiral = [c for c in un_classes.values() if not c[0][4]]
    rev = [c for c in chiral if c[0][3] >= 4]
    irr = [c for c in chiral if c[0][3] == 2]
    other = [c for c in chiral if c[0][3] not in (2,) and c[0][3] < 4]
    print('    bundles: %d; oriented classes: %d; unoriented classes: %d (amphicheiral %d; chiral with group of order >= 4: %d; chiral with group Z/2: %d; other %d)'
          % (len(data), len(or_classes), len(un_classes), len(amph), len(rev), len(irr), len(other)))

    def least(cl):
        best = min(cl, key=lambda c: c[0][5])
        return best[0][5], sorted({d[0] for d in best})[:4], best[0][6]
    for label, cl in (('amphicheiral', amph), ('chiral, order >= 4', rev), ('chiral, Z/2', irr)):
        v, names, h = least(cl)
        print('    least volume, %-18s %.10f at %s (H_1 = %s)' % (label + ':', v, ', '.join(names), h))
    ref = {n: snappy.Manifold(n).isometry_signature() for n in ('b+-LR', 'b++LLLRLL', 'b+-LLLLLRLLRR')}
    lv = [least(amph), least(rev), least(irr)]
    leastsig = [min(cl, key=lambda c: c[0][5])[0][1] for cl in (amph, rev, irr)]
    least_ok = leastsig == [ref['b+-LR'], ref['b++LLLRLL'], ref['b+-LLLLLRLLRR']]
    counts_ok = (len(data), len(or_classes), len(un_classes), len(amph), len(rev), len(irr)) == (285, 228, 124, 20, 70, 34)
    print('B: counts %s; least volumes at the named classes %s' % ('REPRODUCED' if counts_ok else 'NOT REPRODUCED', 'REPRODUCED' if least_ok else 'NOT REPRODUCED'))
    print("A2' on every bundle of the census: holds on %d of %d%s" % (a2_all, len(data), ('; fails on ' + ', '.join(a2_fail[:10])) if a2_fail else ''))
    print('CONTROL  the census without the mark condition: %d necklaces (745 expected)' % chosen[0][3])
    return 0


if __name__ == '__main__':
    sys.exit(main())
