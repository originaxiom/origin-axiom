#!/usr/bin/env python3
"""P-SEAM-02 / G1 + controls.  Nothing hardcoded: every verdict is computed."""
import sympy as sp

R = {}   # results registry -> verdict computed at the end

x, y, z = sp.symbols('x y z')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2          # B293's Casimir, as written in B293

# ---------------------------------------------------------------- G1 / C-collision
# Is B293's kappa literally tr[a,b] on the F2 character variety (B497's object)?
a1,a2,a3,b1,b2,b3 = sp.symbols('a1 a2 a3 b1 b2 b3')
a4 = (1 + a2*a3)/a1        # det a = 1
b4 = (1 + b2*b3)/b1        # det b = 1
A  = sp.Matrix([[a1,a2],[a3,a4]])
B  = sp.Matrix([[b1,b2],[b3,b4]])
Ai = sp.Matrix([[a4,-a2],[-a3,a1]])   # SL2 inverse
Bi = sp.Matrix([[b4,-b2],[-b3,b1]])

tr_comm = sp.simplify(sp.trace(A*B*Ai*Bi))       # tr[a,b], computed from matrices
X, Y, Z = sp.trace(A), sp.trace(B), sp.trace(A*B)
fricke  = X**2 + Y**2 + Z**2 - X*Y*Z - 2          # the claimed polynomial, same coords
G1_resid = sp.simplify(sp.together(tr_comm - fricke))
R['G1_identity'] = (G1_resid == 0)

# C-collision: are B497's coordinates the same (x,y,z)?  Its stratum-1 citizen is
# a -> ab, b -> a, whose induced trace map B497 records as T_gold = (z, x, x*z - y).
# Derive it independently from trace identities and compare.
Xp, Yp, Zp = sp.trace(A*B), sp.trace(A), sp.trace(A*B*A)
derived = [sp.simplify(sp.together(Xp - Z)),
           sp.simplify(sp.together(Yp - X)),
           sp.simplify(sp.together(Zp - (X*Z - Y)))]
R['C_collision_same_coords'] = all(d == 0 for d in derived)

# ---------------------------------------------------------------- C-alive
# Goldman bracket on X(F2).  Verify kappa is Poisson-central: {kappa, .} = 0.
def goldman(f, g):
    bxy = 2*z - x*y; byz = 2*x - y*z; bzx = 2*y - x*z
    fx,fy,fz = [sp.diff(f,v) for v in (x,y,z)]
    gx,gy,gz = [sp.diff(g,v) for v in (x,y,z)]
    return sp.expand((fx*gy-fy*gx)*bxy + (fy*gz-fz*gy)*byz + (fz*gx-fx*gz)*bzx)

cas = [sp.simplify(goldman(KAPPA, v)) for v in (x, y, z)]
R['C_alive_kappa_is_casimir'] = all(c == 0 for c in cas)

# ---------------------------------------------------------------- C-null
# A comparable cubic that is NOT the Casimir must NOT be central.
decoy = x**2*y + z**3 - 3*x*z
dec = [sp.simplify(goldman(decoy, v)) for v in (x, y, z)]
R['C_null_decoy_is_central'] = all(d == 0 for d in dec)   # must be FALSE

# ---------------------------------------------------------------- instrument alive:
# re-derive B497's four kappa-laws instead of trusting the table.
def kap(t):
    return sp.expand(KAPPA.subs({x: t[0], y: t[1], z: t[2]}, simultaneous=True))
S1 = (z, x, x*z - y)                                   # det +-1  (metallic/gold)
S2 = (x**2-2, y**2-2, x*y*z - x**2 - y**2 + 2)         # |det|>=2 (doubling)
S3 = (z, z, x*y*z - x**2 - y**2 + 2)                   # det 0    (Thue-Morse)
laws = {
 'S1  kappa\' = kappa'              : sp.simplify(kap(S1) - KAPPA),
 'S2  kappa\'-2 = (kappa-2)x^2y^2'  : sp.simplify(kap(S2) - 2 - (KAPPA-2)*x**2*y**2),
 'S3  kappa\'-2 = (kappa-2)(x^2+y^2-xyz)': sp.simplify(kap(S3) - 2 - (KAPPA-2)*(x**2+y**2-x*y*z)),
}
R['B497_kappa_laws_rederived'] = all(v == 0 for v in laws.values())
# stratum 4: a->ab, b->ab  (rank 1) : image must lie in {kappa=2}
# a->ab, b->ab : x'=y'=tr(ab)=z ; z'=tr((ab)^2)=z^2-2  (all in the SYMBOL z)
S4 = (z, z, z**2 - 2)
s4k = sp.simplify(kap(S4) - 2)
R['S4_image_in_kappa_eq_2'] = (s4k == 0)

# ---------------------------------------------------------------- report
print("="*70)
print("P-SEAM-02  ---  G1 and controls")
print("="*70)
for k in ['G1_identity','C_collision_same_coords','C_alive_kappa_is_casimir',
          'C_null_decoy_is_central','B497_kappa_laws_rederived','S4_image_in_kappa_eq_2']:
    print(f"  {k:34s} = {R[k]}")
print()
for k,v in laws.items():
    print(f"    {k:42s} residual = {v}")
print()
print("  tr[a,b] - (x^2+y^2+z^2-xyz-2)  residual =", G1_resid)
print("  {kappa,x},{kappa,y},{kappa,z}         =", cas)
print("  decoy brackets (must NOT be all 0)    =", dec)
print()

# certificate: computed, never hardcoded
c_alive   = R['C_alive_kappa_is_casimir']
c_null_ok = (R['C_null_decoy_is_central'] is False)
g1        = R['G1_identity'] and R['C_collision_same_coords']
instr     = R['B497_kappa_laws_rederived'] and R['S4_image_in_kappa_eq_2']
ok = c_alive and c_null_ok and instr
print("-"*70)
print(f"  controls: C-alive={c_alive}  C-null-correctly-fails={c_null_ok}  instrument={instr}")
if not ok:
    print("  VERDICT: VOID -- instrument or controls failed; G1 result is not admissible.")
    raise SystemExit(1)
print(f"  G1 VERDICT: {'TRUE  (same polynomial, same coordinates)' if g1 else 'FALSE (name collision)'}")
print("  Scope: G1 only. G2 (Poisson action of stratum 1) and G3 (degeneracy of")
print("  {kappa=2}) are NOT tested here and remain open per the sealed prereg.")
raise SystemExit(0 if g1 else 1)
