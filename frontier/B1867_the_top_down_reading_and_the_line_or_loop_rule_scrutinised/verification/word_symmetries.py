#!/usr/bin/env python3
"""B1867, part 1 -- the symmetries of a once-punctured torus bundle, read off its cyclic word (main's own code; data-free).

The advisor seat reported ten rows of SnapPy output (its relay, principle_top_down/symmetry_facts.py, not run here). Main states
the law those rows are instances of and tests it on every cyclic word up to a length, with SnapPy as the judge:

  a cyclic word w in L, R (both letters present) is a necklace; three operations act on necklaces --
      rotation (start elsewhere), reversal (read backwards), swap (exchange the letters);
  Stab(w) = the elements of < rotation, reversal > x < swap > that fix the necklace's colouring;
  LAW 1   the number of isometries of the bundle b++w is 2 |Stab(w)|   (the 2 is the hyperelliptic involution, -1);
  LAW 2   an isometry reverses orientation exactly when its element of Stab(w) contains the swap; so the bundle is
          amphicheiral exactly when some element of Stab(w) contains the swap;
  LAW 3   the bundle of swap(w) is the mirror image of the bundle of w (every word); the bundle of reverse(w) is the bundle
          of w with its orientation.

    python3 -B frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/word_symmetries.py [MAXLEN]
"""
import itertools
import sys
import warnings

warnings.filterwarnings("ignore")
import snappy

MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 10
say = print
SW = str.maketrans("LR", "RL")


def stab(w):
    """the elements (shift, reversed?, swapped?) of the dihedral group times the swap that fix the cyclic word w"""
    n = len(w)
    out = []
    for rev in (0, 1):
        for sw in (0, 1):
            u = w[::-1] if rev else w
            u = u.translate(SW) if sw else u
            for s in range(n):
                if u[s:] + u[:s] == w:
                    out.append((s, rev, sw))
    return out


def canon(w):
    """one representative of the class of w under rotation, reversal and swap (the bundles of a class are isometric)"""
    c = []
    for u in (w, w[::-1], w.translate(SW), w[::-1].translate(SW)):
        c += [u[s:] + u[:s] for s in range(len(u))]
    return min(c)


def necklace(w): return min(w[s:] + w[:s] for s in range(len(w)))


def facts(w):
    M = snappy.Manifold("b++" + w)
    G = M.symmetry_group()
    return G.order(), bool(G.is_amphicheiral()), bool(G.is_full_group())


# ---- controls first
M4 = snappy.Manifold("m004")
assert snappy.Manifold("b++LR").is_isometric_to(M4)
o, amph, full = facts("LR")
assert (o, amph, full) == (8, True, True) and 2 * len(stab("LR")) == 8                      # known answer: the figure-eight complement, D4
say("control (known answer): b++LR is m004; SnapPy gives %d isometries, amphicheiral %s; the law gives 2 x %d" % (o, amph, len(stab("LR"))))

# ---- the census
words = sorted({canon("".join(t)) for n in range(2, MAXLEN + 1) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t}, key=lambda u: (len(u), u))
bad1, bad2, notfull, rows = [], [], [], []
for w in words:
    S = stab(w)
    o, amph, full = facts(w)
    if not full: notfull.append(w)
    if o != 2 * len(S): bad1.append((w, o, 2 * len(S)))
    if amph != any(sw for (_, _, sw) in S): bad2.append((w, amph))
    rows.append((w, o, len(S), amph))
say("census: %d classes of cyclic words of length 2 to %d (one per class under rotation, reversal and swap)" % (len(words), MAXLEN))
say("  SnapPy reports the full group for all of them: %s" % (not notfull))
say("  LAW 1 (isometries = 2 |Stab|): %d of %d agree; exceptions: %s" % (len(words) - len(bad1), len(words), bad1))
say("  LAW 2 (amphicheiral iff Stab contains a swap): %d of %d agree; exceptions: %s" % (len(words) - len(bad2), len(words), bad2))
hist = {}
for (_, o, _, a) in rows: hist[(o, a)] = hist.get((o, a), 0) + 1
say("  (isometries, amphicheiral): count -- %s" % ", ".join("(%d, %s): %d" % (k[0], "yes" if k[1] else "no", v) for k, v in sorted(hist.items())))
assert not notfull and not bad1 and not bad2

# ---- a control that can fail: the law with the swap forgotten undercounts exactly on the amphicheiral words
under = [w for (w, o, s, a) in rows if o != 2 * len([x for x in stab(w) if x[2] == 0])]
say("control (can fail): with the swap left out of Stab the count is wrong on %d words, and they are exactly the amphicheiral ones: %s" % (
    len(under), sorted(under) == sorted(w for (w, _, _, a) in rows if a)))
assert under and sorted(under) == sorted(w for (w, _, _, a) in rows if a)

# ---- LAW 3: the swap is the mirror; the reversal keeps the orientation
def dets(a, b):
    A, B = snappy.Manifold("b++" + a), snappy.Manifold("b++" + b)
    isos = A.is_isometric_to(B, return_isometries=True)
    return sorted({int(round(float(i.cusp_maps()[0].det()))) for i in isos}) if isos else None
chiral = [w for (w, o, s, a) in rows if not a]
sample = chiral[:: max(1, len(chiral) // 25)]
m_sw = [dets(w, w.translate(SW)) for w in sample]
m_rv = [dets(w, w[::-1]) for w in sample]
say("LAW 3 on %d chiral words (every %dth of %d): b++w to b++swap(w): the isometries' orientation signs are %s for all; b++w to b++reverse(w): %s for all" % (
    len(sample), max(1, len(chiral) // 25), len(chiral), sorted({tuple(d) for d in m_sw}), sorted({tuple(d) for d in m_rv})))
assert all(d == [-1] for d in m_sw) and all(d == [1] for d in m_rv)

# ---- LAW 4: which element reverses what.  The fibre's boundary is the one peripheral curve that is trivial in rational homology; an
# isometry sends it to itself or to its negative.  Orientation of the bundle = (orientation of the fibre) x (direction of the base), so
#     the direction of the base (the arrow of the history) is reversed exactly when det x (sign on the fibre's boundary) = -1.
# The law: each element (shift, rev, sw) of Stab(w) gives two isometries with det = (-1)^sw and base direction (-1)^rev.
from fractions import Fraction
from math import gcd


def fibre_boundary(M):
    """the peripheral curve (p, q) = meridian^p longitude^q that is trivial in rational homology, computed from the group's
    presentation (SnapPy's own method for this needs Sage): the one homomorphism to Z, evaluated on the two peripheral words"""
    G = M.fundamental_group()
    gens = G.generators()
    ex = lambda word: [sum((1 if c == g else -1 if c == g.upper() else 0) for c in word) for g in gens]
    rows = [[Fraction(x) for x in ex(r)] for r in G.relators()]
    n = len(gens)
    piv, r = [], 0                                                   # reduced row echelon form over Q
    for c in range(n):
        k = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if k is None: continue
        rows[r], rows[k] = rows[k], rows[r]
        rows[r] = [x / rows[r][c] for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0: rows[i] = [x - rows[i][c] * y for x, y in zip(rows[i], rows[r])]
        piv.append(c); r += 1
        if r == len(rows): break
    free = [c for c in range(n) if c not in piv]
    assert len(free) == 1, "the bundle's first homology has rank one"
    phi = [Fraction(0)] * n
    phi[free[0]] = Fraction(1)
    for i, c in enumerate(piv): phi[c] = -rows[i][free[0]]
    den = 1
    for x in phi: den = den * x.denominator // gcd(den, x.denominator)
    phi = [int(x * den) for x in phi]
    mer, lon = G.peripheral_curves()[0]
    a, b = sum(x * y for x, y in zip(phi, ex(mer))), sum(x * y for x, y in zip(phi, ex(lon)))
    g = gcd(abs(a), abs(b))
    assert g > 0                                                     # the base's direction is seen on the cusp
    return (b // g, -a // g)


def kinds_by_snappy(w):
    M = snappy.Manifold("b++" + w)
    h = fibre_boundary(M)
    out = {}
    for i in M.is_isometric_to(M, return_isometries=True):
        C = i.cusp_maps()[0]
        img = (C[0, 0] * h[0] + C[0, 1] * h[1], C[1, 0] * h[0] + C[1, 1] * h[1])
        sgn = 1 if tuple(img) == tuple(h) else -1 if tuple(img) == (-h[0], -h[1]) else None
        assert sgn is not None, (w, C, h)
        d = int(round(float(C.det())))
        out[(d, d * sgn)] = out.get((d, d * sgn), 0) + 1                # (orientation, base direction)
    return out
def kinds_by_law(w):
    out = {}
    for (_, rev, sw) in stab(w):
        k = ((-1) ** sw, (-1) ** rev)
        out[k] = out.get(k, 0) + 2
    return out
bad4 = [w for w in words if kinds_by_snappy(w) != kinds_by_law(w)]
say("LAW 4 (orientation = the swap, the base's direction = the reversal), on all %d classes: %d agree; exceptions: %s" % (len(words), len(words) - len(bad4), bad4))
assert not bad4
arrowless = [w for w in words if any(rev for (_, rev, _) in stab(w))]
say("  words with an isometry that reverses the base's direction: %d of %d; the run of 6 is one: %s; (2,3) is not: %s" % (
    len(arrowless), len(words), canon("LLLLLLRLR") in arrowless, canon("LLRRRLR") not in arrowless))

# ---- the advisor seat's ten rows, as instances
say("the advisor seat's rows, by the law (no SnapPy in this column) and by SnapPy:")
for name, w in (("golden, 1 period", "LR"), ("golden, 2 periods", "LRLR"), ("golden, 3 periods (not in its table)", "LRLRLR"), ("golden, 4 periods", "LRLRLRLR"),
                ("(6)", "LLLLLLRLR"), ("(2,2,2)", "LLRRLLRLR"), ("(2,1,1,1,2)", "LLRLRLLRLR"), ("(2,1,2,1,2)", "LLRLLRLLRLR"),
                ("(2,3)", "LLRRRLR"), ("(6), two golden periods", "LLLLLLRLRLR")):
    S = stab(w)
    kinds = {"rotations": sum(1 for x in S if x[1] == 0 and x[2] == 0), "rotation with swap": sum(1 for x in S if x[1] == 0 and x[2] == 1),
             "reversals": sum(1 for x in S if x[1] == 1 and x[2] == 0), "reversal with swap": sum(1 for x in S if x[1] == 1 and x[2] == 1)}
    o, amph, full = facts(w)
    root = next(w[:d] for d in range(1, len(w) + 1) if len(w) % d == 0 and w[:d] * (len(w) // d) == w)
    say("  %-38s %-12s law: 2 x %-2d = %-3d SnapPy: %-3d amphicheiral %-3s | rotations %d, rotation with swap %d, reversals %d, reversal with swap %d%s" % (
        name, w, len(S), 2 * len(S), o, "yes" if amph else "no", kinds["rotations"], kinds["rotation with swap"], kinds["reversals"], kinds["reversal with swap"],
        "" if root == w else "   [the word is (%s)^%d]" % (root, len(w) // len(root))))
    assert o == 2 * len(S)
say("so: the golden ground with k periods keeps all three kinds (4k elements: k rotations, k rotations with the swap, 2k reversals with or without it);")
say("    the run of 6 keeps one reversal and nothing else; (2,3) keeps nothing; and the row called (2,1,1,1,2) is the square of LLRLR, which is why it has 8.")
