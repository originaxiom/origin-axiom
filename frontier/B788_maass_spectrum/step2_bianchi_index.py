r"""Maass programme Step 2: the index [PSL(2,O3) : Gamma_41].

Chat-1 handoff (MAASS_SPECTRUM_HANDOFF, 2026-07-25), Step 2, owner CC3:
determine the index of the figure-eight knot group's holonomy image
Gamma_41 inside the Bianchi group PSL(2, O3), O3 = Z[omega] the
Eisenstein integers.

METHOD. Finite-index subgroups of a lattice satisfy
    [G : H] = Vol(H\H^3) / Vol(G\H^3).
Both volumes are EXACT closed forms:

  Vol(m004)            = 2 * V_tet = 2 * Cl2(pi/3)   (two regular ideal
                         tetrahedra; V_tet = 3*Lob(pi/3) = Cl2(pi/3))
  Vol(PSL(2,O3)\H^3)   = |D|^(3/2) * zeta_K(2) / (4 pi^2),  D = -3
                         (Humbert's formula, a theorem)

Both reduce to rational multiples of L(2, chi_{-3}):
  V_tet              = (3 sqrt(3) / 4) * L(2, chi_{-3})
  Vol(PSL(2,O3)\H^3) = (sqrt(3) / 8)  * L(2, chi_{-3})

so the index is EXACT -- the transcendental L-value cancels:
  [PSL(2,O3) : Gamma_41] = 2 * (3 sqrt(3)/4) / (sqrt(3)/8) = 12.

This matches Riley (1975): the figure-eight group is an index-12
subgroup of PSL(2, Z[omega]).

Pitfall-4 antidote (handoff): m004 vs sister m003 have the SAME volume;
distinguish by homology H1(m004) = Z vs H1(m003) = Z + Z/5.

Gate 5-Q.
"""
import mpmath as mp

mp.mp.dps = 60

print("=" * 72)
print("SECTION 1: MANIFOLD IDENTITY (SnapPy, pitfall-4 check)")
print("=" * 72)
print()

import snappy

M = snappy.ManifoldHP('m004')
Sister = snappy.ManifoldHP('m003')
K = snappy.ManifoldHP('4_1')

vol_m004 = M.volume()
vol_m003 = Sister.volume()
vol_41 = K.volume()

print(f"  m004 volume (quad precision): {vol_m004}")
print(f"  m003 volume (sister):         {vol_m003}")
print(f"  4_1  volume (knot exterior):  {vol_41}")
print()
print(f"  H1(m004) = {M.homology()}   <- Z: this IS the knot complement")
print(f"  H1(m003) = {Sister.homology()}   <- Z + Z/5: the sister, NOT the knot")
print(f"  H1(4_1)  = {K.homology()}")
print()
iso = K.is_isometric_to(snappy.Manifold('m004'))
print(f"  4_1 isometric to m004: {iso}")
print(f"  m004 solution type: {M.solution_type()}")
print(f"  m004 cusps: {M.num_cusps()}")
print(f"  m004 tetrahedra: {M.num_tetrahedra()}  (the 2 regular ideal tetrahedra)")
print()

# ================================================================
print("=" * 72)
print("SECTION 2: EXACT VOLUME OF m004")
print("=" * 72)
print()

# V_tet = Cl2(pi/3) (Gieseking constant), Vol(m004) = 2 * V_tet.
# Cl2(x) = sum sin(n x)/n^2 = Im Li2(e^{ix}).
Cl2_pi3 = mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
V_tet = Cl2_pi3
vol_exact = 2 * V_tet

# L(2, chi_{-3}) via trigamma: L = (psi_1(1/3) - psi_1(2/3)) / 9
L2 = (mp.polygamma(1, mp.mpf(1) / 3) - mp.polygamma(1, mp.mpf(2) / 3)) / 9

# Closed-form check: V_tet = (3 sqrt(3)/4) L(2, chi_{-3})
V_tet_from_L = 3 * mp.sqrt(3) / 4 * L2

print(f"  Cl2(pi/3) (Gieseking const.) = {mp.nstr(Cl2_pi3, 50)}")
print(f"  Vol(m004) = 2*Cl2(pi/3)      = {mp.nstr(vol_exact, 50)}")
print(f"  L(2, chi_-3)                 = {mp.nstr(L2, 50)}")
print(f"  (3 sqrt3/4) * L(2,chi_-3)    = {mp.nstr(V_tet_from_L, 50)}")
print(f"  V_tet identity holds: {abs(V_tet - V_tet_from_L) < mp.mpf(10) ** -55}")
print(f"  SnapPy vol matches exact: {abs(mp.mpf(repr(vol_m004)) - vol_exact) < mp.mpf(10) ** -25}")
print()

# ================================================================
print("=" * 72)
print("SECTION 3: HUMBERT'S FORMULA FOR THE BIANCHI ORBIFOLD")
print("=" * 72)
print()

# Vol(PSL(2,O_d)\H^3) = |D|^{3/2} zeta_K(2) / (4 pi^2), D = disc = -3
# zeta_K(2) = zeta(2) * L(2, chi_{-3})
zeta_K2 = mp.zeta(2) * L2
vol_bianchi = mp.mpf(3) ** mp.mpf(1.5) * zeta_K2 / (4 * mp.pi ** 2)

# Closed form: = (sqrt(3)/8) L(2, chi_{-3})
vol_bianchi_closed = mp.sqrt(3) / 8 * L2

print(f"  |D|^(3/2) = 3^(3/2)          = {mp.nstr(mp.mpf(3) ** mp.mpf(1.5), 30)}")
print(f"  zeta_K(2) = zeta(2)*L(2,chi) = {mp.nstr(zeta_K2, 50)}")
print(f"  Vol(PSL(2,O3)\\H^3)           = {mp.nstr(vol_bianchi, 50)}")
print(f"  (sqrt3/8)*L(2,chi_-3)        = {mp.nstr(vol_bianchi_closed, 50)}")
print(f"  Closed form holds: {abs(vol_bianchi - vol_bianchi_closed) < mp.mpf(10) ** -55}")
print()
print("  Derivation: 3^(3/2) * (pi^2/6) * L / (4 pi^2) = (3 sqrt3 / 24) L")
print("            = (sqrt3/8) L.  The pi^2 cancels; only L remains.")
print()

# ================================================================
print("=" * 72)
print("SECTION 4: THE INDEX (EXACT)")
print("=" * 72)
print()

index_numeric = vol_exact / vol_bianchi
print(f"  Vol(m004) / Vol(PSL(2,O3)\\H^3) = {mp.nstr(index_numeric, 50)}")
print()
print("  Exact cancellation:")
print("    index = 2 * (3 sqrt3/4) L  /  ((sqrt3/8) L)")
print("          = (3 sqrt3/2) * (8/sqrt3)")
print("          = 24/2 = 12       (L and sqrt3 cancel EXACTLY)")
print()
print(f"  |index - 12| = {mp.nstr(abs(index_numeric - 12), 5)}")
print()
print("  [PSL(2,O3) : Gamma_41] = 12   (exact; Riley 1975 concurs)")
print()
print("  PGL note: PGL(2,O3) contains PSL(2,O3) with index 2, so")
print("  [PGL(2,O3) : Gamma_41] = 24. The handoff's restriction step")
print("  should use PSL (holonomy lands in PSL(2,C)).")
print()

# ================================================================
print("=" * 72)
print("SECTION 5: CONSEQUENCES FOR THE MAASS PROGRAMME")
print("=" * 72)
print()

weyl_c_m004 = vol_exact / (6 * mp.pi ** 2)
weyl_c_bianchi = vol_bianchi / (6 * mp.pi ** 2)

print("  Spectral inclusion: every PSL(2,O3)-invariant Maass form is")
print("  automatically Gamma_41-invariant (Gamma_41 is a SUBgroup), with")
print("  the SAME eigenvalue. So the level-1 Bianchi spectrum embeds in")
print("  the m004 spectrum. Restriction preserves eigenvalues.")
print()
print("  Weyl-law bookkeeping (N(T) ~ c T^3):")
print(f"    c(m004)    = Vol/(6 pi^2) = {mp.nstr(weyl_c_m004, 10)}")
print(f"    c(Bianchi) = {mp.nstr(weyl_c_bianchi, 10)}")
print(f"    ratio = 12: the m004 spectrum is ~12x denser.")
print()
print("  => Asymptotically only ~1/12 of m004 eigenvalues are 'old'")
print("     (level-1 Bianchi) forms; ~11/12 are NEW forms of Gamma_41.")
print("     LMFDB level-1 d=3 data (Step 1, CC2) covers at most the old")
print("     1/12. The handoff's false-failure clause (index > 100 =>")
print("     direct computation) does NOT trigger, but 12 is enough that")
print("     Step 3 (direct computation) is required for the new forms.")
print()
print(f"    Expected counts for m004: N(5) ~ {mp.nstr(weyl_c_m004 * 125, 4)}, "
      f"N(10) ~ {mp.nstr(weyl_c_m004 * 1000, 4)}, "
      f"N(20) ~ {mp.nstr(weyl_c_m004 * 8000, 4)}, "
      f"N(50) ~ {mp.nstr(weyl_c_m004 * 125000, 5)}")
print()
print("  Congruence structure: Gamma_41 is index 12 = |PSL(2,F_3)| in")
print("  PSL(2,O3); the quotient acts on the 12 cosets. Useful for Step 3:")
print("  the fundamental domain of Gamma_41 = 12 copies of the Bianchi")
print("  domain (or SnapPy's 2-tetrahedron Ford domain directly).")
