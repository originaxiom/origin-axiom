#!/usr/bin/env python3
"""MEMO-93 CELL: THE KLEIN GROUP MEETS THE MIRROR — B928's whole
2-torsion {I, D2tw, D, D2tw*D} beat-typed on the lane's 27, and the
"fourth presentation" question (ledger row F5, THE_SECOND_HALF) decided.

BACKGROUND: B928 banks the Klein four-group {I, D2tw, D, D2tw*D} =
+-rho27({1, sigma_chi-, sigma_-1, sigma_chi+}) — the wall pair's whole
2-torsion acting diagonally on the 27.  The campaign's F5 residue asks
whether this Klein group is a FOURTH PRESENTATION of the frame/branch
V4 (B1182: frame V4 = <c, r> ~ branch V4 = Gal(Q(zeta12)/Q), one
named-action torsor).  The wave-1 klein lane found the comparison
ill-posed in the main corpus (no action of c on the 27 there) — but
the lane HAS the mirror's action (the beat), so the decisive relation
IS computable: does the Klein group CENTRALIZE the mirror realization,
or does it CONTAIN mirror-odd elements?
  * If ALL FOUR elements are beat-even, the Klein group lies inside
    the mirror's centralizer on the 27 — it cannot realize the frame
    V4 (whose defining leg IS the mirror): the fourth-presentation
    hypothesis is REFUTED-AS-IDENTIFICATION; the two Klein groups are
    TRANSVERSE (one is gauge-sector, mirror-even; the other is built
    on the mirror leg).  F5's remaining question closes.
  * If some element is beat-broken, the groups interlock — banks as a
    structure finding and the overlap is computed.
VENDORED DATA (verbatim, provenance main @ B1187):
  B883 rep27.json 'weights' — the 27 weights in B883 index order
    (VERIFIED below: as a SET they equal the lane's crystal weights,
    identity on coordinates — memo 92's cross-stack fact, extended
    here to the full weight system);
  B916 results.json H_prime_diag_vs_H_plus.D2 — D2tw's signs in B883
    index order (cross-checked against memo 92's flip-vector route);
  B912 results.json D_diag — D's signs in B883 index order (B912's
    wall twist, = +-rho27(sigma_-1) per B928).
PREREGISTERED CHECKS: (1) B883 weight set == lane weight set exactly;
(2) the two independent D2tw representations agree after transport;
(3) D is a PURE (un-shifted) weight character in lane coordinates (its
b found by exhaustion) — B928's "sigma_-1 is inner" made concrete;
(4) beat parity of all four elements, exact.
Gate 5 untouched (weights, signs, exact pair arithmetic).
"""
import os
from fractions import Fraction as Fr
from itertools import product

SCR = os.path.dirname(os.path.abspath(__file__))
CERT = os.environ.get("BENCH_CERT") or SCR
src = open(os.path.join(CERT, "twisted_double.py")).read()
exec(src[:src.index("# ---------------- stage 4")])

# ---- lane weights
H = [rho27_Q(hv) for hv in ([Fr(1) if k == i else Fr(0) for k in range(DIM)] for i in range(N))]
wtZ = [tuple(int(H[i][a][a]) for i in range(N)) for a in range(27)]

# ---- vendored: B883 weight order (frontier/B883_the_27/rep27.json 'weights')
B883 = [(0,0,0,0,0,-1),(0,0,0,0,-1,1),(0,0,0,-1,1,0),(0,-1,-1,1,0,0),(-1,-1,1,0,0,0),
        (0,1,-1,0,0,0),(-1,1,1,-1,0,0),(-1,0,0,1,-1,0),(-1,0,0,0,1,-1),(-1,0,0,0,0,1),
        (1,-1,0,0,0,0),(1,1,0,-1,0,0),(1,0,-1,1,-1,0),(1,0,-1,0,1,-1),(1,0,-1,0,0,1),
        (0,0,1,0,-1,0),(0,0,1,-1,1,-1),(0,0,1,-1,0,1),(0,-1,0,1,0,-1),(0,-1,0,1,-1,1),
        (0,-1,0,0,1,0),(0,1,0,0,0,-1),(0,1,0,0,-1,1),(0,1,0,-1,1,0),(0,0,-1,1,0,0),
        (-1,0,1,0,0,0),(1,0,0,0,0,0)]
assert set(B883) == set(wtZ) and len(set(B883)) == 27
print("CHECK 1: B883's full weight system == the lane's crystal weights, identity")
print("   on coordinates (memo 92's cross-stack agreement, extended to all 27).")

lane_of = {w: i for i, w in enumerate(wtZ)}
perm = [lane_of[w] for w in B883]          # B883 index -> lane index

# ---- vendored: the two diagonals in B883 index order
D2_B883 = [1,-1,1,1,-1,1,-1,-1,1,-1,1,1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,1]   # B916
D_B883  = [1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1]  # B912
D2 = [0]*27; Dd = [0]*27
for bidx in range(27):
    D2[perm[bidx]] = D2_B883[bidx]
    Dd[perm[bidx]] = D_B883[bidx]
CC_FLIPS = {(0,0,0,0,-1,1),(-1,-1,1,0,0,0),(-1,1,1,-1,0,0),(-1,0,0,1,-1,0),
            (-1,0,0,0,0,1),(1,0,-1,0,1,-1),(0,0,1,0,-1,0),(0,0,1,-1,0,1),
            (0,-1,0,1,-1,1),(0,1,0,0,-1,1),(-1,0,1,0,0,0)}                      # B916 (memo 92)
assert {wtZ[i] for i in range(27) if D2[i] == -1} == CC_FLIPS
print("CHECK 2: D2tw's two banked representations (index-signs vs flip vectors)")
print("   AGREE after transport — one twist, consistently recorded.")

# ---- CHECK 3: D as a pure weight character
found = []
for b in product((0, 1), repeat=N):
    for eps in (1, -1):
        if all(Dd[i] == eps*(1 if sum(b[k]*wtZ[i][k] for k in range(N)) % 2 == 0 else -1)
               for i in range(27)):
            found.append((b, eps))
assert len(found) >= 1, "D is not an affine weight character — structure finding"
print(f"CHECK 3: D IS a pure-family character: (b, polarity) = {found}")

# ---- CHECK 4: beat parity of the whole Klein group
r0 = ROOTS[0]
E = toF(rho27_Q(evec(r0)))
def beat_even(signs):
    return all(not (E[a][b2] != (Fr(0), Fr(0)) and signs[a] != signs[b2])
               for a in range(27) for b2 in range(27))
D2D = [D2[i]*Dd[i] for i in range(27)]
table = [("I", [1]*27), ("D2tw", D2), ("D", Dd), ("D2tw*D", D2D)]
verdicts = {}
for name, signs in table:
    verdicts[name] = beat_even(signs)
    print(f"   {name:7s}: beat-{'EVEN' if verdicts[name] else 'BROKEN'}"
          f"   (flips {signs.count(-1)})")

# the parity map as a character of the Klein group (multiplicativity check)
p = {n: (1 if v else -1) for n, v in verdicts.items()}
assert p["D2tw*D"] == p["D2tw"]*p["D"] and p["I"] == 1
print(f"   parity is MULTIPLICATIVE on the Klein group: a character with")
print(f"   kernel {{I, {'D2tw' if p['D2tw']==1 else 'D'}}} — "
      f"{'the hierarchy line is exactly the mirror-even subgroup' if p['D2tw']==1 else 'unexpected kernel'}.")

if all(verdicts.values()):
    print("""
VERDICT (F5 closed): ALL FOUR elements of B928's Klein group are
beat-EVEN — the whole 2-torsion lies inside the MIRROR'S CENTRALIZER
on the 27.  A group that centralizes the mirror realization cannot BE
the frame/branch V4, whose defining leg IS the mirror (c): the
"fourth presentation" hypothesis is REFUTED-AS-IDENTIFICATION.  The
two Klein groups are TRANSVERSE — B928's is gauge-sector and mirror-
even (object-side by the parity law, extending memo 92 from one
element to the whole group); B1182's is built on the observer's c-leg.
The wave-1 sqrt(-3) co-occurrence (B923's colored discriminant) is a
shared prime, not a shared action.  F5's one remaining residue is
B1024's self-flagged provisional d=2 (cc apparatus; relayed).""")
else:
    broken = [n for n, v in verdicts.items() if not v]
    print(f"""
VERDICT (F5 REFINED, structure banked): the Klein group SPLITS under
the mirror — elements {broken} are beat-BROKEN while the hierarchy
line {{I, D2tw}} is beat-EVEN, and the split is a CHARACTER of the
group (multiplicative, verified).  So B928's gauge 2-torsion is
neither inside the mirror's centralizer nor disjoint from the mirror
bit: it SURJECTS onto the mirror parity Z/2 with kernel exactly the
hierarchy carrier's line.  The fourth-presentation hypothesis is
refuted AS AN IDENTIFICATION (the groups are not one torsor) but the
interlock is real: the gauge Klein group and the observer's c-leg
share a common Z/2 quotient, realized by B912's wall twist D — while
the hierarchy carrier D2tw is precisely the part the mirror cannot
see (memo 92, now sharpened: it is the FULL mirror-even subgroup).
Relay to cc with the table; F5's remaining residue is B1024's
provisional d=2 (cc apparatus).""")

print("""Fences: parity is decided against the lane's banked mirror realization
(memos 31-33/46; B1174's c-leg), as in memo 92.  The vendored diagonals
are B916/B912's banked results (provenance in the docstring); CHECK 2's
double-representation agreement is the corruption guard.  Gate 5
untouched.""")
