"""Validate the cup-product implementation on H^1(T;W) before trusting any verdict.

Three independent checks, on random commuting pairs (A,B) in SL2 acting via Sym^m:
  1. WELL-DEFINED: <B^1, Z^1> = 0  (coboundaries pair to zero) -- catches sign/order errors
  2. PARITY:  Gram on H^1 is antisymmetric for m even, symmetric for m odd
  3. PERFECT: Gram on H^1 has full rank = t_1  (Poincare duality on the torus)
"""
import sys; sys.path.insert(0,'/tmp/sweep')
from cup import *
from q12 import *
from fi_lib import sym, invariants
from fractions import Fraction as Fr

def q(a,b=0,c=0,d=0): return (Fr(a),Fr(b),Fr(c),Fr(d))
def qf(a,b=0,c=0,d=0): return (Fr(a),Fr(b),Fr(c),Fr(d))

def check(A2,B2,m,label):
    d=m+1
    A=sym(A2,m); B=sym(B2,m)
    # A,B must commute (they are the images of a commuting pair)
    assert mm(A,B)==mm(B,A), "images do not commute"
    g1=[[ONE,ONE],[Z,ONE]]; g2=[[ONE,Z],[ONE,ONE]]
    Fm=invariant_forms([sym(g1,m),sym(g2,m)],d)[0]
    # GUARD: the SL2 form must actually be invariant under A,B -- catches non-SL2 test inputs
    for g,nm in ((A,'A'),(B,'B')):
        gt=transpose(g)
        assert mm(mm(gt,Fm),g)==Fm, f"{label} m={m}: Sym^m form NOT invariant under {nm} (is the pair in SL2?)" 
    Zs,Bs=cocycles(A,B,d)
    t1=len(Zs)-rank(Bs); t0=invariants([A,B],d)
    # 1. coboundaries annihilate everything
    worst=max((0 if is_zero(cup(b,z,A,B,Fm,d)) else 1) for b in Bs for z in Zs) if Bs and Zs else 0
    worst2=max((0 if is_zero(cup(z,b,A,B,Fm,d)) else 1) for b in Bs for z in Zs) if Bs and Zs else 0
    # 2/3. Gram on a basis of H^1 = Z^1/B^1
    H=reduce_mod(Zs,Bs,2*d)
    G=gram(H,A,B,Fm,d)
    n=len(G)
    symm = all(G[i][j]==G[j][i] for i in range(n) for j in range(n))
    alt  = all(G[i][j]==neg(G[j][i]) for i in range(n) for j in range(n))
    rk   = rank(G) if n else 0
    print(f"  {label} m={m}: t0={t0} t1={t1} dimH1={n} | coboundary-kills={'YES' if worst==0 and worst2==0 else '** NO **'}"
          f" | sym={symm} alt={alt} | rank={rk}/{n} {'PERFECT' if rk==n else '** DEGENERATE **'}")
    return (worst==0 and worst2==0), (alt if m%2==0 else symm), rk==n

# --- test pairs: commuting elements of SL2 ---
PAIRS=[
  ("unipotent", [[ONE,ONE],[Z,ONE]],          [[ONE,q(3)],[Z,ONE]]),
  ("unipotent2",[[ONE,q(1,0,0,1)],[Z,ONE]],   [[ONE,q(0,0,2,0)],[Z,ONE]]),   # entries in Q(zeta12)
  ("diagonal",  [[q(2),Z],[Z,qf(Fr(1,2))]],    [[q(3),Z],[Z,qf(Fr(1,3))]]),
  ("dg-zeta",   [[q(1,1),Z],[Z,inv(q(1,1))]],   [[q(2),Z],[Z,inv(q(2))]]),
]
ok=True
for label,A2,B2 in PAIRS:
    print(f"[{label}]")
    for m in range(1,7):
        a,b,c=check(A2,B2,m,label)
        ok &= a and b
print("\nALL WELL-DEFINEDNESS + PARITY CHECKS PASSED:",ok)
