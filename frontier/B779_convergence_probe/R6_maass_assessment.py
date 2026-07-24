"""R6': Discrete Maass newforms at level (8) — feasibility probe.

What we CAN compute:
  - Length spectrum from SnapPy (geodesic lengths)
  - Weyl asymptotic (expected eigenvalue density from volume)
  - Heat trace bound via the trace formula

What we CANNOT compute without specialist software:
  - Individual Maass eigenvalues
  - Hecke eigenvalues of specific newforms
"""
import sys
import math

try:
    import snappy
except ImportError:
    print("ERROR: snappy required")
    sys.exit(1)

print("=" * 72)
print("R6': DISCRETE MAASS NEWFORM FEASIBILITY PROBE")
print("=" * 72)

# ============================================================
# 1. Length spectrum of m004
# ============================================================
print("\n--- 1. LENGTH SPECTRUM ---")
M = snappy.Manifold("m004")
vol = float(M.volume())
print(f"Volume of m004: {vol:.10f}")

try:
    lengths = M.length_spectrum(cutoff=5.0)
    print(f"Geodesic lengths (cutoff=5.0): {len(lengths)} found")
    print(f"\n{'mult':>4} {'length':>12} {'Im(length)':>12}  topology")
    print("-" * 55)
    for i, g in enumerate(lengths[:20]):
        L = complex(g['length'])
        print(f"{g['multiplicity']:>4} {L.real:>12.8f} {L.imag:>12.8f}  {g.get('topology', '?')}")
except Exception as e:
    print(f"length_spectrum failed: {e}")
    print("Trying alternative approach...")
    lengths = []

# ============================================================
# 2. Weyl asymptotic
# ============================================================
print("\n--- 2. WEYL ASYMPTOTIC ---")
# For H^3 quotients, the Weyl law for eigenvalues lambda = 1 + r^2
# (where r is the spectral parameter) gives:
# N(R) ~ vol / (6 pi^2) * R^3
# where N(R) counts eigenvalues with |r| <= R
# lambda = 1 + r^2, so r = sqrt(lambda - 1) for lambda > 1

print(f"Volume = {vol:.6f}")
print(f"Weyl coefficient vol/(6*pi^2) = {vol / (6 * math.pi**2):.6f}")
print()

for R in [1, 2, 5, 10, 20]:
    N = vol / (6 * math.pi**2) * R**3
    lam = 1 + R**2
    print(f"  |r| <= {R:>2}: ~{N:>8.1f} eigenvalues (lambda <= {lam})")

# For the orbifold (vol = vol_m004 / 12):
vol_orb = vol / 12
print(f"\nOrbifold volume = {vol_orb:.6f}")
for R in [1, 2, 5, 10]:
    N = vol_orb / (6 * math.pi**2) * R**3
    print(f"  |r| <= {R:>2}: ~{N:>8.1f} orbifold eigenvalues")

# ============================================================
# 3. Spectral gap estimate
# ============================================================
print("\n--- 3. SPECTRAL GAP ---")
print("Selberg eigenvalue conjecture for congruence subgroups of")
print("Bianchi groups: lambda_1 >= 1 (r >= 0, no small eigenvalues).")
print()
print("m004 IS congruence at level (8) [B734].")
print("If Selberg's conjecture holds: lambda_1 >= 1.")
print()
print("The conjecture is PROVEN for:")
print("  - PSL(2,Z) (Selberg 1965, partial; Kim-Sarnak 2003: >= 975/4096)")
print("  - Some specific Bianchi groups with small class number")
print("  - NOT proven in full generality for PSL(2, O_3)")
print()
print("Best known general bound (Luo-Rudnick-Sarnak): lambda_1 >= 3/4")
print("for congruence subgroups of PSL(2, O_K) with K imaginary quadratic.")

# ============================================================
# 4. Newform dimension estimate
# ============================================================
print("\n--- 4. NEWFORM SPACE ---")
print("Index [PSL(2,O_3) : Gamma(m004)] = 12")
print("|PSL(2, O_3/(8))| = 30720 [from B734]")
print()
print("The space of level-(8) automorphic forms decomposes as:")
print("  S(8) = S_old(8) + S_new(8)")
print("  S_old = forms pulled back from lower levels (1), (2), (4)")
print("  S_new = genuinely new forms at level (8)")
print()
print("For weight-2 cohomological forms (Bianchi modular forms):")
print("  These are computable via modular symbols (Cremona/Sengun).")
print("  LMFDB may have tabulated data for Q(sqrt(-3)) at level (8).")
print()
print("For weight-0 Maass forms (the target):")
print("  These require Hejhal-class eigenvalue search.")
print("  No implementation exists in this repo.")
print("  External software: Then (2004), Avelin (2010), Stromberg (2008).")

# ============================================================
# 5. What the trace formula gives
# ============================================================
print("\n--- 5. TRACE FORMULA INFORMATION ---")
if lengths:
    # The shortest geodesic length gives a bound via the
    # Cheeger constant and Cheeger's inequality
    shortest = float(complex(lengths[0]['length']).real)
    print(f"Shortest geodesic length: {shortest:.8f}")

    # Cheeger constant h(M) >= 1/injrad for closed manifolds
    # For cusped manifolds, the situation is more delicate
    injrad = shortest / 2
    print(f"Injectivity radius (half shortest geodesic): {injrad:.8f}")
    print()
    print("The length spectrum encodes the Selberg zeta function Z(s).")
    print("Zeros of Z(s) on Re(s) = 1 correspond to eigenvalues")
    print("lambda = s(2-s) = 1 + r^2 where s = 1 + ir.")
    print()
    print("Computing Z(s) from the length spectrum is feasible but")
    print("extracting individual zeros requires root-finding on the")
    print("critical line — analogous to computing Riemann zeros.")
else:
    print("No length spectrum data available.")

# ============================================================
# Summary
# ============================================================
print(f"\n{'=' * 72}")
print("SUMMARY")
print("=" * 72)
print("""
STATUS: R6' is BLOCKED at the individual-eigenvalue level.

WHAT IS PROVEN (without computing eigenvalues):
  - The discrete spectrum carries m004-specific arithmetic [B739]
  - The conductor-(4)/(8) Hecke palette lives ONLY in discrete newforms
  - The continuous spectrum is generic (field-level, not object-level)
  - m004 is congruence at level (8) [B734]

WHAT IS COMPUTABLE IN-SANDBOX:
  - Length spectrum (done above)
  - Weyl eigenvalue count estimates
  - Spectral gap lower bound via Selberg conjecture (conditional)
  - Weight-2 Bianchi modular forms via LMFDB lookup

WHAT IS BLOCKED:
  - Individual Maass eigenvalues at level (8)
  - Hecke eigenvalue decomposition of the newform space
  - The specific arithmetic content (golden? Eisenstein?) of newforms

RECOMMENDATION:
  1. Check LMFDB for existing Bianchi modular form data at level (8)
     over Q(sqrt(-3)) — weight-2 forms may already be tabulated
  2. The weight-0 Maass computation requires either:
     (a) Adapting Then/Avelin software for PSL(2, O_3) at level (8), or
     (b) A targeted research collaboration with a specialist
  3. This is a natural boundary of what the program can compute solo
""")
