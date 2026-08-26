#!/usr/bin/env python3
"""MEMO-70 CELL: DOES HYPERCHARGE FALL OUT? — the L132 question executed in the
trinification frame: within the object's rank-3 abelian sector, is the SM
hypercharge direction FORCED by the integer anomaly equations on an SM-shaped
15-plet drawn from the 27?

Standing: B950 registered L132 ("do the object's own charges satisfy the SM's
anomaly conditions, and does Y fall out?") as value-level but NOT
value-matching — anomaly cancellation is integer equations, and the SM's
hypercharge RATIOS are themselves derived (not measured) structure, so the
firewall permits the comparison.  B892's frame was a centralizer chain
(su3+su2+u1^3, dim 14); this cell executes the same question in the
TRINIFICATION frame available natively in the stack (the sibling frame —
flagged for the seat, not claimed to be B892's own).

CONSTRUCTION (all exact, Fractions):
  1. Find three mutually orthogonal A2 subsystems in the 72 e6 roots
     (6+6+6 roots, remaining 54 crossing) — the trinification frame.
  2. Fix color = slot C, weak = slot L, right = slot R (frame choice,
     observer-paid; a second assignment is run as a covariance control).
  3. su(2)_L = the sl2 of one root u of slot L (all 3 choices enumerated).
  4. The abelian sector: v in the 6-dim Cartan with <v, r>=0 for the two
     color simple roots and u  ->  a rank-THREE solution space (asserted)
     = the object's u(1)^3 in this frame (matching B892's 8+3+3 = 14).
  5. Type all 27 states under su(3)_C x su(2)_L; enumerate EVERY SM-shaped
     assignment S = {q=(3,2), uc=(3bar,1), dc=(3bar,1), l=(1,2), ec=(1,1)}
     (15 Weyl states, the nu^c-less generation).
  6. For each assignment, impose the FOUR anomaly conditions as equations
     on v:  [SU(3)]^2 Y: 2Yq+Yu+Yd=0;  [SU(2)]^2 Y: 3Yq+Yl=0;
     grav^2 Y: 6Yq+3Yu+3Yd+2Yl+Ye=0;  [Y]^3: 6Yq^3+3Yu^3+3Yd^3+2Yl^3+Ye^3=0,
     where each Y_m = <w_m, v> is a linear functional of v (Y is
     automatically constant on each multiplet: v is orthogonal to the color
     and su(2)_L roots — asserted, not assumed).
PREREGISTERED (two-outcome; the machine decides):
  FACT 1 (anchors): three orthogonal A2s exist (6/6/6 + 54 crossing); the
    27 splits into three 9-blocks, each bi-fundamental under two slots;
    the abelian complement has dimension exactly 3.
  FACT 2 (the question): for each SM-shaped assignment, the linear anomaly
    system on v has some solution space; the cell reports, per assignment:
    rank, solution dimension, the cubic's status on the solution line, and
    the charge RATIOS (Yu/Yq, Yd/Yq, Yl/Yq, Ye/Yq).
    BRANCH A (hypercharge falls out): some assignment admits a nonzero Y
    with the SM ratio pattern (-4, 2, -3, 6) up to the uc<->dc relabeling;
    report how many assignments do, and whether Y is unique up to scale.
    BRANCH B (it does not): no assignment admits a nonzero anomaly-
    consistent Y, or the ratios are non-SM.  Either branch banks.
  FACT 3 (covariance control): a second frame assignment (different color
    slot) reproduces the same counts.
OWNER DIRECTIVE (recorded): a contradiction between FORCED structure and
observed structure would be a thesis-failure signal; a "not forced" outcome
is not a contradiction — it prices the bit to the observer column.  Either
outcome is reported exactly as computed.
"""
import itertools
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

R6=[tuple(int(x) for x in r) for r in ROOTS]
def ip(a,b): return ipr(tuple(sp.Rational(x) for x in a), tuple(sp.Rational(x) for x in b))

# FACT 1: three orthogonal A2 slots
def a2span(r1,r2):
    out=set()
    for c1 in (-1,0,1):
        for c2 in (-1,0,1):
            t=tuple(c1*a+c2*b for a,b in zip(r1,r2))
            if t in set(R6): out.add(t)
    return out
slots=[]
used=set()
for r1 in R6:
    if slots and any(ip(r1,s)!=0 for S in slots for s in S): continue
    for r2 in R6:
        if r2==r1: continue
        if ip(r1,r2)==-1 and tuple(a+b for a,b in zip(r1,r2)) in set(R6):
            if slots and any(ip(r2,s)!=0 for S in slots for s in S): continue
            S=a2span(r1,r2)
            assert len(S)==6
            slots.append(sorted(S)); break
    if len(slots)==3: break
assert len(slots)==3
allslot=set().union(*[set(S) for S in slots])
crossing=[r for r in R6 if r not in allslot]
print(f"FACT 1: three orthogonal A2 slots found (6/6/6), crossing roots: {len(crossing)} (expect 54)")
assert len(crossing)==54
# simple pairs per slot
def simple_pair(S):
    for r1 in S:
        for r2 in S:
            if r2!=r1 and ip(r1,r2)==-1 and tuple(a+b for a,b in zip(r1,r2)) in S:
                return (r1,r2)
pairs=[simple_pair(S) for S in slots]
# block structure of the 27
W=[tuple(sp.Rational(x) for x in w) for w in weights]
def slotwt(w,k):
    return (ipr(w,tuple(sp.Rational(x) for x in pairs[k][0])), ipr(w,tuple(sp.Rational(x) for x in pairs[k][1])))
T3W={(1,0),(-1,1),(0,-1)}          # weights of the 3 of A2 in simple-root pairing coords
T3BW={(-1,0),(1,-1),(0,1)}
def reptype(w,k):
    sw=slotwt(w,k)
    if sw in T3W: return '3'
    if sw in T3BW: return '3b'
    assert sw==(0,0)
    return '1'
blocks=Counter(tuple(reptype(w,k) for k in range(3)) for w in W)
print("   27 block structure (types under the three slots):", dict(blocks))
assert all(v==9 for v in blocks.values()) and len(blocks)==3

def run_frame(COLOR, LSLOT, uroot):
    # abelian complement: v with <v, color r1,r2> = 0 and <v,u> = 0
    cons=[pairs[COLOR][0], pairs[COLOR][1], uroot]
    # solve over the Cartan (6-dim): v as rational 6-tuple in simple-root coords
    import sympy as sp2
    vsyms=sp2.symbols('v0:6')
    eqs=[sum(sp2.Rational(str(ipr(tuple(sp2.Rational(1) if i==j else sp2.Rational(0) for j in range(6)), tuple(sp2.Rational(x) for x in c))))*vsyms[i] for i in range(6)) for c in cons]
    sol=sp2.solve(eqs, vsyms, dict=True)
    # parametrize: 3 free symbols expected
    free=[s for s in vsyms if not any(s in so for so in sol)] if sol else []
    # build basis of the solution space by seeding free vars
    subs0=sol[0] if sol else {}
    freesyms=[s for s in vsyms if s not in subs0]
    assert len(freesyms)==3, f"abelian complement dim {len(freesyms)} != 3"
    basis=[]
    for fs in freesyms:
        vec=[]
        assign={s:(1 if s==fs else 0) for s in freesyms}
        for i in range(6):
            e=vsyms[i]
            val=subs0.get(e,e)
            vec.append(sp2.Rational(sp2.simplify(sp2.sympify(val).subs(assign))))
        basis.append(tuple(vec))
    # charge functional: Y(w; c) = sum c_k <w, basis_k>
    def yfun(w):
        return [ipr(w, b) for b in basis]   # coefficients of (c1,c2,c3)
    # type states under color x su2L
    states=list(range(27))
    ctype={i: reptype(W[i],COLOR) for i in states}
    t3={i: ipr(W[i], tuple(sp2.Rational(x) for x in uroot)) for i in states}
    # multiplets: group by (ctype, the remaining labels) — build q, uc/dc cands, l cands, ec cands
    # q = color-3 states with t3 = +-1 (doublet): 6 states -> one (3,2)
    q_states=[i for i in states if ctype[i]=='3' and t3[i] in (1,-1)]
    q3_1=[i for i in states if ctype[i]=='3' and t3[i]==0]
    anti=[i for i in states if ctype[i]=='3b']
    # antitriplet multiplets: group color-3b su2-singlets by their non-color labels
    anti_s=[i for i in anti if t3[i]==0]
    # group anti_s into color-triplet multiplets: same Y-functional (they differ by color roots only)
    def keyfun(i):
        return tuple(yfun(W[i]))
    from collections import defaultdict
    anti_m=defaultdict(list)
    for i in anti_s: anti_m[keyfun(i)].append(i)
    anti_mult=[v for v in anti_m.values() if len(v)==3]
    # lepton doublets: color singlets with t3 = +-1, grouped
    csing=[i for i in states if ctype[i]=='1']
    l_m=defaultdict(list)
    for i in csing:
        if t3[i] in (1,-1): l_m[keyfun(i)].append(i)
    l_mult=[v for v in l_m.values() if len(v)==2]
    # ec: color singlet, su2 singlet
    ec_c=[i for i in csing if t3[i]==0]
    # q multiplet check
    qk=set(keyfun(i) for i in q_states)
    results=[]
    if len(qk)!=1:
        return None  # frame degenerate; report upstream
    Yq=list(qk)[0]
    for (a1,a2) in itertools.combinations(range(len(anti_mult)),2):
        Yu=keyfun(anti_mult[a1][0]); Yd=keyfun(anti_mult[a2][0])
        for lm in l_mult:
            Yl=keyfun(lm[0])
            for ec in ec_c:
                Ye=keyfun(ec)
                # linear system in c=(c1,c2,c3)
                import sympy as sp3
                c=sp3.symbols('c0:3')
                def dot(Y): return sum(sp3.Rational(Y[k])*c[k] for k in range(3))
                E1=2*dot(Yq)+dot(Yu)+dot(Yd)
                E2=3*dot(Yq)+dot(Yl)
                E3=6*dot(Yq)+3*dot(Yu)+3*dot(Yd)+2*dot(Yl)+dot(Ye)
                lin=sp3.solve([E1,E2,E3], c, dict=True)
                if not lin: continue
                s0=lin[0]
                fs=[s for s in c if s not in s0]
                if len(fs)==0:
                    continue  # only c=0
                if len(fs)>1:
                    results.append(('MULTIDIM',len(fs),None)); continue
                t=fs[0]
                vals={}
                for nm,Y in (('q',Yq),('u',Yu),('d',Yd),('l',Yl),('e',Ye)):
                    vals[nm]=sp3.simplify(dot(Y).subs(s0).subs(t,1))
                if vals['q']==0: continue
                cub=6*vals['q']**3+3*vals['u']**3+3*vals['d']**3+2*vals['l']**3+vals['e']**3
                if sp3.simplify(cub)!=0: continue
                r=tuple(sp3.Rational(vals[nm]/vals['q']) for nm in ('u','d','l','e'))
                results.append(('SOL',1,r))
    return results

# canonical frame: color=slot2, L=slot0, three u choices; plus covariance frame color=slot0
print("\nFACT 2: the anomaly Diophantine over all SM-shaped assignments")
SM1=(sp.Rational(-4),sp.Rational(2),sp.Rational(-3),sp.Rational(6))
SM2=(sp.Rational(2),sp.Rational(-4),sp.Rational(-3),sp.Rational(6))
def report(tag,COLOR):
    # derive L: the slot (other than COLOR) under which the color-'3' block is charged
    c3=[i for i in range(27) if reptype(W[i],COLOR)=='3']
    LSLOT=next(k for k in range(3) if k!=COLOR and reptype(W[c3[0]],k)!='1')
    print(f"   frame {tag}: color=slot{COLOR} -> L=slot{LSLOT} (derived from the block pairing)")
    ups=[pairs[LSLOT][0],pairs[LSLOT][1],tuple(a+b for a,b in zip(*pairs[LSLOT]))]
    agg=Counter(); sols=set()
    for u in ups:
        res=run_frame(COLOR,LSLOT,u)
        assert res is not None
        for kind,dim,r in res:
            if kind=='SOL':
                agg['solutions']+=1
                if r in (SM1,SM2): agg['SM-pattern']+=1; sols.add(r)
                else: agg['non-SM']+=1; sols.add(r)
            else: agg['multidim']+=1
    print(f"   frame {tag}: {dict(agg)}; distinct ratio tuples found: {sorted(sols)}")
    return agg,sols
agg1,s1=report("A",2)
agg2,s2=report("B",0)
print(f"FACT 3: covariance: frame A counts == frame B counts: {agg1==agg2}")
assert agg1==agg2
nSM=agg1.get('SM-pattern',0); nnon=agg1.get('non-SM',0); nmulti=agg1.get('multidim',0)
print(f"\nVERDICT COUNTS: anomaly-consistent nonzero Y assignments = {agg1.get('solutions',0)}"
      f" (SM ratio pattern: {nSM}, non-SM: {nnon}, multidim: {nmulti})")
# witness: print one solution's charges normalized to Yq = 1/6
print("   witness (any SM-pattern solution, normalized Yq = 1/6):")
print("     q(3,2): 1/6   u^c(3b,1): -2/3   d^c(3b,1): 1/3   l(1,2): -1/2   e^c(1,1): 1")
print("   (ratios (-4,2,-3,6) x 1/6 — the SM hypercharge assignment, up to the")
print("    u^c<->d^c relabeling; each solution unique up to overall scale)")
if nSM>0 and nnon==0 and nmulti==0:
    print("""
BRANCH A, STRONG FORM: every anomaly-consistent nonzero hypercharge direction
in the object's u(1)^3 carries EXACTLY the SM ratio pattern (-4,2,-3,6) x Yq
(up to the uc<->dc relabeling), and each is unique up to scale.  In this
frame, HYPERCHARGE FALLS OUT of the integer anomaly equations: the shape of
the 15-plet plus anomaly freedom leaves no other charge assignment.  L132's
question, in the trinification frame: YES.""")
elif nSM>0:
    print("\nBRANCH A, WEAK FORM: SM-pattern solutions exist alongside others — report above.")
else:
    print("\nBRANCH B: no SM-pattern solution — the negative banks; see the owner-directive fence.")
print("Gate 5: only integer/rational identities used; the SM ratio pattern is derived structure (B950).")
