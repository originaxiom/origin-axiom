#!/usr/bin/env python3
"""B1872 -- 'all allowed histories together': the web seat's exact facts at level 5, re-derived by main (integers only; data-free).

The owner's confirmed ruling puts the claim on all allowed histories together.  The web seat defined 'together' as the joint
action of the allowed histories on the shared records -- the group they generate -- and backed its relay with eleven exact
facts.  B1868 recomputed the first seven.  This file recomputes the other four with main's own code, and for the one that is a
statement about an infinite group (the index of a subgroup of PSL(2, Z)) it uses another instrument than the seat's: sympy's
coset enumeration on the presentation < s, u | s^2, u^3 >.

The seat's letters: L = [[1,0],[1,1]], R = [[1,1],[0,1]] on column vectors.  The marked line is +-v with v spanning LR's eigenline.

    python3 -B frontier/B1872_all_histories_together_the_exact_facts_verified/verification/together_facts.py
"""
import itertools

say = print
Lm, Rm, I2 = ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((1, 0), (0, 1))


def mul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
def word(w):
    M = I2
    for c in w: M = mul(M, Lm if c == "L" else Rm)
    return M
def act(M, v, N=5): return ((M[0][0] * v[0] + M[0][1] * v[1]) % N, (M[1][0] * v[0] + M[1][1] * v[1]) % N)
def neg(v, N=5): return ((-v[0]) % N, (-v[1]) % N)
def mod(M, N=5): return tuple(tuple(x % N for x in r) for r in M)


# the marked line: LR's eigenline at level 5
LR = word("LR")
eig = [v for v in itertools.product(range(5), repeat=2) if v != (0, 0) and act(LR, v) in (v, neg(v))]
v0 = min(eig)
keeps_line = lambda M: act(M, v0) in (v0, neg(v0))
keeps_twins = lambda M: keeps_line(M) and act(M, ((2 * v0[0]) % 5, (2 * v0[1]) % 5)) in (((2 * v0[0]) % 5, (2 * v0[1]) % 5), ((-2 * v0[0]) % 5, (-2 * v0[1]) % 5))
say("the marked line: LR mod 5 = %s keeps the points %s, acting by -1 on them: %s; the line is +-%s and its twin +-%s" % (
    mod(LR), sorted(eig), all(act(LR, v) == neg(v) for v in eig), v0, ((2 * v0[0]) % 5, (2 * v0[1]) % 5)))
assert len(eig) == 4 and all(act(LR, v) == neg(v) for v in eig)

# ------------------------------------------------------------------ F9: the two readings allow different words
pos = ["".join(t) for n in range(1, 13) for t in itertools.product("LR", repeat=n)]
keep = [w for w in pos if keeps_line(word(w))]
def is_charge_form(w):
    """E followed by golden periods: w = E (LR)^k with k >= 0 and E a positive word (possibly empty) that is +-1 mod 5"""
    k = 0
    while True:
        E = w[: len(w) - 2 * k]
        if w[len(E):] != "LR" * k: return False
        M = mod(word(E))
        if M in (mod(I2), mod(((-1, 0), (0, -1)))): return True
        k += 1
        if 2 * k > len(w): return False
charge = [w for w in keep if is_charge_form(w)]
say("F9. positive words of 1 to 12 letters that keep the line: %d; of those, a word that is +-1 mod 5 (possibly empty) followed by golden periods: %d" % (len(keep), len(charge)))
# REVIEW 78 (2026-11-11), its reader's finding, checked by main: the line printed here before, "every one of them keeps the twin line
# as well: True", was not a fact about the 694.  The twin is twice the mark, so a matrix that keeps +-v keeps +-2v by linearity, and
# the check could not fail.  It is kept as what it is, an identity, and the count that is not an identity is put beside it: the
# words that keep LR's eigenline as a set of four points, and how many of those exchange the mark with its twin.
twin = ((2 * v0[0]) % 5, (2 * v0[1]) % 5)
assert all(keeps_twins(word(w)) for w in keep) and twin == act(((2, 0), (0, 2)), v0)       # the identity, by linearity
set_keep = [w for w in pos if act(word(w), v0) in eig]
exchange = [w for w in set_keep if act(word(w), v0) in (twin, neg(twin))]
say("    (that every one of them keeps the twin as well is an identity and not a count: the twin is twice the mark)")
say("    what is a count: positive words of 1 to 12 letters that keep LR's eigenline as a set of four points: %d; of those %d keep the mark +-v and %d carry it to its twin (first: %s)" % (
    len(set_keep), len(keep), len(exchange), exchange[0] if exchange else "none"))
assert (len(keep), len(charge)) == (694, 204) and len(set_keep) == len(keep) + len(exchange)

# ------------------------------------------------------------------ F10: a thread's own line moves with its base point
def necklace(w): return min(w[s:] + w[:s] for s in range(len(w)))
cyc = sorted({necklace(w) for w in pos if len(w) >= 2 and "L" in w and "R" in w}, key=lambda u: (len(u), u))
tr2 = [w for w in cyc if (word(w)[0][0] + word(w)[1][1]) % 5 in (2, 3)]
none = [w for w in tr2 if not any(keeps_line(word(w[s:] + w[:s])) for s in range(len(w)))]
say("F10. cyclic words of 2 to 12 letters with trace +-2 mod 5: %d; with no rotation that keeps the marked line: %d (first: %s)" % (len(tr2), len(none), none[0]))
assert (len(tr2), len(none), none[0]) == (330, 23, "LLLRLRRR")

# ------------------------------------------------------------------ F11: one thread from its two base points keeps no line jointly
def group(gens, N=5):
    seen = {mod(I2, N)}; fr = [mod(I2, N)]
    while fr:
        nx = []
        for a in fr:
            for g in gens:
                x = mod(mul(a, g), N)
                if x not in seen: seen.add(x); nx.append(x)
        fr = nx
    return seen
say("F11. the group generated mod 5 by LR and RL has %d elements (all of SL(2, F5)): read from its two base points one thread keeps no line jointly" % len(group([word("LR"), word("RL")])))
assert len(group([word("LR"), word("RL")])) == 120

# ------------------------------------------------------------------ F8: four charge-invisible histories generate the line's whole stabiliser in PSL(2, Z)
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup

Fg, s, u = free_group("s, u")
PSL = FpGroup(Fg, [s ** 2, u ** 3])
S, U = ((0, -1), (1, 0)), ((0, -1), (1, 1))                                      # S of order 2 and U = S R of order 3 in PSL(2, Z)
pm = lambda A, B: A == B or A == tuple(tuple(-x for x in r) for r in B)
assert pm(mul(S, S), I2) and pm(mul(mul(U, U), U), I2) and pm(mul(S, Rm), U)
# R = S^-1 U = S U in PSL; L = its transpose: found here by search over short words, and checked as matrices up to sign
def find(M):
    for n in range(1, 7):
        for t in itertools.product("su", repeat=n):
            X = I2
            for c in t: X = mul(X, S if c == "s" else U)
            if pm(X, M): return "".join(t)
wR, wL = find(Rm), find(Lm)
say("F8. in PSL(2, Z) = < s, u | s^2, u^3 >: R = %s and L = %s (checked as matrices up to sign)" % (wR, wL))
sym = {"s": s, "u": u}
def elt(w):
    """a positive word in L, R as an element of the free group on s, u"""
    out = Fg.identity
    for c in w:
        for d in (wL if c == "L" else wR): out = out * sym[d]
    return out
def index(words):
    C = PSL.coset_enumeration([elt(w) for w in words], max_cosets=20000)
    C.compress()
    return len(C.table)
gens_a = ["LLLLLLR" + "LR" * k for k in (1, 2)] + ["LRRRRRR" + "LR" * k for k in (1, 2)]
assert all(keeps_line(word(w)) for w in gens_a)
# REVIEW 78 (2026-11-11), its reader's finding, checked by main: the findings called all four "histories that the charge reading
# allows", and this file's own test of the charge reading's word form says False for two of them.  What holds, each part checked:
SWAP = str.maketrans("LR", "RL")
word_form = [is_charge_form(w) for w in gens_a]
mirror_form = [any(is_charge_form((w[t:] + w[:t]).translate(SWAP)) for t in range(len(w))) for w in gens_a]
powers = [mod(word("LR" * k)) for k in range(1, 11)]
assert word_form == [True, True, False, False] and mirror_form[2:] == [True, True] and all(mod(word(w)) in powers for w in gens_a)
say("    of the four: L^6 R (LR)^k is of the charge reading's word form (a positive word that is +-1 mod 5, then golden periods); L R^6 (LR)^k is not,")
say("    and is that form's image under the exchange of the letters, read as a cyclic word; all four are a power of LR mod 5")
ia = index(gens_a)
ctl = index(["L", "R"])                                                          # the control: the whole group has index 1
ctl2 = index(["LL", "R"])                                                        # a known answer: < L^2, R > is of index 3 in PSL(2, Z)
G5 = group([Lm, Rm])
stab5 = [g for g in G5 if act(g, v0) in (v0, neg(v0))]
stab_index = (len(G5) // 2) // (len(stab5) // 2)                                 # up to sign; reduction mod 5 is onto, so this is the index in PSL(2, Z)
assert (len(G5), len(stab5), stab_index) == (120, 10, 12) and mod(((-1, 0), (0, -1))) in stab5
say("    the four histories L^6 R (LR)^k and L R^6 (LR)^k, k = 1, 2, each keeping the line, generate a subgroup of index %d; the line's stabiliser has index %d, computed (%d of the %d elements mod 5 keep +-v, and -1 is among them)" % (ia, stab_index, len(stab5), len(G5)))
say("    controls of the instrument: < L, R > has index %d; < L^2, R > has index %d" % (ctl, ctl2))
# Review 78: the mark as one twin (+-v, or +-2v: the same group, by the identity above) against the mark as the whole eigenline.
# (The record's words: a line of order 5 is a point v up to sign; its twin is 2v; an eigenline is the group of order 5 that holds one pair of twins.)
line5 = [g for g in G5 if act(g, v0) in eig]
line_index = (len(G5) // 2) // (len(line5) // 2)
assert (len(line5), line_index) == (20, 6) and set(stab5) < set(line5)
say("    the mark as the whole eigenline (both twins as one datum) instead of one twin: %d of the %d elements mod 5 keep the four points as a set, a stabiliser of index %d; so 'one twin or both' changes what is allowed, and 'which twin' does not" % (len(line5), len(G5), line_index))
assert ia == 12 and ctl == 1 and ctl2 == 3
# and with one sign only: in SL(2, Z) the histories that are +1 mod 5 generate a group that does not contain -1 -- seen mod 5
g_plus = group([word(w) for w in gens_a])
say("    as matrices mod 5 those four generate a group of %d elements; it contains -1: %s; the line's stabiliser mod 5 has 10" % (len(g_plus), mod(((-1, 0), (0, -1))) in g_plus))
