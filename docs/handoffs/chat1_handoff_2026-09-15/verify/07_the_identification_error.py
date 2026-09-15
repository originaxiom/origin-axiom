#!/usr/bin/env python3
"""ITEM 7 --- THE IDENTIFICATION ERROR cc CAUGHT. Verified here. This is the correction
that matters most in this drop; read it before anything else.

WHAT I DID: called (x,y,z) = (w-1, -2w, -2) "the object's geometric point" and then
evaluated B497's strata multipliers there.

WHY IT IS WRONG: that point is the geometric character of the KNOT GROUP, computed from
SnapPy's 2-generator presentation of pi_1(m004). B497's strata are trace maps of the
FIBER's F_2 (the once-punctured torus). Those are different F_2's. Evaluating a
fiber-side multiplier at a knot-group character is a category error.

THE TEST cc NAMES: the fiber's geometric point must be FIXED by the monodromy trace map
T_1 (and by T_1^2). Mine is fixed by neither.
"""
import sympy as sp
x,y,z=sp.symbols('x y z'); K=x**2+y**2+z**2-x*y*z-2
T1=(z,x,x*z-y)                                  # a->ab, b->a  (the tick's square, RL)
def ap(T,p): return tuple(sp.simplify(c.subs({x:p[0],y:p[1],z:p[2]},simultaneous=True))
                          if hasattr(c,'subs') else c for c in T)
w=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
mine=(w-1,-2*w,sp.Integer(-2))
print("=== my point ===")
print(f"  p      = {tuple(sp.simplify(c) for c in mine)}")
print(f"  kappa  = {sp.simplify(sp.expand(K.subs({x:mine[0],y:mine[1],z:mine[2]},simultaneous=True)))}  (= 2 + w)")
p1=ap(T1,mine); p2=ap(T1,p1)
print(f"  T1(p)  = {p1}   fixed by T1  : {all(sp.simplify(a-b)==0 for a,b in zip(p1,mine))}")
print(f"  T1^2(p)= {p2}   fixed by T1^2: {all(sp.simplify(a-b)==0 for a,b in zip(p2,mine))}")
print()
print("=== the actual fixed points of T1 ===")
sol=sp.solve([T1[0]-x,T1[1]-y,T1[2]-z],[x,y,z],dict=True)
for s in sol:
    p=(s.get(x,x),s.get(y,y),s.get(z,z))
    if all(getattr(v,'is_number',False) or isinstance(v,(int,sp.Integer)) for v in p):
        kv=sp.simplify(K.subs({x:p[0],y:p[1],z:p[2]},simultaneous=True))
        print(f"  {str(p):18s}  kappa = {kv}")
print()
print("  The fiber boundary of a once-punctured-torus bundle IS the commutator [a,b],")
print("  which is PERIPHERAL, hence parabolic at the complete structure: tr = -+2,")
print("  i.e. kappa = -+2. cc's 'not -2' is exactly this. My kappa = 2+w is not +-2,")
print("  so my point is NOT the fiber's geometric point.")
print()
print("  CONSEQUENCE: the 'kappa-2 = w' identification, the 'stratum-3 multiplier = w'")
print("  coincidence, and the 'omega -> omega^2' reading are all evaluations of")
print("  fiber-side objects at a knot-side point. WITHDRAWN IN FULL.")
print("  What survives: the multiplier IDENTITIES (item 3b) and J(m004) = 1 (item 5),")
print("  neither of which uses this point.")
