#!/usr/bin/env python3
"""MEMO-61 CELL: WHAT A VEV WOULD BREAK — the kinematic survival table of the
record's two Z/2s over every direction of the 27, and the finding that the
standard dark-parity-preserving vev (the E6 singlet) BREAKS the object's lock.

The last kinematic rung of the dark arc (memos 56-58).  A vev direction v in
the 27 kinematically preserves a diagonal Z/2 iff v is EVEN under it (a
charged vev breaks the symmetry it is charged under — the standard necessary
condition; no dynamics, no potential, no vev is claimed to exist).  The two
Z/2s on the table: the frame-paid matter parity P (memo 56; -1 on the 16)
and the object-paid lock C_27 = (-1)^wt (memos 46/50/51/59: the center of
the holonomy closure, the longitude's sign).

PREREGISTERED (asserts):
  FACT 1: P-preserving directions = the 11 states of 10 (+) 1;
          C-preserving directions = the 15 states with wt = 0;
          BOTH-preserving = exactly the 5 states of class 10 with wt 0.
  FACT 2 (the sharp finding): the E6 SINGLET — the standard choice for
    breaking E6 while preserving the dark matter parity — has wt = -1:
    a singlet vev preserves P but BREAKS THE LOCK (the object's one
    group-paid Z/2, = the longitude's semisimple sign).
  FACT 3 (portal participation): each direction's count of cubic triples
    containing it — the 27-row ledger printed in full; anchors: the
    singlet sits in 5 triples (all portal), every 16-state in >= 1.
  FACT 4 (escalator cross-check): none of the 5 both-preserving directions
    is a chain top or bottom (they are bridge-singlets, wt 0) — a vev
    there leaves the escalator's rungs uncharged... verified: E27 kills
    all wt-0 states, so the both-preserving directions are exactly
    meridian-frozen (depth-1 under the internal clock).
FENCES: kinematic necessary conditions only — no potential is minimized, no
vev is asserted to exist, no stability beyond the Z/2 bookkeeping; the D5
frame fence (memo 56) applies to P; Gates 2/3/5 not crossed.
"""
from fractions import Fraction as F
from collections import Counter
import itertools
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# classes and gradings
q3={a: int(3*ipr(weights[a], omega1)) for a in range(27)}
cnt=Counter(q3.values())
c16=next(v for v,m in cnt.items() if m==16); c10=next(v for v,m in cnt.items() if m==10)
cls={a:('16' if q3[a]==c16 else '10' if q3[a]==c10 else '1') for a in range(27)}
r0=ROOTS[0]
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
Ppar={a:(-1 if cls[a]=='16' else 1) for a in range(27)}
C27={a:(1 if wt[a]%2==0 else -1) for a in range(27)}

# cubic triples (weight-zero, as memo 56)
ws=[tuple(sp.Rational(v) for v in w) for w in weights]
tri=[]
for a in range(27):
    for b in range(a,27):
        target=tuple(-(ws[a][k]+ws[b][k]) for k in range(6))
        for c in range(b,27):
            if ws[c]==target: tri.append((a,b,c))
assert len(tri)==45
inT=Counter()
for T_ in tri:
    for a in set(T_): inT[a]+=1

# FACT 1
Pok=[a for a in range(27) if Ppar[a]==1]
Cok=[a for a in range(27) if C27[a]==1]
both=[a for a in range(27) if Ppar[a]==1 and C27[a]==1]
print(f"FACT 1: P-preserving directions: {len(Pok)} (classes {Counter(cls[a] for a in Pok)});")
print(f"        lock-preserving: {len(Cok)}; BOTH: {len(both)} (all class {set(cls[a] for a in both)}, wt {set(wt[a] for a in both)})")
assert len(Pok)==11 and len(Cok)==15 and len(both)==5
assert all(cls[a]=='10' and wt[a]==0 for a in both)

# FACT 2
sing=[a for a in range(27) if cls[a]=='1'][0]
print(f"FACT 2: the E6 singlet has wt = {wt[sing]}: P({'+' if Ppar[sing]==1 else '-'}) preserved, lock C({'+' if C27[sing]==1 else '-'}) BROKEN")
assert Ppar[sing]==1 and C27[sing]==-1

# FACT 3: the 27-row ledger
print("FACT 3: the vev ledger (direction: class, q, wt, P, C, #triples):")
for a in range(27):
    print(f"   v{a:02d}: {cls[a]:>3}  q={q3[a]:+d}  wt={wt[a]:+d}  P={'+' if Ppar[a]==1 else '-'}  C={'+' if C27[a]==1 else '-'}  triples={inT[a]}")
assert inT[sing]==5
assert all(inT[a]>=1 for a in range(27) if cls[a]=='16')

# FACT 4: both-preserving directions are meridian-frozen
E27=rho27_Q(evec(r0))
frozen=all(all(E27[l][a]==0 for l in range(27)) for a in both)
print(f"FACT 4: E27 annihilates all 5 both-preserving directions (bridge-singlets): {frozen}")
assert frozen

print("""
WHAT A VEV WOULD BREAK: the record's two Z/2s cannot both survive the
standard E6 dark-sector vev — the singlet preserves the frame's matter
parity but breaks the object's lock (the center of the holonomy closure,
the longitude's sign).  The only directions kinematically neutral under
BOTH are the five 10-class bridge-singlets, which the meridian's clock
freezes (depth 1).  So the dark arc closes on a fork: keep the dark parity
and pay the lock, or keep the lock and confine breaking to the five frozen
directions.  Necessary conditions only — no potential, no vev, no values;
Gates 2/3/5 not crossed.""")
