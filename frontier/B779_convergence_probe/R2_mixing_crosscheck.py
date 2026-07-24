"""R2: mixing number cross-check against Reidemeister torsion.

Verify that the mixing number 1/(phi*sqrt(5)) from B753 is structurally
consistent with the torsion data (-3, -5) from B425.
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
sqrt5 = sp.sqrt(5)

# ============================================================
# The mixing number (B753)
# ============================================================
p = 1 / (phi * sqrt5)
# Galois conjugate sigma: sqrt(5) -> -sqrt(5)
p_conj = sp.simplify(p.subs(sqrt5, -sqrt5))

print("=" * 72)
print("R2: MIXING NUMBER CROSS-CHECK")
print("=" * 72)
print(f"\np = 1/(phi*sqrt(5)) = {sp.simplify(p)} = {float(p):.10f}")
print(f"sigma(p) = 1/(phi_bar*sqrt(5)) = {sp.simplify(p_conj)} = {float(p_conj):.10f}")

# ============================================================
# Identity 1: sigma(p) = 1 - p (doubly stochastic)
# ============================================================
id1 = sp.simplify(p_conj - (1 - p))
print(f"\n--- Identity 1: sigma(p) = 1 - p ---")
print(f"sigma(p) - (1-p) = {id1}")
assert id1 == 0, "FAILED: sigma(p) != 1-p"
print("CONFIRMED: mixing matrix is doubly stochastic by Galois symmetry")

# ============================================================
# Identity 2: p * sigma(p) = 1/5 = 1/|tau_dyn|
# ============================================================
norm_p = sp.simplify(p * p_conj)
print(f"\n--- Identity 2: N(p) = p * sigma(p) = 1/|tau_dyn| ---")
print(f"p * sigma(p) = {norm_p}")
assert norm_p == sp.Rational(1, 5), "FAILED: norm != 1/5"

tau_dyn = -5  # dynamical torsion from B425
print(f"|tau_dyn| = {abs(tau_dyn)}")
print(f"1/|tau_dyn| = {sp.Rational(1, abs(tau_dyn))}")
assert norm_p == sp.Rational(1, abs(tau_dyn))
print("CONFIRMED: Galois norm of mixing number = 1/|dynamical torsion|")

# ============================================================
# Identity 3: |tau_geo| = phi^2 + phi^(-2) = tr(RL)
# ============================================================
tau_geo = -3  # geometric torsion from B425
monodromy_trace = phi**2 + phi**(-2)
monodromy_trace_simplified = sp.simplify(monodromy_trace)
print(f"\n--- Identity 3: |tau_geo| = phi^2 + phi^(-2) = tr(RL) ---")
print(f"phi^2 + phi^(-2) = {monodromy_trace_simplified}")
assert monodromy_trace_simplified == abs(tau_geo)
print(f"|tau_geo| = {abs(tau_geo)}")
print("CONFIRMED: geometric torsion = monodromy trace = golden identity")

# ============================================================
# Identity 4: |tau_geo| * |tau_dyn| = |disc(Q(sqrt(-15)))|
# ============================================================
product = abs(tau_geo) * abs(tau_dyn)
disc_meeting = abs(-15)  # disc(Q(sqrt(-15))) = -15 (fund disc = -15)
# Actually disc(Q(sqrt(-15))) = -60 (since -15 = (-1)*3*5, -15 ≡ 1 mod 4, so disc = 4*(-15) = -60)
# Wait: -15 ≡ 1 mod 4, so disc = -15. No: d = -15, d ≡ 1 mod 4, disc = d = -15.
# Actually -15 mod 4 = 1 (since -15 = -4*4 + 1), so disc = -15. |disc| = 15.
print(f"\n--- Identity 4: |tau_geo| * |tau_dyn| = |disc(Q(sqrt(-15)))| ---")
print(f"|tau_geo| * |tau_dyn| = {abs(tau_geo)} * {abs(tau_dyn)} = {product}")
print(f"|disc(Q(sqrt(-15)))| = {disc_meeting}")
assert product == disc_meeting
print("CONFIRMED: torsion product = meeting-face discriminant")
print("The three V4 quadratic subfields:")
print(f"  Q(sqrt(-3)):  disc = -3  = tau_geo")
print(f"  Q(sqrt(5)):   disc = 5   = |tau_dyn|")
print(f"  Q(sqrt(-15)): disc = -15 = tau_geo * tau_dyn")

# ============================================================
# Identity 5: p = 1/(phi^2 + 1) (connecting mixing to monodromy)
# ============================================================
print(f"\n--- Identity 5: p = 1/(phi^2 + 1) ---")
alt_p = 1 / (phi**2 + 1)
id5 = sp.simplify(p - alt_p)
print(f"1/(phi^2 + 1) = {sp.simplify(alt_p)}")
assert id5 == 0
print("CONFIRMED: phi*sqrt(5) = phi^2 + 1")
print(f"Therefore: p = 1/(phi^2 + 1) = 1/(|tau_geo| - phi^(-2) + 1)")
print(f"  = 1/(3 - {sp.simplify(phi**(-2))} + 1)")
print(f"  = 1/({sp.simplify(3 - phi**(-2) + 1)})")

# ============================================================
# Identity 6: the mixing entry squared sum
# ============================================================
print(f"\n--- Identity 6: p^2 + (1-p)^2 ---")
sum_sq = sp.simplify(p**2 + (1 - p)**2)
print(f"p^2 + (1-p)^2 = {sum_sq} = {float(sum_sq):.10f}")
print(f"|tau_geo| / |tau_dyn| = 3/5 = {3/5}")
assert sum_sq == sp.Rational(3, 5)
print("CONFIRMED: sum of squared mixing entries = |tau_geo|/|tau_dyn| = 3/5")
print("This ratio IS the two-column law: Eisenstein/golden = geometric/dynamical")

# ============================================================
# Summary
# ============================================================
print(f"\n{'=' * 72}")
print("SUMMARY: ALL 6 IDENTITIES CONFIRMED")
print("=" * 72)
print("""
The mixing number 1/(phi*sqrt(5)) from B753 (quantum topology)
and the torsion data (-3, -5) from B425 (classical topology)
are connected by six golden identities:

  1. sigma(p) = 1 - p              [doubly stochastic = Galois symmetry]
  2. p * sigma(p) = 1/|tau_dyn|    [Galois norm = 1/dynamical torsion]
  3. |tau_geo| = phi^2 + phi^(-2)  [geometric torsion = monodromy trace]
  4. |tau_geo| * |tau_dyn| = 15    [torsion product = meeting discriminant]
  5. p = 1/(phi^2 + 1)             [mixing = reciprocal of shifted trace]
  6. p^2 + (1-p)^2 = 3/5           [squared sum = torsion ratio]

Identity 6 is the cross-check's strongest result:
the sum of squared Born weights equals the ratio of geometric
to dynamical torsion. This is the two-column law (Eisenstein/golden)
appearing inside the mixing matrix itself.
""")
