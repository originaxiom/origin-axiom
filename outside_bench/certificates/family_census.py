#!/usr/bin/env python3
"""MEMO-74 CELL: THE FAMILY CENSUS — is there a family index INSIDE one 27?
(D4 of the MSSM-debt programme: where does generation multiplicity live?)

The trinification frame (memo 70) splits the 27 into three 9-blocks.  A
natural question — and a standard confusion — is whether the visible Z3
cycling the three A2 slots is a FAMILY symmetry (three copies of the same
SM content).  This cell decides it exactly.

CONSTRUCTION (all exact, rationals):
  1. Rebuild the trinification frame (three orthogonal A2 slots, memo 70).
  2. Enumerate EVERY linear map T with T(slot0)=slot1, T(slot1)=slot2,
     T(slot2)=slot0, where each slot map is one of the 12 automorphisms of
     the A2 root system (all ordered simple-pair images with the right
     Gram); 12^3 = 1728 candidates.  Keep those that permute the 72 e6
     roots (isometry is automatic from the frame Grams).
  3. Among the valid T: count those with T^3 = 1; pick the first as the
     canonical slot-cycler.
  4. Does T preserve the 27's weight multiset?  (Weights are
     multiplicity-free — memo 71 FACT B(i) — so a preserved weight set
     gives a well-defined permutation of the 27 states.)
  5. THE CENSUS: compute T's orbits on the 27 states and, per orbit, which
     9-block each member lies in.
PREREGISTERED (two-outcome; the machine decides):
  FACT 1: at least one slot-cycling root-system automorphism exists;
    report the count, and the count with T^3 = 1 (expected nonzero:
    trinification's Z3 is standard CITED structure — but the count itself
    is measured, not assumed).
  FACT 2: whether the canonical T preserves the 27's weight set.
    (Either way banks; if NOT, the Z3 is adjoint-only and the census is
    already over: no action on matter at all.)
  FACT 3 (the decisive fork), if FACT 2 lands YES:
    BRANCH F (family index): some T-orbit lies entirely inside blocks of
      the SAME slot-type triple — three copies of identical content.
    BRANCH S (sector rotation): every size-3 orbit meets all three
      DISTINCT 9-blocks — the Z3 rotates quarks->leptons->antiquarks
      WITHIN one generation-worth of states.  The block types
      ('3b','3b','1'), ('3','1','3b'), ('1','3','3') are pairwise distinct
      (asserted), so the three blocks are NOT three copies of anything:
      one 27 carries NO family index, and the record's only true
      three-copies structure is E8's (3,27) (memo 53, banked) — family
      multiplicity is a possibility-space fact, not an intra-27 one.
  FACT 4 (reported, no assert): T(r0) vs r0 (does the cycler move the
    meridian's root?) and whether T preserves the lock grading
    (-1)^(1+wt) — the lock is built on r0, so a moved r0 makes a moved
    lock the expectation; measured either way.
FENCE: the corpus scorecard (B950) mentions "generation count
structurally" as a claim of the record; that claim is NOT audited by this
cell (it concerns E8-level counting, memo 53's lane) — flagged for the
seat's cross-check, not contradicted and not certified here.
Gate 5 untouched (no measured value enters; 3 = a count of orbits/slots).
"""
import itertools
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

R6=[tuple(int(x) for x in r) for r in ROOTS]
RSET=set(R6)
def ip(a,b): return ipr(tuple(sp.Rational(x) for x in a), tuple(sp.Rational(x) for x in b))

# trinification frame (memo 70 construction, verbatim logic)
def a2span(r1,r2):
    out=set()
    for c1 in (-1,0,1):
        for c2 in (-1,0,1):
            t=tuple(c1*a+c2*b for a,b in zip(r1,r2))
            if t in RSET: out.add(t)
    return out
slots=[]
for r1 in R6:
    if slots and any(ip(r1,s)!=0 for S in slots for s in S): continue
    for r2 in R6:
        if r2==r1: continue
        if ip(r1,r2)==-1 and tuple(a+b for a,b in zip(r1,r2)) in RSET:
            if slots and any(ip(r2,s)!=0 for S in slots for s in S): continue
            S=a2span(r1,r2)
            assert len(S)==6
            slots.append(sorted(S)); break
    if len(slots)==3: break
assert len(slots)==3
def simple_pair(S):
    for r1 in S:
        for r2 in S:
            if r2!=r1 and ip(r1,r2)==-1 and tuple(a+b for a,b in zip(r1,r2)) in S:
                return (r1,r2)
pairs=[simple_pair(S) for S in slots]

# block structure of the 27 (memo 70 FACT 1, re-derived)
W=[tuple(sp.Rational(x) for x in w) for w in weights]
T3W={(1,0),(-1,1),(0,-1)}; T3BW={(-1,0),(1,-1),(0,1)}
def reptype(w,k):
    sw=(ipr(w,tuple(sp.Rational(x) for x in pairs[k][0])),
        ipr(w,tuple(sp.Rational(x) for x in pairs[k][1])))
    if sw in T3W: return '3'
    if sw in T3BW: return '3b'
    assert sw==(0,0)
    return '1'
btype=[tuple(reptype(w,k) for k in range(3)) for w in W]
blocks=Counter(btype)
assert all(v==9 for v in blocks.values()) and len(blocks)==3
assert len(set(blocks))==3, "block types pairwise distinct"
print(f"frame rebuilt: 3 orthogonal A2 slots; 27 blocks {dict(blocks)} (pairwise DISTINCT types)")

# FACT 1: enumerate slot-cycling root automorphisms
import sympy as sp2
Bsrc=sp2.Matrix([list(pairs[k][j]) for k in range(3) for j in range(2)]).T  # columns = source basis
Binv=Bsrc.inv()
def a2_ordered_pairs(S):
    out=[]
    for x in S:
        for y in S:
            if y!=x and ip(x,y)==-1: out.append((x,y))
    return out
opairs=[a2_ordered_pairs(S) for S in slots]
assert all(len(o)==12 for o in opairs)
valid=[]; validT3=[]
for i0 in range(12):
    for i1 in range(12):
        for i2 in range(12):
            img=[opairs[1][i0][0],opairs[1][i0][1],   # slot0 pair -> slot1
                 opairs[2][i1][0],opairs[2][i1][1],   # slot1 pair -> slot2
                 opairs[0][i2][0],opairs[0][i2][1]]   # slot2 pair -> slot0
            Timg=sp2.Matrix([list(v) for v in img]).T
            T=Timg*Binv
            ok=True
            for r in R6:
                v=T*sp2.Matrix(list(r))
                if tuple(int(x) for x in v) not in RSET: ok=False; break
            if ok:
                valid.append(T)
                if T**3==sp2.eye(6): validT3.append(T)
print(f"FACT 1: slot-cycling (0->1->2->0) root-system automorphisms: {len(valid)} of 1728;")
print(f"        with T^3 = 1: {len(validT3)}")
assert len(validT3)>0
T=validT3[0]

# FACT 2: action on the 27's weight set
WSET=set(tuple(x) for x in [tuple(sp.Rational(y) for y in w) for w in weights])
Wl=[tuple(sp.Rational(x) for x in w) for w in weights]
def applyT(v):
    u=T*sp2.Matrix([sp2.Rational(x) for x in v])
    return tuple(sp.Rational(x) for x in u)
TW=[applyT(w) for w in Wl]
preserves=set(TW)==set(Wl)
print(f"FACT 2: canonical T preserves the 27 weight set: {preserves}")
if not preserves:
    print("   -> the Z3 acts on the adjoint only; no action on matter; census over.")
else:
    perm={a: Wl.index(TW[a]) for a in range(27)}   # multiplicity-free (memo 71 B(i))
    # FACT 3: orbits and their block membership
    seen=set(); orbits=[]
    for a in range(27):
        if a in seen: continue
        orb=[a]; x=perm[a]
        while x!=a: orb.append(x); x=perm[x]
        seen.update(orb); orbits.append(orb)
    sizes=Counter(len(o) for o in orbits)
    print(f"FACT 3: T-orbit sizes on the 27: {dict(sizes)}")
    same_type=[o for o in orbits if len(o)==3 and len(set(btype[a] for a in o))==1]
    cross=[o for o in orbits if len(o)==3 and len(set(btype[a] for a in o))==3]
    print(f"   size-3 orbits within ONE block type: {len(same_type)}; crossing all three: {len(cross)}")
    if same_type:
        print("BRANCH F: a same-content triple exists — a family index inside the 27.")
    else:
        assert len(cross)==sizes.get(3,0)
        print("""BRANCH S: every size-3 orbit meets all three DISTINCT 9-blocks — the Z3
   rotates quark-sector -> lepton-sector -> anti-sector states WITHIN one
   generation-worth of matter.  The three blocks carry pairwise-distinct
   slot-type triples (asserted above): they are NOT three copies of the
   same content.  ONE 27 CARRIES NO FAMILY INDEX.  The record's only true
   three-copies structure is E8's (3,27) (memo 53, banked): family
   multiplicity is a possibility-space fact, not an intra-27 one.""")

# FACT 4 (reported): the meridian root and the lock under T
r0=R6[0]
tslot=[k for k in range(3) if any(tuple(r0)==tuple(s) for s in slots[k])]
Tr0=tuple(int(x) for x in (T*sp2.Matrix(list(r0))))
print(f"FACT 4: r0 = {r0} (in slot {tslot if tslot else 'CROSSING'}); T(r0) = {Tr0}; fixed: {Tr0==r0}")
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(R6[0][k])
Hint=rho27_Q(hA)
wt=[int(Hint[a][a]) for a in range(27)]
if preserves:
    lockpat=[(1+wt[a])%2 for a in range(27)]
    lock_pres=all(lockpat[perm[a]]==lockpat[a] for a in range(27))
    print(f"        T preserves the lock grading (-1)^(1+wt): {lock_pres} (reported, not asserted)")
print("""
FENCE: B950's "generation count structurally" scorecard claim is not audited
here — it lives at the E8 level (memo 53's lane); flagged for the seat.
Gate 5 untouched.""")
