#!/usr/bin/env python3
"""B1875 (data-free) -- the web seat's sealed card "is 'a single state' closed under composition" (its relay at 8718d4677),
re-derived by main with its own code.  None of the seat's code is run.

THE INSTRUMENT is the record's own for the state (B1857): a history is a closed positive word, written by its runs
r_1 ... r_n (n even, L first).  The height of run i is the radius of the history's axis when that run's fixed class is put
at infinity:  H_i = (r_i + x_i + y_i)/2 = sqrt(tr^2 - 4) / (2 c_i),  c_i the lower-left entry of the word's matrix started at
run i.  So a tie of two heights is an equality of two integers, and nothing here is decided by a tolerance.  The history is
SINGLE when the greatest height is attained by one run.

Main's parts:
  0  controls: the integer form against the continued fraction at 60 digits on every word used; B1857's four apexes; and,
     by brute force over classes, that the classes of height above 1 are exactly the runs' own (one height per run is enough);
  1  the card's cells C1, C2, C3, C5 in integers;
  2  C4: for each of the 18 same-departure composites, the symmetry as an integer matrix g, the relation it satisfies, what
     it does to the two departures and to LR's line modulo 5; and SnapPy's count of the bundle's isometries against the word's;
  3  the amendment: the 216 triples (P1) and "the apex is one orbit of the word's symmetries" on the 258 words (P2);
  4  what the seat's referee reported and the seat did not seal: ties with no symmetry behind them (a census to 18 letters),
     the four-factor words, composites of two non-single pairs, a departure that is not a palindrome, and the record's own two
     'mirror' departures.

    python3 -B frontier/B1875_a_single_state_is_not_closed_under_composition_verified/verification/closure_on_main.py [--no-snappy]
"""
import itertools
import math
import sys
import warnings

import mpmath as mp

mp.mp.dps = 60
say = print
I2 = ((1, 0), (0, 1))
L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))
P = ((0, 1), (1, 0))
G0 = ((1, 0), (0, -1))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def mat(letters):
    M = I2
    for ch in letters:
        M = mul(M, L if ch == "L" else R)
    return M


def inv(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert d in (1, -1)
    return ((A[1][1] * d, -A[0][1] * d), (-A[1][0] * d, A[0][0] * d))


def det(A): return A[0][0] * A[1][1] - A[0][1] * A[1][0]
def tr(A): return A[0][0] + A[1][1]
def letters(runs): return "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))


def cs(runs):
    """c_i for every run i: the lower-left entry of the word started at run i, that run's letter taken as the translation L"""
    n = len(runs)
    assert n % 2 == 0 and all(r >= 1 for r in runs)
    out = []
    for i in range(n):
        seq = runs[i:] + runs[:i]
        out.append(mat(letters(seq))[1][0])
    return out


def trace(runs): return tr(mat(letters(runs)))


def heights_cf(runs, terms=400):
    """the same heights from the continued fractions, at 60 digits: H_i = (r_i + [0; r_{i+1}, ...] + [0; r_{i-1}, ...])/2"""
    n = len(runs)
    H = []
    for i in range(n):
        x = mp.mpf(0)
        for k in range(terms, 0, -1):
            x = 1 / (runs[(i + k) % n] + x)
        y = mp.mpf(0)
        for k in range(terms, 0, -1):
            y = 1 / (runs[(i - k) % n] + y)
        H.append((runs[i] + x + y) / 2)
    return H


def apex(runs):
    """(the runs at the apex, the apex's height, its lead over the next distinct height); ties decided in integers"""
    c = cs(runs)
    lo = min(c)
    top = [i for i, x in enumerate(c) if x == lo]
    d = mp.sqrt(mp.mpf(trace(runs)) ** 2 - 4)
    rest = sorted(set(c))
    lead = d / (2 * lo) - (d / (2 * rest[1]) if len(rest) > 1 else 0)
    return top, d / (2 * lo), lead


def stabiliser(runs):
    """the symmetries of the cyclic run sequence: (kind, s) with kind 'rot' (i -> i + s) or 'ref' (i -> s - i); s odd exchanges the letters"""
    n = len(runs)
    out = []
    for s in range(n):
        if all(runs[(i + s) % n] == runs[i] for i in range(n)):
            out.append(("rot", s))
        if all(runs[(s - i) % n] == runs[i] for i in range(n)):
            out.append(("ref", s))
    return out


def orbit(runs, i, S=None):
    n = len(runs)
    S = stabiliser(runs) if S is None else S
    return sorted({(i + s) % n if k == "rot" else (s - i) % n for k, s in S})


V = (1, 2)                                   # LR's line modulo 5 in main's convention: (LR + 1) v = 0 mod 5
LR = mul(L, R)
assert all(x % 5 == 0 for x in (LR[0][0] * V[0] + LR[0][1] * V[1] + V[0], LR[1][0] * V[0] + LR[1][1] * V[1] + V[1]))


def on_line(g):
    """what g does to the line of v modulo 5: the scalar c with g v = c v, or None if g moves the line"""
    w = ((g[0][0] * V[0] + g[0][1] * V[1]) % 5, (g[1][0] * V[0] + g[1][1] * V[1]) % 5)
    for c in range(1, 5):
        if ((c * V[0]) % 5, (c * V[1]) % 5) == w:
            return c
    return None


def matrix_of(runs, kind, s):
    """the symmetry (kind, s) of the cyclic run sequence as g in GL(2, Z), with the relation it satisfies checked exactly.
    Returns (g, 'keeps' or 'inverts' the history).  A rotation by s runs is conjugation by the prefix U; reading the word
    backwards is conjugation of the inverse by diag(1, -1); exchanging the letters is conjugation by the exchange P."""
    n = len(runs)
    W = mat(letters(runs))
    if kind == "rot":
        U = mat(letters(runs[:s]))
        g = U if s % 2 == 0 else mul(U, P)
        assert mul(mul(g, W), inv(g)) == W
        return g, "keeps"
    # reflection i -> s - i: the reversed word, started after the run that position 0 came from
    rev = runs[::-1]                                         # run j of the reversed word is run n-1-j
    k = (n - 1 - s) % n                                      # the reversed sequence rotated by k equals runs (as numbers)
    assert all(rev[(j + k) % n] == runs[j] for j in range(n))
    # letters: the reversed word starts with the letter of the last run (R, n even); its rotation by k runs starts with R if k even
    U = mat("".join(("R" if i % 2 == 0 else "L") * r for i, r in enumerate(rev[:k])))
    Wrev = mul(mul(G0, inv(W)), G0)
    assert Wrev == mat("".join(("R" if i % 2 == 0 else "L") * r for i, r in enumerate(rev)))
    rot = mul(mul(inv(U), Wrev), U)                          # the reversed word, rotated by k runs
    if k % 2 == 1:                                           # it starts with L: it is the word itself
        assert rot == W
        g = mul(inv(U), G0)
        assert mul(mul(g, inv(W)), inv(g)) == W
    else:                                                    # it starts with R: it is the word with its letters exchanged
        assert rot == mul(mul(P, W), P)
        g = mul(mul(P, inv(U)), G0)
        assert mul(mul(g, inv(W)), inv(g)) == W
    return g, "inverts"


def classes_above(runs, h0=mp.mpf("0.999")):
    """brute force: the heights of ALL primitive classes above h0, counted once per period of the history.
    The class p/q has height |xi - zeta| / (2 |q xi - p| |q zeta - p|) on the history's axis (endpoints xi, zeta)."""
    W = mat(letters(runs))
    a, b, c, d = W[0][0], W[0][1], W[1][0], W[1][1]
    disc = mp.sqrt(mp.mpf(a + d) ** 2 - 4)
    xi, zeta = (a - d + disc) / (2 * c), (a - d - disc) / (2 * c)      # attracting, repelling
    assert xi > 1 and -1 < zeta < 0
    B = (xi - zeta) / (2 * h0)                                           # |q xi - p| |q zeta - p| <= B
    found = []
    # the arc between the fixed points: a period is [0, W(0)) = [0, b/d)
    hi = mp.mpf(b) / d
    q = 1
    while True:
        # p/q in [0, hi): (xi - p/q) >= xi - hi > 0, so q^2 (xi - hi)(p/q - zeta) <= B  ->  q^2 <= B / ((xi - hi)(-zeta))
        if mp.mpf(q) ** 2 * (xi - hi) * (-zeta) > B:
            break
        for p in range(0, (b * q) // d + 1):
            if math.gcd(p, q) != 1 or not (p * d < b * q):               # p/q < W(0) = b/d, decided in integers
                continue
            h = (xi - zeta) / (2 * abs(q * xi - p) * abs(q * zeta - p))
            if h > h0:
                found.append(h)
        q += 1
    # the other arc: a period is [infinity, W(infinity)) = {infinity} and the p/q above a/c
    lo = mp.mpf(a) / c
    found.append((xi - zeta) / 2)                                        # the class at infinity
    q = 1
    while True:
        if mp.mpf(q) ** 2 * (lo - xi) * (lo - zeta) > B:
            break
        p = (a * q) // c + 1                                             # p/q > W(infinity) = a/c, decided in integers
        while True:
            h = (xi - zeta) / (2 * abs(q * xi - p) * abs(q * zeta - p))
            if h <= h0 and p > q * lo + 2:
                break
            if math.gcd(p, q) == 1 and h > h0:
                found.append(h)
            p += 1
        q += 1
    return sorted(found, reverse=True)


# ---------------------------------------------------------------- the family
def dep6(k): return (6,) + (1,) * (2 * k + 1)                       # L^6 R (LR)^k
def dep2(k): return (2, 1, 2, 1, 2) + (1,) * (2 * k + 1)            # (L^2 R)^3 (LR)^k
SIX = [("(6)_%d" % k, dep6(k)) for k in (1, 2, 3)] + [("(2,1,2,1,2)_%d" % k, dep2(k)) for k in (1, 2, 3)]
assert [letters(r) for _, r in SIX][:1] == ["LLLLLLRLR"] and letters(dep2(1)) == "LLRLLRLLRLR"
kind = {name: ("6" if name.startswith("(6)") else "2") for name, _ in SIX}
NOSNAPPY = "--no-snappy" in sys.argv


def main():
    # ---- 0. controls
    say("0. CONTROLS")
    every = [r for _, r in SIX] + [a + b for (_, a) in SIX for (_, b) in SIX]
    worst = mp.mpf(0)
    for runs in every:
        c = cs(runs)
        d = mp.sqrt(mp.mpf(trace(runs)) ** 2 - 4)
        for h_int, h_cf in zip((d / (2 * x) for x in c), heights_cf(runs)):
            worst = max(worst, abs(h_int - h_cf))
    assert worst < mp.mpf(10) ** -50
    say("   the integer form sqrt(tr^2 - 4)/(2 c_i) against the continued fraction (r_i + x_i + y_i)/2, on the 6 histories and their 36 composites: greatest difference %s" % mp.nstr(worst, 3))
    # B1857's four apexes, in a long golden background (200 ones)
    for runs, want, mult in (((6,), "3.618034", 1), ((2, 1, 2, 1, 2), "1.723607", 1), ((2, 1, 1, 1, 2), "1.625437", 2), ((2,) + (1,) * 8 + (2,), "1.617974", 2)):
        long = runs + (1,) * (201 if len(runs) % 2 else 200)
        top, h, lead = apex(long)
        assert mp.nstr(h, 7) == want and len(top) == mult, (runs, mp.nstr(h, 9), top)
        say("   B1857's apex of %-22s in a long golden background: %s, attained %d time(s)" % (runs, mp.nstr(h, 7), len(top)))
    assert abs(apex((6,) + (1,) * 201)[1] - (6 + 2 / ((1 + mp.sqrt(5)) / 2)) / 2) < mp.mpf(10) ** -30
    # one height per run is enough: by brute force over every primitive class
    n_checked, worst_other = 0, mp.mpf(0)
    for name, runs in SIX[:2] + SIX[3:5] + [("(6)_1(6)_2", dep6(1) + dep6(2)), ("(2,1,2,1,2)_1(6)_1", dep2(1) + dep6(1)), ("LLR", (2, 1)), ("LR", (1, 1))]:
        c = cs(runs)
        d = mp.sqrt(mp.mpf(trace(runs)) ** 2 - 4)
        mine = sorted((d / (2 * x) for x in c), reverse=True)            # every run's height; each is above 1/2
        brute = classes_above(runs, mp.mpf("0.5"))                       # every class above 1/2, once per period
        rest = list(brute)
        for h in mine:
            hit = [u for u in rest if abs(u - h) < mp.mpf(10) ** -40]
            assert hit, (name, mp.nstr(h, 8))
            rest.remove(hit[0])
        assert all(u < 1 for u in rest), (name, [mp.nstr(u, 6) for u in rest[:3]])
        assert max(mine) >= mp.sqrt(5) / 2 - mp.mpf(10) ** -40
        worst_other = max([worst_other] + rest)
        n_checked += 1
    say("   by brute force over all primitive classes above height 1/2, on %d histories: every run's own class is there once per period, and every other class is below 1 (the greatest: %s); every apex is at least sqrt(5)/2. So one height per run is enough for the apex" % (n_checked, mp.nstr(worst_other, 5)))

    # ---- 1. the card
    say("1. THE CARD (ties are equalities of integers)")
    for name, runs in SIX:
        top, h, lead = apex(runs)
        W = mat(letters(runs))
        assert len(top) == 1 and on_line(W) is not None
    lead6 = [apex(r)[2] for n_, r in SIX if kind[n_] == "6"]
    lead2 = [apex(r)[2] for n_, r in SIX if kind[n_] == "2"]
    say("   C1  the six histories: each has one run at the apex and keeps LR's line modulo 5; the lead is %s to %s for (6) and %s to %s for (2,1,2,1,2)" % (
        mp.nstr(min(lead6), 3), mp.nstr(max(lead6), 3), mp.nstr(min(lead2), 3), mp.nstr(max(lead2), 3)))
    M2 = mat(letters((2, 1) * 3))
    assert tuple(tuple(x % 5 for x in row) for row in M2) == I2 and tuple(tuple(x % 5 for x in row) for row in mat("LLLLL")) == I2
    say("       why: modulo 5, (L^2 R)^3 = 1 and L^5 = 1, so every word of the family is a power of LR")
    same, diff = [], []
    for (n1, a), (n2, b) in itertools.product(SIX, SIX):
        (same if kind[n1] == kind[n2] else diff).append((n1 + n2, a + b, kind[n1]))
    assert len(same) == 18 and len(diff) == 18
    rng = {"6": [], "2": []}
    for name, runs, kd in same:
        top, h, lead = apex(runs)
        assert len(top) == 2, (name, top)
        assert all(runs[i] == (6 if kd == "6" else 2) for i in top)
        rng[kd].append(h)
    say("   C2  the 18 composites with the same departure: the apex is attained by exactly two runs in every one (the two integers c_i are equal); heights %s to %s for (6), %s to %s for (2,1,2,1,2)" % (
        mp.nstr(min(rng["6"]), 5), mp.nstr(max(rng["6"]), 5), mp.nstr(min(rng["2"]), 5), mp.nstr(max(rng["2"]), 5)))
    leads = []
    for name, runs, kd in diff:
        top, h, lead = apex(runs)
        assert len(top) == 1 and runs[top[0]] == 6
        leads.append(lead)
    assert min(leads) > 1
    say("   C3  the 18 composites with different departures: one run at the apex, the run of 6, leading by %s to %s" % (mp.nstr(min(leads), 3), mp.nstr(max(leads), 3)))
    F8 = [("L^6 R (LR)^%d" % k, dep6(k)) for k in (1, 2)] + [("L R^6 (LR)^%d" % k, (1, 6) + (1,) * (2 * k)) for k in (1, 2)]
    assert letters(F8[2][1]) == "LRRRRRRLR"
    for name, runs in F8:
        assert len(apex(runs)[0]) == 1
    say("   C5  the four generators of the allowed subweave (B1872: index 12 in PSL(2, Z)) each have one run at the apex")
    top, h, lead = apex((1, 1))
    assert len(top) == 2 and on_line(LR) is not None
    say("       LR itself keeps the line and is not single: its two runs tie")
    say("   SO: of the 36 composites of two single histories, 18 are single and 18 are not")

    # ---- 2. the symmetry behind each tie
    say("2. C4: THE SYMMETRY BEHIND EACH OF THE 18 TIES")
    n_sq = n_rev = 0
    rev_minus = 0
    for name, runs, kd in same:
        n = len(runs)
        S = [x for x in stabiliser(runs) if x != ("rot", 0)]
        top = apex(runs)[0]
        assert all(s % 2 == 0 for _, s in S)                        # no symmetry of the family exchanges the letters
        moves = [(k, s) for k, s in S if ((top[0] + s) % n if k == "rot" else (s - top[0]) % n) == top[1]]
        assert moves, name
        for k, s in moves:                                          # every symmetry that exchanges the two departures keeps the line
            g, how = matrix_of(runs, k, s)
            assert on_line(g) in (1, 4), (name, k, s)
            assert (det(g), how) == ((1, "keeps") if k == "rot" else (-1, "inverts"))
        W5 = tuple(tuple(x % 5 for x in row) for row in mat(letters(runs)))
        if runs[:n // 2] == runs[n // 2:]:                          # a square
            assert len(S) == 3 and sorted(k for k, _ in S) == ["ref", "ref", "rot"] and ("rot", n // 2) in S and ("rot", n // 2) in moves
            assert sum(1 for k, _ in moves if k == "ref") == 1      # of its two reversals one exchanges the departures and one fixes each
            n_sq += 1
        else:
            assert len(S) == 1 and S[0][0] == "ref" and moves == S
            n_rev += 1
            rev_minus += (W5 == ((4, 0), (0, 4)))
    assert (n_sq, n_rev) == (6, 12)
    say("   in every one a symmetry of the cyclic word exchanges the two departures, and every such symmetry keeps the line (g v = +-v modulo 5):")
    say("     6 squares: the rotation by half the word, det g = +1, g W g^-1 = W (the deck move of the double cover); a square also has two reversals, one of them exchanging the departures")
    say("     12 others: exactly one symmetry besides the identity, a reversal, det g = -1, g W^-1 g^-1 = W (it reverses fibre and base, and keeps the 3-manifold's orientation)")
    ten = sum(1 for (n1, a), (n2, b) in itertools.product(SIX, SIX) if tuple(tuple(x % 5 for x in row) for row in mat(letters(a + b))) == ((4, 0), (0, 4)))
    say("   no symmetry exchanges the letters; %d of the 12 are -1 modulo 5, and %d of the 36 composites" % (rev_minus, ten))
    if not NOSNAPPY:
        warnings.filterwarnings("ignore")
        import snappy
        ok = 0
        for name, runs, kd in same:
            w = letters(runs)
            G = snappy.Manifold("b++" + w).symmetry_group()
            want = 8 if runs[:len(runs) // 2] == runs[len(runs) // 2:] else 4
            assert G.is_full_group() and G.order() == 2 * len(stabiliser(runs)) == want, (name, G.order())
            assert not G.is_amphicheiral()
            ok += 1
        ctrl = {}
        for name, runs, kd in diff:
            G = snappy.Manifold("b++" + letters(runs)).symmetry_group()
            assert G.is_full_group() and G.order() == 2 * len(stabiliser(runs)), (name, G.order())
            top = apex(runs)[0]
            assert orbit(runs, top[0]) == top                        # where a symmetry exists it fixes the apex
            ctrl[G.order()] = ctrl.get(G.order(), 0) + 1
        say("   SnapPy, on the bundles: all %d have twice as many isometries as the word has symmetries (B1867's law): 8 for the 6 squares, 4 for the 12 others; none is its own mirror" % ok)
        say("   control, the 18 composites with different departures: the same law holds; %s (a reversal exists when the two golden gaps are equal, and it fixes the apex)" % ", ".join("%d have %d isometries" % (v, k) for k, v in sorted(ctrl.items())))

    # ---- 3. the amendment
    say("3. THE AMENDMENT (post hoc at the seat): THREE FACTORS")
    table = {}
    words = [(n_, r, (kind[n_],)) for n_, r in SIX]
    words += [(n1 + n2, a + b, (kind[n1], kind[n2])) for (n1, a), (n2, b) in itertools.product(SIX, SIX)]
    triples = [(n1 + n2 + n3, a + b + c_, (kind[n1], kind[n2], kind[n3])) for (n1, a), (n2, b), (n3, c_) in itertools.product(SIX, SIX, SIX)]
    lead_with6, lead_no6 = [], []
    for name, runs, kds in triples:
        top, h, lead = apex(runs)
        key = kds.count("6")
        table.setdefault(key, [0, 0, 0, 0])
        table[key][0] += 1
        table[key][len(top)] += 1
        if len(top) == 1:
            (lead_with6 if key >= 2 else lead_no6 if key == 0 else []).append(lead)
    assert table == {1: [81, 81, 0, 0], 2: [81, 54, 27, 0], 3: [27, 15, 9, 3], 0: [27, 15, 9, 3]}, table
    tot = [sum(table[k][j] for k in table) for j in range(4)]
    assert tot == [216, 165, 45, 6]
    say("   P1  the 216 ordered triples: %d single, %d with the apex twice, %d three times" % (tot[1], tot[2], tot[3]))
    for key, lab in ((1, "one"), (2, "two"), (3, "three"), (0, "none")):
        say("       factors with the departure (6): %-5s  triples %3d  single %3d  twice %2d  three times %d" % (lab, *table[key]))
    say("       a single triple's lead: %s to %s where two or three runs of 6 compete; %s to %s with no run of 6" % (
        mp.nstr(min(lead_with6), 3), mp.nstr(max(lead_with6), 3), mp.nstr(min(lead_no6), 3), mp.nstr(max(lead_no6), 3)))
    a = dep6(1) + dep6(2)
    assert len(apex(a)[0]) == 2
    back = [len(apex(a + dep2(k))[0]) for k in (1, 2, 3)]
    assert back == [1, 2, 1]
    say("       (6)_1(6)_2 is not single; followed by (2,1,2,1,2)_1 or _3 it is single again, and by (2,1,2,1,2)_2 it is not")
    all258 = words + triples
    assert len(all258) == 258
    nosym = onerev = swaps = 0
    for name, runs, kds in all258:
        S = stabiliser(runs)
        top = apex(runs)[0]
        assert orbit(runs, top[0], S) == top, name                 # the runs at the apex are exactly one orbit
        swaps += any(s % 2 for _, s in S)
        if len(kds) == 3 and len(top) == 1:
            nosym += (len(S) == 1)
            onerev += (len(S) == 2 and S[1][0] == "ref")
    assert swaps == 0 and (nosym, onerev) == (120, 45)
    say("   P2  on all 258 words (6 + 36 + 216) the runs at the apex are exactly one orbit of the symmetries of the cyclic run sequence;")
    say("       of the 165 single triples %d have no symmetry and %d have one reversal, which fixes the apex; no word of the 258 has a symmetry exchanging the letters" % (nosym, onerev))

    # ---- 4. what the referee reported
    say("4. BEYOND THE CARD (the seat's referee's reports, recomputed)")
    for runs, want in (((1, 3, 1, 3, 4, 3), 72), ((2, 2, 1, 3, 3, 1, 1, 3), 196)):
        c = cs(runs)
        top = apex(runs)[0]
        S = stabiliser(runs)
        assert min(c) == want and len(top) == 2 and orbit(runs, top[0], S) != top
        assert orbit(runs, top[0], S) == [top[0]] and orbit(runs, top[1], S) == [top[1]]      # every symmetry fixes each of the two runs
        say("   runs %s (%d letters): the runs %s tie at the apex (c = %d for both); the word's symmetries besides the identity: %s; keeps LR's line: %s" % (
            runs, sum(runs), [runs[i] for i in top], want, [x for x in S if x != ("rot", 0)] or "none", on_line(mat(letters(runs))) is not None))
    # the census: every cyclic run sequence to 18 letters, up to rotation by any number of runs
    seen, total, unexplained, examples = set(), 0, 0, []
    for nletters in range(2, 19):
        for nruns in range(2, nletters + 1, 2):
            for runs in compositions(nletters, nruns):
                key = min(runs[s:] + runs[:s] for s in range(nruns))
                if key in seen:
                    continue
                seen.add(key)
                total += 1
                top = apex(key)[0]
                if len(top) > 1 and orbit(key, top[0]) != top:
                    unexplained += 1
                    if len(examples) < 3:
                        examples.append(key)
    say("   the census: %d cyclic run sequences to 18 letters; in %d the apex is attained by runs that no symmetry of the word relates (the first: %s)" % (total, unexplained, examples))
    assert (total, unexplained) == (15641, 16), (total, unexplained)
    four = sum(1 for q in itertools.product(SIX, repeat=4) if (lambda r: orbit(r, apex(r)[0][0]) != apex(r)[0])(sum((x[1] for x in q), ())))
    assert four == 0
    say("   the 1296 four-factor words of the family: %d with such a tie" % four)
    pairs_ns = [runs for name, runs, kd in same]
    single2 = sum(1 for a_ in pairs_ns for b_ in pairs_ns if len(apex(a_ + b_)[0]) == 1)
    assert single2 == 180
    top, h, lead = apex(dep6(1) + dep6(1) + dep6(3) + dep6(3))
    assert len(top) == 1
    say("   composites of two non-single pairs: %d of the 324 are single; (6)_1(6)_1(6)_3(6)_3 is single, leading by %s" % (single2, mp.nstr(lead, 3)))
    np_leads = []
    for j, k in itertools.permutations((1, 2, 3), 2):
        top, h, lead = apex((2, 1, 3) + (1,) * (2 * j + 1) + (2, 1, 3) + (1,) * (2 * k + 1))
        assert len(top) == 1
        np_leads.append(lead)
    say("   a departure that is not a palindrome: two copies of (2,1,3) with different golden gaps are single, leading by %s to %s" % (mp.nstr(min(np_leads), 2), mp.nstr(max(np_leads), 2)))
    # the record's own two 'mirror' departures
    r1 = (2, 1, 1, 1, 2) + (1,) * 3
    assert letters(r1) == "LLRLR" * 2
    W = mat(letters(r1))
    assert tuple(tuple(x % 5 for x in row) for row in W) == ((4, 0), (0, 4))
    S = [x for x in stabiliser(r1) if x != ("rot", 0)]
    acts = {}
    for k, s in S:
        g, how = matrix_of(r1, k, s)
        acts[(k, s)] = (det(g), on_line(g))
    say("   (2,1,1,1,2) closed by one golden period is LLRLR twice over, and is -1 modulo 5; its symmetries (kind, shift): (det g, g v = c v): %s" % acts)
    assert on_line(mat("LLRLR")) is None
    assert acts == {("ref", 0): (-1, None), ("rot", 4): (1, None), ("ref", 4): (-1, 4)}
    assert apex(r1)[0] == [0, 4]                                    # the two runs of 2; ref 4 exchanges them, ref 0 fixes each
    say("       the deck move acts by LLRLR, which moves the line; the reversal that exchanges the two runs of 2 keeps it (g v = -v); the reversal that fixes each of them moves it")
    for k in (1, 2, 3):
        r2 = (2,) + (1,) * 8 + (2,) + (1,) * (2 * k)
        top = apex(r2)[0]
        S = [x for x in stabiliser(r2) if x != ("rot", 0)]
        assert len(top) == 2 and len(S) == 1 and S[0][0] == "ref" and S[0][1] % 2 == 1
        g, how = matrix_of(r2, *S[0])
        assert det(g) == 1 and how == "inverts" and on_line(g) in (2, 3)
    say("   (2,1^8,2) closed by an even number of golden runs (k = 1, 2, 3): the two runs of 2 are L^2 and R^2 and tie; one symmetry, a reversal that exchanges the letters, det g = +1, g W^-1 g^-1 = W; g v = +-2 v, so it carries the line to its twin")
    say("ALL CHECKS PASS")


def compositions(total, parts):
    """the ordered ways of writing total as a sum of `parts` positive integers"""
    if parts == 1:
        yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


if __name__ == "__main__":
    main()
