#!/usr/bin/env python3
"""Is C1's criterion as written TRUE?  'tau anti-symplectic involution preserving L
setwise  =>  L isotropic'.   Tested by explicit counterexample search."""
import sympy as sp

# standard symplectic R^4 : basis e1,f1,e2,f2 ; omega = e1^f1 + e2^f2
J = sp.Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]])
def om(a,b): return (a.T*J*b)[0,0]

e1 = sp.Matrix([1,0,0,0]); f1 = sp.Matrix([0,1,0,0])
e2 = sp.Matrix([0,0,1,0]); f2 = sp.Matrix([0,0,0,1])

# tau : e1<->f1 , e2<->f2   (an involution)
T = sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])

invol      = sp.simplify(T*T - sp.eye(4)) == sp.zeros(4,4)
antisympl  = sp.simplify(T.T*J*T + J) == sp.zeros(4,4)          # om(Ta,Tb) = -om(a,b)
L          = [e1, f1]                                            # span(e1,f1)
preserved  = all(any(sp.simplify(T*v - w).norm() == 0 or
                     sp.simplify(T*v - (-w)).norm() == 0 for w in L) for v in L)
isotropic  = all(sp.simplify(om(a,b)) == 0 for a in L for b in L)
fixed_ptwise = all(sp.simplify(T*v - v).norm() == 0 for v in L)

print("="*74)
print("C1 criterion as shipped:  tau anti-symplectic involution, tau(L)=L  =>  L isotropic")
print("="*74)
print(f"  tau is an involution            : {invol}")
print(f"  tau is anti-symplectic          : {antisympl}")
print(f"  tau preserves L = span(e1,f1)   : {preserved}")
print(f"  L is FIXED POINTWISE by tau     : {fixed_ptwise}")
print(f"  L is isotropic                  : {isotropic}   <-- om(e1,f1) = {om(e1,f1)}")
print()
counterexample = invol and antisympl and preserved and (not isotropic)
print(f"  COUNTEREXAMPLE FOUND            : {counterexample}")
print()

# the CORRECTED criterion: L inside the fixed-point set of an anti-symplectic involution
print("-"*74)
print("corrected criterion:  L contained in Fix(tau), tau anti-symplectic  =>  L isotropic")
T2 = sp.diag(1,-1,1,-1)                       # e_i fixed, f_i negated
inv2   = sp.simplify(T2*T2 - sp.eye(4)) == sp.zeros(4,4)
anti2  = sp.simplify(T2.T*J*T2 + J) == sp.zeros(4,4)
L2     = [e1, e2]                             # inside Fix(T2)
fix2   = all(sp.simplify(T2*v - v).norm() == 0 for v in L2)
iso2   = all(sp.simplify(om(a,b)) == 0 for a in L2 for b in L2)
print(f"  tau2 involution={inv2}  anti-symplectic={anti2}  L2 in Fix(tau2)={fix2}")
print(f"  L2 isotropic                    : {iso2}")
print()
print("  PROOF (one line): a,b in Fix(tau) => om(a,b) = om(tau a, tau b) = -om(a,b) => 0.")
print("  The shipped version replaced 'Fix(tau)' with 'tau(L)=L', which does NOT give the")
print("  first equality. The counterexample above is that gap, realised.")

ok = counterexample and (inv2 and anti2 and fix2 and iso2)
print()
print(f"  VERDICT: C1 as shipped is FALSE. Corrected form verified. (test valid: {ok})")
raise SystemExit(0 if ok else 1)
