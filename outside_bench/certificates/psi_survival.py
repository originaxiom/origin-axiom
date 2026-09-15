#!/usr/bin/env python3
"""MEMO-77 CELL: NOTHING ABELIAN SURVIVES BUT THE SM — the surviving torus of
the unique chain IS the SM torus exactly (no extra u(1) of any kind), the
family/psi u(1) is broken with the maximal charges available, and the dark
arc's continuous protection dies with it.  (The memo 72 x memos 56-58
cross-link: what the unique chain does to the dark ledger.)

Setup: memo 72's machinery rebuilt (frame, forced Y, the two SM-safe vev
directions w1 = nu^c-like, w2 = S-like of this frame).

PREREGISTERED (asserts; each two-outcome where marked):
  FACT 1 (torus equality): the annihilator of {w1, w2} in the Cartan is
    EXACTLY span{color Cartan, T3, Y} — dim 4 (memo 72) AND the 4 SM
    generators are independent inside it => equality, not just containment:
    the chain leaves NO extra u(1).  In particular no u(1)_psi, no u(1)_chi,
    no gauged family charge — every abelian direction beyond the SM sees a
    vev.
  FACT 2 (how the family charge dies): the psi-charges of the two vev
    states are (1, -2) (memo 72, re-derived): BOTH nonzero — the family
    u(1) is broken TWICE over.  Moreover the pair (q_psi(w1), q_psi(w2))
    generates all of Z as a subgroup (gcd 1): no Z/n remnant of u(1)_psi
    with n > 1 survives as an unbroken subgroup EXCEPT what the gcd allows;
    computed: gcd(1,2) = 1 => the psi remnant is TRIVIAL — not even a
    discrete shadow survives from the continuous side.  (Cross-check with
    memo 72 FACT 3 / memo 76: the psi-parity PATTERN is likewise not among
    the lattice survivors — the two computations agree from opposite ends.)
  FACT 3 (the dark ledger after the chain — the consequence, stated
    kinematically): memo 58's anomaly-payment theorem (T_dark = -T_16) is
    conditional on a GAUGED family u(1); after the unique chain that u(1)
    is broken with trivial remnant (FACT 2), and memo 76 measured that NO
    surviving Z/2 protects the psi-10 dark class and NO R-parity substitute
    exists (BRANCH N).  The kinematic conclusion: below the chain the dark
    block's stability is protected by NOTHING the root lattice or the
    surviving gauge group supplies.  Either dark-state stability comes from
    a mechanism beyond this kinematics (a global symmetry of the potential,
    an accident — Gates 2/3 territory), or the E6 dark candidates of this
    frame are NOT stable.  The payment theorem itself survives ABOVE the
    breaking as a consistency condition on the UV spectrum (unchanged).
FENCES: necessary conditions only; the vevs are directions, not vacua; no
potential, no values.  Frame observer-paid; Y in-frame forced (memo 70,
R019-scoped).  Gate 5 untouched.
"""
import itertools
from fractions import Fraction as F
from collections import Counter, defaultdict
from math import gcd
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

R6=[tuple(int(x) for x in r) for r in ROOTS]
def ip(a,b): return ipr(tuple(sp.Rational(x) for x in a), tuple(sp.Rational(x) for x in b))
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
safe=[i for i in range(27) if ctype[i]=='1' and t3[i]==0 and Y[i]==0]
assert len(safe)==2
w1,w2=W[safe[0]],W[safe[1]]

# FACT 1: torus equality
rows=[]
for wv in (w1,w2):
    rows.append([sp2.Rational(ipr(tuple(sp2.Rational(1) if j==i else sp2.Rational(0) for j in range(6)), wv)) for i in range(6)])
ann=sp2.Matrix(rows).nullspace()
assert len(ann)==4
smgens=[tuple(pairs[COLOR][0]), tuple(pairs[COLOR][1]), tuple(u), tuple(vdir)]
# each SM generator annihilates both vevs
for g in smgens:
    for wv in (w1,w2):
        assert ipr(wv, tuple(sp2.Rational(x) for x in g))==0
# the 4 SM generators are linearly independent
Msm=sp2.Matrix([[sp2.Rational(x) for x in g] for g in smgens])
assert Msm.rank()==4
print("FACT 1: annihilator of the two vevs = dim 4; the 4 SM generators lie inside it")
print("   and are independent => the surviving torus IS the SM torus EXACTLY.")
print("   NO extra u(1) survives the unique chain — not u(1)_psi, not u(1)_chi,")
print("   not any gauged family direction.")

# FACT 2: how the family charge dies
q3psi={a: int(3*ipr(W[a], omega1)) for a in range(27)}
qv=[q3psi[i] for i in safe]
print(f"FACT 2: psi-charges of the vev pair: {qv} — both nonzero (broken twice over);")
g=gcd(abs(qv[0]),abs(qv[1]))
print(f"   gcd(|{qv[0]}|,|{qv[1]}|) = {g} => the unbroken remnant of u(1)_psi is Z/{g} = TRIVIAL")
assert all(q!=0 for q in qv) and g==1
# cross-check from the lattice side (memo 72 FACT 3 recomputed):
alpha=[tuple(1 if j==i else 0 for j in range(6)) for i in range(6)]
Mint=[[int(ipr(W[a], tuple(sp2.Rational(x) for x in alpha[i]))) for i in range(6)] for a in range(27)]
con=[[Mint[safe[0]][i]%2 for i in range(6)],[Mint[safe[1]][i]%2 for i in range(6)]]
def gf2_null(rows_,n):
    A=[r[:] for r in rows_]; piv=[]; r=0
    for cc2 in range(n):
        p=next((i for i in range(r,len(A)) if A[i][cc2]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(len(A)):
            if i!=r and A[i][cc2]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(cc2); r+=1
    free=[cc2 for cc2 in range(n) if cc2 not in piv]
    out=[]
    for fc in free:
        v=[0]*n; v[fc]=1
        for i,cc2 in enumerate(piv):
            v[cc2]=A[i][fc]
        out.append(v)
    return out
null=gf2_null(con,6)
pset=set()
for coefs in itertools.product((0,1),repeat=len(null)):
    h=[0]*6
    for cf,vv in zip(coefs,null):
        if cf: h=[(a+b)%2 for a,b in zip(h,vv)]
    pset.add(tuple(sum(Mint[a][i]*h[i] for i in range(6))%2 for a in range(27)))
cnt=Counter(q3psi.values())
c16=next(v for v,m in cnt.items() if m==16)
Ppat=tuple(1 if q3psi[a]==c16 else 0 for a in range(27))
assert Ppat not in pset
print("   cross-check (lattice side, memo 72/76 recomputed): the psi-parity pattern is")
print("   NOT among the surviving gradings — both ends of the computation agree.")

# FACT 3: the dark ledger consequence (kinematic statement; measured inputs cited in-run)
print("""FACT 3: memo 58's payment theorem (T_dark = -T_16) is conditional on a GAUGED
   family u(1).  After the unique chain: the family u(1) is broken with TRIVIAL
   remnant (FACT 2), and memo 76 measured BRANCH N — no surviving Z/2 is odd on
   the whole 15-plet, none is constant-odd on the psi-10 dark class.  KINEMATIC
   CONCLUSION: below the chain, NOTHING the root lattice or the surviving gauge
   group supplies protects the E6 dark candidates of this frame; their stability
   (if any) is a Gates-2/3 question (potential accidents, global symmetries) —
   or absent.  ABOVE the breaking, the payment theorem stands unchanged as a
   consistency condition on the UV spectrum.""")

print("""
NOTHING ABELIAN SURVIVES BUT THE SM: the unique chain's surviving torus is
the SM torus exactly; the family charge dies with gcd-1 charges (trivial
remnant), its discrete shadow was already absent from the lattice
survivors, and the dark block exits the chain unprotected.  Necessary
conditions only; no potential, no vacuum, no values; Gate 5 untouched.""")
