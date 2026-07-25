"""B780 coordinate audit — resolve the theta/iota mislabeling.

B780 attributes the permutation (1 4)(2 5)(3 8)(6 7) on the 8 Lawton
SL(3) trace coordinates to "theta at SL(3)". This audit proves the
permutation is INVERSION (iota: w -> w^-1), not REVERSAL (theta: w -> w^R).

The 8 Lawton coordinates (B71/B48):
    x = (tr A, tr B, tr AB, tr A^-1, tr B^-1, tr A^-1 B, tr A B^-1, tr A^-1 B^-1)

Reversal theta: w -> w^R (reverse letter order, keep generators).
    theta(A) = A, theta(B) = B, theta(AB) = BA, theta(A^-1 B) = B A^-1, etc.
    On traces: tr(XY) = tr(YX) by cyclicity -> theta = IDENTITY on all 8.

Inversion iota: w -> w^-1 (invert the group element).
    iota(A) = A^-1, iota(B) = B^-1, iota(AB) = B^-1 A^-1, etc.
    On SL(2) traces: tr(M) = tr(M^-1) -> iota trivial.
    On SL(3) traces: tr(M) != tr(M^-1) -> iota = (1 4)(2 5)(3 8)(6 7).

Gate 5-Q.
"""
import numpy as np
import sympy as sp

np.random.seed(42)
results = {}

print("=" * 80)
print("B780 COORDINATE AUDIT: theta vs iota on the 8 Lawton SL(3) traces")
print("=" * 80)


def random_sl3():
    M = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
    M /= np.linalg.det(M) ** (1.0 / 3.0)
    return M


def lawton_coords(A, B):
    Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
    return np.array([
        np.trace(A), np.trace(B), np.trace(A @ B),
        np.trace(Ai), np.trace(Bi), np.trace(Ai @ B),
        np.trace(A @ Bi), np.trace(Ai @ Bi),
    ])


A3 = random_sl3()
B3 = random_sl3()
x = lawton_coords(A3, B3)

# --- theta (reversal) ---
# theta(w) reverses letter order: AB -> BA, A^-1 B -> B A^-1, etc.
# On traces: tr(XY) = tr(YX), so theta = identity.
A3i, B3i = np.linalg.inv(A3), np.linalg.inv(B3)
x_theta = np.array([
    np.trace(A3),          # A -> A
    np.trace(B3),          # B -> B
    np.trace(B3 @ A3),     # AB -> BA
    np.trace(A3i),         # A^-1 -> A^-1
    np.trace(B3i),         # B^-1 -> B^-1
    np.trace(B3 @ A3i),    # A^-1 B -> B A^-1
    np.trace(B3i @ A3),    # A B^-1 -> B^-1 A
    np.trace(B3i @ A3i),   # A^-1 B^-1 -> B^-1 A^-1
])

theta_diffs = np.abs(x - x_theta)
theta_is_id = np.all(theta_diffs < 1e-10)
print(f"\ntheta (reversal) = identity on all 8 coords? {theta_is_id}")
print(f"  max |x - x_theta| = {np.max(theta_diffs):.2e}")

# --- iota (inversion) ---
# iota(w) = w^-1: A -> A^-1, AB -> (AB)^-1 = B^-1 A^-1, etc.
x_iota = np.array([
    np.trace(A3i),         # A -> A^-1   = x4
    np.trace(B3i),         # B -> B^-1   = x5
    np.trace(B3i @ A3i),   # AB -> B^-1 A^-1 = x8  (by cyclicity: tr(B^-1 A^-1) = tr(A^-1 B^-1))
    np.trace(A3),          # A^-1 -> A   = x1
    np.trace(B3),          # B^-1 -> B   = x2
    np.trace(B3i @ A3),    # A^-1 B -> B^-1 A = x7  (by cyclicity: tr(B^-1 A) = tr(A B^-1))
    np.trace(B3 @ A3i),    # A B^-1 -> B A^-1 = x6  (by cyclicity: tr(B A^-1) = tr(A^-1 B))
    np.trace(B3 @ A3),     # A^-1 B^-1 -> BA = x3   (by cyclicity: tr(BA) = tr(AB))
])

perm = {0: 3, 3: 0, 1: 4, 4: 1, 2: 7, 7: 2, 5: 6, 6: 5}
iota_diffs = np.array([abs(x_iota[i] - x[perm[i]]) for i in range(8)])
iota_matches = np.all(iota_diffs < 1e-10)
print(f"\niota (inversion) = permutation (1 4)(2 5)(3 8)(6 7)? {iota_matches}")
print(f"  max |x_iota[i] - x[perm[i]]| = {np.max(iota_diffs):.2e}")

# --- V0 check: on Sym^2 locus, iota is also trivial ---
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
A2 = sp.Matrix([[1, 1], [0, 1]])
B2 = sp.Matrix([[1, 0], [-omega, 1]])


def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([
        [a**2, 2 * a * b, b**2],
        [a * c, a * d + b * c, b * d],
        [c**2, 2 * c * d, d**2],
    ])


print("\n" + "=" * 80)
print("V0 (Sym^2) CHECK: iota on Sym^2 traces at the geometric point")
print("=" * 80)

pairs = [
    ("A", A2, A2.inv()),
    ("B", B2, B2.inv()),
    ("AB", A2 * B2, (A2 * B2).inv()),
    ("A^-1 B", A2.inv() * B2, (A2.inv() * B2).inv()),
]
all_collapse = True
for name, M, Mi in pairs:
    t_direct = sp.simplify(sym2(M).trace())
    t_inverse = sp.simplify(sym2(Mi).trace())
    eq = sp.simplify(t_direct - t_inverse) == 0
    if not eq:
        all_collapse = False
    print(f"  tr(Sym^2({name})) = {t_direct},  tr(Sym^2({name}^-1)) = {t_inverse},  equal = {eq}")

print(f"\niota trivial on V0 (Sym^2)? {all_collapse}")

# --- final verdict ---
print("\n" + "=" * 80)
print("VERDICT")
print("=" * 80)
print()
if theta_is_id and iota_matches and all_collapse:
    print("B780 MISLABELS iota (inversion) as theta (reversal).")
    print()
    print("  theta (word reversal): IDENTITY on all 8 Lawton coords, ALL ranks.")
    print("  iota (inversion):      permutation (1 4)(2 5)(3 8)(6 7) at SL(3),")
    print("                         trivial at SL(2), trivial on V0 (Sym^2 locus).")
    print()
    print("  The mislabeling arises because theta and iota coincide at SL(2)")
    print("  (tr(M) = tr(M^-1) and tr(XY) = tr(YX)). They separate at SL(3).")
    print()
    print("  The 'rank-onset at SL(3)' signature in B780 is REAL but belongs to")
    print("  iota, not theta. theta has NO rank-onset (trivial at all ranks on traces).")
    print("  theta's non-triviality is matrix-level (Sym^2(AB) != Sym^2(BA)), not trace-level.")
    verdict = "B780_MISLABEL_CONFIRMED"
else:
    verdict = "UNEXPECTED"
    print(f"UNEXPECTED RESULT: theta_id={theta_is_id}, iota_perm={iota_matches}, v0={all_collapse}")

results["theta_is_identity"] = bool(theta_is_id)
results["iota_matches_permutation"] = bool(iota_matches)
results["iota_trivial_on_V0"] = bool(all_collapse)
results["verdict"] = verdict
