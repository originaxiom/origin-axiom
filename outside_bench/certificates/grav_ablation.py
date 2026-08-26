#!/usr/bin/env python3
"""MEMO-78 CELL (WAVE-3 ME2): IS GRAVITY LOAD-BEARING IN THE FORCED
HYPERCHARGE?  The memo-70 anomaly system re-run with the GRAVITATIONAL
condition ablated — and, as controls, with the cubic ablated and with each
gauge condition ablated.

Memo 70 (verified by cc B1160, extended by codex R019, re-scoped memo 75):
in the object's rank-3 abelian complement, the four anomaly conditions
  [SU(3)]^2 Y :  2Yq + Yu + Yd = 0
  [SU(2)]^2 Y :  3Yq + Yl = 0
  grav^2  Y   :  6Yq + 3Yu + 3Yd + 2Yl + Ye = 0     <- THE GRAVITATIONAL ONE
  [Y]^3       :  6Yq^3 + 3Yu^3 + 3Yd^3 + 2Yl^3 + Ye^3 = 0
force the SM ratio pattern for every SM-shaped 15-plet assignment (36/36,
zero non-SM).  The grav^2 Y condition is the mixed GAUGE-GRAVITATIONAL
anomaly: it is the one place 4d gravity touches the record's forced
structure.  Nobody has measured whether it carries weight.

THE ABLATIONS (same frame A, color=slot2, all three su(2)_L choices, every
SM-shaped assignment — the memo 70 enumeration exactly):
  V0 FULL          (anchor: must reproduce 36 solutions, all SM)
  V1 NO-GRAV       (drop grav^2 Y, keep both gauge linears + cubic)
  V2 NO-CUBIC      (drop [Y]^3, keep all three linears)
  V3 NO-GRAV+CUBIC (gauge linears only — the pure-gauge floor)
  V4 NO-SU2        (control: drop a GAUGE condition instead)
Per variant: number of assignments with solution lines, solution-space
dimensions, the census of ratio tuples, SM vs non-SM counts.

PREREGISTERED (two-outcome):
  BRANCH LB (gravity load-bearing): under V1 the forcing DEGRADES — extra
    solution dimensions appear or non-SM ratio tuples survive the cubic =>
    the SM hypercharge pattern in the record NEEDS the gravitational
    consistency condition; gravity is a required ingredient of the one
    forced value-structure.  (Universal-reduction context, R019/memo 75:
    dropping grav frees Ye — the in-frame question is whether the object's
    REALIZATION re-supplies the constraint.)
  BRANCH R (redundant): V1 reproduces V0 exactly => on the 27's realized
    functionals the gravitational condition is implied by the gauge ones;
    gravity adds no information here.  Either branch banks.
Gate 5 untouched (integer/rational identities; ratio patterns are derived
structure per B950).
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
c3s=[i for i in range(27) if reptype(W[i],COLOR)=='3']
LSLOT=next(k for k in range(3) if k!=COLOR and reptype(W[c3s[0]],k)!='1')

import sympy as sp2
def run_variant(uroot, use_su3, use_su2, use_grav, use_cubic):
    vsyms=sp2.symbols('v0:6')
    cons=[pairs[COLOR][0], pairs[COLOR][1], uroot]
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
    t3={i: ipr(W[i], tuple(sp2.Rational(x) for x in uroot)) for i in range(27)}
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
    c=sp2.symbols('c0:3')
    def dot(Y): return sum(sp2.Rational(Y[k])*c[k] for k in range(3))
    agg=Counter(); ratset=Counter()
    for (a1,a2) in itertools.combinations(range(len(anti_mult)),2):
        Yu=key(anti_mult[a1][0]); Yd=key(anti_mult[a2][0])
        for lmu in l_mult:
            Yl=key(lmu[0])
            for ec in ec_c:
                Ye=key(ec)
                lin=[]
                if use_su3: lin.append(2*dot(Yq)+dot(Yu)+dot(Yd))
                if use_su2: lin.append(3*dot(Yq)+dot(Yl))
                if use_grav: lin.append(6*dot(Yq)+3*dot(Yu)+3*dot(Yd)+2*dot(Yl)+dot(Ye))
                solL=sp2.solve(lin, c, dict=True)
                if not solL:
                    agg['inconsistent']+=1; continue
                s0=solL[0]; fs=[s for s in c if s not in s0]
                if len(fs)==0:
                    agg['only-zero']+=1; continue
                if len(fs)==1:
                    t=fs[0]
                    vals={nm:sp2.simplify(dot(Y).subs(s0).subs(t,1)) for nm,Y in (('q',Yq),('u',Yu),('d',Yd),('l',Yl),('e',Ye))}
                    if vals['q']==0: agg['q-zero-line']+=1; continue
                    if use_cubic:
                        cub=sp2.simplify(6*vals['q']**3+3*vals['u']**3+3*vals['d']**3+2*vals['l']**3+vals['e']**3)
                        if cub!=0: agg['cubic-killed']+=1; continue
                    r=tuple(sp2.Rational(vals[nm]/vals['q']) for nm in ('u','d','l','e'))
                    agg['line-solutions']+=1
                    ratset[r]+=1
                else:
                    # solution space dim >= 2: with cubic, a curve of ratios survives
                    agg[f'dim-{len(fs)}']+=1
    return agg, ratset

SM=( (sp2.Rational(-4),sp2.Rational(2),sp2.Rational(-3),sp2.Rational(6)),
     (sp2.Rational(2),sp2.Rational(-4),sp2.Rational(-3),sp2.Rational(6)) )
ups=[pairs[LSLOT][0],pairs[LSLOT][1],tuple(a+b for a,b in zip(*pairs[LSLOT]))]
variants=[('V0 FULL',        True,True,True, True),
          ('V1 NO-GRAV',     True,True,False,True),
          ('V2 NO-CUBIC',    True,True,True, False),
          ('V3 GAUGE-ONLY',  True,True,False,False),
          ('V4 NO-SU2',      True,False,True,True)]
summary={}
for name,s3,s2v,gv,cb in variants:
    AGG=Counter(); RS=Counter()
    for u in ups:
        agg,rs=run_variant(u,s3,s2v,gv,cb)
        AGG.update(agg); RS.update(rs)
    nSM=sum(m for r,m in RS.items() if r in SM)
    nnon=sum(m for r,m in RS.items() if r not in SM)
    ndim=sum(m for k,m in AGG.items() if k.startswith('dim-'))
    summary[name]=(nSM,nnon,ndim)
    print(f"{name}: {dict(AGG)}")
    print(f"   ratio census: SM-pattern {nSM}, non-SM {nnon}, higher-dim spaces {ndim}")
    if nnon and nnon<=12:
        print(f"   non-SM tuples: {sorted([r for r in RS if r not in SM])[:6]}")

# anchors and the branch
assert summary['V0 FULL']==(36,0,0), "anchor must reproduce memo 70"
print("\nANCHOR: V0 reproduces memo 70 (36 SM, 0 non-SM, 0 higher-dim): PASS")
nSM1,nnon1,ndim1=summary['V1 NO-GRAV']
if (nSM1,nnon1,ndim1)==(36,0,0):
    print("""
BRANCH R: dropping the GRAVITATIONAL anomaly condition changes NOTHING —
on the 27's realized charge functionals, grav^2 Y is implied by the gauge
conditions.  Gravity's consistency adds no information to the in-frame
forcing.""")
else:
    print(f"""
BRANCH LB: GRAVITY IS LOAD-BEARING.  Without the grav^2 Y condition the
forcing degrades ({nSM1} SM, {nnon1} non-SM, {ndim1} higher-dimensional
solution spaces vs 36/0/0 with it).  The SM hypercharge pattern in the
object's abelian sector NEEDS the mixed gauge-GRAVITATIONAL anomaly
condition: the one forced value-structure in the record has gravity as a
required ingredient.  (The controls above show what each other condition
carries.)  Gate 5 untouched.""")
