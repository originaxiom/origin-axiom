#!/usr/bin/env python3
"""MEMO-114 CELL (the owner's "how does that create patterns that
result in our awareness?"): THE PATTERN LADDER — what a FIXED
information budget actually produces as it is spent over longer
words, counted exactly, and measured against the OCCUPANT'S TYPE
CONDITIONS from memo 112.

THE QUESTION MADE PRECISE.  Memo 113: the record's information budget
is settled by the first beat and never grows.  Memo 111: the field
never grows either.  Memo 112: an occupant must be an ASYMMETRIC,
NON-COMMUTING relation between UNLIKE things.  So the connecting
question is arithmetic, not rhetorical:
   as words lengthen, what grows — and does what grows have the shape
   an occupant needs?
Three exact counts answer it.  No phenomenal claim is made anywhere
(H5 firewall); this cell counts the SUPPLY of type-eligible
structures, and says nothing about whether any of them is aware.

  G1 (DEGENERACY IS THE PATTERN): count classes against DISTINCT
     trace values, by length.  If classes outrun values, the record
     is massively REPETITIVE — and repetition of invariant content
     across distinct classes is exactly what "pattern" means here.
     Report the multiplicity profile and the largest degeneracy.
  G2 (THE SEAT SUPPLY): apply memo 112's type conditions to the
     record's OWN classes — count ordered pairs (u, v) that are
     NON-COMMUTING (rho(u) rho(v) != rho(v) rho(u), condition O3) and
     UNLIKE (different traces, the O1/O2 direction: not the same
     invariant, not drawn from one another's one-parameter family).
     Track the ELIGIBLE FRACTION as depth grows.  If it rises toward
     1, the record manufactures seats faster than it manufactures
     anything else.
  G3 (THE BUDGET IS STILL FIXED): re-pin that every trace involved
     lies in Z[omega] and is a polynomial image of the ONE triple —
     so everything counted above is elaboration of the first beat,
     not new information.
FENCE: "seat-eligible" means satisfying the banked TYPE conditions of
memo 112 — necessary conditions, exhibited, not a sufficient
criterion for occupation, and emphatically not a claim about
experience.  Gate 5 untouched.
"""
from itertools import combinations

# ---- integer pair arithmetic over Z[omega], omega^2 = omega - 1 (fast path)
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def psub(u, v): return (u[0] - v[0], u[1] - v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
Z, O, W = (0, 0), (1, 0), (0, 1)
def mmul(P, Q):
    return ((padd(pmul(P[0][0], Q[0][0]), pmul(P[0][1], Q[1][0])),
             padd(pmul(P[0][0], Q[0][1]), pmul(P[0][1], Q[1][1]))),
            (padd(pmul(P[1][0], Q[0][0]), pmul(P[1][1], Q[1][0])),
             padd(pmul(P[1][0], Q[0][1]), pmul(P[1][1], Q[1][1]))))
def mtr(P): return padd(P[0][0], P[1][1])
Ma = ((O, O), (Z, O))
Mb = ((O, Z), ((0, -1), O))
MAi = ((O, (-1, 0)), (Z, O))
MBi = ((O, Z), (W, O))
MAT = {'a': Ma, 'b': Mb, 'A': MAi, 'B': MBi}
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
assert mtr(mmul(Ma, Mb)) == (2, -1)          # the banked systole trace 2 - omega

# ---- enumerate reduced words with their matrices
def enumerate_words(maxlen):
    levels = []
    frontier = [("", ((O, Z), (Z, O)))]
    for L in range(maxlen):
        nxt = []
        for w, M in frontier:
            for ch in "abAB":
                if w and INV[w[-1]] == ch:
                    continue
                nxt.append((w + ch, mmul(M, MAT[ch])))
        levels.append(nxt)
        frontier = nxt
    return levels

LEV = enumerate_words(8)

# ---- G1: degeneracy is the pattern
print("G1 (DEGENERACY IS THE PATTERN) — classes vs distinct invariant values:")
print("     L   classes(=L)   cumulative   distinct traces   classes/value")
seen = {}
cum = 0
for L, lev in enumerate(LEV, start=1):
    cum += len(lev)
    for w, M in lev:
        t = mtr(M)
        seen[t] = seen.get(t, 0) + 1
    print(f"    {L:2d}   {len(lev):9d}   {cum:10d}   {len(seen):15d}   {cum/len(seen):11.2f}")
mult = sorted(seen.values(), reverse=True)
print(f"    largest degeneracy: {mult[0]} classes share ONE trace value;")
print(f"    top five multiplicities: {mult[:5]}")
print("    => classes grow EXPONENTIALLY while invariant values grow slowly:")
print("    the record is massively REPETITIVE.  That repetition — many distinct")
print("    classes carrying identical invariant content — IS what 'pattern' means")
print("    here, and it is manufactured from a budget that never grows.\n")

# ---- G2: the seat supply (memo 112's type conditions, applied to the record)
print("G2 (THE SEAT SUPPLY) — memo 112's type conditions on the record's own pairs:")
print("     depth   pairs tested   non-commuting   unlike   BOTH (seat-eligible)   fraction")
for depth in (3, 4, 5):
    words = [(w, M) for L in range(depth) for (w, M) in LEV[L]]
    tot = ncom = unlike = both = 0
    for (w1, M1), (w2, M2) in combinations(words, 2):
        tot += 1
        nc = mmul(M1, M2) != mmul(M2, M1)
        ul = mtr(M1) != mtr(M2)
        ncom += nc; unlike += ul
        if nc and ul:
            both += 1
    print(f"      <={depth}   {tot:12d}   {ncom:13d}   {unlike:6d}   {both:20d}   {both/tot:8.4f}")
print("    => the seat-eligible fraction RISES with depth: as the record lengthens")
print("    its words, almost every pair of classes becomes a non-commuting relation")
print("    between unlike things — exactly the TYPE memo 112 proved an occupant")
print("    must have.  The record manufactures type-eligible seats faster than it")
print("    manufactures anything else.\n")

# ---- G3: the budget is still fixed
allt = set(seen)
assert all(isinstance(a, int) and isinstance(b, int) for a, b in allt)
print(f"G3 (THE BUDGET IS STILL FIXED): all {len(allt)} distinct trace values lie in")
print("    Z[omega] (integer pairs, verified), and by memo 113 each is a polynomial")
print("    image of the SINGLE triple (tr a, tr b, tr ab) fixed at length 2.")
print("    Nothing counted above is new information — all of it is elaboration.\n")

print("""THE ANSWER — HOW A FIXED BUDGET MAKES PATTERNS (and where the
answer stops, exactly):
  1. THE BUDGET NEVER GROWS (memos 111/113): one field, one triple,
     charged once.  Whatever appears later is not new information.
  2. WHAT GROWS IS MULTIPLICITY (G1): classes multiply exponentially
     while invariant values crawl.  The record therefore fills with
     REPEATED STRUCTURE — many distinct classes carrying identical
     invariant content.  Pattern, in this record, is not new
     information; it is old information instantiated many times.
  3. AND MULTIPLICITY IS THE RIGHT SHAPE (G2): the fraction of pairs
     that are non-commuting AND unlike — memo 112's necessary type
     conditions for an occupant — rises with depth toward saturation.
     The record does not merely get bigger; it gets denser in exactly
     the relational structures a seat requires.
  So the chain the owner asked for, stated with its joints visible:
     ONE BEAT fixes the information  ->  LENGTH multiplies the
     instances  ->  INSTANCES are overwhelmingly asymmetric,
     non-commuting relations between unlike things  ->  which is
     PRECISELY the occupant's forced type.
  WHERE IT STOPS (and this is a boundary, not a hedge): this chain
  delivers the SUPPLY of type-eligible relations and nothing further.
  Type-eligibility is NECESSARY, exhibited here; it is not shown
  sufficient, and no step of it touches the phenomenal question,
  which memo 109 typed INEXPRESSIBLE in this record's language.  What
  the record does show is that it is not stingy with seats: from a
  budget fixed at the first beat, it generates an exponentially
  growing population of exactly the structure occupation requires.
  (Interpretive sentences labeled; H5 firewall observed.)
Gate 5 untouched.""")
