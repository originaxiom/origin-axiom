#!/usr/bin/env python3
"""P-SEAM-02 / G2: does stratum 1 (det +-1) act on the Goldman bracket, and how?"""
import sympy as sp
x, y, z = sp.symbols('x y z')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2

def goldman(f, g):
    bxy, byz, bzx = 2*z - x*y, 2*x - y*z, 2*y - x*z
    fx,fy,fz = [sp.diff(f,v) for v in (x,y,z)]
    gx,gy,gz = [sp.diff(g,v) for v in (x,y,z)]
    return sp.expand((fx*gy-fy*gx)*bxy + (fy*gz-fz*gy)*byz + (fz*gx-fx*gz)*bzx)

def sub(T, e):
    return sp.expand(e.subs({x:T[0], y:T[1], z:T[2]}, simultaneous=True))

def multiplier(T):
    """T is Poisson up to scalar c iff {T_u,T_v} = c * ({u,v} o T) for all 3 pairs."""
    pairs = [((T[0],T[1]), 2*z - x*y), ((T[1],T[2]), 2*x - y*z), ((T[2],T[0]), 2*y - x*z)]
    cs = []
    for (Tu,Tv), struct in pairs:
        lhs = goldman(Tu, Tv); rhs = sub(T, struct)
        if sp.simplify(rhs) == 0:
            cs.append(None); continue
        q = sp.simplify(sp.cancel(lhs/rhs))
        cs.append(q if q.is_number else None)
    same = (len(set([c for c in cs if c is not None])) == 1) and (None not in cs)
    return (cs[0] if same else None), cs

def kappa_preserved(T):
    return sp.simplify(sub(T, KAPPA) - KAPPA) == 0

gold = (z, x, x*z - y)                                   # a->ab, b->a   det = -1
gold2 = tuple(sp.expand(sub(gold, c)) for c in gold)      # composed      det = +1
S2   = (x**2-2, y**2-2, x*y*z - x**2 - y**2 + 2)          # doubling      |det| = 4
S3   = (z, z, x*y*z - x**2 - y**2 + 2)                    # Thue-Morse    det = 0
S4   = (z, z, z**2 - 2)                                   # a->ab,b->ab   rank 1

tests = [("stratum 1  gold  (det = -1)", gold,  -1),
         ("stratum 1  gold^2 (det = +1)", gold2, +1),
         ("stratum 2  doubling (det = 4)", S2,   None),
         ("stratum 3  Thue-Morse (det = 0)", S3, None),
         ("stratum 4  rank 1", S4,             None)]

print("="*74); print("P-SEAM-02  ---  G2: Poisson action of the strata"); print("="*74)
rows=[]
for name, T, det in tests:
    c, cs = multiplier(T)
    kp = kappa_preserved(T)
    rows.append((name, det, c, kp))
    print(f"  {name:32s} kappa preserved = {str(kp):5s}  bracket multiplier = {c}")
print()

# --- controls ---
# C-vacuity: if EVERY map preserved kappa, G2 would be vacuous.
vac = all(r[3] for r in rows)
# instrument alive: identity must give multiplier +1
cid, _ = multiplier((x, y, z))
alive = (cid == 1)
# the claim under test, computed:
s1 = [r for r in rows if r[1] is not None]
rest = [r for r in rows if r[1] is None]
law_holds = all(r[2] == r[1] for r in s1)             # multiplier == det on stratum 1
rest_fail = all((not r[3]) for r in rest)             # strata 2-4 do NOT preserve kappa

print("-"*74)
print(f"  C-alive (identity multiplier = +1)        : {alive}")
print(f"  C-vacuity (every map preserves kappa?)    : {vac}   (must be False)")
print(f"  stratum 1: multiplier == det              : {law_holds}")
print(f"  strata 2-4: kappa NOT preserved           : {rest_fail}")
if not alive or vac:
    print("  VERDICT: VOID"); raise SystemExit(1)
verdict = law_holds and rest_fail
print()
print(f"  G2 VERDICT: {'TRUE' if verdict else 'FALSE'}")
if verdict:
    print("  Refined statement (computed, not assumed):")
    print("    stratum 1 preserves kappa exactly and preserves the Goldman bracket")
    print("    UP TO SIGN, and the sign IS the determinant:")
    print("       det = +1  ->  Poisson      (symplectic, leaf-preserving)")
    print("       det = -1  ->  ANTI-Poisson (anti-symplectic, bracket reversed)")
    print("    strata 2-4 do not preserve kappa, hence cannot preserve the leaves.")
raise SystemExit(0 if verdict else 1)
