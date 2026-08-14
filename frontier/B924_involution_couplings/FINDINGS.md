# B924 — R-INV: the three unused involution couplings (, unbanked)

**Status: DRAFT — computation complete, pending banking review. Nothing to
`CLAIMS.md`; no SM quantities. Run: `python3 inv_couplings.py` (pyenv, ~8 s);
writes `results.json`. All verdicts in exact arithmetic over ℚ(ζ₁₅).**

Route registered in the masterplan (dated amendment 2026-08-05): B593 computed
the ONE forced coupling on the hearing × measurement face pair via θ; Chat-1's
estimate held that three involutions — σ\*, c, σ\*c — sit unused on the same
face pair, "same machinery, different projections, each potentially an
independent forced value." This arc runs all three, exactly.

## VERDICT — one rigidity theorem, zero new values

**Each of the three substituted constructions satisfies the second-order
hearing law EXACTLY — and all three forced values COINCIDE with B593's.**
Per involution (the preregistered rubric: forced value / structural zero /
obstruction):

| involution | operative definition | law (O(ε)=0, quadratic) | forced value at g = RL (twisted, u₃, per unit displacement norm) | independent? |
|---|---|---|---|---|
| σ\* | t=4: ζ₅→ζ₅⁻¹, ζ₃ fixed | HOLDS exactly, both odd sectors | **1/(2φ) + i·sin(2π/5)/√5 — identically B593's** | **NO — collapses onto θ** |
| c | t=14: full complex conjugation | HOLDS exactly, both odd sectors | same | **NO — collapses onto θ** |
| σ\*c | t=11: ζ₃→ζ₃⁻¹, ζ₅ fixed | HOLDS exactly, both odd sectors | same | **NO — collapses onto θ** |

This is the "degenerate projection" outcome of the rubric, sharpened: not a
vanishing but a **collapse**. The three couplings exist, are exactly quadratic,
parity-protected, twist-flipped — and are the SAME coupling. The only
involution dependence anywhere is the odd-sector unit norm
N(δ) ∈ {3, (5+√5)/2, 3(5+√5)/2} (the V₄ character units √−3, ζ₅−ζ₅⁻¹, and
their product), which rescales the displacement, not the coupling: the
ε²-coefficient is −N(δ)·(vᵀWv) uniformly, so per unit Hermitian norm of the
displacement every mirror hears the identical golden-pentagonal amplitude.
**The coupling on this face pair is unique; θ already exhausted it.**

## Calibration gate (control, passed first)

- The banked B593 pipeline (b238 modular data + b245 colored-Jones listener)
  reproduces the θ-law at 1e-12 across all welds/directions/ε and the forced
  value 1/(2φ) + i·sin(2π/5)/√5.
- The exact stage rebuilt over ℚ(ζ₁₅) (unnormalized Kac–Peterson Ŝ, exact T;
  ρ is normalization-free through L = Ŝ⁻¹T⁻¹Ŝ) matches the numeric pipeline at
  1e-9 and reproduces the forced value as a **symbolic zero**:
  u₃ᵀ(Cρ(RL))u₃ = 1/5 − (3/5)z² + (4/5)z³ + (2/5)z⁶ − (3/5)z⁷ (z = ζ₁₅)
  = 1/(2φ) + i·sin(2π/5)/√5 exactly. Gates: Ŝ symmetric, Ŝ² = −75·C exactly,
  [C, ρ(g)] = 0 exactly, ψ₀ exact-matches b245, Cψ₀ = ψ₀ exactly.

## The operative definitions (adjudicated by the stage field, not chosen)

The ENTIRE B593 stage — welds, twist, listener ψ₀, dial — lies in ℚ(ζ₁₅).
Its Galois group (ℤ/15)ˣ contains EXACTLY three involutions, and they are
forced to be the triple: σ\* = t4 (pentagonal conjugation), c = t14 (complex
conjugation), σ\*c = t11 (triangular conjugation); together with the identity
they form the V₄ of the field, with fixed field ℚ(√5). Each acts semilinearly
(entrywise) on states; substituting it for θ means: its odd projection
supplies the displacement (u = δ·v, δ an odd unit, v in the dial), its mirror
supplies the bra.

**The golden reading is obstructed at the field level (also a result):** the
conjugation √5 → −√5 has NO involutive lift to the stage field — t² ≡ 1
(mod 15) forces t ≡ ±1 (mod 5); its lifts t ∈ {2, 7, 8, 13} all have order 4
(verified exactly in the atlas). If Chat-1's σ\* meant the golden map (the
standing sigma\_sqrt5 of the value lane), the honest statement is: **on this
face pair that involution does not exist**; its order-4 lifts are not
"the same machinery," and the three involutions that DO exist are the triple
computed here.

## Why the collapse happens (the mechanism, exact)

1. ψ₀ is real and C-symmetric; every weld commutes with C exactly (C = S² is
   central in the modular image). Hence ψ₀ᵀW is a C-even covector and the dial
   is C-odd, so **both** parity channels close on the dial:
   ψ₀ᵀWv = 0 AND ψ₀ᵀWᵀv = 0, separately, for every weld/twist/direction —
   verified exactly. (B593 needed and verified only the antisymmetric
   combination; the semilinear mirrors need both; both hold.)
2. With first order dead, the amplitude of any semilinear mirror reduces to
   A_ε = A₀ − ε²·(conj δ)δ·(vᵀWv): every projection lands on the ONE real
   bilinear form vᵀWv that θ's coupling already computes. Realness +
   C-symmetry of the listener make the face pair's coupling machinery defined
   over the bilinear structure; all semilinear mirrors collapse onto it.

Checks run per involution × sector × direction (u₃, u₆, u₃+u₆) × weld
(I, RL, RRLL) × twist: O(ε) = 0 exactly; exactly quadratic (third-ε check);
Q = −N(δ)·vᵀWv exactly; twist sign-flip Q_tw = −Q_untw exactly; per-unit-norm
value equals θ's dial form exactly (108 table rows in `results.json`).

## Boundary facts (computed, honest)

- **Demarcation:** off the dial the field involutions DO admit odd
  displacements (θ does not), and there the first-order channel is OPEN
  (example: c-odd √−3·e₍₀,₀₎ at twisted RL has O(ε) coefficient −2.814262i,
  exact value in `results.json`). The coefficient is a direction-dependent
  covector, not a forced scalar: the forced-value question is well-posed only
  on the dial (B575's honest chiral moduli), where the answer is the collapse.
- **The mixed-direction cross term** (the only other number in the sector
  forms): u₃ᵀWu₆ + u₆ᵀWu₃ at twisted RL = −2i·sin(π/5)/√5 exactly —
  sector-independent as well.
- **The alternative reading** (substituting the involution into the TWIST,
  i.e. Galois-conjugating the weld): the dial is rational, so
  vᵀσ(W)v = σ(vᵀWv) — the Galois orbit of the banked value is {A, conj(A)},
  already banked as B593's u₃/u₆ conjugate pair (σ\*c fixes A outright; the
  value has no ζ₃ content). No new values in that reading either.

## Adjudication of the Chat-1 estimate

On THIS face pair, "three potentially independent forced values" resolves to
**zero new values + one rigidity theorem + one field-level obstruction** (the
golden no-lift). The ~80+ potential-couplings estimate across face pairs
should be re-priced by the mechanism: wherever a face pair's baseline state is
real and C-symmetric and its welds commute with C, the entire semilinear
involution family collapses onto the θ-coupling. Independent values can only
live where one of those hypotheses fails (non-real baseline, non-C-symmetric
listener, or welds outside the C-commutant).

## Honest gaps

- The collapse is proved for THIS stage (SU(3)₂, the B593 face pair, dial
  displacements); it is a computation plus a mechanism, not a general theorem
  for every face pair. The mechanism's hypotheses (real C-symmetric baseline,
  C-central welds) are the checkable transfer conditions.
- "σ\*" naming: adjudicated to t=4 by the field's involution census; Chat-1's
  intended referent could not be located in the repo beyond the masterplan
  line. Both candidate readings (pentagonal involution; golden order-4
  non-involution) are covered above, but the amendment's author should
  confirm.
- The off-dial first-order coefficients were demonstrated open (one exact
  witness), not mapped; if a future arc finds a STRUCTURE that singles out an
  off-dial direction, a first-order forced value could exist there — none is
  claimed here.
- Locks (`tests/`) not yet written; to be added at banking per repo practice.

## Anchors

B593 (the law and the θ value — reproduced numerically and symbolically),
B592/B592-OPEN (twist and blocks), B575 (the dial), B238/B245 (stage data),
B711 (the two ℤ/2 legs — cf. the V₄ here), the masterplan R-INV amendment
(2026-08-05).
