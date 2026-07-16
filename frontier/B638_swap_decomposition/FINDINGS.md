# B638 — C1: THE SWAP MECHANISM FOUND (the chord's core law explained)

**Date: 2026-07-16. Prereg a645834a… (sealed first). All computed gates
green. Mathematics only.**

## G1 — the swap acts (all exact)

u·conj(u) = +1 (J = Ad(U₂₇)∘conj is a genuine antilinear involution);
σ*(rep_i) are cocycles 5/5; σ*² = id mod coboundaries 5/5. **The deck
involution acts on H¹(D;27) as an antilinear involution** — the chord
carries a canonical real structure.

## G2 — the σ*-matrix: THE EISENSTEIN-UNIT SPECTRUM

Lower-triangular in the banked basis with diagonal
**(ζ₆, ζ̄₆, −ζ₆, −ζ̄₆, 1)** — the five modes carry five distinct
sixth-root swap-phases (all but −1), with mixing only INTO the
boundary-born pair {0,1} (rows 2,3,4 mix into 0,1; the pair itself is
σ*-triangular: σ*(0) = ζ₆·0, σ*(1) = ζ̄₆·1 + (√−3/24)·0).

## G3 — the transformation law

**Y(σ*α, σ*β, σ*γ) = conj(Y(α, β, γ))** — verified on all three test
triples (the plus_conj law; the orientation-reversal sign is absorbed
into J's phase structure). Combined with G2 this FORCES the observed
phase pattern:

- conj(Y[023]) = ζ₆·ζ₆·ζ̄₆·Y[023] = ζ₆·Y[023] (the zero law kills all
  mixing terms) ⇒ Y[023] lies on the e^{5πi/6}·ℝ line — exactly where
  the banked value sits (verified: −7983360 + 2661120√−3 has
  imag/real = −1/√3);
- conj(Y[123]) = −Y[123] ⇒ pure √−3-imaginary ✓ (banked);
- the pure-imaginary components (Y[034], Y[124]) and the mixed Y[023]
  are all phase-forced by the diagonal units.

## G4/G5 status

The reality theorem (G4) is PROVED by the above phase bookkeeping for
every component whose mixing terms are killed by the zero law. The
24ζ₆ RATIO mechanism (G5): the law + the σ*-matrix REDUCE the identity
Y[023] = 24ζ₆·Y[123] to the mixing-entry bookkeeping of rows 2–4 (the
symbolic expansion over the lower-triangular matrix); the full
derivation is registered as the closing step (the phase parts are
already forced; the magnitude 24 = the remaining content). The zero
law's mechanism (why Y[01k] = 0) also follows the same route: classes
0,1 have swap-phases ζ₆, ζ̄₆ whose product constraints conflict with
the law unless the components vanish — the full statement banked with
the derivation step.

## The upshot

The Law of the Chord's Core is no longer bare data: **the swap real
structure with Eisenstein-unit spectrum is its mechanism** — the phase
content of every component is now theorem-grade, with one bookkeeping
derivation (registered) remaining for the magnitude-24 part.

---

## The closing derivation (2026-07-16): PARTIAL — the phases proved, uniqueness not forced

The full σ*-law system over all ten triples with the complete exact
matrix (`b638_closure.py`, `b638_closure2.py`):

- **PROVED:** the pair {Y[123] pure imaginary, Y[023] = 24ζ₆·Y[123]}
  IMPLIES the (1,2,3) law equation exactly (direction 1); the banked
  unbent table satisfies the FULL 20-equation σ*-system with ZERO
  violations; the phase constraints of every component follow
  (conj(Y[023]) = ζ₆Y[023]; conj(Y[123]) = −Y[123] given the ratio;
  the Y[034]/Y[124] pure-imaginarity given the zero law).
- **NOT FORCED:** the σ*-system's solution space is 10-real-dimensional
  (of 20) — the swap halves the freedom and locks the phase geometry,
  but does not uniquely determine the magnitude ratios. The
  first-draft claim "the law is proved from the swap data" is
  OVERSTATED and corrected here: the swap is necessary-and-satisfied,
  not sufficient.
- **The registered follow-up (the second symmetry):** one more
  symmetry constraint would close the gap — the natural candidate is
  the object's own amphichiral flip (R ↔ L exchange) acting on the
  double alongside the swap; its σ*-analog + this system plausibly
  pins the ratios. Registered as the B638-completion cell.

The mechanism scoreboard: the reality/phase pattern of the chord's
core = THEOREM (the swap); the 24ζ₆ magnitude = LAW (9/9 exact,
swap-consistent, awaiting the second symmetry for forcing); the zero
law = LAW (9/9, mechanism open).
