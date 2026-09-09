#!/usr/bin/env python3
"""P-SEAM-02: (A) upgrade G2 from 2 citizens to all of Aut(F2); (B) run G3."""
import sympy as sp, itertools
x, y, z = sp.symbols('x y z')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2
BXY, BYZ, BZX = 2*z - x*y, 2*x - y*z, 2*y - x*z

def goldman(f, g):
    fx,fy,fz = [sp.diff(f,v) for v in (x,y,z)]
    gx,gy,gz = [sp.diff(g,v) for v in (x,y,z)]
    return sp.expand((fx*gy-fy*gx)*BXY + (fy*gz-fz*gy)*BYZ + (fz*gx-fx*gz)*BZX)

def sub(T, e): return sp.expand(e.subs({x:T[0], y:T[1], z:T[2]}, simultaneous=True))
def compose(T, S):  # apply S then T  (pullback composition on coordinates)
    return tuple(sp.expand(sub(S, c)) for c in T)

def multiplier(T):
    out=[]
    for (u,v), st in [((T[0],T[1]), BXY), ((T[1],T[2]), BYZ), ((T[2],T[0]), BZX)]:
        lhs, rhs = goldman(u,v), sub(T, st)
        if sp.simplify(rhs)==0: return None
        q = sp.simplify(sp.cancel(lhs/rhs))
        if not q.is_number: return None
        out.append(q)
    return out[0] if len(set(out))==1 else None

# ---------- (A) generators of Aut(F2): trace map + abelianization determinant ----------
P = ((y, x, z),            sp.Matrix([[0,1],[1,0]]))        # a<->b
I = ((x, y, x*y - z),      sp.Matrix([[-1,0],[0,1]]))       # a -> a^-1
U = ((z, y, y*z - x),      sp.Matrix([[1,1],[0,1]]))        # a -> ab
gens = {'P (a<->b)': P, 'I (a->a^-1)': I, 'U (a->ab)': U}

print("="*74); print("(A)  G2 upgraded: multiplier vs det on GENERATORS of Aut(F2)"); print("="*74)
gen_ok = True
for n,(T,M) in gens.items():
    c, d = multiplier(T), M.det()
    agree = (c == d); gen_ok &= bool(agree)
    print(f"  {n:14s} multiplier = {str(c):>3s}   det = {str(d):>3s}   agree = {agree}")

# multiplicativity check on composites (both maps are homomorphisms -> agreement extends)
print("\n  composites (spot-check that both are multiplicative):")
comp_ok = True
for a,b in itertools.product(gens, repeat=2):
    Ta,Ma = gens[a]; Tb,Mb = gens[b]
    T = compose(Ta,Tb); c = multiplier(T); d = (Ma*Mb).det()
    ok = (c == d); comp_ok &= bool(ok)
    print(f"    {a[:1]}o{b[:1]}  multiplier = {str(c):>3s}  det = {str(d):>3s}  {ok}")
print(f"\n  generators agree: {gen_ok}   composites agree: {comp_ok}")
print("  => multiplier and det are BOTH homomorphisms Aut(F2)->{+-1}; agreeing on a")
print("     generating set, they agree on ALL of Aut(F2). Stratum 1 is now covered,")
print("     not sampled.")

# ---------- (B) G3: where does the Goldman bivector actually degenerate? ----------
print("\n"+"="*74); print("(B)  G3: rank of the Poisson bivector, and is it {kappa=2}?"); print("="*74)
# 3x3 antisymmetric => rank is 0 or 2; rank 0 iff all three structure functions vanish
sols = sp.solve([BXY, BYZ, BZX], [x,y,z], dict=True)
print("  rank-0 locus (all three brackets vanish):")
pts=[]
for s in sols:
    pt = (s.get(x,x), s.get(y,y), s.get(z,z))
    if all(v.is_number for v in pt):
        k = sp.simplify(KAPPA.subs({x:pt[0],y:pt[1],z:pt[2]}, simultaneous=True))
        pts.append((pt,k)); print(f"     {str(pt):20s}  kappa = {k}")
on2  = [p for p,k in pts if k == 2]
off2 = [(p,k) for p,k in pts if k != 2]
# is the WHOLE surface kappa=2 degenerate?  test a generic point on it
tp = sp.solve(KAPPA.subs({x:1,y:1}) - 2, z); generic = [(1,1,t) for t in tp]
deg_generic = []
for g in generic:
    vals = [sp.simplify(b.subs({x:g[0],y:g[1],z:g[2]}, simultaneous=True)) for b in (BXY,BYZ,BZX)]
    deg_generic.append(all(v==0 for v in vals))
print(f"\n  generic points tested on {{kappa=2}}: {generic}")
print(f"  degenerate there? {deg_generic}")
G3_as_stated = bool(deg_generic) and all(deg_generic)
print(f"\n  G3 AS STATED ('{{kappa=2}} is exactly where the form drops rank'): {G3_as_stated}")
print(f"  CORRECTED STATEMENT:")
print(f"    the bivector is antisymmetric 3x3, so rank is 0 or 2 -- it degenerates only")
print(f"    at {len(pts)} ISOLATED POINTS, not on a surface.")
print(f"    {len(on2)} of them lie on {{kappa=2}}: {on2}")
print(f"    the others: {off2}")
print(f"    {{kappa=2}} is the Cayley cubic x^2+y^2+z^2-xyz-4=0, and those points are")
print(f"    its NODES. So erasure lands on the classical floor, but the floor itself is")
print(f"    NOT degenerate -- only its singular points are.")
raise SystemExit(0 if (gen_ok and comp_ok) else 1)
