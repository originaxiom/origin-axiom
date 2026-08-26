#!/usr/bin/env python3
"""MEMO-80 CELL (WAVE-3 MB1): THE TEXTURE — the unique coupling C (memo
32/47/48) read on the PHYSICAL roster of the unique chain (memo 76): which
Yukawa shapes exist, which are texture zeros, all dimensionless, all exact.

cc's B1162 meditation SS-B: "structure forced, values withheld" may really
be "dimensionless forced, scales withheld."  The texture — the zero/nonzero
pattern of the one allowed coupling on the physical states — is DIMENSIONLESS
structure.  This cell computes it entry-exactly.

Setup: the Jordan cubic C rebuilt in-run by the memo-47 nullspace
construction (dim 1, 45 triples, coefficients +-1 — asserted); the
trinification frame + forced Y + captured SM assignment rebuilt as memo 76
(roster: q 6, uc 3, dc 3, l 2, ec 1; Higgs docket 4 = 2 doublets; exotics
6 = D+Dc; neutral pair nu^c-like, S-like).  Y is normalized to Y(q) = 1/6.

PREREGISTERED (each shape a two-outcome measurement; E6-folklore expects
the full standard 27^3 pattern, but here it is COMPUTED from the unique C
on the FORCED roster, not assumed):
  SHAPE 1  up-type      q . uc . H(+1/2):    exists / absent
  SHAPE 2  down-type    q . dc . H(-1/2):    exists / absent
  SHAPE 3  lepton       l . ec . H(-1/2):    exists / absent
  SHAPE 4  Dirac-nu     l . nu^c . H(+1/2):  exists / absent
  SHAPE 5  the NMSSM lambda-term  S . H(+1/2) . H(-1/2): exists / absent
  SHAPE 6  exotic mass  D . Dc . S:          exists / absent
  SHAPE 7  exotic mass' D . Dc . nu^c:       exists / absent
  SHAPE 8  diquark/leptoquark couplings of D (q.q.D / uc.dc.Dc / ...):
           measured and listed (the proton-decay-shaped sector — counted,
           not interpreted; stability was already settled kinematically in
           memos 76/77: no surviving parity forbids them).
  PLUS the complete sector-pair table: for every pair of roster multiplets,
  the number of nonzero C entries and the third legs that couple; and the
  full census that every one of the 45 triples is accounted for by the
  roster decomposition (assert: total = 45).
SIGNIFICANCE GATES (asserted where two-outcome lands as expected-by-
folklore; REPORTED exactly if not — either way banks):
  the up-type shape's existence/absence is the sharp one: cc's SEAM-Y wall
  (mu_u = 0, cohomological, on THEIR bundle witness) vs the record's OWN
  channel.  If SHAPE 1 EXISTS here, the two walls are proven DIFFERENT
  facts (the rhyme of memo 75 sharpened to a disagreement of mechanisms —
  the object's kinematics allows what their cohomology forbids).
ERROR FILED AT POINT OF OCCURRENCE (first execution): the captured
assignment was the uc<->dc RELABELED branch, so the slot names 'uc'/'dc'
were physically swapped and the first run printed q.uc.Hd / q.dc.Hu — a
Y-violating impossibility that flagged the slip.  Fixed: physical labels
are now assigned by MEASURED hypercharge, and a Y-CONSERVATION GATE
(every nonzero triple sums to Y = 0) is asserted so the whole class of
labeling slips is machine-caught.
Gate 5 untouched (zero/nonzero patterns and counts only; no values).
"""
import itertools
from fractions import Fraction as F
from collections import defaultdict, Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- Jordan cubic C (memo 47 construction, verbatim)
H=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt6=[tuple(H[i][a][a] for i in range(N)) for a in range(27)]
def addw(*ws): return tuple(sum(x) for x in zip(*ws))
ZERO6=tuple(F(0) for _ in range(N))
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    gens.append(rho27_Q(evec(r)))
    gens.append(rho27_Q(evec(tuple(-x for x in r))))
triples=[t for t in itertools.combinations_with_replacement(range(27),3) if addw(wt6[t[0]],wt6[t[1]],wt6[t[2]])==ZERO6]
tid={t:n for n,t in enumerate(triples)}
def key3(a,b,c): return tuple(sorted((a,b,c)))
def deriv_rows(M):
    col_of=defaultdict(list)
    for l in range(27):
        for i in range(27):
            if M[l][i]!=0: col_of[i].append(l)
    nz0=next(((l,i) for l in range(27) for i in range(27) if M[l][i]!=0), None)
    shift=tuple(a-b for a,b in zip(wt6[nz0[0]],wt6[nz0[1]]))
    target=tuple(-x for x in shift)
    rows=[]
    for (i,j,k) in itertools.combinations_with_replacement(range(27),3):
        if addw(wt6[i],wt6[j],wt6[k])!=target: continue
        row=defaultdict(F)
        for (x_,y_,z_) in ((i,j,k),(j,i,k),(k,i,j)):
            for l in col_of.get(x_,[]):
                t=key3(l,y_,z_)
                if t in tid: row[tid[t]]+=M[l][x_]
        if row: rows.append(row)
    return rows
rows=[]
for M in gens: rows.extend(deriv_rows(M))
def nullspace(rows,n):
    dense=[[F(0)]*n for _ in range(len(rows))]
    for ri,row in enumerate(rows):
        for c,v in row.items(): dense[ri][c]=v
    m=len(dense); r=0; piv=[]
    for col in range(n):
        p=next((i for i in range(r,m) if dense[i][col]!=0),None)
        if p is None: continue
        dense[r],dense[p]=dense[p],dense[r]
        pv=dense[r][col]; dense[r]=[x/pv for x in dense[r]]
        for i in range(m):
            if i!=r and dense[i][col]!=0:
                fq=dense[i][col]; dense[i]=[x-fq*y for x,y in zip(dense[i],dense[r])]
        piv.append(col); r+=1
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[F(0)]*n; v[fc]=F(1)
        for i,col in enumerate(piv): v[col]=-dense[i][fc]
        out.append(v)
    return out
NS=nullspace(rows,len(triples))
assert len(NS)==1
C=NS[0]
p0=next(i for i,v in enumerate(C) if v!=0); C=[v/C[p0] for v in C]
assert sum(1 for v in C if v!=0)==45
def Cval(a,b,c):
    t=key3(a,b,c)
    return C[tid[t]] if t in tid else F(0)
print("C rebuilt in-run: dim 1, 45 triples (memo 47 reproduced)")

# ---- the frame, forced Y, and the captured roster (memo 76 machinery)
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
c3s=[i for i in range(27) if reptype(W[i],COLOR)=='3']
LSLOT=next(k for k in range(3) if k!=COLOR and reptype(W[c3s[0]],k)!='1')
u=pairs[LSLOT][0]
import sympy as sp2
vsyms=sp2.symbols('v0:6')
cons=[pairs[COLOR][0], pairs[COLOR][1], u]
eqs=[sum(sp2.Rational(str(ip(tuple(1 if i==j else 0 for j in range(6)), c)))*vsyms[i] for i in range(6)) for c in cons]
sol=sp2.solve(eqs, vsyms, dict=True)
subs0=sol[0]; freesyms=[s for s in vsyms if s not in subs0]
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
vdir=None; SM15=None
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
                cc2={c[k]: (s0.get(c[k],c[k]) if c[k] in s0 else 1) for k in range(3)}
                cvals=[sp2.Rational(sp2.sympify(cc2[c[k]]).subs(t,1)) for k in range(3)]
                vdir=tuple(sum(sp2.Rational(cvals[k])*sp2.Rational(basis[k][i]) for k in range(3)) for i in range(6))
                SM15=dict(q=list(q_states), uc=list(anti_mult[a1]), dc=list(anti_mult[a2]), l=list(lmu), ec=[ec])
                break
assert vdir is not None
Yv={i: ipr(W[i], vdir) for i in range(27)}
Yqv=Yv[q_states[0]]
Ysm={i: sp2.Rational(Yv[i]/Yqv)/6 for i in range(27)}   # normalized Y(q)=1/6
safe=[i for i in range(27) if ctype[i]=='1' and t3[i]==0 and Yv[i]==0]
SMset=set(SM15['q'])|set(SM15['uc'])|set(SM15['dc'])|set(SM15['l'])|set(SM15['ec'])
others=[i for i in range(27) if i not in SMset]
higgsD=[i for i in others if ctype[i]=='1' and t3[i] in (1,-1)]
exoT=[i for i in others if ctype[i]!='1']
Hu=[i for i in higgsD if Ysm[i]==sp2.Rational(1,2)]
Hd=[i for i in higgsD if Ysm[i]==sp2.Rational(-1,2)]
Dst=[i for i in exoT if ctype[i]=='3']; Dcst=[i for i in exoT if ctype[i]=='3b']
assert len(Hu)==2 and len(Hd)==2 and len(Dst)==3 and len(Dcst)==3
# CORRECTION IN-RUN (caught by the Y-conservation gate below on the first
# execution): the captured assignment may be the uc<->dc RELABELED branch
# (ratios (2,-4,...)), in which case the slot named 'uc' carries Y=+1/3.
# Physical identity is fixed by MEASURED hypercharge, not by slot name:
if Ysm[SM15['uc'][0]]==sp2.Rational(1,3):
    SM15['uc'],SM15['dc']=SM15['dc'],SM15['uc']
assert Ysm[SM15['uc'][0]]==sp2.Rational(-2,3) and Ysm[SM15['dc'][0]]==sp2.Rational(1,3)
nuS=safe
print(f"ROSTER (labels by measured Y): SM15 q{SM15['q']} uc{SM15['uc']} dc{SM15['dc']} l{SM15['l']} ec{SM15['ec']}")
print(f"   H(+1/2) {Hu}, H(-1/2) {Hd}, D {Dst}, Dc {Dcst}, neutrals {nuS}")

MULT={'q':SM15['q'],'uc':SM15['uc'],'dc':SM15['dc'],'l':SM15['l'],'ec':SM15['ec'],
      'Hu':Hu,'Hd':Hd,'D':Dst,'Dc':Dcst,'N1':[nuS[0]],'N2':[nuS[1]]}
names=list(MULT)
# THE Y-CONSERVATION GATE (would catch any labeling slip): every nonzero
# C triple must have Y summing to zero on the roster labels
for t in triples:
    if Cval(*t)!=0:
        assert sum(Ysm[x] for x in t)==0, f"Y non-conservation at {t}"
print("Y-conservation gate: every nonzero C triple sums to Y=0 on the roster: PASS")
# full triple census over multiplet triples
cens=Counter()
for na,nb,nc in itertools.combinations_with_replacement(names,3):
    cnt=0
    seen=set()
    for a in MULT[na]:
        for b in MULT[nb]:
            for cx in MULT[nc]:
                t=key3(a,b,cx)
                if t in seen: continue
                seen.add(t)
                if Cval(*t)!=0: cnt+=1
    if cnt: cens[(na,nb,nc)]=cnt
tot=sum(cens.values())
print(f"\nSECTOR TRIPLE TABLE (nonzero C entries per multiplet triple; total {tot}, expect 45):")
for k,v in sorted(cens.items(), key=lambda x:-x[1]):
    print(f"   {'.'.join(k):15s} : {v}")
assert tot==45

def shape(*mults):
    cnt=0
    seen=set()
    for a in MULT[mults[0]]:
        for b in MULT[mults[1]]:
            for cx in MULT[mults[2]]:
                t=key3(a,b,cx)
                if t not in seen:
                    seen.add(t)
                    if Cval(*t)!=0: cnt+=1
    return cnt
shapes=[("1 up-type      q.uc.Hu", ('q','uc','Hu')),
        ("2 down-type    q.dc.Hd", ('q','dc','Hd')),
        ("3 lepton       l.ec.Hd", ('l','ec','Hd')),
        ("4 Dirac-nu     l.N.Hu ", None),
        ("5 lambda-term  N.Hu.Hd", None),
        ("6 exotic mass  D.Dc.N ", None),
        ("7 diquark      q.q.D  ", ('q','q','D')),
        ("8 leptoquark   uc.dc.Dc",('uc','dc','Dc'))]
print("\nTHE SHAPES (nonzero entries; N = each neutral separately):")
res={}
for label,m in shapes:
    if m: res[label]=shape(*m); print(f"   {label}: {res[label]}")
    else:
        if 'Dirac' in label:
            r1,r2=shape('l','N1','Hu'), shape('l','N2','Hu')
        elif 'lambda' in label:
            r1,r2=shape('N1','Hu','Hd'), shape('N2','Hu','Hd')
        else:
            r1,r2=shape('D','Dc','N1'), shape('D','Dc','N2')
        res[label]=(r1,r2); print(f"   {label}: N1 -> {r1}, N2 -> {r2}")

# the neutral-role split (measured; cross-frame identity per memo 72's lesson)
q3psi={a: int(3*ipr(W[a], omega1)) for a in range(27)}
roleN1=[lab for lab,m in (("lambda",'x'),) if False]
r_lam=(shape('N1','Hu','Hd'), shape('N2','Hu','Hd'))
r_dir=(shape('l','N1','Hu'), shape('l','N2','Hu'))
r_exo=(shape('D','Dc','N1'), shape('D','Dc','N2'))
S_state = nuS[0] if r_lam[0]>0 else nuS[1]
nu_state = nuS[1] if S_state==nuS[0] else nuS[0]
assert {S_state,nu_state}==set(nuS) and r_lam[nuS.index(S_state)]>0 and r_dir[nuS.index(nu_state)]>0
assert r_lam[nuS.index(nu_state)]==0 and r_dir[nuS.index(S_state)]==0
print(f"\nNEUTRAL ROLES (by coupling, measured): state {S_state} is the S (lambda-term")
print(f"   Hu.Hd + exotic-mass D.Dc partner); state {nu_state} is the nu^c (Dirac partner).")
print(f"   Cross-frame note: their psi-charges are {q3psi[S_state]} and {q3psi[nu_state]} —")
print(f"   the S-COUPLING role is played by the psi-{'16' if q3psi[S_state]==1 else '10'}-class state:")
print("   coupling roles and psi-frame class labels MISALIGN (memo 72's frame lesson,")
print("   now measured at the coupling level; roles here are intrinsic, labels are not)")

up=res["1 up-type      q.uc.Hu"]
print(f"\nTHE SHARP ONE: the record's OWN up-type Yukawa shape has {up} nonzero entries.")
if up>0:
    print("""   IT EXISTS: the object's kinematics ALLOWS the up-Yukawa that cc's bundle
   cohomology FORBIDS (SEAM-Y mu_u = 0).  The two walls are now proven
   DIFFERENT facts: SEAM-Y is a property of the heterotic dressing, not of
   the object's coupling structure — memo 75's 'rhyme' sharpened into a
   mechanism disagreement, exactly where link A's import bites.""")
else:
    print("   IT IS ABSENT: the record's own channel reproduces SEAM-Y kinematically.")
print("""
All entries are +-1 zero/nonzero facts (dimensionless texture); no value,
scale, or hierarchy is claimed.  Gate 5 untouched.""")
