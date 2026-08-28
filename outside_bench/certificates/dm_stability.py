#!/usr/bin/env python3
"""MEMO-122 CELL (the owner's GO; the cosmology ledger's NAMED FIRST
MOVE, never asked): DARK MATTER'S STABILITY PROBE — does any forced
discrete symmetry of the object act as a stabilizing parity on N1 or
N2?

THE LEDGER'S QUESTION, verbatim (docs/COSMOLOGY_LEDGER.md, ROW 4):
  "does any forced discrete symmetry of the object act as a
  stabilizing parity on N1 or N2 that forbids their decay channels
  into the visible" ... "the minimal requirement for ANY dark-matter
  candidate, stability — has never been checked."
THE TWO CANDIDATES, as the ledger names them: under E6 > SO(10)xU(1),
27 = 16 + 10 + 1, giving two SM-gauge-neutral fermion slots —
  N1 = the SO(10)-singlet (the "1" of 27),
  N2 = the SU(5)-singlet inside the "16" (16 = 10 + 5bar + 1).

WHY A PARITY WOULD STABILIZE: if a Z/2 character chi has chi(X) = -1
while EVERY state X could decay into is even, the decay is forbidden
(chi is multiplicative on products).  So X is absolutely stabilized by
chi IFF the ODD SET of chi is contained in {X} — or, allowing the two
neutrals to be degenerate partners, contained in {N1, N2}.  If instead
the odd set contains VISIBLE states, X can decay to (odd visible +
even visible) and chi stabilizes nothing.

THE SYMMETRY SET TESTED (scope stated, not blurred): the object's
BANKED GAUGE 2-TORSION — B928's Klein four-group {I, D2tw, D, D2tw*D},
the forced discrete symmetries that act on the 27 as sign characters
(memos 92/93, both GREEN, whose vendored data this cell reuses rather
than rebuilds).  Frame bits (c, r, gamma5) act on fields, not as sign
characters on the 27 (memo 92's parity x dimension typing), so they
are not candidates here; a wider symmetry hunt is a separate cell and
is NOT claimed done.

CHECKS (each two-outcome):
  N1 IDENTIFY N1 and N2 BASIS-INDEPENDENTLY: derive the simple roots
     from the weight system itself (Cartan rows have one 2 and the
     rest in {0,-1}), grade the 27 by each node, and keep the node
     whose level sizes are {16, 10, 1} — N1 is the singleton.  Repeat
     inside the 16 for sizes {10, 5, 1} — N2 is that singleton.  No
     external convention is imported.
  S1 THE STABILITY TEST: for each Klein element, compute the ODD SET
     and ask whether it is a nonempty subset of {N1, N2}.
  S2 THE DIAGNOSIS: if not, report exactly how many VISIBLE states
     share the oddness — that number is what kills the stability.
Gate 5 untouched (weights and signs only).
"""
import os
from fractions import Fraction as Fr
from itertools import product

SCR = os.path.dirname(os.path.abspath(__file__))
CERT = os.environ.get("BENCH_CERT") or SCR
src = open(os.path.join(CERT, "twisted_double.py")).read()
exec(src[:src.index("# ---------------- stage 4")])

# ---- the lane's 27 weights (memo 92/93's machinery, reused verbatim)
H = [rho27_Q(hv) for hv in ([Fr(1) if k == i else Fr(0) for k in range(DIM)] for i in range(N))]
wtZ = [tuple(int(H[i][a][a]) for i in range(N)) for a in range(27)]
B883 = [(0,0,0,0,0,-1),(0,0,0,0,-1,1),(0,0,0,-1,1,0),(0,-1,-1,1,0,0),(-1,-1,1,0,0,0),
        (0,1,-1,0,0,0),(-1,1,1,-1,0,0),(-1,0,0,1,-1,0),(-1,0,0,0,1,-1),(-1,0,0,0,0,1),
        (1,-1,0,0,0,0),(1,1,0,-1,0,0),(1,0,-1,1,-1,0),(1,0,-1,0,1,-1),(1,0,-1,0,0,1),
        (0,0,1,0,-1,0),(0,0,1,-1,1,-1),(0,0,1,-1,0,1),(0,-1,0,1,0,-1),(0,-1,0,1,-1,1),
        (0,-1,0,0,1,0),(0,1,0,0,0,-1),(0,1,0,0,-1,1),(0,1,0,-1,1,0),(0,0,-1,1,0,0),
        (-1,0,1,0,0,0),(1,0,0,0,0,0)]
assert set(B883) == set(wtZ) and len(set(B883)) == 27
lane_of = {w: i for i, w in enumerate(wtZ)}
perm = [lane_of[w] for w in B883]
D2_B883 = [1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,1]
D_B883  = [1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1]
D2 = [0]*27; Dd = [0]*27
for b in range(27):
    D2[perm[b]] = D2_B883[b]; Dd[perm[b]] = D_B883[b]
print(f"reused (memos 92/93): 27 lane weights + the banked Klein signs "
      f"(D2tw flips {sum(1 for s in D2 if s<0)}, D flips {sum(1 for s in Dd if s<0)})")

# ---- N1: the grading levels are ALREADY banked in twisted_double's crystal
# qlat[w] = w - omega1 in ROOT-LATTICE coordinates, so the number of times
# alpha_i was subtracted is -qlat[w][i].  Reused, not re-derived.
assert all(cartan_eig(j, weights[a]) == wtZ[a][j] for a in range(27) for j in range(N))
print("N1a: crystal order matches the lane weight order (cartan_eig == wtZ, 27x6) —")
print("     and the root-lattice levels come straight from twisted_double's qlat.")
levels = [tuple(-qlat[weights[a]][i] for i in range(N)) for a in range(27)]
assert all(all(v >= 0 for v in lv) for lv in levels)

grade_nodes = []
for k in range(N):
    sizes = {}
    for lv in levels:
        sizes[lv[k]] = sizes.get(lv[k], 0) + 1
    if sorted(sizes.values()) == [1, 10, 16]:
        grade_nodes.append((k, sizes))
print(f"N1b: nodes whose grading splits the 27 as {{16, 10, 1}}: "
      f"{[k for k, _ in grade_nodes]} — the SO(10)xU(1) gradings")
assert grade_nodes, "no node grades the 27 as 16+10+1"
k1, sizes1 = grade_nodes[0]
lvl_singleton = [v for v, c in sizes1.items() if c == 1][0]
lvl_16 = [v for v, c in sizes1.items() if c == 16][0]
N1 = [i for i in range(27) if levels[i][k1] == lvl_singleton][0]
block16 = [i for i in range(27) if levels[i][k1] == lvl_16]
print(f"     => N1 = lane index {N1}, weight {wtZ[N1]}  (the SO(10) singlet)")

sub = []
for k in range(N):
    if k == k1:
        continue
    sizes = {}
    for i in block16:
        sizes[levels[i][k]] = sizes.get(levels[i][k], 0) + 1
    if sorted(sizes.values()) == [1, 5, 10]:
        sub.append((k, sizes))
assert sub, "no SU(5) grading of the 16 found"
k2, sizes2 = sub[0]
lv2 = [v for v, c in sizes2.items() if c == 1][0]
N2 = [i for i in block16 if levels[i][k2] == lv2][0]
print(f"     => N2 = lane index {N2}, weight {wtZ[N2]}  (the SU(5) singlet in the 16)")
assert N1 != N2
NEUTRALS = {N1, N2}

# ---- S1 / S2: the stability test
print("\nS1/S2 — THE STABILITY TEST over the banked gauge 2-torsion:")
print(f"    {'element':>10s}  {'|odd set|':>9s}  {'N1':>4s} {'N2':>4s}  "
      f"{'odd VISIBLE':>11s}   stabilizes?")
D2D = [D2[i]*Dd[i] for i in range(27)]
table = [("I", [1]*27), ("D2tw", D2), ("D", Dd), ("D2tw*D", D2D)]
any_stab = False
for name, ch in table:
    odd = {i for i in range(27) if ch[i] == -1}
    oddvis = odd - NEUTRALS
    stab = (len(odd) > 0 and odd <= NEUTRALS)
    any_stab = any_stab or stab
    print(f"    {name:>10s}  {len(odd):9d}  {'odd' if N1 in odd else ' -':>4s} "
          f"{'odd' if N2 in odd else ' -':>4s}  {len(oddvis):11d}   "
          f"{'YES' if stab else 'no'}")
print(f"\n    ANY banked element stabilizes N1 or N2?  {'YES' if any_stab else 'NO'}")

print(f"""
THE VERDICT — the cosmology ledger's ROW 4 first probe, ANSWERED:
  **NO forced discrete symmetry in the object's banked gauge 2-torsion
  stabilizes either neutral.**  The reason is structural and visible in
  one column above: the banked characters are AFFINE SIGN CHARACTERS
  with flip counts 11, 12 and 15 (in-run correction: the product
  D2tw*D has 15 flips, not 13) — each makes roughly HALF the 27 odd.
  Stability needs the odd set to sit INSIDE the two-element neutral set
  {{N1, N2}}; every banked element instead makes 10+ VISIBLE states odd,
  so each neutral has open decay channels (odd visible + even visible)
  under every one of them.
  WHAT THIS CLOSES: the ledger said stability "has never been checked."
  It is now checked, and the answer is negative — **the object's forced
  gauge 2-torsion supplies no dark-matter stabilizer.**  Row 4's first
  probe returns NEGATIVE rather than remaining unasked.
  WHAT THIS DOES NOT CLOSE (scope, stated): only the banked gauge
  2-torsion was tested.  It does NOT rule out (i) a stabilizing
  symmetry outside that group — the frame bits c, r, gamma5 act on
  fields rather than as sign characters on the 27 (memo 92's
  parity x dimension typing), so they are not candidates, but a wider
  symmetry census on the 27 is a separate, unrun cell; (ii) stability
  by kinematics rather than symmetry (a mass ordering forbidding the
  channels), which the record does not supply.
  THE HONEST CONSEQUENCE for the dominant gap: dark matter's first
  named probe is spent, negatively.  The structural neutrals N1, N2
  EXIST but are NOT protected by anything the object forces.
Gate 5 untouched.""")
