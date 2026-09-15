#!/usr/bin/env python3
"""ITEM 2 --- 'tonight's G2', cited twice. This is all it is.

CLAIM (verified): on Aut(F_2), the multiplier by which a trace map rescales the
Goldman bracket EQUALS the determinant of its abelianisation.
Goldman bracket on X(F_2): {x,y} = 2z-xy, {y,z} = 2x-yz, {z,x} = 2y-xz.
kappa = x^2+y^2+z^2-xyz-2 is its Casimir.
NOTE: the structure functions ARE grad(kappa) --- so this is the Nambu bracket of
kappa, and it degenerates exactly at kappa's critical points (= codex R036's 5 points).
SCOPE: this is a statement about Aut(F_2) acting on the character variety. It does
NOT by itself give B497's strata 2/3/4 'a geometric meaning' --- that was my gloss.
"""
import sympy as sp
x, y, z = sp.symbols('x y z')
KAP = x**2 + y**2 + z**2 - x*y*z - 2
BXY, BYZ, BZX = 2*z - x*y, 2*x - y*z, 2*y - x*z
def goldman(f, g):
    fx, fy, fz = [sp.diff(f, v) for v in (x, y, z)]
    gx, gy, gz = [sp.diff(g, v) for v in (x, y, z)]
    return sp.expand((fx*gy-fy*gx)*BXY + (fy*gz-fz*gy)*BYZ + (fz*gx-fx*gz)*BZX)
def sub(T, e): return sp.expand(e.subs({x: T[0], y: T[1], z: T[2]}, simultaneous=True))
def multiplier(T):
    out = []
    for (u, v), st in [((T[0],T[1]),BXY), ((T[1],T[2]),BYZ), ((T[2],T[0]),BZX)]:
        lhs, rhs = goldman(u, v), sub(T, st)
        if sp.simplify(rhs) == 0: return None
        q = sp.simplify(sp.cancel(lhs/rhs))
        if not q.is_number: return None
        out.append(q)
    return out[0] if len(set(out)) == 1 else None
print("kappa is the Casimir:", all(sp.simplify(goldman(KAP, v)) == 0 for v in (x,y,z)))
print("C-NULL decoy x^2y+z^3-3xz central:",
      all(sp.simplify(goldman(x**2*y+z**3-3*x*z, v)) == 0 for v in (x,y,z)), "(must be False)")
print("structure fns == grad(kappa):",
      all(sp.simplify(a-b)==0 for a,b in [(BXY,sp.diff(KAP,z)),(BYZ,sp.diff(KAP,x)),(BZX,sp.diff(KAP,y))]))
print()
for nm, T, det in [('P  a<->b',(y,x,z),-1), ('I  a->a^-1',(x,y,x*y-z),-1), ('U  a->ab',(z,y,y*z-x),1)]:
    print(f"  {nm:12s} multiplier = {multiplier(T)}   det = {det}")
print("  identity multiplier (C-ALIVE):", multiplier((x,y,z)))
