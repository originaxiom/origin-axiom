#!/usr/bin/env python3
"""MEMO-56 CELL: THE DARK LEDGER — the family grading 27 = 16 (+) 10 (+) 1
crossed with the object's own gradings, exactly: the singlet's only coupling
channel is the 10.10.1 portal, a matter parity is conserved by the unique
cubic, and the ledger records which of these Z/2s the object pays.

Ladder rung X3 (dark matter) reads "1 arc — ledger, not probe"; the one probe
(B657) was a refutation.  This cell is the first PROBE-GRADE KINEMATIC LEDGER
from the object side: everything a dark-sector discussion needs that is
computable without dynamics, breaking, or values — and nothing more.

Setup: the D5 x u(1) grading of the 27 (the SO(10)-family split: 16 = one SM
generation's shape, 10 = vector-like states, 1 = the singlet — the classic
E6 dark-sector candidates).  The u(1) direction is the centralizer of the D5
obtained by deleting the minuscule node; FENCE: choosing this D5 in E6 is
OBSERVER-PAID (a frame), the charges and everything after are then forced.

PREREGISTERED (two-outcome; anchors as asserts, cross-tables measured):
  FACT 1 (anchor): charge q = 3<w, omega_1> takes exactly THREE values on
    the 27 with multiplicities {16, 10, 1} (golden_gate G-3's banked family
    table, re-derived in this stack), and the charge values satisfy the two
    conservation identities 2 q16 + q10 = 0 and 2 q10 + q1 = 0.
  FACT 2 (anchor): the 45 weight-zero triples of the cubic, re-enumerated
    from the crystal, split by charge class into ONLY the two types
    {16,16,10} and {10,10,1} (charge conservation forbids the rest —
    verified by enumeration, not cited); counts measured (expected 40 + 5).
  FACT 3 (THE PORTAL SHAPE): therefore, in the UNIQUE coupling (memos
    32/35/48): the singlet couples ONLY through 10.10.1; the 16 NEVER
    couples to the singlet in any triple; every 16-coupling is 16.16.10.
    The vector-like 10 is the sole portal between the SM-shaped block and
    the singlet — the Higgs-portal shape, as a theorem of the cubic.
  FACT 4 (MATTER PARITY): P = -1 on the 16, +1 on 10 and 1 is conserved by
    every cubic triple (verified on all 45).  P is the standard U(1)_chi
    Z/2; here it is FORCED once the D5 frame is chosen.
  FACT 5 (the ledger question — which Z/2s does the OBJECT pay?): cross
    the charge classes with the bridge grading (the lock C_27 = (-1)^wt,
    memos 46/50/51 — object-paid, = the longitude's sign): the 3x3 table
    (class x bridge-weight) is MEASURED, and the cell decides whether the
    object's lock aligns with, or is independent of, the matter parity P
    (equality/negation as diagonal operators, or neither).  Either branch
    is the result.  Also measured: the charge shift q(r0) of the bridge
    root (does the bridge sl2 even preserve the family grading?).

Gate 5 untouched: shapes and selection rules only — no stability, no relic
abundance, no masses, no values.  E6-level kinematics; the D5 frame choice
is fenced above.
"""
import itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- FACT 1: the family grading
q3={a: 3*ipr(weights[a], omega1) for a in range(27)}
assert all(q3[a]==int(q3[a]) for a in q3)
q3={a:int(q3[a]) for a in q3}
cnt=Counter(q3.values())
print("FACT 1: u(1) charge multiset on the 27:", dict(cnt))
assert sorted(cnt.values())==[1,10,16]
c16=next(v for v,m in cnt.items() if m==16)
c10=next(v for v,m in cnt.items() if m==10)
c1 =next(v for v,m in cnt.items() if m==1)
print(f"   classes: 16 at q={c16}, 10 at q={c10}, 1 at q={c1}")
assert 2*c16+c10==0 and 2*c10+c1==0
cls={a:('16' if q3[a]==c16 else '10' if q3[a]==c10 else '1') for a in range(27)}

# ---- the object's bridge grading (memos 46/50/51)
r0=ROOTS[0]
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
assert dict(Counter(wt))=={1:6,0:15,-1:6}
qr0=3*ipr(tuple(sp.Rational(x) for x in r0), omega1)
print(f"   bridge root charge shift: q(r0) = {qr0}")

# ---- FACT 2: cubic support typed by class
tri=[]
ws=[tuple(sp.Rational(x) for x in w) for w in weights]
for a in range(27):
    for b in range(a,27):
        target=tuple(-(ws[a][k]+ws[b][k]) for k in range(6))
        for c in range(b,27):
            if ws[c]==target: tri.append((a,b,c))
assert len(tri)==45
types=Counter(tuple(sorted((cls[a],cls[b],cls[c]))) for (a,b,c) in tri)
print("FACT 2: the 45 cubic triples by family type:", dict(types))
assert set(types)<={('10','16','16'),('1','10','10')}
n16=types[('10','16','16')]; n10=types[('1','10','10')]
assert n16+n10==45
print(f"   => {n16} of type 16.16.10 and {n10} of type 10.10.1, nothing else")

# ---- FACT 3: portal shape (read off the typing, asserted explicitly)
no_16_1=all(not(set((cls[a],cls[b],cls[c]))>={'16','1'}) for (a,b,c) in tri)
sing_tris=[t for t in tri if '1' in (cls[t[0]],cls[t[1]],cls[t[2]])]
sing_ok=all(sorted((cls[a],cls[b],cls[c]))==['1','10','10'] for (a,b,c) in sing_tris)
print(f"FACT 3: no triple couples 16 with the singlet: {no_16_1};")
print(f"        every singlet coupling is 10.10.1: {sing_ok} ({len(sing_tris)} triples)")
assert no_16_1 and sing_ok
print("        => THE PORTAL SHAPE: the 10 is the sole channel between the")
print("           SM-shaped 16 and the singlet, in the unique coupling")

# ---- FACT 4: matter parity conserved
Ppar={a:(-1 if cls[a]=='16' else 1) for a in range(27)}
okP=all(Ppar[a]*Ppar[b]*Ppar[c]==1 for (a,b,c) in tri)
print(f"FACT 4: matter parity P (=-1 on 16, +1 on 10,1) conserved by all 45 triples: {okP}")
assert okP

# ---- FACT 5: the cross-table and the Z/2 comparison
tab=Counter((cls[a],wt[a]) for a in range(27))
print("FACT 5: family class x bridge weight (the DARK LEDGER cross-table):")
for cl in ('16','10','1'):
    row={w:tab.get((cl,w),0) for w in (-1,0,1)}
    print(f"   {cl:>3}: wt -1: {row[-1]:2d}   wt 0: {row[0]:2d}   wt +1: {row[1]:2d}")
c27={a:(1 if wt[a]%2==0 else -1) for a in range(27)}
eq = all(c27[a]==Ppar[a] for a in range(27))
neg= all(c27[a]==-Ppar[a] for a in range(27))
print(f"   lock C_27 == P: {eq};  lock == -P: {neg}")
if eq or neg:
    print("   => the object's lock IS the matter parity (up to global sign)")
else:
    both=Counter((Ppar[a],c27[a]) for a in range(27))
    print(f"   => INDEPENDENT Z/2s: joint distribution {dict(both)}")
    print("      the object-paid lock (longitude's sign) and the frame-paid")
    print("      matter parity are DIFFERENT gradings of the 27")

print(f"""
THE DARK LEDGER: in the unique coupling the singlet talks only through the
vector-like 10 (the portal shape is a theorem), a matter parity separating
the SM-shaped 16 from the rest is conserved exactly, and the ledger now
records which Z/2 is whose: the matter parity is frame-paid (it exists once
the D5 is chosen), the lock is object-paid (the longitude's own sign), and
the table above states their exact relation.  What remains dark is exactly
what needs the unpaid verbs: stability, abundance, mass — dynamics and
values, behind the gates where they belong.""")
