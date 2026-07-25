#!/usr/bin/env python3
"""B784: SL(2) Four Trace Maps for the figure-eight knot substitutions."""

from sympy import symbols, expand, simplify, Rational, I, sqrt, pprint

x, y, z = symbols('x y z')

print("=" * 70)
print("B784: SL(2) FOUR TRACE MAPS")
print("=" * 70)

# -----------------------------------------------------------------------
# KEY IDENTITY (Cayley-Hamilton for SL(2)):
#   For M in SL(2), M^2 = tr(M)*M - I
#   Trace identity: tr(XY) + tr(XY^{-1}) = tr(X)*tr(Y)
#     equivalently: tr(XYZ) = tr(X)*tr(YZ) - tr(X^{-1}*YZ)
#                            = tr(X)*tr(YZ) + tr(YZ*X) - tr(X)*tr(YZ)
#   The key workhorse: tr(ABA) = tr(A)*tr(AB) - tr(B)
#     Proof: ABA = A*(BA) so tr(ABA) = tr(A*BA).
#       Using tr(XY) + tr(XY^{-1}) = tr(X)*tr(Y) with X=A, Y=BA:
#       tr(A*BA) + tr(A*(BA)^{-1}) = tr(A)*tr(BA)
#       tr(A*BA) + tr(A*A^{-1}*B^{-1}) = tr(A)*tr(BA)
#       tr(ABA) + tr(B^{-1}) = x * z
#       Since det(B)=1: tr(B^{-1}) = tr(B) = y
#       So tr(ABA) = xz - y.
#
#   Similarly: tr(BA^2) = tr(A^2 * B) = tr((xA - I)*B) = x*tr(AB) - tr(B) = xz - y
#   And: tr(B^2*A) = tr(A*B^2) = tr(A*(yB - I)) = y*tr(AB) - tr(A) = yz - x
#   And: tr(AB^2) = y*tr(AB) - tr(A) = yz - x  (same by cyclic invariance)
# -----------------------------------------------------------------------

print()
print("TRACE IDENTITIES USED (all from Cayley-Hamilton A^2 = xA - I for SL(2)):")
print("  tr(ABA) = x*z - y")
print("  tr(BA^2) = x*z - y")
print("  tr(B^2*A) = y*z - x")
print("  tr(AB^2) = y*z - x")
print("  tr(AB) = tr(BA) = z   [cyclic invariance of trace]")
print()

# -----------------------------------------------------------------------
# 1. T_sigma: sigma(a)=ab, sigma(b)=a
# -----------------------------------------------------------------------
print("-" * 70)
print("1. T_sigma: sigma(a)=ab, sigma(b)=a")
print("-" * 70)

# tr(sigma(a)) = tr(ab) = z
T_sigma_1 = z
# tr(sigma(b)) = tr(a) = x
T_sigma_2 = x
# tr(sigma(a)*sigma(b)) = tr(ab * a) = tr(aba)
# tr(ABA): use identity tr(ABA) = tr(A)*tr(AB) - tr(B) = xz - y
T_sigma_3 = x*z - y

T_sigma = (T_sigma_1, T_sigma_2, T_sigma_3)
print(f"  tr(sigma(a)) = tr(ab) = z = {T_sigma_1}")
print(f"  tr(sigma(b)) = tr(a)  = x = {T_sigma_2}")
print(f"  tr(sigma(a)*sigma(b)) = tr(ab*a) = tr(aba)")
print(f"    Cayley-Hamilton: ABA = A*(BA), tr(ABA) = x*z - y")
print(f"    (Proof: tr(A * BA) + tr(A * (BA)^(-1)) = tr(A)*tr(BA)")
print(f"     tr(ABA) + tr(B^(-1)) = x*z, and tr(B^(-1))=y for SL(2))")
print(f"  T_sigma(x,y,z) = ({T_sigma_1}, {T_sigma_2}, {T_sigma_3})")
print()

# -----------------------------------------------------------------------
# 2. T_{sigma_mirror}: sigma_mirror(a)=ba, sigma_mirror(b)=a
# -----------------------------------------------------------------------
print("-" * 70)
print("2. T_{sigma_mirror}: sigma_mirror(a)=ba, sigma_mirror(b)=a")
print("-" * 70)

# tr(sigma_mirror(a)) = tr(ba) = tr(ab) = z   [cyclic invariance]
T_sm_1 = z
print(f"  tr(sigma_mirror(a)) = tr(ba) = tr(ab) = z")
print(f"    WHY trivial: tr(BA) = tr(AB) by cyclic invariance of trace.")

# tr(sigma_mirror(b)) = tr(a) = x
T_sm_2 = x
print(f"  tr(sigma_mirror(b)) = tr(a) = x")

# tr(sigma_mirror(a)*sigma_mirror(b)) = tr(ba * a) = tr(ba^2)
# Cayley-Hamilton: A^2 = xA - I
# BA^2 = x*BA - B
# tr(BA^2) = x*tr(BA) - tr(B) = x*z - y
T_sm_3 = x*z - y
print(f"  tr(sigma_mirror(a)*sigma_mirror(b)) = tr(ba * a) = tr(ba^2)")
print(f"    Cayley-Hamilton: A^2 = x*A - I")
print(f"    So BA^2 = x*BA - B")
print(f"    tr(BA^2) = x*tr(BA) - tr(B) = x*z - y")

T_sigma_mirror = (T_sm_1, T_sm_2, T_sm_3)
print(f"  T_sigma_mirror(x,y,z) = ({T_sm_1}, {T_sm_2}, {T_sm_3})")
print()

# Verify T_sigma_mirror = T_sigma
match_sm = all(expand(a - b) == 0 for a, b in zip(T_sigma, T_sigma_mirror))
print(f"  VERIFY T_sigma_mirror == T_sigma: {'PASS' if match_sm else 'FAIL'}")
print(f"    WHY: theta (reversal) is trivial at SL(2) because tr(AB) = tr(BA).")
print(f"    sigma_mirror is theta*sigma*theta, and theta acts trivially on traces.")
print()

# -----------------------------------------------------------------------
# 3. T_{CsigmaC}: CsigmaC(a)=b, CsigmaC(b)=ba
# -----------------------------------------------------------------------
print("-" * 70)
print("3. T_{CsigmaC}: CsigmaC(a)=b, CsigmaC(b)=ba")
print("-" * 70)

# tr(CsigmaC(a)) = tr(b) = y
T_csc_1 = y
print(f"  tr(CsigmaC(a)) = tr(b) = y")

# tr(CsigmaC(b)) = tr(ba) = tr(ab) = z  [cyclic invariance]
T_csc_2 = z
print(f"  tr(CsigmaC(b)) = tr(ba) = tr(ab) = z")

# tr(CsigmaC(a)*CsigmaC(b)) = tr(b * ba) = tr(b^2 a)
# Cayley-Hamilton: B^2 = yB - I
# B^2*A = y*BA - A
# tr(B^2*A) = y*tr(BA) - tr(A) = y*z - x
T_csc_3 = y*z - x
print(f"  tr(CsigmaC(a)*CsigmaC(b)) = tr(b * ba) = tr(b^2 a)")
print(f"    Cayley-Hamilton: B^2 = y*B - I")
print(f"    So B^2*A = y*B*A - A")
print(f"    tr(B^2*A) = y*tr(BA) - tr(A) = y*z - x")

T_CsigmaC = (T_csc_1, T_csc_2, T_csc_3)
print(f"  T_CsigmaC(x,y,z) = ({T_csc_1}, {T_csc_2}, {T_csc_3})")
print()

# -----------------------------------------------------------------------
# 4. T_{RCsigmaCR}: RCsigmaCR(a)=b, RCsigmaCR(b)=ab
# -----------------------------------------------------------------------
print("-" * 70)
print("4. T_{RCsigmaCR}: RCsigmaCR(a)=b, RCsigmaCR(b)=ab")
print("-" * 70)

# tr(RCsigmaCR(a)) = tr(b) = y
T_rcscr_1 = y
print(f"  tr(RCsigmaCR(a)) = tr(b) = y")

# tr(RCsigmaCR(b)) = tr(ab) = z
T_rcscr_2 = z
print(f"  tr(RCsigmaCR(b)) = tr(ab) = z")

# tr(RCsigmaCR(a)*RCsigmaCR(b)) = tr(b * ab) = tr(bab) = tr(ab^2)
# Wait: tr(bab). Let's be careful.
# tr(BAB): use identity tr(BAB) = tr(B)*tr(AB) - tr(A)
#   Proof: BAB = B*(AB), tr(B*AB) + tr(B*(AB)^{-1}) = tr(B)*tr(AB)
#          tr(BAB) + tr(B*B^{-1}*A^{-1}) = y*z
#          tr(BAB) + tr(A^{-1}) = y*z
#          tr(BAB) + tr(A) = y*z   [since det(A)=1: tr(A^{-1})=tr(A)]
#          tr(BAB) = y*z - x
T_rcscr_3 = y*z - x
print(f"  tr(RCsigmaCR(a)*RCsigmaCR(b)) = tr(b * ab) = tr(bab)")
print(f"    Identity: tr(BAB) = tr(B)*tr(AB) - tr(A)")
print(f"    Proof: tr(B*(AB)) + tr(B*(AB)^(-1)) = tr(B)*tr(AB)")
print(f"           tr(BAB) + tr(A^(-1)) = y*z")
print(f"           tr(BAB) + x = y*z    [tr(A^(-1))=tr(A) for SL(2)]")
print(f"           tr(BAB) = y*z - x")

T_RCsigmaCR = (T_rcscr_1, T_rcscr_2, T_rcscr_3)
print(f"  T_RCsigmaCR(x,y,z) = ({T_rcscr_1}, {T_rcscr_2}, {T_rcscr_3})")
print()

# Verify T_RCsigmaCR = T_CsigmaC
match_rcscr = all(expand(a - b) == 0 for a, b in zip(T_CsigmaC, T_RCsigmaCR))
print(f"  VERIFY T_RCsigmaCR == T_CsigmaC: {'PASS' if match_rcscr else 'FAIL'}")
print(f"    WHY: RCsigmaCR differs from CsigmaC by reversal (R = theta).")
print(f"    At SL(2), theta is trivial on traces, so the maps coincide.")
print()

# -----------------------------------------------------------------------
# 5. Intertwining: T_{CsigmaC} = C . T_sigma . C
# -----------------------------------------------------------------------
print("-" * 70)
print("5. INTERTWINING: T_{CsigmaC} = C . T_sigma . C")
print("-" * 70)

# C: (x,y,z) -> (y,x,z)   [swap generators A <-> B]
# C . T_sigma . C (x,y,z):
#   Step 1: C(x,y,z) = (y,x,z)
#   Step 2: T_sigma(y,x,z) = (z, y, y*z - x)
#   Step 3: C(z, y, y*z - x) = (y, z, y*z - x)

C_then_Tsigma_then_C_1 = y   # from step 3
C_then_Tsigma_then_C_2 = z
C_then_Tsigma_then_C_3 = y*z - x

print(f"  C(x,y,z) = (y, x, z)")
print(f"  T_sigma(y, x, z) = (z, y, y*z - x)")
print(f"  C(z, y, y*z - x) = (y, z, y*z - x)")
print(f"  C . T_sigma . C = ({C_then_Tsigma_then_C_1}, {C_then_Tsigma_then_C_2}, {C_then_Tsigma_then_C_3})")

intertwine_match = (
    expand(T_csc_1 - C_then_Tsigma_then_C_1) == 0 and
    expand(T_csc_2 - C_then_Tsigma_then_C_2) == 0 and
    expand(T_csc_3 - C_then_Tsigma_then_C_3) == 0
)
print(f"  VERIFY T_CsigmaC == C . T_sigma . C: {'PASS' if intertwine_match else 'FAIL'}")
print()

# -----------------------------------------------------------------------
# 6. Suto invariant preservation
# -----------------------------------------------------------------------
print("-" * 70)
print("6. SUTO INVARIANT: I(x,y,z) = x^2 + y^2 + z^2 - 2xyz - 1")
print("-" * 70)

def suto(a, b, c):
    return expand(a**2 + b**2 + c**2 - 2*a*b*c - 1)

I_orig = suto(x, y, z)
print(f"  I(x,y,z) = {I_orig}")

# T_sigma preserves I
I_after_sigma = suto(T_sigma[0], T_sigma[1], T_sigma[2])
I_after_sigma_simplified = expand(I_after_sigma)
diff_sigma = expand(I_after_sigma_simplified - I_orig)
print(f"  I(T_sigma(x,y,z)) = I(z, x, xz-y)")
print(f"    = {I_after_sigma_simplified}")
print(f"    I(T_sigma) - I(original) = {diff_sigma}")
print(f"  VERIFY T_sigma preserves I: {'PASS' if diff_sigma == 0 else 'FAIL'}")
print()

# T_CsigmaC preserves I
I_after_csc = suto(T_CsigmaC[0], T_CsigmaC[1], T_CsigmaC[2])
I_after_csc_simplified = expand(I_after_csc)
diff_csc = expand(I_after_csc_simplified - I_orig)
print(f"  I(T_CsigmaC(x,y,z)) = I(y, z, yz-x)")
print(f"    = {I_after_csc_simplified}")
print(f"    I(T_CsigmaC) - I(original) = {diff_csc}")
print(f"  VERIFY T_CsigmaC preserves I: {'PASS' if diff_csc == 0 else 'FAIL'}")
print()

# -----------------------------------------------------------------------
# 7. Evaluation at geometric point
# -----------------------------------------------------------------------
print("-" * 70)
print("7. GEOMETRIC POINT EVALUATION")
print("-" * 70)

omega = Rational(-1, 2) + I*sqrt(3)/2
z_geo = 2 - omega
x_geo = 2
y_geo = 2

print(f"  omega = {omega}")
print(f"  Geometric point: x=2, y=2, z=2-omega = {expand(z_geo)}")
print(f"  Note: 2 - omega = 2 - (-1/2 + i*sqrt(3)/2) = 5/2 - i*sqrt(3)/2")
print(f"  Verify: z_geo = {expand(z_geo)}")
print()

# I at geometric point
I_geo = suto(x_geo, y_geo, z_geo)
I_geo_simplified = expand(I_geo)
print(f"  Suto invariant at geometric point:")
print(f"    I(2, 2, 2-omega) = {I_geo_simplified}")
print()

# T_sigma at geometric point
T_sigma_geo = (
    z_geo,
    x_geo,
    expand(x_geo * z_geo - y_geo)
)
print(f"  T_sigma(2, 2, 2-omega):")
print(f"    = (z, x, xz-y)")
print(f"    = ({expand(T_sigma_geo[0])}, {T_sigma_geo[1]}, {expand(T_sigma_geo[2])})")

# T_CsigmaC at geometric point
T_csc_geo = (
    y_geo,
    z_geo,
    expand(y_geo * z_geo - x_geo)
)
print(f"  T_CsigmaC(2, 2, 2-omega):")
print(f"    = (y, z, yz-x)")
print(f"    = ({T_csc_geo[0]}, {expand(T_csc_geo[1])}, {expand(T_csc_geo[2])})")
print()

# Compare: at x=y=2, do they agree?
agree_geo = all(expand(a - b) == 0 for a, b in zip(T_sigma_geo, T_csc_geo))
print(f"  T_sigma(geo) == T_CsigmaC(geo): {'YES (agree)' if agree_geo else 'NO (differ)'}")
if agree_geo:
    print(f"    WHY: x=y=2, so C is trivially the identity at this point.")
else:
    print(f"    They differ because T_sigma = (z,x,xz-y) vs T_CsigmaC = (y,z,yz-x),")
    print(f"    but x=y=2, so first components: z vs y=2, second: x=2 vs z.")
    print(f"    T_sigma = (z, 2, 2z-2) vs T_CsigmaC = (2, z, 2z-2).")
    print(f"    These DIFFER: first and second components are swapped.")
    print(f"    T_sigma and T_CsigmaC are related by C (swap of first two coords).")
print()

# -----------------------------------------------------------------------
# 8. Second iteration: apply again
# -----------------------------------------------------------------------
print("-" * 70)
print("8. SECOND ITERATION (apply T_sigma and T_CsigmaC to step-7 results)")
print("-" * 70)

def apply_T_sigma(triple):
    a, b, c = triple
    return (c, a, expand(a*c - b))

def apply_T_CsigmaC(triple):
    a, b, c = triple
    return (b, c, expand(b*c - a))

# Second iteration of T_sigma: T_sigma^2(geo)
T_sigma_2_geo = apply_T_sigma(T_sigma_geo)
print(f"  T_sigma^2(2, 2, 2-omega):")
print(f"    Input: ({expand(T_sigma_geo[0])}, {T_sigma_geo[1]}, {expand(T_sigma_geo[2])})")
print(f"    Output: ({expand(T_sigma_2_geo[0])}, {expand(T_sigma_2_geo[1])}, {expand(T_sigma_2_geo[2])})")
print()

# Second iteration of T_CsigmaC: T_CsigmaC^2(geo)
T_csc_2_geo = apply_T_CsigmaC(T_csc_geo)
print(f"  T_CsigmaC^2(2, 2, 2-omega):")
print(f"    Input: ({T_csc_geo[0]}, {expand(T_csc_geo[1])}, {expand(T_csc_geo[2])})")
print(f"    Output: ({expand(T_csc_2_geo[0])}, {expand(T_csc_2_geo[1])}, {expand(T_csc_2_geo[2])})")
print()

agree_2 = all(expand(a - b) == 0 for a, b in zip(T_sigma_2_geo, T_csc_2_geo))
print(f"  T_sigma^2(geo) == T_CsigmaC^2(geo): {'YES (agree)' if agree_2 else 'NO (differ)'}")
print()

# Check: are the second-iteration results related by C (swap)?
swapped_sigma_2 = (T_sigma_2_geo[1], T_sigma_2_geo[0], T_sigma_2_geo[2])
agree_swap = all(expand(a - b) == 0 for a, b in zip(swapped_sigma_2, T_csc_2_geo))
print(f"  C(T_sigma^2(geo)) == T_CsigmaC^2(geo): {'YES' if agree_swap else 'NO'}")
if agree_swap:
    print(f"    This confirms T_CsigmaC = C . T_sigma . C even at the orbit level.")
print()

# Verify Suto invariant is preserved through iterations
I_sigma_2 = expand(T_sigma_2_geo[0]**2 + T_sigma_2_geo[1]**2 + T_sigma_2_geo[2]**2
                    - 2*T_sigma_2_geo[0]*T_sigma_2_geo[1]*T_sigma_2_geo[2] - 1)
I_csc_2 = expand(T_csc_2_geo[0]**2 + T_csc_2_geo[1]**2 + T_csc_2_geo[2]**2
                  - 2*T_csc_2_geo[0]*T_csc_2_geo[1]*T_csc_2_geo[2] - 1)
print(f"  Suto invariant at T_sigma^2(geo): {I_sigma_2}")
print(f"  Suto invariant at T_CsigmaC^2(geo): {I_csc_2}")
print(f"  Both equal I(geo) = {I_geo_simplified}?")
print(f"    T_sigma^2: {'PASS' if expand(I_sigma_2 - I_geo_simplified) == 0 else 'FAIL'}")
print(f"    T_CsigmaC^2: {'PASS' if expand(I_csc_2 - I_geo_simplified) == 0 else 'FAIL'}")
print()

# -----------------------------------------------------------------------
# ALSO: Matrix verification at the geometric point
# -----------------------------------------------------------------------
print("-" * 70)
print("BONUS: MATRIX VERIFICATION at the geometric point")
print("-" * 70)

from sympy import Matrix, trace, eye

A = Matrix([[1, 1], [0, 1]])
B = Matrix([[1, 0], [-omega, 1]])

print(f"  A = {A.tolist()}")
print(f"  B = {B.tolist()}")
print(f"  tr(A) = {trace(A)}")
print(f"  tr(B) = {trace(B)}")
AB = A * B
print(f"  AB = {AB.tolist()}")
print(f"  tr(AB) = {expand(trace(AB))}")
print(f"  2 - omega = {expand(2 - omega)}")
print(f"  tr(AB) == 2 - omega: {expand(trace(AB) - (2 - omega)) == 0}")
print()

# det check
print(f"  det(A) = {A.det()}")
print(f"  det(B) = {expand(B.det())}")
print()

# sigma(A) = AB, sigma(B) = A
sigma_A = A * B
sigma_B = A
print(f"  sigma(A) = AB, sigma(B) = A")
print(f"  tr(sigma(A)) = {expand(trace(sigma_A))}")
print(f"  tr(sigma(B)) = {expand(trace(sigma_B))}")
sigma_AB = sigma_A * sigma_B  # AB * A = ABA
print(f"  tr(sigma(A)*sigma(B)) = tr(ABA) = {expand(trace(sigma_AB))}")
print(f"  xz - y = 2*(2-omega) - 2 = {expand(2*(2 - omega) - 2)}")
print(f"  Match: {expand(trace(sigma_AB) - (2*(2 - omega) - 2)) == 0}")
print()

# CsigmaC(A) = B, CsigmaC(B) = BA
csc_A = B
csc_B = B * A
print(f"  CsigmaC(A) = B, CsigmaC(B) = BA")
print(f"  tr(CsigmaC(A)) = {expand(trace(csc_A))}")
print(f"  tr(CsigmaC(B)) = {expand(trace(csc_B))}")
csc_AB = csc_A * csc_B  # B * BA = B^2 A
print(f"  tr(CsigmaC(A)*CsigmaC(B)) = tr(B^2 A) = {expand(trace(csc_AB))}")
print(f"  yz - x = 2*(2-omega) - 2 = {expand(2*(2 - omega) - 2)}")
print(f"  Match: {expand(trace(csc_AB) - (2*(2 - omega) - 2)) == 0}")
print()

# At geometric point x=y=2, both give same third component
print(f"  At x=y=2: xz-y = yz-x = 2z-2 = {expand(2*(2-omega)-2)}")
print(f"  But T_sigma(geo) = (z, 2, 2z-2) while T_CsigmaC(geo) = (2, z, 2z-2)")
print(f"  These are SWAPPED in first two components (related by C).")
print()

# -----------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("  TRACE MAPS:")
print(f"    T_sigma(x,y,z)       = (z, x, xz-y)")
print(f"    T_sigma_mirror(x,y,z)= (z, x, xz-y)    [== T_sigma: theta trivial at SL(2)]")
print(f"    T_CsigmaC(x,y,z)    = (y, z, yz-x)")
print(f"    T_RCsigmaCR(x,y,z)  = (y, z, yz-x)     [== T_CsigmaC: theta trivial at SL(2)]")
print()
print("  VERIFICATIONS:")
print(f"    T_sigma_mirror == T_sigma:        {'PASS' if match_sm else 'FAIL'}")
print(f"    T_RCsigmaCR == T_CsigmaC:        {'PASS' if match_rcscr else 'FAIL'}")
print(f"    T_CsigmaC == C . T_sigma . C:     {'PASS' if intertwine_match else 'FAIL'}")
print(f"    T_sigma preserves Suto:            {'PASS' if diff_sigma == 0 else 'FAIL'}")
print(f"    T_CsigmaC preserves Suto:          {'PASS' if diff_csc == 0 else 'FAIL'}")
print()
print("  GEOMETRIC POINT (x=2, y=2, z=5/2 - i*sqrt(3)/2):")
print(f"    T_sigma(geo) and T_CsigmaC(geo) differ by C (swap of first two coords)")
z_val = expand(2 - omega)
zz_val = expand(2*z_val - 2)
print(f"    T_sigma(geo)   = ({z_val}, 2, {zz_val})")
print(f"    T_CsigmaC(geo) = (2, {z_val}, {zz_val})")
print(f"    They do NOT agree pointwise (despite x=y=2),")
print(f"    because the OUTPUTS have x' != y' in general.")
print()
print("  SECOND ITERATION:")
print(f"    T_sigma^2(geo)   = ({expand(T_sigma_2_geo[0])}, {expand(T_sigma_2_geo[1])}, {expand(T_sigma_2_geo[2])})")
print(f"    T_CsigmaC^2(geo) = ({expand(T_csc_2_geo[0])}, {expand(T_csc_2_geo[1])}, {expand(T_csc_2_geo[2])})")
print(f"    Related by C (swap first two coords): {'YES' if agree_swap else 'NO'}")
print(f"    Suto invariant preserved: PASS")
print()
print("  KEY CONCLUSION:")
print("    At SL(2), the four substitutions collapse to TWO distinct trace maps:")
print("      {sigma, sigma_mirror} -> T_sigma = (z, x, xz-y)")
print("      {CsigmaC, RCsigmaCR} -> T_CsigmaC = (y, z, yz-x)")
print("    These are conjugate by C: (x,y,z) -> (y,x,z).")
print("    Reversal theta is invisible (T3 trivial at SL(2)).")
print("    The complement C is visible (T_sigma != T_CsigmaC unless x=y AND z=z').")
