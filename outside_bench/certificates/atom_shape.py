#!/usr/bin/env python3
"""MEMO-84 CELL (WAVE-4 S1): THE ATOM SHAPE — from the forced hypercharge,
the electric-charge functional on the physical roster: charge quantization,
color-singlet composability, and the exact neutrality of the hydrogen- and
neutron-shapes.  (The cosmogony script's last visible rung: the record
forces that neutral atoms are POSSIBLE — their existence-as-events stays
schedule/dynamics, observer-side.)

Setup: the trinification frame, forced Y (memo 70, R019-scoped), and the
physical roster with measured-Y labels and the Y-conservation gate (memo
80's corrected machinery, verbatim).  The electric-charge functional is
the standard combination Q = T3 + Y (CITED convention; in this frame
t3 = 2*T3 in {0,±1}, Y normalized to Y(q) = 1/6, so Q = t3/2 + Ysm).
Q's RATIOS are derived structure exactly as hypercharge's are (B950);
no measured value enters.

PREREGISTERED (two-outcome; asserts):
  FACT 1 (the charge table): Q on the roster lands the SM pattern —
    u-type 2/3, d-type -1/3, u^c -2/3, d^c 1/3, nu 0, e -1, e^c 1;
    Higgs doublets (±1, 0-shaped by member); exotics D -1/3, D^c 1/3;
    the two neutrals 0.  Measured and asserted.
  FACT 2 (charge quantization): every COLOR-SINGLET state has INTEGER
    charge; every colored state has charge in (1/3)Z \\ Z.  BRANCH
    FRACTURE (the failure mode, stated): a color-singlet with
    non-integer Q would contradict OBSERVED structure (no fractionally
    charged leptons/hadrons observed) — per the owner's directive that
    is a thesis-failure signal and would be reported loudly, not
    absorbed.
  FACT 3 (color-singlet composability, weight level): the three color
    weights of the 3 sum to zero (a baryon-shaped singlet exists in
    q x q x q at the weight level) and w + (-w) pairs exist (meson-shaped
    singlets in q x q^c) — the confinement-COMPATIBLE composites the
    script needs are group-theoretically present (existence only; binding
    is dynamics, walled).
  FACT 4 (the punchline): Q(u)+Q(u)+Q(d)+Q(e) = 0 EXACTLY and
    Q(u)+Q(d)+Q(d) = 0 EXACTLY — the hydrogen-shape and neutron-shape
    are FORCED NEUTRAL by the same anomaly arithmetic that forces Y
    (which, per memo 78, NEEDS the gravitational condition): the exact
    neutrality of atoms — the fact that lets large-scale structure be
    gravity-dominated rather than electrically dominated — is a SCRIPT
    row, not an accident of values.
FENCES: existence/neutrality of SHAPES only — no binding energy, no
stability, no abundance (schedule/dynamics, Gates 2/3); Q = T3 + Y is
the standard embedding convention (CITED), its output RATIOS are the
derived structure; frame observer-paid as always.  Gate 5 untouched.
"""
import itertools
from fractions import Fraction as F
from collections import defaultdict
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
Ysm={i: sp2.Rational(Yv[i]/Yqv)/6 for i in range(27)}
if Ysm[SM15['uc'][0]]==sp2.Rational(1,3):
    SM15['uc'],SM15['dc']=SM15['dc'],SM15['uc']
assert Ysm[SM15['uc'][0]]==sp2.Rational(-2,3) and Ysm[SM15['dc'][0]]==sp2.Rational(1,3)

# electric charge functional
Q={i: sp2.Rational(t3[i],2)+Ysm[i] for i in range(27)}

# FACT 1: the charge table
qU=[i for i in SM15['q'] if Q[i]==sp2.Rational(2,3)]
qD=[i for i in SM15['q'] if Q[i]==sp2.Rational(-1,3)]
assert len(qU)==3 and len(qD)==3
lN=[i for i in SM15['l'] if Q[i]==0]; lE=[i for i in SM15['l'] if Q[i]==-1]
assert len(lN)==1 and len(lE)==1
assert all(Q[i]==sp2.Rational(-2,3) for i in SM15['uc'])
assert all(Q[i]==sp2.Rational(1,3)  for i in SM15['dc'])
assert Q[SM15['ec'][0]]==1
others=[i for i in range(27) if i not in set().union(*[set(v) for v in SM15.values()])]
higgsQ=sorted(Q[i] for i in others if ctype[i]=='1' and t3[i] in (1,-1))
exoQ=sorted(set(Q[i] for i in others if ctype[i]!='1'))
neuQ=[Q[i] for i in others if ctype[i]=='1' and t3[i]==0]
print("FACT 1: the forced charge table (Q = T3 + Y, ratios):")
print(f"   u 2/3 (x3), d -1/3 (x3), u^c -2/3, d^c 1/3, nu 0, e -1, e^c 1")
print(f"   Higgs-doublet members {higgsQ}; exotics {exoQ}; neutrals {neuQ}")
# correction filed in-run: the draft preregistered [-1,-1,0,0]; the machine
# returned [-1,0,0,+1] — each doublet has ONE charged and ONE neutral member
# (H_u = (H+, H0), H_d = (H0, H-)): the correct SM Higgs pattern; the
# draft's list was an arithmetic slip, corrected to the measured pattern.
assert sorted(map(sp2.Rational,higgsQ))==[-1,0,0,1]
assert set(exoQ)=={sp2.Rational(-1,3),sp2.Rational(1,3)} and neuQ==[0,0]

# FACT 2: charge quantization
for i in range(27):
    if ctype[i]=='1':
        assert Q[i]==int(Q[i]), f"BRANCH FRACTURE: color-singlet {i} has Q={Q[i]} — non-integer: thesis-failure signal"
    else:
        assert (3*Q[i])==int(3*Q[i]) and Q[i]!=int(Q[i])
print("FACT 2: CHARGE QUANTIZATION — every color-singlet has INTEGER charge;")
print("   every colored state has charge in (1/3)Z \\ Z.  (BRANCH FRACTURE did not fire.)")

# FACT 3: color-singlet composability at weight level
cw=[ (ipr(W[i],tuple(sp2.Rational(x) for x in pairs[COLOR][0])), ipr(W[i],tuple(sp2.Rational(x) for x in pairs[COLOR][1])) ) for i in range(27)]
c3w=sorted(set(cw[i] for i in range(27) if ctype[i]=='3'))
assert len(c3w)==3 and tuple(sum(x) for x in zip(*c3w))==(0,0)
c3bw=sorted(set(cw[i] for i in range(27) if ctype[i]=='3b'))
assert set(c3bw)=={tuple(-x for x in w) for w in c3w}
print("FACT 3: the three color weights of the 3 sum to ZERO (baryon-shaped singlet")
print("   exists in q x q x q at weight level) and the 3b weights are their negatives")
print("   (meson-shaped singlets exist in q x q^c).  Existence only; binding is dynamics.")

# FACT 4: the punchline
H_charge = Q[qU[0]]+Q[qU[0]]+Q[qD[0]]+Q[lE[0]]
N_charge = Q[qU[0]]+Q[qD[0]]+Q[qD[0]]
print(f"FACT 4: Q(uud) + Q(e) = {H_charge}   |   Q(udd) = {N_charge}")
assert H_charge==0 and N_charge==0
print("""   THE HYDROGEN-SHAPE AND NEUTRON-SHAPE ARE EXACTLY NEUTRAL — forced by the
   same anomaly arithmetic that forces Y (which needs the gravitational
   condition, memo 78).  The exact neutrality of atoms — the fact that lets
   the large-scale universe be gravity-dominated instead of electrically
   dominated — is a SCRIPT row of the record, not an accident of values.""")

print("""
THE ATOM SHAPE: the record's script runs one rung further than the SM
spectrum — it forces that neutral atoms are POSSIBLE, exactly: quantized
charges, composable color singlets, and hydrogen/neutron neutrality to
zero, all ratio-level consequences of the forced hypercharge.  Whether
atoms FORM (binding, rates, abundances) is schedule/dynamics —
observer-side or walled, as typed in memo 83.  Gate 5 untouched.""")
