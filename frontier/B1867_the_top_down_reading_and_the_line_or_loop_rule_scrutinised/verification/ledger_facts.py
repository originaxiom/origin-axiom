#!/usr/bin/env python3
"""B1867, part 2 -- the mathematical facts the advisor seat's forcing ledger and its first back-edge design stand on, recomputed
by main in integers (data-free).  The ledger's grades ("argued FORCED") are arguments; this file checks the facts they cite and
exhibits, in integers, the three places where an argument needs a clause that the formal statement v0 does not contain.

    python3 -B frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/ledger_facts.py
"""
import itertools
import warnings

warnings.filterwarnings("ignore")
say = print
L, R, I2 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
Li, Ri = ((1, -1), (0, 1)), ((1, 0), (-1, 1))


def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def neg(A): return tuple(tuple(-x for x in r) for r in A)
def tr(A): return A[0][0] + A[1][1]
def det(A): return A[0][0] * A[1][1] - A[0][1] * A[1][0]
def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def word(w):
    M = I2
    for c in w: M = mul(M, L if c == "L" else R)
    return M
def mod(A, n): return tuple(tuple(x % n for x in r) for r in A)
def minus_I(A): return ((A[0][0] - 1, A[0][1]), (A[1][0], A[1][1] - 1))
def plus_I(A): return ((A[0][0] + 1, A[0][1]), (A[1][0], A[1][1] + 1))
def necklace(w): return min(w[s:] + w[:s] for s in range(len(w)))


# ---------------------------------------------------------------- A. the ledger's cited facts
say("A. The forcing ledger's cited facts")
M = mul(mul(mul(mul(mul(L, L), L), L), L), Ri)
target = neg(word("LR"))
conj = next(g for g in (((a, b), (c, d)) for a, b, c, d in itertools.product(range(-6, 7), repeat=4) if a * d - b * c == 1) if mul(mul(g, M), inv(g)) == target)
say("  GM5d's alternative: L^5 R^-1 = %s has trace %d; it is conjugate to -LR = %s in SL(2, Z), by g = %s" % (M, tr(M), target, conj))
assert tr(M) == -3 and mul(mul(conj, M), inv(conj)) == target and det(conj) == 1

# every hyperbolic matrix is, up to sign and conjugacy, a positive word with both letters (GM5d's 'normal form')
def positive_word(A):
    """a positive word w and a conjugator g with g (+-A) g^-1 = w, found by search; None if the search fails"""
    A0 = A if tr(A) > 0 else neg(A)
    seen, fr = {A0}, [(A0, I2)]
    cap = 4 * max(abs(x) for r in A0 for x in r) + 8
    while fr:
        nx = []
        for B, g in fr:
            if all(x >= 0 for r in B for x in r):
                w, C = "", B
                while C != I2:                                       # SL(2, N) is the free monoid on L and R: strip letters from the right
                    if C[0][1] >= C[0][0] and C[1][1] >= C[1][0]: C = mul(C, Li); w = "L" + w
                    elif C[0][0] >= C[0][1] and C[1][0] >= C[1][1]: C = mul(C, Ri); w = "R" + w
                    else: return None
                return w, g
            for h in (L, R, Li, Ri):
                C = mul(mul(h, B), inv(h))
                if C not in seen and max(abs(x) for r in C for x in r) <= cap:
                    seen.add(C); nx.append((C, mul(h, g)))
        fr = nx
    return None
hyp = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(-5, 6), repeat=4) if a * d - b * c == 1 and abs(a + d) > 2]
good = 0
for A in hyp:
    r = positive_word(A)
    if r is None: continue
    w, g = r
    A0 = A if tr(A) > 0 else neg(A)
    if "L" in w and "R" in w and det(g) == 1 and mul(mul(g, A0), inv(g)) == word(w): good += 1      # checked, not assumed: g (+-A) g^-1 is the word
say("  GM5d: of the %d hyperbolic matrices with entries between -5 and 5, a positive word with both letters and a conjugator g with g (+-A) g^-1 = the word are found for %d" % (len(hyp), good))
assert good == len(hyp)
assert positive_word(L) is None or "R" not in positive_word(L)[0]                                # the control: a shear is not such a word
neg_count = sum(1 for A in hyp if tr(A) < 0)
say("    (%d of them have negative trace and are minus a positive word: the sign is a separate bit)" % neg_count)

# SE1: the number of fibre characters an act fixes is |det(W - 1)| = |tr - 2|; with the sign, |det(-W - 1)| = tr + 2
words = sorted({necklace("".join(t)) for n in range(2, 13) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t}, key=lambda u: (len(u), u))
fixed = {w: abs(det(minus_I(word(w)))) for w in words}
assert all(fixed[w] == tr(word(w)) - 2 for w in words)
ones = [w for w in words if fixed[w] == 1]
say("  SE1: over the %d cyclic positive words of length 2 to 12 with both letters, the number of fixed fibre characters |det(W - 1)| equals tr - 2 for all; it is 1 for %s only" % (len(words), ones))
say("       with the other sign it is |det(-W - 1)| = tr + 2, never 1: at least %d (so 'no fixed character' also decides the sign left open by positivity)" % min(abs(det(minus_I(neg(word(w))))) for w in words))
assert ones == ["LR"] and all(abs(det(minus_I(neg(word(w))))) == tr(word(w)) + 2 for w in words)
dep = word("LLLLLLRLR")
say("       the run of 6, L^6 R L R: trace %d, so it fixes %d characters; the least over all words other than LR is %d" % (tr(dep), fixed[necklace("LLLLLLRLR")], min(v for w, v in fixed.items() if w != "LR")))
assert tr(dep) == 22 and fixed[necklace("LLLLLLRLR")] == 20
# the trefoil's act: trace 1, order 6, and no fixed character either
T = mul(L, Ri)
P6 = I2
for _ in range(6): P6 = mul(P6, T)
say("       the alternative named beside GM3: L R^-1 = %s has trace %d, order 6 (its sixth power is the identity: %s), and fixes %d character: SE1 alone admits it, and GM3 removes it" % (T, tr(T), P6 == I2, abs(det(minus_I(T)))))
assert tr(T) == 1 and P6 == I2 and abs(det(minus_I(T))) == 1

try:
    import snappy
    hom = {}
    for w in [u for u in words if len(u) <= 9]:
        H = snappy.Manifold("b++" + w).homology()
        tors = 1
        for d in H.elementary_divisors():
            if d != 0: tors *= d
        hom[w] = tors
    agree = sum(1 for w in hom if hom[w] == fixed[w])
    m3 = snappy.Manifold("b+-LR")
    t3 = 1
    for d in m3.homology().elementary_divisors():
        if d != 0: t3 *= d
    say("       SnapPy: the torsion of the bundle's first homology equals that number on %d of %d words of length up to 9; and b+-LR is m003 (%s), with torsion %d = 3 + 2" % (
        agree, len(hom), bool(m3.is_isometric_to(snappy.Manifold("m003"))), t3))
    assert agree == len(hom) and t3 == 5
except ImportError:
    say("       (SnapPy not installed here: the homology cross-check is skipped)")

# ---------------------------------------------------------------- B. three places where an argument needs a clause v0 does not contain
say("B. Where a ledger row needs a clause that the formal statement v0 does not contain (exhibited in integers)")
# 1. GM3: v0 calls an act cancelled when it is the identity or becomes it when repeated.  A shear never becomes the identity,
#    and at every level N its N-th power is read as nothing: it meets v0's own form of 'what exists relative to a ground'.
N = 5
LN = I2
for _ in range(N): LN = mul(LN, L)
say("  1. GM3 (the fixed direction): L^%d = %s is the identity mod %d (%s) and is not the identity (%s); no power of L is the identity. v0's clause removes finite order, not this." % (
    N, LN, N, mod(LN, N) == I2, LN != I2))
assert mod(LN, N) == I2 and LN != I2
# 2. GM4: 'the difference between ab and ba is not cancelled' does not make the group free.
def m3(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def inv3(A):                                                         # upper unitriangular
    a, b, c = A[0][1], A[0][2], A[1][2]
    return ((1, -a, a * c - b), (0, 1, -c), (0, 0, 1))
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
a, b = ((1, 1, 0), (0, 1, 0), (0, 0, 1)), ((1, 0, 0), (0, 1, 1), (0, 0, 1))
com = lambda x, y: m3(m3(x, y), m3(inv3(x), inv3(y)))
c = com(a, b)
say("  2. GM4 (free, not only non-commuting): in the integer Heisenberg group, ab differs from ba (%s), and the commutator commutes with a and b (%s, %s): two acts that do not commute and are not free." % (
    c != E, com(a, c) == E, com(b, c) == E))
assert c != E and com(a, c) == E and com(b, c) == E
# 3. SE1: the same relation with two signs.  At the selection layer a departure exists because the ground's level cannot tell it from
#    the ground; at the foundation an act is excluded because a character cannot tell it from nothing.
g2 = word("LRLR")
say("  3. SE1 (two signs of one relation): the run of 6 equals the golden word LRLR mod 5 (%s): the level cannot tell them apart, and this is what selects it;" % (mod(dep, 5) == mod(g2, 5)))
say("     yet it fixes 20 characters, and every word other than LR fixes at least 2. As an exclusion, 'a fixed character is a place where nothing happened' removes every departure too.")
assert mod(dep, 5) == mod(g2, 5) and min(v for w, v in fixed.items() if w != "LR") == 2

# ---------------------------------------------------------------- C. the first back-edge design's exact facts (its A0)
say("C. The first back-edge design's exact facts")
W = word("LR")
anti = sorted({(x, y) for x in range(5) for y in range(5) if (x, y) != (0, 0) and mod(((W[0][0] * x + W[0][1] * y,), (W[1][0] * x + W[1][1] * y,)), 5) == (((-x) % 5,), ((-y) % 5,))})
say("  |det(LR - 1)| = %d, |det(LR + 1)| = %d; the points of order 5 that LR sends to their inverse (column vectors): %s" % (abs(det(minus_I(W))), abs(det(plus_I(W))), anti))
assert abs(det(minus_I(W))) == 1 and abs(det(plus_I(W))) == 5 and len(anti) == 4
def sign_on_line(w):
    """how the history acts on LR's own line of order 5: '+' fixes it pointwise, '-' inverts it, 'all-' is -1 on all of level 5, else '?'"""
    Wm = mod(word(w), 5)
    if Wm == mod(neg(I2), 5): return "-I"
    v = anti[0]
    img = ((Wm[0][0] * v[0] + Wm[0][1] * v[1]) % 5, (Wm[1][0] * v[0] + Wm[1][1] * v[1]) % 5)
    return "+" if img == v else "-" if img == ((-v[0]) % 5, (-v[1]) % 5) else "?"
rows = (("(6)", "LLLLLL" + "R"), ("(2,1,2,1,2)", "LLRLLRLLR"), ("(2,1,1,1,2)", "LLRLRLLR"), ("golden", "LR"))
for name, head in rows:
    say("    %-12s closed by (LR)^k, k = 1, 2, 3: the action on that line is %s" % (name, [sign_on_line(head + "LR" * k) for k in (1, 2, 3)]))
assert [sign_on_line("LLLLLLR" + "LR" * k) for k in (1, 2, 3)] == ["+", "-", "+"]
assert sign_on_line("LLRLRLLR" + "LR") == "-I"
say("  a flat line on the fibre extends over the history exactly when the history fixes its character; so 'the departure fixes the line' is the condition that the line extends.")
say("  on the golden background no non-trivial character is fixed (|det(LR - 1)| = 1): there the line of order 5 exists only together with its inverse.")
