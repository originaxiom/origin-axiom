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

## Full adjudication of the Seat-1 SM-Hunt-Arc handoff (2026-07-08)
CORRECT (already banked, verified): Discovery 1 the Fibonacci-anyon identification (B483);
Discovery 2 the torsion wall — Weil det ∈ ⟨ζ₁₂⟩, 5∤12 (B481/B483); the ten kills (accurately
listed); 6c the braid trace tr = −3/φ (B484). The forcing map (§8) matches K024.

**REFUTED — Discovery 3 / 6a / §9 voice-box / §10 "proven": the cusp is NOT hexagonal.**
The handoff lists "the cusp is hexagonal with exact three-fold degeneracy" as PROVEN while
also carrying CC's rectangular-cusp finding — an internal contradiction. The rectangular one
is correct (this file, verified two ways). The cusp modulus is on the imaginary axis (2√3·i in
the named framing, 1/(2√3)·i-type in the b++ framing — the same rectangular cusp up to the
modular group), NEVER the hexagonal e^{2πi/3}. Consequences that fall with it:
- **6a** (three unit curves, 120°-related): the three curves have DIFFERENT lengths; multiplicity
  2 not 6; refuted.
- **Priority 3** (the "(3,5) surgery has Eisenstein-prime norm 19"): uses the hexagonal norm form
  p²+q²−pq. The actual rectangular form is p² + 12q² (named framing), under which (3,5)↦... a
  different value. The Eisenstein-19 claim is built on the false hexagonal premise — moot.
- **Priority 4** (three degenerate modes → three flat connections → three generations): no
  three-fold degeneracy exists; moot.
- **§9 "voice box: τ = e^{iπ/3}, three vocal modes"**: false; the cusp is rectangular.

**6b (power-set magnitude law) — PLAUSIBLE, not confirmed, priced.** At level 15 the claim
{√(subset products)} = {1,√3,√5,√15} is consistent with the banked master theorem's ℚ(√5,√−3)
values (B474). The composite-N generalization (105 → {1,√3,√5,√7,√15,√21,√35,√105}) is a clean
Gauss-sum/Howe+CRT corollary and is likely true, but the quick check here used a rank-1
projector normalization that gave the wrong object; a clean confirmation needs the exact B474
interaction-form machinery (spectral projectors onto eigenSPACES). Priced, not banked.

**Priority 5 (cusp limit) — REAL.** The b++ cusp shapes: 0.289, 0.500, 0.602, 0.625 (peak m=4),
then slowly decreasing 0.614…0.532 by m=12; volumes → ~7.3. Converging slowly, all rectangular;
no three-fold degeneracy to lose (there never was one).

**The physics program (Priorities 1–2, T[4₁(p,q), G]) — real math, but not the SM.** The
DGG 3d–3d correspondence sends 4₁(p,q) to a 3d N=2 theory (B483); computing T[4₁(15,1), SU(2)]
is a legitimate calculation, but its output is a 3-dimensional supersymmetric theory, not the
4-dimensional Standard Model. "The SM is one specific sound T[4₁(p,q),G]" is the same category
error as the eleven kills (a 3d SUSY theory ≠ the 4d SM). Nothing shifts.

**Net:** the handoff's mathematics is largely correct and already banked (Fibonacci anyon,
torsion wall, kills, braid trace); its one new load-bearing claim (the hexagonal cusp) is false;
its physics program is real math that lands on 3d SUSY, not the SM. 11 kills stand; the delta
(S060) and forcing map (K024) are unchanged.
