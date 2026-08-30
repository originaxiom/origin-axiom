"""INDEPENDENT check of cloud memo 127 (the fence theorem's addendum 3): the mirror is irremovable
by a kappa-invariance identity -- and its convergence with MAIN's own B1203.

B1203 found the founding climb (a->ab, b->a) preserves kappa IDENTICALLY, and read that as: the
climb generates no new invariant, hence ONE bit and not a tower. Memo 127 uses the SAME invariance
to prove the mirror CANNOT be absorbed by any internal operation. Two directions of one identity.
"""
import sympy as sp

x, y, z = sp.symbols("x y z")
kappa = x**2 + y**2 + z**2 - x*y*z - 2

print("=== 1. the internal group preserves kappa IDENTICALLY (not merely at a point) ===")
ops = {
    "letter swap (a<->b)":        (y, x, z),
    "word reversal":              (x, y, x*y - z),      # tr(AB) -> tr(BA^-1)-type Fricke move
    "inversion":                  (x, y, x*y - z),
    "lift sign (a -> -a)":        (-x, y, -z),
    "lift sign (b -> -b)":        (x, -y, -z),
    "lift sign (both)":           (-x, -y, z),
    "Fricke T (tau_a)":           (x, z, x*z - y),      # B148's banked Dehn twist
    "Fricke T (tau_b)":           (z, y, y*z - x),
    "the founding climb (B1203)": (z, x, x*z - y),      # (X,Y) -> (XY,X) in Fricke coordinates
}
for name, (X, Y, Z) in ops.items():
    d = sp.expand(kappa.subs({x: X, y: Y, z: Z}, simultaneous=True) - kappa)
    print(f"    {name:28s} kappa o g - kappa = {d}")
    assert d == 0, name
print("    => every internal operation, INCLUDING B1203's climb, is a kappa-symmetry.")

print("\n=== 2. CONTROL: a map outside the group must MOVE kappa ===")
L = (x**2 - 2, y, z)      # a squaring-type 'bite' control, cf. B1203's (X,Y)->(X^2,Y)
dL = sp.expand(kappa.subs({x: L[0], y: L[1], z: L[2]}, simultaneous=True) - kappa)
print(f"    bite control (X -> X^2):  kappa o L - kappa = {sp.factor(dL)}")
assert dL != 0, "the identity must be able to FAIL, or invariance says nothing"

print("\n=== 3. kappa SEPARATES the object's point from its mirror ===")
w = sp.symbols("w")                      # omega, with w^2 = w - 1
def red(e):
    return sp.simplify(sp.rem(sp.expand(e), w**2 - w + 1, w))
P0 = (sp.Integer(2), sp.Integer(2), 2 - w)
Pg = (sp.Integer(2), sp.Integer(2), 2 - (1 - w))          # gal: omega -> conj(omega) = 1 - omega
k0 = red(kappa.subs({x: P0[0], y: P0[1], z: P0[2]}, simultaneous=True))
kg = red(kappa.subs({x: Pg[0], y: Pg[1], z: Pg[2]}, simultaneous=True))
print(f"    kappa(P0)      = {k0}     (memo: 1 + omega)")
print(f"    kappa(gal P0)  = {kg}     (memo: 2 - omega)")
assert sp.simplify(k0 - (1 + w)) == 0 and sp.simplify(kg - (2 - w)) == 0
assert sp.simplify(k0 - kg) != 0
print("    => DISTINCT. Since every internal operation preserves kappa, NO composition of them")
print("       carries gal(P0) back to P0: THE MIRROR IS IRREMOVABLE. Memo 127 CONFIRMED.")

print("\n=== 4. and the invariant CONTENT is unmoved: both root the same quadratic ===")
s, p = red(k0 + kg), red(sp.expand(k0 * kg))
print(f"    sum = {s}, product = {p}  ->  X^2 - {s}X + {p}")
assert sp.simplify(s - 3) == 0 and sp.simplify(p - 3) == 0
print("    => X^2 - 3X + 3, as the memo states: the VALUE moves, the CONTENT does not.")

print("\n=== 5. exactly 2 of the 8 elements of <letter swap, lift signs> fix P0 ===")
fix = 0
for sw in (False, True):
    for sa in (1, -1):
        for sb in (1, -1):
            X, Y, Z = (2, 2, 2 - w)
            if sw: X, Y = Y, X
            X2, Y2, Z2 = sa * X, sb * Y, sa * sb * Z
            if (sp.simplify(X2 - 2) == 0 and sp.simplify(Y2 - 2) == 0
                    and sp.simplify(Z2 - (2 - w)) == 0):
                fix += 1
print(f"    elements fixing P0: {fix} of 8   (memo: 2)")
assert fix == 2
print("    => at its own point (x = y = 2) the LETTER SWAP is the object's only internal duality.")

print("""
THE CONVERGENCE THIS BENCH ADDS
  B1203 (main, banked NEGATIVE): the founding climb preserves kappa identically, so climbing
    generates no new invariant -- ONE bit, not a tower of bits.
  Memo 127 (cloud): the internal group preserves kappa identically, and kappa separates P0 from
    gal(P0), so the mirror cannot be absorbed -- the bit is IRREMOVABLE.
  These are ONE identity read in two directions. The internal group cannot change kappa; the
  mirror does. So the mirror is precisely the operation the object cannot perform on itself --
  which is WHY the observer's bit is exactly one, and external. The negative and the
  irremovability proof share their mechanism.
VERIFIED""")
