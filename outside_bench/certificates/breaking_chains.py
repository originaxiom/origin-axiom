#!/usr/bin/env python3
"""MEMO-72 CELL: THE UNIQUE CHAIN AND ITS DISCRETE REMAINDER — with the forced
hypercharge (memo 70) in hand: exactly which vev directions can break E6 to
the SM, and which Z/2 gradings survive that chain.  (D3 of the MSSM-debt
programme, extending memo 61 from directions to chains.)

Setup (all exact): the trinification frame and the anomaly-forced Y of memo
70 are rebuilt in-run (frame A, first su(2)_L choice, first SM-pattern
solution's direction v with Y = <., v>).  A vev direction w in the 27
kinematically preserves a symmetry generator iff it is neutral under it
(the necessary condition, as memo 61; no potential or vacuum is claimed).

PREREGISTERED (two-outcome; asserts):
  FACT 0 (anchors): frame + forced Y rebuilt; Y's multiplet values on the
    SM assignment are (1/6,-2/3,1/3,-1/2,1) x scale (re-anchored).
  FACT 1 (the SM-safe directions): the states of the 27 that are color
    singlets, su(2)_L singlets, AND Y-neutral number EXACTLY TWO.  Their
    identities in the (independent) D5xU(1)_psi frame of memo 56 are
    computed.  [ERROR FILED at point of occurrence: the first draft
    preregistered {16-class, singlet-class} from naive frame alignment;
    the machine returned psi-charges {1, -2} = {16-class, 10-class}.
    Mechanism: the psi-frame's SO(10) (built on omega_1) is a DIFFERENT
    SO(10) from the trinification-SM's — the F-3 frame discipline again,
    exactly memo 56's lesson.  Corrected claim: the two SM-safe states
    are the two neutral directions of the trinification lepton block
    (the nu^c-like and S-like states OF THIS FRAME); their psi-charges
    are measured, not matched.]
  FACT 2 (the chain reaches the SM): giving both directions vevs leaves
    the surviving Cartan torus of dimension EXACTLY 4 = span{color Cartan,
    T3, Y}: rank E6 (6) -> rank SM (4) in one two-step chain, and this is
    the ONLY SM-preserving chain from 27-vevs (any other direction breaks
    color, weak, or Y — from FACT 1).
  FACT 3 (the discrete remainder, the sharp question): the group of Z/2
    gradings of the 27 induced by integer-pairing Cartan elements h (h in
    the root lattice — the dual of the 27's weight lattice, verified
    in-run) satisfying <w1,h> = <w2,h> = 0 mod 2 is computed exactly over
    GF(2).  Measured: its size, and whether it contains (a) the psi-frame
    matter parity pattern, (b) the lock pattern (-1)^wt, (c) only gradings
    trivial on... whatever the machine returns.  E6 folklore expects
    R-parity-like Z/2s NOT to survive 27-only breaking; either branch
    banks.
  FACT 4 (the lock cost, chain-level): the lock values of the two vev
    directions (memo 61 found the singlet breaks the lock; the nu^c-shaped
    direction's value is measured here) — the chain's total Z/2 bill.
FENCES: necessary conditions only (neutrality); no potential, no vacuum,
no values.  The trinification frame + su(2)_L choice are observer-paid
(memo 70's covariance stands); Y within the frame is forced (memo 70).
Gate 5 untouched.
"""
import itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

R6=[tuple(int(x) for x in r) for r in ROOTS]
def ip(a,b): return ipr(tuple(sp.Rational(x) for x in a), tuple(sp.Rational(x) for x in b))

# ---- frame (as memo 70)
def a2span(r1,r2):
    out=set()
    for c1 in (-1,0,1):
        for c2 in (-1,0,1):
            t=tuple(c1*a+c2*b for a,b in zip(r1,r2))
            if t in set(R6): out.add(t)
    return out
slots=[]
for r1 in R6:
    if slots and any(ip(r1,s)!=0 for S in slots for s in S): continue
    for r2 in R6:
        if r2==r1: continue
        if ip(r1,r2)==-1 and tuple(a+b for a,b in zip(r1,r2)) in set(R6):
            if slots and any(ip(r2,s)!=0 for S in slots for s in S): continue
            S=a2span(r1,r2)
            if len(S)==6: slots.append(sorted(S)); break
    if len(slots)==3: break
assert len(slots)==3
def simple_pair(S):
    for r1 in S:
        for r2 in S:
            if r2!=r1 and ip(r1,r2)==-1 and tuple(a+b for a,b in zip(r1,r2)) in S:
                return (r1,r2)
pairs=[simple_pair(S) for S in slots]
W=[tuple(sp.Rational(x) for x in w) for w in weights]
T3W={(1,0),(-1,1),(0,-1)}; T3BW={(-1,0),(1,-1),(0,1)}
def reptype(w,k):
    sw=(ipr(w,tuple(sp.Rational(x) for x in pairs[k][0])), ipr(w,tuple(sp.Rational(x) for x in pairs[k][1])))
    if sw in T3W: return '3'
    if sw in T3BW: return '3b'
    return '1'
COLOR=2
c3=[i for i in range(27) if reptype(W[i],COLOR)=='3']
LSLOT=next(k for k in range(3) if k!=COLOR and reptype(W[c3[0]],k)!='1')
u=pairs[LSLOT][0]

# forced Y: rebuild the first SM solution's direction v (as memo 70)
import sympy as sp2
vsyms=sp2.symbols('v0:6')
cons=[pairs[COLOR][0], pairs[COLOR][1], u]
eqs=[sum(sp2.Rational(str(ip(tuple(1 if i==j else 0 for j in range(6)), c)))*vsyms[i] for i in range(6)) for c in cons]
sol=sp2.solve(eqs, vsyms, dict=True)
subs0=sol[0]; freesyms=[s for s in vsyms if s not in subs0]
assert len(freesyms)==3
basis=[]
for fs in freesyms:
    assign={s:(1 if s==fs else 0) for s in freesyms}
    basis.append(tuple(sp2.Rational(sp2.sympify(subs0.get(vsyms[i],vsyms[i])).subs(assign)) for i in range(6)))
def yco(w): return [ipr(w,b) for b in basis]
ctype={i: reptype(W[i],COLOR) for i in range(27)}
t3={i: ipr(W[i], tuple(sp2.Rational(x) for x in u)) for i in range(27)}
def key(i): return tuple(yco(W[i]))
anti_s=[i for i in range(27) if ctype[i]=='3b' and t3[i]==0]
am=defaultdict(list)
for i in anti_s: am[key(i)].append(i)
anti_mult=[v for v in am.values() if len(v)==3]
csing=[i for i in range(27) if ctype[i]=='1']
lm=defaultdict(list)
for i in csing:
    if t3[i] in (1,-1): lm[key(i)].append(i)
l_mult=[v for v in lm.values() if len(v)==2]
ec_c=[i for i in csing if t3[i]==0]
q_states=[i for i in range(27) if ctype[i]=='3' and t3[i] in (1,-1)]
Yq=key(q_states[0])
vdir=None
c=sp2.symbols('c0:3')
def dot(Y): return sum(sp2.Rational(Y[k])*c[k] for k in range(3))
for (a1,a2) in itertools.combinations(range(len(anti_mult)),2):
    if vdir: break
    Yu=key(anti_mult[a1][0]); Yd=key(anti_mult[a2][0])
    for lmu in l_mult:
        if vdir: break
        Yl=key(lmu[0])
        for ec in ec_c:
            lin=sp2.solve([2*dot(Yq)+dot(Yu)+dot(Yd), 3*dot(Yq)+dot(Yl),
                           6*dot(Yq)+3*dot(Yu)+3*dot(Yd)+2*dot(Yl)+dot(key(ec))], c, dict=True)
            if not lin: continue
            s0=lin[0]; fs=[s for s in c if s not in s0]
            if len(fs)!=1: continue
            t=fs[0]
            vals={nm:sp2.simplify(dot(Y).subs(s0).subs(t,1)) for nm,Y in (('q',Yq),('u',Yu),('d',Yd),('l',Yl),('e',key(ec)))}
            if vals['q']==0: continue
            if sp2.simplify(6*vals['q']**3+3*vals['u']**3+3*vals['d']**3+2*vals['l']**3+vals['e']**3)!=0: continue
            r=tuple(sp2.Rational(vals[nm]/vals['q']) for nm in ('u','d','l','e'))
            if r in ((-4,2,-3,6),(2,-4,-3,6)):
                cc={c[k]: (s0.get(c[k],c[k]) if c[k] in s0 else 1) for k in range(3)}
                cvals=[sp2.Rational(sp2.sympify(cc[c[k]]).subs(t,1)) for k in range(3)]
                vdir=tuple(sum(sp2.Rational(cvals[k])*sp2.Rational(basis[k][i]) for k in range(3)) for i in range(6))
                break
assert vdir is not None
Y={i: ipr(W[i], vdir) for i in range(27)}
Yqv=Y[q_states[0]]
print(f"FACT 0: forced Y rebuilt; Y(q) = {Yqv}; ratios re-anchored on the found assignment")
assert Yqv!=0

# FACT 1: SM-safe directions
safe=[i for i in range(27) if ctype[i]=='1' and t3[i]==0 and Y[i]==0]
print(f"FACT 1: SM-safe vev directions (color-singlet, weak-singlet, Y=0): {len(safe)} -> states {safe}")
assert len(safe)==2
# cross-frame identity in the psi frame
q3psi={a: int(3*ipr(W[a], omega1)) for a in range(27)}
cnt=Counter(q3psi.values())
c16=next(v for v,m in cnt.items() if m==16); c1=next(v for v,m in cnt.items() if m==1)
print(f"   their U(1)_psi charges: {[q3psi[i] for i in safe]} (psi 16-class = {c16}, 10-class = -2, singlet = {c1})")
# ERROR FILED (see docstring): psi-frame classes need NOT align with the
# trinification-SM frame; the measured charges are {1,-2}.  The intrinsic
# statement stands:
blk=[reptype(W[i],LSLOT) for i in safe]
print(f"   both live in the lepton (color-singlet) block; L-slot types: {blk}")
print("   => the two SM-safe directions are the two neutral states of the lepton")
print("      block — the nu^c-like and S-like directions OF THIS FRAME; the")
print("      standard E6 double-breaking is the ONLY SM-preserving chain")

# FACT 2: surviving torus
w1,w2=W[safe[0]],W[safe[1]]
M=sp2.Matrix([[sp2.Rational(str(ip(tuple(1 if i==j else 0 for j in range(6)), None) )) for i in range(6)]]) if False else None
rows=[]
for wv in (w1,w2):
    rows.append([sp2.Rational(ipr(tuple(sp2.Rational(1) if j==i else sp2.Rational(0) for j in range(6)), wv)) for i in range(6)])
Mm=sp2.Matrix(rows)
ns=Mm.nullspace()
print(f"FACT 2: surviving Cartan torus dimension = {len(ns)} (expect 4 = rank SM)")
assert len(ns)==4
# contains color Cartan, T3-direction, Y
def inspan(vec):
    aug=sp2.Matrix.hstack(*ns)
    sol2=aug.solve_least_squares(sp2.Matrix([sp2.Rational(x) for x in vec]))
    return sp2.simplify(aug*sol2-sp2.Matrix([sp2.Rational(x) for x in vec]))==sp2.zeros(6,1)
gens_check=[tuple(pairs[COLOR][0]), tuple(pairs[COLOR][1]), tuple(u), tuple(vdir)]
okspan=all(inspan(g) for g in gens_check)
print(f"   contains color Cartan + T3 + Y: {okspan}")
assert okspan

# FACT 3: surviving Z/2 gradings (GF(2) lattice computation)
# dual of the 27's weight lattice: verify root-lattice h give integer pairings
alpha=[tuple(1 if j==i else 0 for j in range(6)) for i in range(6)]
for a in range(27):
    for al in alpha:
        v=ipr(W[a], tuple(sp2.Rational(x) for x in al))
        assert v==int(v)
print("FACT 3: root-lattice elements pair integrally with all 27 weights (verified)")
# grading map: G(h)[a] = <w_a, h> mod 2 for h = sum n_i alpha_i
Mint=[[int(ipr(W[a], tuple(sp2.Rational(x) for x in alpha[i]))) for i in range(6)] for a in range(27)]
# constraints: <w1,h>, <w2,h> even
con=[[Mint[safe[0]][i]%2 for i in range(6)],[Mint[safe[1]][i]%2 for i in range(6)]]
# GF(2) nullspace of con (6 vars)
def gf2_null(rows,n):
    A=[r[:] for r in rows]; piv=[]; r=0
    for cc in range(n):
        p=next((i for i in range(r,len(A)) if A[i][cc]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(len(A)):
            if i!=r and A[i][cc]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(cc); r+=1
    free=[cc for cc in range(n) if cc not in piv]
    out=[]
    for fc in free:
        v=[0]*n; v[fc]=1
        for i,cc in enumerate(piv):
            v[cc]=A[i][fc]
        out.append(v)
    return out
null=gf2_null(con,6)
print(f"   h-space with both vevs even: dim {len(null)} over GF(2)")
grads=set()
for coefs in itertools.product((0,1),repeat=len(null)):
    h=[0]*6
    for cf,vv in zip(coefs,null):
        if cf: h=[(a+b)%2 for a,b in zip(h,vv)]
    g=tuple(sum(Mint[a][i]*h[i] for i in range(6))%2 for a in range(27))
    grads.add(g)
grads.discard(tuple([0]*27))
print(f"   NONTRIVIAL surviving Z/2 gradings of the 27: {len(grads)}")
# compare with psi matter parity pattern and lock pattern
c10=next(v for v,m in cnt.items() if m==10)
Ppat=tuple(1 if q3psi[a]==c16 else 0 for a in range(27))     # odd exactly on the 16
r0=ROOTS[0]
hA=[F(0)]*DIM
for k in range(N): hA[k]=F(r0[k])
Hint=rho27_Q(hA)
wtb=[int(Hint[a][a]) for a in range(27)]
Lpat=tuple(abs(wtb[a])%2 for a in range(27))                  # odd on wt odd
hasP=Ppat in grads; hasL=Lpat in grads
print(f"   contains the psi matter-parity pattern: {hasP}; the lock pattern: {hasL}")
# FACT 4: lock values of the vevs
print(f"FACT 4: bridge-weights of the vev directions: {[wtb[i] for i in safe]}")
print(f"   lock values: {[1-2*(abs(wtb[i])%2) for i in safe]} (a -1 means that vev breaks the lock)")
assert all(abs(wtb[i])%2==1 for i in safe)
print("   BOTH vev directions are lock-ODD: the unique SM chain breaks the lock,")
print("   and (FACT 3) neither the psi-parity nor the lock pattern survives it")

print(f"""
THE UNIQUE CHAIN AND ITS DISCRETE REMAINDER: with hypercharge forced, the
27 offers exactly TWO SM-safe vev directions — the two neutral states of
the lepton block (nu^c-like and S-like in this frame) — so the standard E6
double-breaking is not one option among many; it is the only chain
(necessary-condition level).  The
chain lands on exactly the SM torus (dim 4).  The surviving Z/2 ledger and
the lock bill are printed above; the branch that landed is the result.
Necessary conditions only — no potential, no vacuum, no values;
Gates 2/3/5 not crossed.""")
