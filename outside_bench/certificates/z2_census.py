#!/usr/bin/env python3
"""MEMO-76 CELL: THE SURVIVING Z/2s NAMED — memo 72 found 15 nontrivial Z/2
gradings surviving the unique SM chain, with neither the psi-parity nor the
lock among them.  This cell characterizes ALL 15 exactly: which are shadows
of the surviving SM torus, which are genuinely EXTRA discrete remnants, and
whether ANY acts as an R-parity substitute (odd on the whole SM 15-plet).

Setup: memo 72's machinery rebuilt verbatim (trinification frame, forced Y,
the two SM-safe vev directions, the GF(2) grading space) — plus the FOUND SM
assignment is now CAPTURED (q, uc, dc, l, ec state lists), so each grading
can be read against the physical roster of the 27:
  15-plet (q 6, uc 3, dc 3, l 2, ec 1) + the other 12 (Higgs-candidate
  doublets, exotic color triplets D/Dc, and the two vev states nu^c/S).

PREREGISTERED (two-outcome where marked; asserts):
  FACT 1 (the space is linear): the 15 nontrivial gradings + 0 form a
    GF(2) vector space of dim EXACTLY 4 (the h-null space maps injectively).
  FACT 2 (the SM shadows): the hypercharge pattern P_Y = Y/Yq mod 2 (hY =
    vdir/Yq verified to pair integrally with all 27 weights => hY in the
    root lattice) and the weak pattern P_T = 2T3 mod 2 (h = the su(2)_L
    root u itself) are BOTH in the surviving space (they must be: their h's
    are even on both vevs since the vevs are neutral singlets).
    [ERROR FILED at point of occurrence: the first draft preregistered
    "their span has dim 2 => 3 shadows, 12 extra".  The machine refused:
    P_Y == P_T IDENTICALLY on all 27 states — oddness of 6Y coincides with
    weak-doubletness state-by-state (q,l,H doublets: 6Y odd; all singlets
    and exotics: even).  This is the Z/6-center fact of the SM's global
    structure [SU(3)xSU(2)xU(1)]/Z6 — (-1)^(6Y) acts as the SU(2)-center
    times color triality, and triality is invisible mod 2 (CITED context;
    the identity itself verified exactly here on all 27 states).  Corrected
    claim: the SM-torus shadow subgroup has dim EXACTLY 1 (ONE nontrivial
    shadow, P_Y = P_T), so EXACTLY 14 of the 15 survivors are EXTRA —
    discrete remnants of E6 beyond anything the SM group provides.]
  FACT 3 (the R-parity census — the sharp two-outcome):
    BRANCH R: some surviving grading is odd on ALL 15 SM-plet states ->
      an R-parity substitute survives the chain; report its values on the
      remaining 12 (a true matter parity also needs the Higgs-candidate
      doublets EVEN).
    BRANCH N: no surviving grading is odd on the whole 15-plet -> the
      unique chain leaves NO root-lattice matter parity at all; any
      stability of the lightest exotic/dark state needs a non-lattice
      mechanism or none exists (kinematic statement only).
  FACT 4 (the dark column, measured): for each survivor, whether it is
    CONSTANT on the psi-frame classes (16/10/1, memo 56's dark frame) —
    counts reported; a grading constant-odd on the 10-class and even on
    the vevs would be a dark-protecting parity IN THAT FRAME (measured
    either way; frames are known to misalign — memo 72's filed error).
FENCES: necessary conditions only; no potential, vacuum, or values; the
frame is observer-paid, Y in-frame forced (memo 70, R019-scoped).  Gate 5
untouched.
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
                cc={c[k]: (s0.get(c[k],c[k]) if c[k] in s0 else 1) for k in range(3)}
                cvals=[sp2.Rational(sp2.sympify(cc[c[k]]).subs(t,1)) for k in range(3)]
                vdir=tuple(sum(sp2.Rational(cvals[k])*sp2.Rational(basis[k][i]) for k in range(3)) for i in range(6))
                SM15=dict(q=list(q_states), uc=list(anti_mult[a1]), dc=list(anti_mult[a2]),
                          l=list(lmu), ec=[ec])
                break
assert vdir is not None and SM15 is not None
Y={i: ipr(W[i], vdir) for i in range(27)}
Yqv=Y[q_states[0]]
safe=[i for i in range(27) if ctype[i]=='1' and t3[i]==0 and Y[i]==0]
assert len(safe)==2
SMset=set(SM15['q'])|set(SM15['uc'])|set(SM15['dc'])|set(SM15['l'])|set(SM15['ec'])
assert len(SMset)==15
others=[i for i in range(27) if i not in SMset]
# roster of the other 12
higgsD=[i for i in others if ctype[i]=='1' and t3[i] in (1,-1)]       # Higgs-candidate doublet states
exoT=[i for i in others if ctype[i]!='1']                              # exotic colored states
neut=[i for i in others if ctype[i]=='1' and t3[i]==0]                 # nu^c/S (the vev states)
assert sorted(neut)==sorted(safe)
print(f"ROSTER: SM15 captured (q {SM15['q']}, uc {SM15['uc']}, dc {SM15['dc']}, l {SM15['l']}, ec {SM15['ec']})")
print(f"   other 12: Higgs-candidate doublet states {higgsD}, exotic colored {exoT}, vev states {neut}")
assert len(higgsD)==4 and len(exoT)==6 and len(neut)==2

# GF(2) grading space (memo 72 FACT 3 machinery)
alpha=[tuple(1 if j==i else 0 for j in range(6)) for i in range(6)]
Mint=[[int(ipr(W[a], tuple(sp2.Rational(x) for x in alpha[i]))) for i in range(6)] for a in range(27)]
con=[[Mint[safe[0]][i]%2 for i in range(6)],[Mint[safe[1]][i]%2 for i in range(6)]]
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
assert len(null)==4
def hpat(h):
    return tuple(sum(Mint[a][i]*h[i] for i in range(6))%2 for a in range(27))
pats=[]
for coefs in itertools.product((0,1),repeat=4):
    h=[0]*6
    for cf,vv in zip(coefs,null):
        if cf: h=[(a+b)%2 for a,b in zip(h,vv)]
    pats.append(hpat(h))
space=set(pats)
grads=sorted(space-{tuple([0]*27)})
print(f"FACT 1: grading space |{len(space)}| = 16 (dim 4 over GF(2); map injective on h-space): {len(space)==16}")
assert len(space)==16 and len(grads)==15

# FACT 2: the SM shadows
hYvec=tuple(sp2.Rational(x)/Yqv for x in vdir)      # <w, hY> = Y/Yq: q -> 1
for a in range(27):
    v=ipr(W[a], hYvec)
    assert v==int(v), "hY must pair integrally (root lattice) — verify"
PY=tuple(int(ipr(W[a],hYvec))%2 for a in range(27))
PT=tuple(int(t3[a])%2 for a in range(27))
assert PY in space and PT in space, "SM shadows must survive (even on neutral vevs)"
assert PY!=tuple([0]*27) and PT!=tuple([0]*27)
# ERROR FILED (see docstring): preregistered dim-2 shadow span; machine returned P_Y == P_T
assert PY==PT, "measured: the two SM shadows coincide on the 27"
oddset=sorted(a for a in range(27) if PY[a]==1)
dblset=sorted(a for a in range(27) if t3[a] in (1,-1))
assert oddset==dblset
sm_shadows={PY}
print("FACT 2: P_Y (=Y/Yq mod 2, hY in the root lattice: verified) == P_T (=2T3 mod 2)")
print("   IDENTICALLY on the 27 (odd exactly on the weak doublets — the Z/6-center")
print("   identity, verified state-by-state; preregistered dim-2 span REFUTED, error")
print("   filed) => the SM-torus SHADOW subgroup has dim 1 (ONE nontrivial shadow);")
print(f"   EXTRA (non-SM) survivors: {15-1} = 14 exactly (color center Z/3: no Z/2 shadow)")

# FACT 3: the R-parity census
full_odd=[g for g in grads if all(g[a]==1 for a in SMset)]
print(f"FACT 3: gradings odd on ALL 15 SM-plet states: {len(full_odd)}")
if full_odd:
    for g in full_odd:
        hv=[g[a] for a in higgsD]; ev=[g[a] for a in exoT]; nv=[g[a] for a in neut]
        extra="EXTRA (non-SM-shadow)" if g not in sm_shadows else "SM shadow"
        print(f"   BRANCH R candidate [{extra}]: Higgs doublets {hv}, exotics {ev}, vevs {nv}")
else:
    print("   BRANCH N: NO surviving grading is odd on the whole 15-plet")
# per-grading odd-count table (compact)
print("   census (odd counts): [SM15 | higgs4 | exotic6] per grading:")
tab=Counter()
for g in grads:
    row=(sum(g[a] for a in SMset), sum(g[a] for a in higgsD), sum(g[a] for a in exoT),
         'shadow' if g in sm_shadows else 'extra')
    tab[row]+=1
for row,m in sorted(tab.items(), key=lambda x:(-x[0][0],x[0][1])):
    print(f"     odd on {row[0]:2d}/15 SM, {row[1]}/4 higgs, {row[2]}/6 exotic  [{row[3]}] x{m}")

# FACT 4: the dark column (psi classes)
q3psi={a: int(3*ipr(W[a], omega1)) for a in range(27)}
cnt=Counter(q3psi.values())
c16=next(v for v,m in cnt.items() if m==16); c10=next(v for v,m in cnt.items() if m==10); c1=next(v for v,m in cnt.items() if m==1)
cls={a:('16' if q3psi[a]==c16 else '10' if q3psi[a]==c10 else '1') for a in range(27)}
const_counts=Counter()
dark_protect=[]
for g in grads:
    co={}
    for lab in ('16','10','1'):
        vals={g[a] for a in range(27) if cls[a]==lab}
        co[lab]=vals.pop() if len(vals)==1 else None
    nc=sum(1 for lab in co if co[lab] is not None)
    const_counts[nc]+=1
    if co['10']==1 and all(g[a]==0 for a in safe):
        dark_protect.append((g,co))
print(f"FACT 4: constancy on psi-classes (16/10/1): {dict(const_counts)} (n classes constant -> count)")
print(f"   gradings constant-ODD on the whole psi-10 class: {len([1 for g,co in dark_protect])}")
print("   (frames misalign — memo 72's filed error — so class-wise constancy is the")
print("    measured exception, not the rule)")

print("""
THE SURVIVING Z/2s NAMED: the unique SM chain's discrete remainder is a
dim-4 GF(2) space — ONE shadow of the unbroken SM torus (P_Y = P_T, the
Z/6-center identity measured on the 27) and 14 genuinely EXTRA Z/2
remnants of E6.  The R-parity and dark columns above are the measured
branches.  Necessary conditions only; no potential, no vacuum, no values;
Gate 5 untouched.""")
