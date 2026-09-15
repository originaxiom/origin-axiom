#!/usr/bin/env python3
"""MEMO-58 CELL: THE ANOMALY PAYMENT — the dark block is the exact
quantum-consistency payment for the visible one: the full 27's cubic weight
tensor vanishes identically, the SM-shaped 16 alone is anomalous in every
u(1)-touching channel, and the 10 (+) 1 cancels it component for component.

Serious-probe rung 3 for ladder rung X3.  Anomaly cancellation is INTEGER
equations (value-level but not value-matching — the firewall permits it; cf.
the corpus's registered L132).  B950's rule applies: anomaly-freedom of the
27 is textbook E6 lore, so this cell REPRODUCES it in the object's own stack
— the added exact content is the SPLIT: the component-by-component payment
structure between the visible and dark blocks, in the object's coordinates.

Basis of Cartan functionals: q = the family u(1) charge (q3 = 3<w,omega_1>,
integer: {1 on 16, -2 on 10, 4 on 1}) plus the five D5 Dynkin labels
m_j = <w, alpha_j> (j = the non-minuscule nodes).  Frame check: the deleted-
node subdiagram must be D5 (Cartan submatrix determinant 4).

PREREGISTERED (every claim an assert):
  FACT 0 (all anomalies die at once): the full symmetric cubic tensor
    T_27[abc] = sum over the 27 of f_a f_b f_c  (f in {q, m_j}) vanishes in
    ALL 56 components — every gauge anomaly of every subgroup chain with
    legs in the Cartan (and by invariance, every nonabelian leg) is zero.
  FACT 1 (the visible block alone is inconsistent): T_16 does NOT vanish.
    Its pure-D5 components are all zero (the 16 is an so(10) rep — SO(10)
    is anomaly-safe), and its nonzero content is exactly the q-touching
    channels:  [u(1)]^3 = 16,  linear/grav = sum q = 16,  and the mixed
    [D5]^2 u(1) form  B_16[jk] = sum_{16} m_j m_k  with coefficient q16=1.
  FACT 2 (the payment): T_{10+1} = -T_16 in EVERY component (with FACT 0
    this is forced; asserted directly): the dark block carries exactly the
    opposite anomaly tensor.  [u(1)]^3: 10.(-8) + 64 = -16; linear:
    -20 + 4 = -16; mixed: q10 B_10 = -2 B_10.
  FACT 3 (the mechanism is the Dynkin ratio): the mixed cancellation
    q16 B_16 + q10 B_10 = 0 with q16=1, q10=-2 forces B_16 = 2 B_10 as
    5x5 forms — the so(10) Dynkin-index ratio T(16)/T(10) = 2, exact,
    entry by entry; and the singlet contributes B_1 = 0.
=> READING (labeled): if the family u(1) is gauged, the visible generation
   alone is quantum-inconsistent; the dark states are not decoration but
   the anomaly payment.  Reproduced-not-predicted per B950; the D5 frame
   fence of memo 56 applies.  Gate 5 untouched (integer identities only).
"""
import itertools
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# family charge and classes
q3={a: int(3*ipr(weights[a], omega1)) for a in range(27)}
cnt=Counter(q3.values())
c16=next(v for v,m in cnt.items() if m==16); c10=next(v for v,m in cnt.items() if m==10)
c1 =next(v for v,m in cnt.items() if m==1)
assert (c16,c10,c1)==(1,-2,4)
cls={a:('16' if q3[a]==c16 else '10' if q3[a]==c10 else '1') for a in range(27)}

# D5 nodes = all but the minuscule node (node 0, where omega_1 pairs 1)
d5nodes=[j for j in range(6) if j!=0]
# frame check: deleted-node diagram is D5 (Cartan submatrix det 4)
import sympy as sp2
sub=sp2.Matrix(5,5, lambda i,j: ipr(simple[d5nodes[i]], simple[d5nodes[j]]))
print(f"frame check: det(Cartan of deleted-node subdiagram) = {sub.det()} (D5 expects 4)")
assert sub.det()==4

# functionals: f[0] = q3, f[1..5] = Dynkin labels on D5 nodes
def mval(a,j): return int(ipr(weights[a], simple[j]))
FUN=[lambda a: q3[a]] + [ (lambda j: (lambda a: mval(a,j)))(j) for j in d5nodes ]
NAMES=['q']+[f"m{j}" for j in d5nodes]
NF=len(FUN)

def cubic_tensor(states):
    T={}
    for i in range(NF):
        for j in range(i,NF):
            for k in range(j,NF):
                T[(i,j,k)]=sum(FUN[i](a)*FUN[j](a)*FUN[k](a) for a in states)
    return T
ALL=list(range(27))
S16=[a for a in ALL if cls[a]=='16']; S10=[a for a in ALL if cls[a]=='10']; S1=[a for a in ALL if cls[a]=='1']
T27=cubic_tensor(ALL); T16=cubic_tensor(S16); TD=cubic_tensor(S10+S1)

# FACT 0
nz27=[k for k,v in T27.items() if v!=0]
print(f"FACT 0: full 27 cubic tensor: {len(T27)} components, nonzero: {len(nz27)}")
assert not nz27

# FACT 1
pure=[k for k in T16 if 0 not in k]
assert all(T16[k]==0 for k in pure)
qq=[k for k,v in T16.items() if v!=0]
print(f"FACT 1: 16-block: pure-D5 components all ZERO ({len(pure)} checked);")
print(f"        nonzero components (all q-touching): "+", ".join(f"{tuple(NAMES[i] for i in k)}={T16[k]}" for k in sorted(qq)))
assert all(0 in k for k in qq) and qq
assert T16[(0,0,0)]==16
lin16=sum(q3[a] for a in S16); linD=sum(q3[a] for a in S10+S1)
print(f"        linear (grav^2 u(1)) channel: sum q over 16 = {lin16}, over dark = {linD}")
assert lin16==16 and linD==-16

# FACT 2
assert set(TD)==set(T16) and all(TD[k]==-T16[k] for k in T16)
print("FACT 2: T_dark = -T_16 in EVERY component — the payment is exact")
print(f"        [u(1)]^3: 16 vs {10*(-2)**3 + 4**3} (= -16)")

# FACT 3: Dynkin ratio
B16={(i,j): sum(mval(a,d5nodes[i-1])*mval(a,d5nodes[j-1]) for a in S16) for i in range(1,6) for j in range(i,6)}
B10={k: sum(mval(a,d5nodes[k[0]-1])*mval(a,d5nodes[k[1]-1]) for a in S10) for k in B16}
B1 ={k: sum(mval(a,d5nodes[k[0]-1])*mval(a,d5nodes[k[1]-1]) for a in S1) for k in B16}
assert all(v==0 for v in B1.values())
assert all(B16[k]==2*B10[k] for k in B16)
assert any(v!=0 for v in B10.values())
print("FACT 3: B_16 = 2 * B_10 entry-by-entry (so(10) Dynkin ratio T(16)/T(10) = 2,")
print("        exact) and B_singlet = 0: the mixed [D5]^2 u(1) cancellation is")
print("        1*B_16 + (-2)*B_10 = 0 — the index ratio IS the payment mechanism")

print("""
THE ANOMALY PAYMENT: the object's 27 kills every gauge anomaly at once
(cubic weight tensor identically zero, reproduced in-stack), but the split
is not symmetric — the SM-shaped 16 alone is anomalous in exactly the
u(1)-touching channels, its pure-D5 anomalies already vanishing, and the
dark block 10 (+) 1 carries the precise opposite tensor: [u(1)]^3 16 vs
-16, linear 16 vs -16, mixed via the exact Dynkin ratio 2.  If the family
u(1) is gauged, the dark states are the quantum-consistency payment for
the visible generation.  Integer identities only; reproduced-not-predicted
(B950); D5 frame fence carried; Gates 2/3/5 not crossed.""")
