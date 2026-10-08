# W31 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed. Most
were seen in the plan review, which computed W31's main numbers in memory before this rule existed. Nothing here is a
result.

## Why this route

- **The owner's approved plan, its last step: the ℤ₅ / SU(5) flux.**
- **Why ℤ₅ and not another** (Reading W24–W29, point 2):
  - holonomies that keep the whole Standard Model lie in its centraliser in E₈;
  - a twist-eater's commutator is central there, so it has order 5;
  - so ℤ₅ is the only twist-eater flux compatible with an unbroken Standard Model.
- **Main's grade (GENESIS v1.28, S86, §4)** names SU(5) among the holonomy groups with complex representations that
  would finish the derivation if forced.

## Weave or thread?

- **The object is chosen, not forced.** Every claim is conditional on the shared fibre carrying a ℤ₅ flux.
- **The computations are joint over the moves** (the convention below).
- So this is a weave-type computation on a hand-picked structure, labelled so.

## Labels and conventions (TERMINOLOGY's overloaded-symbol registry, 2026-10-08)

- **The factors.** E₈ ⊃ (SU(5)_g × SU(5)_b)/ℤ₅:
  - **SU(5)_g** is the gauge factor, containing the Standard Model (the audit lane's R40, quoted in B1509, calls a
    factor SU(5)′; this rule does not use that name);
  - **SU(5)_b** is the bundle factor, the Standard Model's centraliser, where the clock and shift live;
  - 248 = (24, 1) + (1, 24) + (10, 5) + (10̄, 5̄) + (5̄, 10) + (5, 10̄), with centre kernel (ζ, ζ⁻²).
- **The pair.** A = C₅ = diag(ζ^k) and B = S₅, with ζ = e^{2πi/5}.
  - det A = det B = 1, so no scaling is needed.
  - The flux ζ^m (m = 1, …, 4) is the pair (C₅^m, S₅), with commutator ζ^m·1.
- **The moves:**
  - L and R (the grammar's moves, GENESIS GM2) define "the moves";
  - the bare sign −I (GENESIS GM5b), the swap P (GENESIS GM5c) and P∘K (the swap with conjugation) are reported as
    their own cells (W29, post hoc P3; W30).
- **The index (this arc's sign, as in W22 and W29).**
  - The 5-sector (the 10 of SU(5)_g) has puncture holonomy ζ^m on 5 channels: index −m + d₅.
  - The Λ²5-sector (the 5̄ of SU(5)_g) has ζ^{2m} on 10 channels, α = {2m/5}: index −10α + d₁₀.
  - F-HE's convention (N = −I, B1509) flips every sign; the anomaly condition below is unchanged.
- **The anomaly.** SU(5)_g's cubic anomaly vanishes when n(10) = n(5̄).

## The cells

The script is `the_z5_twist_eater.py`, writing `.json` beside it.

- **F1, the group** (computed; the lemma PROVED).
  - |⟨C₅, S₅⟩| = 125; centre ζ^j·1; commutator ζ·1; irreducible; Frobenius–Schur 0.
  - The lemma (as in W29): an invariant subspace W has ζ^{dim W} = 1, so it has dimension 0 or 5. Hence no U(1) of
    SU(5)_b commutes with the pair.
- **F2, the centraliser in E₈.**
  - The mean of W25's chi248 at diag(h, 1) ∈ SU(6)′, over the 125 elements: **24**, exactly SU(5)_g.
  - The code check: the explicit SU(5)_g × SU(5)_b character, tr h · tr h⁻¹ + 23 + 10(tr h + tr h⁻¹) +
    5(tr Λ²h + tr Λ²h⁻¹), agrees on every element. The two forms are one expression, so this checks the code, not a
    second route.
- **F3, the matter.**
  - The 5 occurs 10 times (the 10 of SU(5)_g).
  - Λ²5 is two copies of one 5-dimensional type, which occurs 10 times (the 5̄ of SU(5)_g, twice).
  - Both types are complex (indicator 0): complete SU(5) generations, 10 + 5̄.
- **F4, the flux, the hypercharge and the orientation.**
  - Z(SU(5)_g) ⊂ U(1)_Y: exp(2πi·(6j/5)·Y) = ζ^{−2j}·1₅ on SU(5)_g's 5, with Y = diag(−1/3 ×3, 1/2 ×2) (exact,
    sympy). Through the centre kernel, the flux is a hypercharge rotation.
  - L, R and −I keep the flux ζ (one intertwiner each); P sends it to ζ̄ (none); P∘K keeps it (one).
  - **The moves force trivial hypercharge Wilson lines** (up to μ₅, which is a centre twist of the pair). L keeps ζ,
    so a conjugating element cannot complex-conjugate SU(5)_b, so it cannot invert Y. L then fixes (y_a, y_b) only if
    y_a = 1, and R only if y_b = 1. PROVED by this argument; nothing is computed.
- **F5, the moves at the puncture** (flux ζ).
  - The lifts of L and R (normalised to det 1) have projective order 120 (SL(2, 𝔽₅) ≅ 2I) and commutant 2, split
    3 ⊕ 2.
  - Golden traces: |tr|² of the lifts includes φ² and φ⁻² on the 2-piece, which is the spin representation of 2I. The
    3-piece factors through A₅.
  - The pieces are the eigenspaces of the lift of (LR⁻¹L)², a reflection k ↦ 4 − k up to phases.
  - The bare −I's lift is k ↦ −k. It has 3- and 2-dimensional eigenspaces too, but they are not the pieces.
  - With the bare −I added: commutant 1, projective order 3000.
  - On Λ²ℂ⁵ the lifts' structure is [1, 3, 6].
- **F6, the counts, for every flux ζ^m.** These are this arc's main table, from the move-invariant dimensions
  d₅ ∈ {0, 2, 3, 5} and d₁₀ ∈ {0, 1, 3, 4, 6, 7, 9, 10}:

  | flux | n(10) under the moves | n(10) under locality | the SU(5)³-free counts under the moves | under locality |
  |---|---|---|---|---|
  | ζ | −1, 1, 2, 4 | −1, 4 | −1, 2 | none |
  | ζ² | −2, 0, 1, 3 | −2, 3 | −2, 1 | none |
  | ζ³ | −3, −1, 0, 2 | −3, 2 | −1, 2 | none |
  | ζ⁴ | −4, −2, −1, 1 | −4, 1 | −2, 1 | none |

  - **The headline: no ℤ₅ flux gives an anomaly-free three,** under the moves or under locality.
  - (With ζ^{±2}, three 10s occur under locality, but never with three 5̄s.)
- **F7, the verdict.**
  - **What it gives** (conditional): complete SU(5) generations with the hypercharge inside SU(5)_g, and the moves
    acting through 2I, with golden traces.
  - **NEGATIVE as a derivation:**
    - no anomaly-free three for any ℤ₅ flux;
    - SU(5)_g is not broken to the Standard Model by anything forced (F4);
    - an unbroken SU(5) is not the Standard Model, and F-MC's derived cascade skips SU(5) (SMT, B892);
    - the flux is not forced: W30's lemma holds for any order above 2, and the record's order-5 structures are
      properties of the modulus or of threads (B206; the golden-covers dossier);
    - and, as in W30, the swap sends the flux to its conjugate, so it is a common point only on the swap's fork
      (GENESIS GM5c).

## What each outcome means

- **As stated.** The ℤ₅ route closes. With W29 and W30, the twist-eater programme gives no forced three:
  - ℤ₆ breaks the hypercharge;
  - a qutrit is allowed only on the swap's fork;
  - ℤ₅ keeps the hypercharge but allows no anomaly-free three.

  Main's finishing condition is not met by any flux tried. The record's best statement stays the state page of
  2026-10-08.
- **F6 shows an anomaly-free three for some flux.** That would reopen the route at once, under that flux's own
  forcing question.
- **F2 not 24, or F5's commutant not 2.** The picture differs. Record it, and re-derive F6 from the computed structure
  before anything is written.

## Seen before this was written

- **The plan review (2026-10-08, computed in memory and not committed):**
  - F1's group facts;
  - F5's projective order 120, split 3 ⊕ 2, golden |tr|², the reflections k ↦ 4 − k and k ↦ −k, and with −I commutant
    1 and order 3000;
  - Λ² = [1, 3, 6];
  - F6's whole table;
  - "raw null-space phases give 1200 elements in U(5)", which is why the lifts are det-normalised.
- **By hand:**
  - F2's 24 (23 + 1);
  - the character identity chi248(diag(h, 1)) = the explicit SU(5)_g × SU(5)_b form;
  - F4's argument.
- **The record:** TERMINOLOGY's registry for SU(5)′ and Λ; B1509 (R40's branching); SMT (B892); B206; the golden-covers
  dossier; W29 (post hoc P3); W30; main's S86.
