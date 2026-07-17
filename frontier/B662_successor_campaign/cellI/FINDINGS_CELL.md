# B662 CELL I — THE γ₅′ UPSTREAM MATHEMATICS: THE FIRST EXACT MAP

**Date: 2026-07-17. Campaign prereg: `../CAMPAIGN_PREREGISTRATION.md`
(cell I, wave 3; sealed before launch). Script `gamma5_map.py`
(sha256 2b0ac503…bd40) → `cellI_output.txt` (sha256 69aa67f4…7fcce).
All arithmetic exact (ℚ(ζ₂₀) with Fraction coefficients mod Φ₂₀; no
floats anywhere). Gate 5 clean: pure representation theory, no SM
values. Two-outcome verdict: the EXACT-CORRESPONDENCE branch fired.**

## VERDICT

1. **The ear's hearing representation IS the Γ₅′-doublet 2̂′** (exact
   character equality on all 9 conjugacy classes of SL(2,5), under the
   canonical identification Γ₅′ = SL(2,ℤ)/Γ(5) = SL(2,𝔽₅)), and the
   ear's Galois pair (χ_golden, χ̄) **is their (2̂′, 2̂) doublet pair**
   (the √5 ↦ −√5 automorphism carries χ_2̂′ to χ_2̂ class-by-class,
   verified exactly).
2. **H129 resolved — weight 5 is FORCED, not a coincidence:** level-5
   integral-weight forms are Sym^{5k} of the doublet (two weight-1/5
   generators), and the doublet multiplicity series in Sym^n has
   numerator exponents = **the E₈ exponents** over the 2I invariant
   degrees (1−t¹²)(1−t²⁰); the first n ≡ 0 (mod 5) occurrence is
   n = 1 + 2·12 = 25, i.e. **weight 5**.
3. Upgrade per the prereg: **PLACEMENT → CANDIDATE FUNCTOR** — the
   framework derives, from the monodromy, exactly the flavor
   representation the Γ₅′ paradigm postulates (see the honest gap
   below).

## Task 1 — the exact map, with the class-matching displayed

Both sides live on the SAME concrete group. The ear (banked B640/B644,
theorem grade): ρ_hear|ker(det) = χ_golden ∘ (mod-5 reduction), letters
R ↦ [[1,1],[0,1]], L ↦ [[1,0],[1,1]] over 𝔽₅, closing to SL(2,𝔽₅).
The literature (Yao–Liu–Ding [YLD], Table 11): the doublets 2̂, 2̂′ of
Γ₅′ ≅ SL(2,ℤ₅), with Γ₅′ = SL(2,ℤ)/Γ(5) and S ↦ [[0,1],[−1,0]],
T ↦ [[1,1],[0,1]] mod 5 (their Eqs. (2), (5)). So the comparison is
canonical — no basis choice enters the verdict. (Naming clash flagged:
the object's cat-map letters R, L vs the literature's central
R = S²; context disambiguates.)

The literature matrices (YLD Table 11, extracted 2026-07-17, verified
in-sandbox against their presentation Eq. (4): S² = −1, S⁴ = T⁵ =
(ST)³ = 1, S²T = TS²; note (ST)³ = +1 in their S-sign convention):

- ρ_2̂(S) = i·√(1/(√5·φ))·[[φ, 1],[1, −φ]], ρ_2̂(T) = diag(ω₅², ω₅³)
- ρ_2̂′(S) = i·√(1/(√5·φ))·[[1, φ],[φ, −1]], ρ_2̂′(T) = diag(ω₅, ω₅⁴)

(ω₅ = e^{2πi/5}; √(√5φ) = 2cos(π/10) ∈ ℚ(ζ₂₀), so everything is exact
in ℚ(ζ₂₀).) BFS over words in {S,T} tracking (mod-5 matrix, exact 2̂
matrix, exact 2̂′ matrix): closure has exactly 120 elements, **121
collisions with 0 exact-matrix mismatches** — the homomorphism onto
concrete SL(2,𝔽₅) is well-defined and faithful (kernel of scalars =
{±I} = center; complete relation check, stronger than generator
relations).

The class-matching (all values exact; ear column = the B644 banked
corrected table, whose Schur norm ⟨χ,χ⟩ = 1 and parity χ(−g) = −χ(g)
were re-verified here exactly):

| class (YLD label) | (order, qr) | size | χ_ear | χ_2̂′ | χ_2̂ |
|---|---|---|---|---|---|
| 1C₁ | (1, —) | 1 | 2 | 2 | 2 |
| 1C₂ (R) | (2, —) | 1 | −2 | −2 | −2 |
| 20C₃ (ST) | (3, —) | 20 | −1 | −1 | −1 |
| 30C₄ (S) | (4, —) | 30 | 0 | 0 | 0 |
| 12C₅ (T) | (5, QR) | 12 | 1/φ | **1/φ** | −φ |
| 12C₅′ (T²) | (5, nQR) | 12 | −φ | **−φ** | 1/φ |
| 20C₆ (S³T) | (6, —) | 20 | 1 | 1 | 1 |
| 12C₁₀ (TR) | (10, QR) | 12 | −1/φ | **−1/φ** | φ |
| 12C₁₀′ (T²R) | (10, nQR) | 12 | φ | **φ** | −1/φ |

χ_ear = χ_2̂′ on **all 9 classes**; χ_ear ≠ χ_2̂ (differs on the four
golden classes). Character equality is a complete isomorphism
invariant, so **ρ_hear ≅ 2̂′ as Γ₅′-representations**. The computed
table equals YLD Table 10's rows for 2̂ and 2̂′ (both cross-checked
exactly, so the extraction and the computation agree).

Anchors to the banked record:
- the cat map RL mod 5 = [[2,1],[1,1]] lies in class 12C₁₀, where
  χ_2̂′ = −1/φ = the banked hearing headline tr ρ_hear(RL) (B640/B644);
- χ_2̂(12C₁₀) = +φ = the banked B642 k = 7-stage twist value — so
  **the stage-twist Galois partner (K020-in-the-ear) is exactly their
  2̂**; the Galois map √5 ↦ −√5 (ζ ↦ ζ³ on ℚ(ζ₂₀)) sends χ_2̂′ ↦ χ_2̂
  class-by-class (verified exactly).

Precision note on "which one": the outer automorphism of SL(2,5)
(PGL(2,5)-conjugation by diag(1, non-residue)) swaps the two unipotent
classes and hence 2̂ ↔ 2̂′; the specific label "2̂′" is meaningful
because BOTH sides are pinned to the same concrete mod-5 reduction of
SL(2,ℤ) (the ear by construction, Γ₅′ by definition). The pair-level
statement (ear pair = their doublet pair) is convention-free.

## Task 2 — the weight-5 mechanism (H129): FOUND, exact

The literature facts (YLD Section 2.1, accessed 2026-07-17): dim
M_k(Γ(5)) = 5k+1; the space of weight-1/5 level-5 forms is spanned by
two algebraically independent functions F₁, F₂ (their Eq. (12), citing
their ref. [68] = Ibukiyama for the weight-1/5 theory — second-hand
through YLD); every integral weight-k level-5 form is a degree-5k
homogeneous polynomial in F₁, F₂ (their Eq. (14)); the S/T action on
(F₁, F₂) is their Eq. (13).

The mechanism, verified exactly in-sandbox:

1. **The Eq.-(13) action is 2̂ up to 20th-root scalars:** the S-matrix
   e^{iπ/10}·√(1/(√5φ))·[[φ,1],[1,−φ]] = ζ₂₀¹⁶·ρ_2̂(S) and the
   T-matrix diag(1, ω₅) = ζ₂₀¹²·ρ_2̂(T) — exact matrix identities.
   The scalars die on 5k-th symmetric powers (ζ^{80k} = ζ^{60k} = 1),
   so **M_k(Γ(5)) ≅ Sym^{5k}(2̂) as Γ₅′-representations**.
2. **Confirmation against the literature:** the exact decomposition of
   Sym^{5k}(2̂) (Chebyshev recursion h_n = χ·h_{n−1} − h_{n−2} per
   class, full 9-character table built and orthonormality-verified
   in-sandbox) reproduces YLD Table 1 at ALL six weights:
   k=1: 6̂; k=2: 3⊕3′⊕5; k=3: 4′⊕2·6̂; k=4: 1⊕3⊕3′⊕4⊕2·5;
   **k=5: 2̂⊕2̂′⊕4′⊕3·6̂** (first doublets); k=6: 1⊕2·3⊕2·3′⊕2·4⊕2·5.
3. **Where the doublets live (the McKay arithmetic):** the exact
   multiplicity generating functions in Sym^n(2̂), verified as
   polynomial-numerator identities to n = 75:
   - 2̂ : (t¹ + t¹¹ + t¹⁹ + t²⁹) / ((1−t¹²)(1−t²⁰))
   - 2̂′: (t⁷ + t¹³ + t¹⁷ + t²³) / ((1−t¹²)(1−t²⁰))
   The numerator exponents **partition the E₈ exponents
   {1,7,11,13,17,19,23,29}** (pairs summing to 30 = h(E₈)); the
   denominator degrees 12, 20 are the binary-icosahedral invariant
   degrees (McKay: 2I ↔ E₈). Occurrence sets: 2̂ at n ∈ {1,11,13,19,
   21,23,25,29,31,33,35,…}; 2̂′ at n ∈ {7,13,17,19,23,25,27,29,…}.
4. **The congruence that forces weight 5:** doublets appear at
   n ∈ {E₈-exponent} + 12ℤ≥0 + 20ℤ≥0; level 5 samples only n = 5k.
   Minimal solutions of n ≡ 0 (mod 5): for 2̂, 1 + 12r + 20s ≡ 0
   (mod 5) ⟺ r ≡ 2 (mod 5) ⇒ n = 1 + 2·12 = **25**; for 2̂′,
   13 + 12·1 = **25**. Both doublets first at n = 25 ⇒ **weight
   25/5 = 5** (computed first-occurrence: 25 for both).

So H129's "weight 5 = level 5 = conductor = disc(A₁)" has a mechanism
for its first equality: **the level (two weight-1/5 generators ⇒ 5k
homogeneity) meshed with the E₈ exponents mod the 2I invariant degrees
12, 20 forces the doublets to weight (1+2·12)/5 = 5.** This lands
directly on the banked McKay placement (B640: the hearing group is the
E₈-McKay shadow; B247–B261 two-ended theorem): the weight at which the
ear's doublet first materializes as a modular form is E₈-exponent
arithmetic.

## Task 3 — the assembled upstream statement

Sharpened claim (candidate-functor grade, per the prereg's positive
branch): **the framework derives the Γ₅′-doublet flavor representation
from the monodromy.** Concretely: ρ_hear = 2̂′ ∘ (mod-5 reduction) with
the stage-twist selecting the Galois partner 2̂ — the exact
representation-with-Galois-pair that the modular-flavor paradigm
postulates as input (its group choice from a catalog, its level, its
doublet assignment), obtained here as a theorem about the object's
hearing (B640/B644) + this cell's exact character isomorphism. φ sits
at the same structural locus on both sides (the S-transform mixing of
the R = −I doublets).

**The honest gap to a genuine functor:** this cell identifies the
REPRESENTATION exactly, and gives the weight-5 mechanism on the
literature's side; what is NOT yet derived is the framework-side
modular-form assignment — producing the weight-5 doublet forms
Y_2̂^(5)(τ) from the framework's own tower with the modulus τ playing
its literature role. Until then the upgrade is PLACEMENT → candidate
functor, not functor.

Gate-5 note: everything above is representation theory and modular-form
dimension arithmetic; no SM quantity appears anywhere.

## Verification hygiene

- Exact field ℚ(ζ₂₀) implemented from scratch (Fraction coefficients
  mod Φ₂₀, Gaussian-elimination inverses); self-tests: Φ₂₀(ζ) = 0,
  i² = −1, φ² = φ+1, (2cos π/10)² = √5φ, Galois ζ↦ζ³ sends √5 ↦ −√5.
- The banked ear table re-verified in-sandbox (Schur = 1, parity) and
  the literature characters computed from their matrices, not copied;
  the Table 10 rows then matched as a cross-check of the extraction.
- The full 9-character table rebuilt from 2̂ by exact tensor calculus
  (Sym powers + 2̂⊗2̂′), orthonormality verified; Σdim² = 120.
- Script correction disclosure: after the first run, one PRINT-side
  relation check ((ST)³ = −I, wrong for the paper's S-sign convention;
  the correct (ST)³ = +I now asserted and passing) and one vacuous
  assert (`… or True`, an MB12-class slip in a non-decisive guard)
  were fixed; no decisive number changed between runs. The final
  hashes above are of the corrected script and its rerun output.
- Verification is internal (owner + AI seats), per PROVENANCE.

## Sources (per GOVERNANCE §16 spirit: source + access date for every extracted fact)

- [YLD] C.-Y. Yao, X.-G. Liu, G.-J. Ding, "Fermion Masses and Mixing
  from Double Cover and Metaplectic Cover of A₅ Modular Group,"
  Phys. Rev. D 103, 095013 (2021), arXiv:2011.03501. PDF fetched and
  read 2026-07-17. Facts extracted: Eq. (2) S/T convention; Eq. (4)
  relations; Eqs. (5)–(6) Γ(5), Γ₅′ presentation; §2.1 dim = 5k+1;
  Eqs. (12)–(14) F₁/F₂ weight-1/5 pair and degree-5k structure;
  Eq. (13) S/T transformation of (F₁,F₂); Eq. (16) weight-1 sextet;
  Table 1 weight-by-irrep summary (k ≤ 6); Table 10 character table;
  Table 11 representation matrices; (A.11) conjugacy classes.
- T. Ibukiyama, "Modular forms of rational weights and modular
  varieties" — the weight-1/5 span theorem, cited SECOND-HAND as
  YLD's ref. [68] (not independently accessed).
- X.-G. Liu, G.-J. Ding, arXiv:1907.01488 (double covers Γ_N′,
  first Γ₅′ weight-1 construction) — identified at search level
  2026-07-17 as the framework paper; no facts extracted from it
  directly (all extractions above are from [YLD]).
- Search trail (2026-07-17): arXiv listings for Γ₅′/A₅′ modular flavor
  (incl. arXiv:2010.10159, arXiv:2206.14869) — context only.

Banked-side inputs: B640 (hearing group theorem), B644 (mod-5 shadow,
the corrected golden table + M3 adjudication), B642 (stage-twist
Galois partner), B660/S1 (the correspondence PLACEMENT), B663 (credit
adjudication), HINT_LEDGER H129.
