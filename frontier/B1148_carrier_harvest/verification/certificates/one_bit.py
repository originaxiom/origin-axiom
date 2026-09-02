#!/usr/bin/env python3
"""MEMO-44 CELL: ONE BIT OR TWO — is the geometric branch's mirror the beat's
bit, or the beat's bit composed with charge conjugation?

The reduction (exact): the beat's real structure is sigma_beat = exp(ad qE) o gal,
whose linear part is an EXPONENTIAL — manifestly inner.  The closing's real
structure is sigma_close = T o conj with T = theta_matrix(g,c) (the memo-10 hit's
mirror, memo 27/33's gluing map), a rational linear automorphism.  Their ratio is
T o (inner), so:  THE TWO REAL STRUCTURES DEFINE THE SAME Z/2 CLASS  <=>  T IS
INNER.  E6 separates inner from outer on the 27: inner automorphisms preserve the
27's isomorphism class; outer ones carry it to the dual 27-bar.

PREREGISTERED two-outcome:
  A (T inner):  27 o T ~ 27  — ONE BIT: the geometric mirror IS the beat's bit
     up to inner; the internal->spacetime bridge candidate stands at algebra level.
  B (T outer):  27 o T ~ 27-bar — TWO FACES: the geometric mirror = the beat's
     bit composed with the OUTER class (charge conjugation); the observer's C is
     exactly the discrepancy between the two mirrors.
Cross-check: tr(T) on the 78 pins the involution class (outer: 26 [f4] or -6
[sp8]; inner: -2 [sl2+sl6] or 14 [so(10)+u(1)]).
"""
import random
from fractions import Fraction as F
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])   # exact e6 + the 27 (rho27_Q verified on 3003 brackets in-run)

import importlib.util
spec=importlib.util.spec_from_file_location("theta_dump", SCR+"/theta_dump.py")
td=importlib.util.module_from_spec(spec); spec.loader.exec_module(td)
assert td.N_FP==N and td.DIM_FP==DIM
assert list(td.ROOTS_FP)==list(ROOTS), "ccb basis fingerprint mismatch between stacks"
T=td.TMAT
print("frame check: ROOTS fingerprint identical across stacks (%d roots)"%len(ROOTS))

def mv(M,v): return [sum(M[i][j]*v[j] for j in range(DIM) if v[j]!=0) for i in range(DIM)]
# T is an involution and a bracket automorphism IN THIS STACK (operational frame proof)
random.seed(7)
for _ in range(25):
    i=random.randrange(DIM); j=random.randrange(DIM)
    ei=[F(1) if k==i else F(0) for k in range(DIM)]; ej=[F(1) if k==j else F(0) for k in range(DIM)]
    Ti=mv(T,ei); Tj=mv(T,ej)
    assert mv(T,Ti)==ei
    assert br(Ti,Tj)==mv(T,br(ei,ej))
print("T^2 = id and bracket equivariance: verified on 25 random basis pairs, exact")

trT=sum(T[i][i] for i in range(DIM))
print(f"tr(T) on the 78 = {trT}   (outer involutions: 26 [f4] / -6 [sp8]; inner: -2 / 14)")

# Cartan preservation and the induced 6x6 block
cart_ok=all(all(T[i][j]==0 for i in range(N,DIM)) for j in range(N))
print("T preserves the Cartan subalgebra:", cart_ok)
assert cart_ok
Th=[[T[i][j] for j in range(N)] for i in range(N)]
def inv6(M):
    n=N; aug=[[F(M[i][j]) for j in range(n)]+[F(1) if k==i else F(0) for k in range(n)] for i in range(n)]
    for col in range(n):
        p=next(i for i in range(col,n) if aug[i][col]!=0)
        aug[col],aug[p]=aug[p],aug[col]
        pv=aug[col][col]; aug[col]=[x/pv for x in aug[col]]
        for i in range(n):
            if i!=col and aug[i][col]!=0:
                fq=aug[i][col]; aug[i]=[x-fq*y for x,y in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]
Thi=inv6(Th)

# 27 weights in pairing coordinates
Hs=[rho27_Q([F(1) if k==i else F(0) for k in range(DIM)]) for i in range(N)]
wt=[tuple(Hs[i][a][a] for i in range(N)) for a in range(27)]
# transformed weight: mu' = (Th^{-1})^T mu   (mu'(h_i) = mu(Th^{-1} h_i))
def transf(mu): return tuple(sum(Thi[j][i]*mu[j] for j in range(N)) for i in range(N))
tw=[transf(m) for m in wt]
setA=set(wt); setB=set(tuple(-x for x in m) for m in wt)
inA=all(m in setA for m in tw); inB=all(m in setB for m in tw)
print(f"T-transformed 27-weight set == 27 weights: {inA}   == 27-BAR weights (negatives): {inB}")
assert inA != inB, "weight test inconclusive"

if inA:
    # hypothesis A: monomial intertwiner M with rho(Tx) = M rho(x) M^-1
    pi={a: wt.index(tw[a]) for a in range(27)}
    def rho_of(x): return rho27_Q(x)
    hyp='A'
else:
    # hypothesis B: rho(Tx) = M rhobar(x) M^-1 with rhobar(x) = -rho(x)^T
    negwt=[tuple(-x for x in m) for m in wt]
    pi={a: wt.index(transf(negwt[a])) if False else None for a in range(27)}
    # basis vector a carries rhobar-weight -wt[a]; its image must carry (rho o T)-weight
    # = transf^{-1}? — set up directly: M e_a = m_a e_{sig(a)} with wt[sig(a)] = transf(-wt[a])
    pi={a: wt.index(transf(tuple(-x for x in wt[a]))) for a in range(27)}
    hyp='B'
print(f"proceeding under hypothesis {hyp}; the permutation is a bijection: {sorted(pi.values())==list(range(27))}")
assert sorted(pi.values())==list(range(27))

# generators and their T-images (in this stack)
gens=[]
for i in range(N):
    r=tuple(1 if k==i else 0 for k in range(N))
    for rr in (r, tuple(-x for x in r)):
        x=evec(rr)
        gens.append((rho27_Q(x), rho27_Q(mv(T,x))))
def rbar(Mx): return [[-Mx[j][i] for j in range(27)] for i in range(27)]

# scalar propagation: m_a unknowns; equations rho(Tx)[pi(a2),pi(a1)] * m_a1 = m_a2 * S(x)[a2,a1]
# where S = rho (hyp A) or rhobar (hyp B)
m=[None]*27; m[0]=F(1)
changed=True
while changed:
    changed=False
    for S,RT in ((s, rt) for s,rt in [(g[0] if hyp=='A' else rbar(g[0]), g[1]) for g in gens]):
        for a1 in range(27):
            if m[a1] is None: continue
            for a2 in range(27):
                s=S[a2][a1]
                if s==0: continue
                lhs=RT[pi[a2]][pi[a1]]
                if m[a2] is None:
                    assert lhs!=0, "structure mismatch: zero vs nonzero entry"
                    m[a2]=lhs*m[a1]/s; changed=True
assert all(x is not None and x!=0 for x in m), "propagation incomplete or singular"
# full verification of the intertwiner on ALL 12 generators
ok=True
for g in gens:
    S=g[0] if hyp=='A' else rbar(g[0]); RT=g[1]
    for a1 in range(27):
        for a2 in range(27):
            lhs=RT[pi[a2]][pi[a1]]*m[a1]
            rhs=m[a2]*S[a2][a1]
            if lhs!=rhs: ok=False
print(f"monomial intertwiner M (27 scalars, all nonzero) verified on ALL 12 generators: {ok}")
assert ok

if hyp=='A':
    print("""
VERDICT — OUTCOME A: T is INNER-CLASS on the 27 (27 o T ~ 27).  ONE BIT:
the geometric branch's mirror and the beat's mirror define the same Z/2
real-structure class up to inner automorphism — the internal->spacetime
bridge candidate stands at the algebra level.""")
else:
    print("""
VERDICT — OUTCOME B: T is OUTER (27 o T ~ 27-BAR, the dual).  TWO FACES OF
THE MIRROR: the geometric branch's real structure equals the beat's real
structure COMPOSED WITH THE OUTER CLASS of E6 — charge conjugation.  The
discrepancy between the two mirrors is exactly the C bit (observer-paid in
the freedom ledger): sigma_close = sigma_beat o C up to inner.  Read with
memo 33's colored-sector fact (theta swaps 3 <-> 3bar pointwise): the
geometric mirror is the beat wearing charge conjugation — one private bit,
one public dressing, and the bridge question sharpens to whether the
DRESSED or the BARE mirror is the one spacetime reads.""")
