#!/usr/bin/env python3
"""MEMO-98 CELL: THE FOUNDING TORSOR, VERIFIED — independent bench
verification of cc's basepoint theorem (B1083 / THE_FORCED_AND_THE_FREE
/ the founding-bit answer relayed 2026-08-28), at the exactly
computable level, with two sharp lane additions.

CC'S CLAIM (relayed; verified here from scratch): writing the founding
rule sigma: a->ab, b->a was a BASEPOINT-TAKING — the four natural
substitution rules form a free, transitive K4-torsor under C (the
a<->b letter swap) and P (reading-direction/word reversal), with
trivial stabilizer; the two spendable founding bits are C and P; THE
ARROW IS NOT ONE OF THEM (B1083: the arrow = monoid non-surjectivity,
not a torsor bit).

VERIFIED HERE (all exact):
  FACT 1 (the torsor): K4 = {1, C, P, CP} with C(s) = swap o s o swap,
     P(s) = rev o s is a group action on substitution rules (C^2 = P^2
     = (CP)^2 = id, C P = P C — verified on words); the orbit of the
     founding rule is EXACTLY the four rules {(ab,a), (ba,a), (b,ba),
     (b,ab)} — four DISTINCT elements: free + transitive, trivial
     stabilizer.  cc's torsor claim REPRODUCED from scratch.
  FACT 2 (the A-level shadow of "the axioms cannot distinguish"): all
     four rules abelianize to matrices with the SAME char poly
     x^2 - x - 1; moreover P is ABELIANIZATION-INVISIBLE (P fixes the
     abelianized matrix exactly) and C acts by swap-conjugation.
  FACT 3 (LANE ADDITION — P is CHARACTER-INVISIBLE, proved + machine-
     checked): word reversal fixes the Fricke coordinates (x, y fixed;
     tr(ba) = tr(ab) by cyclicity), and every word's trace is a
     polynomial in (x,y,z) — so P acts TRIVIALLY on the whole SL(2)
     character variety.  Machine check: with m004's exact holonomy
     matrices over Z[omega] (Riley rep, verified against the banked
     systole trace), tr(w) = tr(rev(w)) for ALL 1364 words of length
     <= 5 over {a, b, a^-1, b^-1}.
  FACT 4 (LANE ADDITION — the branch bit is invisible to BOTH founding
     bits): at the Fricke level C acts as s: (x,y,z) -> (y,x,z), which
     memo 97 proved does not swap the branches; P acts trivially
     (FACT 3), so it cannot swap anything.  THE BRANCH Z/2 IS NEITHER
     FOUNDING BIT — it is not C, not P (and not c, memo 97): new
     input to the branch->r identification cell (cc's batch), from the
     word level.
  FACT 5 (the arrow is not a torsor bit — the computable shadow):
     sigma is NON-SURJECTIVE as a monoid endomorphism: every image
     word starts with the letter a (first-letter induction, verified
     by exhaustive enumeration of the image submonoid to composition
     depth 6), so the letter b is not in the image — sigma has no
     inverse substitution.  The arrow = this non-invertibility (order,
     memo 86), NOT a K4 coordinate — cc's re-typing confirmed.
Gate 5 untouched (words, matrices, exact arithmetic).
"""
import os
from fractions import Fraction as Fr
from itertools import product

# ---------------- words as tuples of letters: 'a','b','A','B' (A = a^-1)
def rev(w):
    return tuple(reversed(w))
def swap(w):
    m = {'a': 'b', 'b': 'a', 'A': 'B', 'B': 'A'}
    return tuple(m[c] for c in w)

# a substitution rule = (image of a, image of b), positive words
R0 = (('a', 'b'), ('a',))            # sigma: a -> ab, b -> a
def actC(rule):
    ia, ib = rule
    return (swap(ib), swap(ia))      # C(s) = swap o s o swap: new a-image = swap(s(b))
def actP(rule):
    ia, ib = rule
    return (rev(ia), rev(ib))        # P(s) = rev o s

# FACT 1: group law + the orbit
r_C = actC(R0); r_P = actP(R0); r_CP = actC(actP(R0))
assert actC(actC(R0)) == R0 and actP(actP(R0)) == R0
assert actC(actP(R0)) == actP(actC(R0))
assert actC(actC(r_P)) == r_P
orbit = {R0, r_C, r_P, r_CP}
assert len(orbit) == 4, orbit
labels = {R0: "founding (ab, a)", r_P: "mirror (ba, a)", r_C: "swapped", r_CP: "fourth"}
assert r_P == (('b', 'a'), ('a',))                       # a -> ba, b -> a  (the mirror rule)
assert r_C == (('b',), ('b', 'a'))                       # a -> b,  b -> ba (the swapped rule)
assert r_CP == (('b',), ('a', 'b'))                      # a -> b,  b -> ab (the fourth)
print("FACT 1: K4 = {1, C, P, CP} verified (involutions, commuting); the orbit of")
print("   the founding rule = 4 DISTINCT rules {(ab,a), (ba,a), (b,ba), (b,ab)}:")
print("   FREE + TRANSITIVE, trivial stabilizer — cc's torsor claim REPRODUCED.")

# FACT 2: abelianizations
import sympy as sp
def abel(rule):
    ia, ib = rule
    ca = (sum(1 for c in ia if c == 'a'), sum(1 for c in ia if c == 'b'))
    cb = (sum(1 for c in ib if c == 'a'), sum(1 for c in ib if c == 'b'))
    return sp.Matrix([[ca[0], cb[0]], [ca[1], cb[1]]])
X = sp.symbols('X')
cps = {}
for r in (R0, r_P, r_C, r_CP):
    M = abel(r)
    cps[r] = sp.expand(M.charpoly(X).as_expr())
assert all(sp.expand(c - (X**2 - X - 1)) == 0 for c in cps.values())
assert abel(r_P) == abel(R0)                              # P abelianization-invisible
S = sp.Matrix([[0, 1], [1, 0]])
assert abel(r_C) == S*abel(R0)*S                          # C = swap-conjugation
print("FACT 2: all four rules share char poly x^2 - x - 1 (the A-level shadow of")
print("   indistinguishability); P is ABELIANIZATION-INVISIBLE; C = swap-conjugation.")

# FACT 3: P is character-invisible — exact check on m004's holonomy over Z[omega]
# pair-field arithmetic over Q(omega), omega^2 = omega - 1  (the lane's q)
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def pmul(u, v):
    a, b = u; c, d = v
    # (a + b w)(c + d w) = ac + (ad + bc) w + bd w^2,  w^2 = w - 1
    return (a*c - b*d, a*d + b*c + b*d)
ZERO, ONE_ = (Fr(0), Fr(0)), (Fr(1), Fr(0))
W = (Fr(0), Fr(1))
def mmul(A, B):
    return tuple(tuple(padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j]))
                 for j in range(2)) for i in range(2))
def mtr(A): return padd(A[0][0], A[1][1])
# Riley rep of the figure-eight: a = [[1,1],[0,1]], b = [[1,0],[-w,1]]
Ma = ((ONE_, ONE_), (ZERO, ONE_))
Mb = ((ONE_, ZERO), ((-W[0], -W[1]), ONE_))
def minv(A):
    (p, q_), (r_, s_) = A
    det = padd(pmul(p, s_), (-pmul(q_, r_)[0], -pmul(q_, r_)[1]))
    assert det == ONE_, det
    return ((s_, (-q_[0], -q_[1])), ((-r_[0], -r_[1]), p))
MAT = {'a': Ma, 'b': Mb, 'A': minv(Ma), 'B': minv(Mb)}
def ev(w):
    M = ((ONE_, ZERO), (ZERO, ONE_))
    for c in w:
        M = mmul(M, MAT[c])
    return M
# control: the banked systole trace 2 - omega (memo 81's class [AB] = (ab)^-1,
# same trace as ab) reproduced by the vendored Riley matrices:
t = mtr(ev(('a', 'b')))
assert t == (Fr(2), Fr(-1)), t
assert mtr(ev(('A', 'B'))) == t          # tr(w^-1) = tr(w) in SL2
print(f"   control: tr(ab) = tr((ab)^-1) = {t} = 2 - omega — the banked systole")
print("   class trace (memo 81) reproduced exactly by the vendored Riley matrices.")
count = 0
for L in range(1, 6):
    for w in product('abAB', repeat=L):
        assert mtr(ev(w)) == mtr(ev(rev(w))), w
        count += 1
print(f"FACT 3: tr(w) = tr(rev(w)) for ALL {count} words of length <= 5 (exact, Z[omega])")
print("   — P (reading direction) is CHARACTER-INVISIBLE, as the Fricke argument")
print("   proves in general (x, y, z all reversal-fixed; traces are polynomials in them).")

# FACT 4 is a corollary (memo 97's s-verdict + FACT 3); printed as the finding:
print("FACT 4: at the character level C acts as s:(x,y,z)->(y,x,z) [memo 97: does not")
print("   swap the branches] and P acts trivially [FACT 3] => THE BRANCH Z/2 IS")
print("   NEITHER FOUNDING BIT — not C, not P (and not c, memo 97).  Filed to the")
print("   branch->r identification cell (cc's batch) as word-level input.")

# FACT 5: sigma's image submonoid misses b (non-surjectivity, the arrow's home)
def subst(w, rule):
    ia, ib = rule
    out = []
    for c in w:
        out.extend(ia if c == 'a' else ib)
    return tuple(out)
img = {('a',), ('a', 'b')}
frontier_ = set(img)
for depth in range(6):
    new = set()
    for u in frontier_:
        for v in ({('a',), ('a', 'b')} | img):
            uv = u + v
            if len(uv) <= 8 and uv not in img:
                new.add(uv)
    img |= new
    frontier_ = new
assert ('b',) not in img
assert all(w[0] == 'a' for w in img)
print(f"FACT 5: the image submonoid of sigma ({len(img)} words to length 8) contains NO")
print("   word starting with b — in particular b itself is unreachable: sigma is")
print("   NON-SURJECTIVE, hence non-invertible.  The arrow is this monoid fact (order,")
print("   memo 86), NOT a K4 coordinate — cc's B1083 re-typing CONFIRMED.")

print("""
THE FOUNDING TORSOR STANDS, INDEPENDENTLY VERIFIED: the first written
symbol of the programme took exactly one K4-basepoint of choice — four
equivalent founding rules, freely and transitively permuted by the
letter-swap C and the reading-direction P, indistinguishable at the
abelianized level (one golden polynomial for all four) — and the two
lane additions sharpen the map: P is invisible to the entire character
variety (the object cannot even SEE the reading direction), and the
branch bit is neither founding bit.  The owner's oldest question closes
its founding level: a/ab/ba took the bit AT THE FIRST SYMBOL, spendable
as C and P; the arrow was never one of them — it is the substitution's
non-invertibility, exactly where memo 86 priced the order.  Gate 5
untouched.""")
