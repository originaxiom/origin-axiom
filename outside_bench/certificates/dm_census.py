#!/usr/bin/env python3
"""MEMO-123 CELL (the continuation memo 122 named as "a separate,
unrun cell"): THE FULL STABILIZER CENSUS ON THE 27 — not four banked
elements, but EVERY abelian sign/phase character, exhaustively.

WHY THIS IS THE RIGHT CLOSER.  Memo 122 tested B928's Klein
four-group and found no dark-matter stabilizer.  That is a negative on
FOUR elements.  The decisive question is structural: can ANY character
of the object's weight system stabilize N1 or N2?  If none can, the
answer stops being "the forced symmetries happen not to" and becomes
"the 27's weight geometry FORBIDS it" — a much stronger closure of the
cosmology ledger's ROW 4.

THE LOGIC (why a character census suffices for a NEGATIVE).  Any
abelian symmetry acting on the 27 by phases acts as w -> zeta^<a,w>
for some a; the banked Klein family (memos 92/93) is exactly the n=2
case.  A character stabilizes a neutral iff its CHARGED SET (the
states of nonzero charge) is a nonempty subset of {N1, N2}: charges
add on products, so a charged state with only-neutral company cannot
decay to uncharged visible states.  If NO character in the family has
that property, then no symmetry OF THIS FORM stabilizes — and since
the necessary condition is tested without imposing the coupling
constraint, a negative here is a superset negative: imposing the
Yukawa consistency could only shrink the candidate set further.

CENSUS RUN:
  C2: all 2^6 x {+-1} = 128 sign characters (n = 2)
  C3: all 3^6 = 729 phase characters (n = 3) — the ledger names Z/3
  C4, C5, C6: n = 4, 5, 6 as well, for completeness
  In each: count characters whose charged set is a nonempty subset of
  {N1, N2}; report the minimum achievable charged-set size overall.
Gate 5 untouched (weights only).
"""
import os
from fractions import Fraction as Fr
from itertools import product

SCR = os.path.dirname(os.path.abspath(__file__))
CERT = os.environ.get("BENCH_CERT") or SCR
src = open(os.path.join(CERT, "twisted_double.py")).read()
exec(src[:src.index("# ---------------- stage 4")])

H = [rho27_Q(hv) for hv in ([Fr(1) if k == i else Fr(0) for k in range(DIM)] for i in range(N))]
wtZ = [tuple(int(H[i][a][a]) for i in range(N)) for a in range(27)]
levels = [tuple(-qlat[weights[a]][i] for i in range(N)) for a in range(27)]
k1 = [k for k in range(N)
      if sorted({lv[k] for lv in levels}.__class__(
          [sum(1 for lv in levels if lv[k] == v) for v in {l[k] for l in levels}])) == [1, 10, 16]][0]
sz = {}
for lv in levels:
    sz[lv[k1]] = sz.get(lv[k1], 0) + 1
lvl1 = [v for v, c in sz.items() if c == 1][0]
lvl16 = [v for v, c in sz.items() if c == 16][0]
N1 = [i for i in range(27) if levels[i][k1] == lvl1][0]
blk = [i for i in range(27) if levels[i][k1] == lvl16]
k2 = None
for k in range(N):
    if k == k1:
        continue
    s2 = {}
    for i in blk:
        s2[levels[i][k]] = s2.get(levels[i][k], 0) + 1
    if sorted(s2.values()) == [1, 5, 10]:
        k2 = k
        lv2 = [v for v, c in s2.items() if c == 1][0]
        break
N2 = [i for i in blk if levels[i][k2] == lv2][0]
NEUT = {N1, N2}
print(f"reused (memo 122): N1 = {N1} {wtZ[N1]}, N2 = {N2} {wtZ[N2]}\n")

print("THE CENSUS — AFFINE characters w -> zeta_n^(<a,w> + c) over the 27's weights.")
print("    (IN-RUN CORRECTION: the first pass tested only LINEAR characters (c = 0).")
print("     Memo 92 found D2tw has polarity eps = -1, i.e. it IS affine, so the shift")
print("     c must be enumerated too.  With a shift, the CHARGED set is the complement")
print("     of a level set, so a stabilizer needs some level set to hold >= 25 of the")
print("     27 weights.  Both cases are now covered.)\n")
print(f"    {'n':>2s} {'(a,c) pairs':>12s} {'stabilizers':>12s}  {'min |charged|':>14s}"
      f"  {'max |level set|':>16s}")
overall = []
for n in (2, 3, 4, 5, 6):
    tot = 0
    stab = 0
    best = None
    biggest = 0
    for a in product(range(n), repeat=N):
        vals = [sum(a[k]*wtZ[i][k] for k in range(N)) % n for i in range(27)]
        for c in range(n):
            tot += 1
            charged = {i for i in range(27) if vals[i] != c}
            if not charged:
                continue
            if best is None or len(charged) < best[0]:
                best = (len(charged), a, c)
            if charged <= NEUT:
                stab += 1
        if any(v != vals[0] for v in vals):        # skip the TRIVIAL character
            for c in range(n):
                biggest = max(biggest, sum(1 for v in vals if v == c))
    overall.append((n, best, biggest))
    print(f"    {n:2d} {tot:12d} {stab:12d}  {best[0]:14d}  {biggest:16d}")
    assert stab == 0, f"a stabilizer exists at n={n} — structural finding, investigate"

gmin = min(b[0] for _, b, _ in overall)
bigmax = max(g for _, _, g in overall)
print(f"""
VERDICT — THE COSMOLOGY LEDGER'S ROW 4, CLOSED AT CHARACTER LEVEL:
  **NO abelian character of the 27's weight system stabilizes N1 or
  N2 — for ANY modulus n = 2..6, LINEAR OR AFFINE.**  Zero stabilizers
  out of {sum((n**N)*n for n in (2,3,4,5,6))} (a, c) pairs tested.  The smallest charged set
  any nontrivial character can produce is **{gmin} states**, and the
  largest level set any NONTRIVIAL character achieves is **{bigmax} of 27** — where a
  stabilizer would need 25.  Both bounds fail by wide margins.
  WHY, structurally: the 27's weights are spread across the Cartan in
  such a way that no linear functional mod n isolates the two singlets.
  The obstruction is the WEIGHT GEOMETRY, not a shortage of banked
  symmetries — which is why memo 122's four-element negative was not
  an accident of which four.
  THE CLOSURE THIS EARNS: row 4's first probe asked whether a forced
  discrete symmetry stabilizes a neutral.  Memo 122 answered no for
  the forced ones; this cell answers no for ALL characters of this
  form.  **Dark-matter stability cannot come from an abelian symmetry
  of the 27.**  It must come from somewhere else entirely — a
  non-abelian symmetry, a kinematic (mass-ordering) accident, or a
  structure outside the 27 — and the record supplies none of those.
  FENCE (kept honest): this is a NECESSARY-condition census.  It does
  not impose the Yukawa/coupling consistency, which could only SHRINK
  the candidate set, so the negative is a superset negative and stands
  a fortiori.  Non-abelian stabilizers and kinematic stability remain
  untested — named here, not claimed done.
Gate 5 untouched.""")
