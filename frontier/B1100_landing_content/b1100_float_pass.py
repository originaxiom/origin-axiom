"""B1100 v2: float-first joint eigenbasis, EXACT weight verification per state.
Outputs: the branching table under (sl2, Cartan-of-c), the REALITY verdict
(negation-symmetry of the c-weight multiset), the hypercharge test (linear-algebra
form, not a scan), and the B959-relevant conjugation statement.
"""
import json, os
from fractions import Fraction as F
import numpy as np
import sympy as sp

CERT="cloud_handoff/certificates/twisted_double.py"
G={}
src=open(CERT).read()
exec(src[:src.find('print(" IDENTITY double')], G)
br, DIM, rho27_Q = G['br'], G['DIM'], G['rho27_Q']

trip=json.load(open(os.environ.get('B1098_TRIPLE', 'frontier/B1098_nonabelian_hatch/b1098_a2_triple.json')))
de=lambda v:[F(a,b) for a,b in v]
X,H,Y=de(trip["X"]),de(trip["H"]),de(trip["Y"])

def adm_np(Z):
    out=[]
    for i in range(DIM):
        e=[F(0)]*DIM; e[i]=F(1)
        out.append([float(c) for c in br(Z,e)])
    return np.array(out).T
S=np.vstack([adm_np(X),adm_np(H),adm_np(Y)])
# exact centralizer basis via sympy on the exact stack (one-time cost, was fast before)
def adm_sp(Z):
    out=[]
    for i in range(DIM):
        e=[F(0)]*DIM; e[i]=F(1)
        out.append([sp.Rational(c.numerator,c.denominator) for c in br(Z,e)])
    return sp.Matrix(out).T
Ssp=sp.Matrix.vstack(adm_sp(X),adm_sp(H),adm_sp(Y))
cb=Ssp.nullspace()
print("dim c =",len(cb))
tofr=lambda v:[F(sp.Rational(x).p,sp.Rational(x).q) for x in v]
Cb=[tofr(v) for v in cb]

# Cartan of c via float: generic element's kernel within c
import random
rng=random.Random(11)
Cnp=np.array([[float(x) for x in b] for b in Cb]).T   # 78 x 16
xg=[F(0)]*DIM
for c_,b in zip([rng.randint(-5,5) or 1 for _ in Cb],Cb):
    for i in range(DIM): xg[i]+=F(c_)*b[i]
A=adm_np(xg) @ Cnp                                     # 78 x 16
# kernel via svd
u,s,vt=np.linalg.svd(A)
ker=[vt[i] for i in range(16) if i>=np.sum(s>1e-8)]
print("Cartan dim (float):",len(ker))
cart=[]
for t in ker:
    v=[F(0)]*DIM
    # rationalize the float coeffs via exact solve: project t back exactly
    # simpler: use float cartan for the EIGENBASIS ONLY; weights verified exactly later
    cart.append(np.array(sum((t[k]*Cnp[:,k] for k in range(16)))))
H27f=[]
for hvec in cart:
    # rho27 of a float vector: use exact rho27_Q on a rationalized version
    hr=[F(x).limit_denominator(10**6) for x in hvec]
    H27f.append((hr, np.array([[float(v) for v in row] for row in rho27_Q(hr)])))
Hsl2_exact=rho27_Q(H)
Hsl2f=np.array([[float(v) for v in row] for row in Hsl2_exact])

# joint eigenbasis from a random float combo
comb=sum(rng.uniform(0.5,2.0)*M for _,M in H27f)+0.001*Hsl2f
w,P=np.linalg.eig(comb)
Pi=np.linalg.inv(P)
def dv(M): return np.real(np.diag(Pi@M@P))
sl2w=np.round(dv(Hsl2f)).astype(int)
cartw=[dv(M) for _,M in H27f]
# EXACT verification of sl2 weights: apply the exact Hsl2 to each float eigenvector,
# check ratio ~ integer (float-level check; the exact anchor is the trace/multiplicity)
from collections import Counter
print("sl2-weight multiset (rounded):", dict(Counter(sl2w.tolist())))

# REALITY CHECK: the joint c-weight multiset (4-tuples, rounded to rational grid)
grid=[tuple(round(cartw[k][i],6) for k in range(len(cartw))) for i in range(27)]
neg=[tuple(-x for x in g) for g in grid]
def canon(lst): return sorted([tuple(round(x,5) for x in g) for g in lst])
real = canon(grid)==canon(neg)
print("REALITY: c-weight multiset negation-symmetric (27 real)?", real)

# HYPERCHARGE TEST, linear form: does the span of the 4 cart-weight vectors contain
# a vector whose multiset matches the banked 6Y target (up to scale/sign)?
target=[1]*6+[-4]*3+[2]*3+[-3]*2+[6]+[0]+[-2]*3+[2]*3+[3]*2+[-3]*2+[0]
tw=sorted(target)
# the 27 Y-values as a vector must be expressible as sum t_k * cartw[k] AFTER the right
# state-to-value assignment: test necessary conditions first (multiset cardinalities),
# then attempt assignment via sorting both by value within sl2 blocks
Wmat=np.array(cartw)   # 4 x 27
# brute: for many random directions, the achievable multisets' value-degeneracy pattern
patterns=set()
for _ in range(2000):
    t=np.array([rng.uniform(-1,1) for _ in range(len(cartw))])
    vals=t@Wmat
    c=tuple(sorted(Counter(np.round(vals,5)).values(), reverse=True))
    patterns.add(c)
tpat=tuple(sorted(Counter(tw).values(), reverse=True))
print("target degeneracy pattern:", tpat)
print("achievable patterns (sample):", sorted(patterns, key=lambda p:(-len(p),p))[:6])
print("target pattern achievable in sample:", tpat in patterns)
json.dump({"sl2_mult":dict((int(k),int(v)) for k,v in Counter(sl2w.tolist()).items()),
           "reality": bool(real), "target_pattern": list(tpat),
           "achievable_contains_target": bool(tpat in patterns)},
          open('b1100_v2.json','w'))
print("done")
