#!/usr/bin/env python3
"""ITEM 3b --- B497's four kappa-multiplier identities, verified."""
import sympy as sp
x,y,z=sp.symbols('x y z'); K=x**2+y**2+z**2-x*y*z-2
def kap(T): return sp.expand(K.subs({x:T[0],y:T[1],z:T[2]},simultaneous=True))
for nm,T,m in [('1 evolution   det +-1',(z,x,x*z-y),None),
               ('2 renormalize |det|>=2',(x**2-2,y**2-2,x*y*z-x**2-y**2+2),x**2*y**2),
               ('3 decoherence det 0',(z,z,x*y*z-x**2-y**2+2),x**2+y**2-x*y*z),
               ('4 erasure     non-inj',(z,z,z**2-2),0)]:
    ok = sp.simplify(kap(T)-K)==0 if m is None else sp.simplify(kap(T)-2-(K-2)*m)==0
    print(f"  stratum {nm}: identity holds = {ok}")
print()
print("  AT m004's GEOMETRIC POINT (x,y,z) = (w-1, -2w, -2):")
w=sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2
X,Y,Z=w-1,-2*w,sp.Integer(-2)
kk=sp.simplify(sp.expand(X**2+Y**2+Z**2-X*Y*Z-2))
print(f"     kappa = {kk}   kappa-2 = {sp.simplify(kk-2)}   == w : {sp.simplify(kk-2-w)==0}")
print(f"     stratum-3 multiplier = {sp.simplify(sp.expand(X**2+Y**2-X*Y*Z))}")
print()
print("  *** SCOPE, from the producing seat: this is ONE POINT. Applying the stratum-3")
print("  map moves you to a DIFFERENT point with a DIFFERENT multiplier. The 'omega ->")
print("  omega^2' reading is a single-step evaluation, NOT a group action. I presented")
print("  it as structure; that presentation is withdrawn.")
