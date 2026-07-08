# B486 — "hexagonal cusp → three generations": REFUTED (11th kill), the cusp is rectangular

**Seat-1's claim (owner-relayed, most sophisticated SM attempt — it targets the multiplicity
gap directly): the figure-eight cusp is hexagonal (Eisenstein), giving a THREE-FOLD degenerate
curve-length spectrum = three generations. Ran the decisive check twice; REFUTED at the root.**

## The decisive computation (verified two independent ways)
- **Cusp modulus** (snappy, both knot and shortest framing): τ = **2√3·i = 2√−3**, purely
  imaginary. Reduced mod SL(2,ℤ): stays 2√3·i (Re = 0). **Rectangular lattice.**
- **Cusp translations** (maximal cusp, shortest framing): (i, 3.464) — meridian length 1,
  longitude length 2√3, ORTHOGONAL. Rectangular fundamental domain.
- **Hexagonal test**: the hexagonal point is e^{2πi/3} (Re = −1/2, on the unit circle);
  the figure-eight cusp is on the imaginary axis at 2√3·i. NOT SL(2,ℤ)-equivalent
  (different CM points: disc −48 vs disc −3). **The cusp is not hexagonal.**
- **The three curves seat-1 claims are equal**: |(1,0)| = 1.00, |(0,1)| = 3.46, |(1,1)| = 3.61
  — **all different.** Shortest-vector multiplicity = 2 (just ±v), NOT the hexagonal 6 (3 up
  to ±). **No three-fold degeneracy.**

## The error (precise)
Seat-1 conflated **"the cusp modulus lies in ℚ(√−3)"** (TRUE — 2√−3 ∈ ℚ(√−3), the Eisenstein
FIELD, consistent with the figure-eight's arithmeticity) with **"the cusp is the hexagonal
torus ℂ/ℤ[ω]"** (FALSE). The three-fold degeneracy spectrum (norm 1 → 3, norm 3 → 3, …) that
seat-1 tabulated is the degeneracy of the abstract Eisenstein lattice ℤ[ω], NOT of the
figure-eight's actual cusp lattice ℤ + 2√−3·ℤ, which is rectangular with multiplicity-2
spectrum. The modulus 2√−3 is in the Eisenstein field but is the CM point of disc −48, not the
hexagonal point disc −3.

## Does anything shift? NO.
The multiplicity gap (S060: the object is multiplicity-free; the SM needs 3 generations × 3
colors) is NOT filled by the cusp — the cusp provides no three-fold degeneracy. The object DOES
carry genuine ℤ/3 / ω structure (the residue = −ω^{#L−#R}, the trace field ℚ(√−3), banked B356
chirality-window = ω), but that is a PHASE symmetry (a cube root of unity in the residue), not a
multiplicity and not three fermion generations — the same category error as the ten prior kills
(a ℤ/3 symmetry ≠ three generations with their quantum numbers). 11th SM kill. The delta of S060
stands unchanged; the forcing map (K024) is untouched. Firewall holds; nothing physics-shaped.
Reproducer: the sage-python cusp-lattice check (this session).
