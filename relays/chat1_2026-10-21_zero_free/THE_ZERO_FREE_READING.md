# The zero-free reading: PF1 read on the weave's divisors (a READING, with one sealed run)

chat1, 2026-10-21. This is a reading, offered for the owner's ruling. One sealed run backs its facts:
- the rule `ZERO_FREE_RULE.md` (48e2105f4);
- the script `zero_free_checks.py` (57f38493a), with a launch fix (298224eb5) that only extracts two data files the
  SM seat's module reads at import (the first launch failed there, before any cell; its log is kept);
- the output `zero_free_checks_run.txt` and `.json` (808dd4aef).

Refereed read-only before commit (7ff595af0) and corrected; a follow-up commit (8793d4afa) applies the referee's
second pass. A lepton test built on it was sealed and launched before this file
was committed (§6). Nothing here lowers the count. 0 of 19.

## 0. In brief

- **W114 called the strong angle "bought".** In the record's frame, θ̄ = 0 at every τ costs one real condition per
  tuned sector. Its compatible quark fits carry the Standard Model's own count with θ̄ tuned.
- **That condition is the absence of a massless quark anywhere inside the weave.** This is W113's lemma (det Y = η^a·g,
  and g zero-free on H only if g = cΔⁿ), read physically. The run confirms the parts the reading uses:
  - every impossible sector (w ≡ 6 mod 12, w > 0) has a massless quark at τ = i, for every coupling;
  - with real coefficients (CP in the law), a generic tuned member has exactly one massless point, on a CP locus;
  - the one real condition sends that point to the cusp.
- **The reading, PF1-W.** On the weave, the law's holomorphic invariants cancel only at the end, the cusp.
  - The record has read PF1 this way once before: in the SM seat's ladder reading (a READING in its NOTE, level 7;
    B497, B1342), a factor of κ − 2 "that vanishes somewhere" is where "cancelling completes".
  - PF1-W applies the same reading to the mass determinants over the weave's states.
  - Under it, a quark sector's determinant is c·η^{6k}: it vanishes only where the records' torus degenerates.
- **What it would give, as candidates, post hoc, given the frame:**
  - **θ̄.** W114's tunings become forced. In the two exact assignments (11, 13), 10 numbers then carry 11 quark
    observables, and θ̄ ∈ {0, π} at every τ. That needs, besides PF1-W, the counterterm (W101's H-θ) and the swap in the
    law (GM5c, OPEN).
  - **The cusp's dressing.** A reason for the record's own "no zeros on the open surface": among W48's candidates only
    1/Δ is zero-free with trivial multiplier.
  - **The hierarchy.** It excludes the frames on record whose determinant vanishes at an interior τ (listed in §3.3),
    including the near-ω mechanism.
- **Prior art.** Feruglio, Marrone, Strumia and Titov (arXiv:2505.20395, 2025) assume the analogous condition, with
  zeros only at decompactification. Their determinant is Δ^m, in supersymmetry. They also fit the leptons at the
  quark-fixed τ. The record does not cite them.
- **Status.** A READING. It is not derived, and adopting it is the owner's call. Even adopted, θ̄ is a candidate for
  main to bank, not a prediction: θ̄ ≈ 0 was known. 0 of 19.
- **Where it collides with the seat's next arc.** W115's only predictive charged-lepton couplings are T⊗T at k = 3
  and mixed at k = 2. Both are impossible-class: they have a massless point at τ = i, so PF1-W forbids them. A W115
  success would count against PF1-W; a failure would be consistent with it, not evidence for it (§6).

## 1. What the record already had, and what the run confirms

- **On record (W113's lemma, the SM seat's).**
  - A sector's determinant is det Y = η^a·g, with g a level-one form of weight w = 3k − a/2.
  - With the counterterm N = 6K, θ̄ is constant over τ exactly when each sector's g is zero-free on H, that is
    g = cΔ^{w/12}. So w = 12n, at n real conditions.
  - The classes: automatic at w = 0; tuned at w = 12n, n ≥ 1; det ≡ 0 at w < 0 (T̄⊗T̄ at k = 1); impossible otherwise.
  - W114 fitted the tuned layer. No assignment with a degree of freedom passes. Assignments 11, 13 and 16 fit exactly,
    and 14 reaches χ² 2.55 at a = 0.10 (9.59 at a = 0.05, and its J is 3.5 × 10⁻⁶ against the measured 3.1 × 10⁻⁵).
- **What the run confirms** (every cell as predicted; the SM seat's code at c9f001d9d, imported unchanged and
  hash-checked; 50 digits). Most of this re-checks the record or is textbook; what it adds is the physical reading.

| cell | result | status |
| --- | --- | --- |
| Z0 | the 16 (type, k) reproduce W113's dimensions and classes; every w lies in 6ℤ, so the impossible class is w ≡ 6 (mod 12) with w > 0 | re-check |
| Z1 | every impossible sector has a massless quark at τ = i, for every coupling: r(i) ≤ 5.2 × 10⁻⁵¹ over 70 members of the seven sectors, while r ≥ 0.02 at ω and r ≥ 4.2 × 10⁻⁴ at three generic τ (g carries E₆, which vanishes at i) | W113 F2 plus E₆(i) = 0, read as massless |
| Z2 | a generic tuned member: G = det Y/η^{6k} = αj + β to 2 × 10⁻⁴⁷, with α and β real, so j₀ = −β/α is real and the zero lies on a CP locus; r(τ₀) ≤ 6 × 10⁻⁴⁹ there | the CP-locus placement follows from W113 C1 (real coefficients) |
| Z3 | tuned members are zero-free: G constant to 2.1 × 10⁻⁴² across six τ; the massless measure ≥ 1.1 × 10⁻¹⁰ (≥ 1.2 × 10⁻⁴ at i, ≥ 2.6 × 10⁻³ at ω); no rank-two root among 40 | re-check of W113 T1, W114 U1 |
| Z4 | \|E₄(ω)\| = 7 × 10⁻⁵¹; the Niemeier dressings j − 720 + N vanish inside F̄ (Leech at −0.235 + 0.972i, D₂₄⁺ at −½ + 1.090i); η^c has trivial multiplier among c = 8, 12, 16, 24 only at c = 24 | textbook |
| R1 | ψ = (Im τ)^{1/2}\|η\|² is largest on F̄ at ω (0.59645), with ψ(i) = 0.59017 | a known theorem (Osgood–Phillips–Sarnak) |
| R2 | the leptons' feasibility (§6) | read-out |

- **The physical reading of W113's classes.**
  - **Impossible:** a massless quark at τ = i, whatever the coupling.
  - **Tuned:** with real coefficients, one massless point on a CP locus for a generic coupling. The 40 sampled points
    have Im τ₀ from 0.90 to 2.06, but j₀ ranges over all of ℝ. The one real condition (α → 0) sends the point to the
    cusp.
  - **Automatic, or tuned on the variety:** no massless point anywhere inside H.
  - With complex coefficients (no CP in the law), the tuned member's zero would sit at a generic point instead.

## 2. The reading: PF1-W

- **The statement.** On the weave, the law's holomorphic invariants have their zeros and poles only at the end, the
  cusp τ → i∞. Here those invariants are the mass determinants as functions of τ, and the cusp's dressing.
- **How it reads PF1.** It rests on two identifications, each named.
  1. **"A zero is cancellation completed."**
     - PF1 says existence is what remains when cancelling to nothing cannot complete.
     - The record has read a factor that vanishes somewhere as cancelling completing: at ladder level 7,
       non-automorphisms multiply κ − 2 by such a factor. That is the SM seat's ladder reading, a READING, not a
       banked result.
     - PF1-W extends this from κ to the law's determinants. A massless quark still exists, so this is an
       identification for that invariant, not a theorem.
  2. **"The end is where a record cancels."**
     - The record ties cancelling completing to κ = 2, "the locus where the cancellation completes" (GENESIS's PF1
       note, v1.1). The fibre's κ is "−2 at the root, which is the parabolic cusp" (GENESIS; E72).
     - PF1-W instead uses the weave's surface, read as parametrising the records' torus (W19's reading). There the end
       τ → i∞ is where the torus degenerates and the discriminant Δ vanishes.
     - Identifying that end with "a record cancels" is a second identification.
- **What it needs.**
  - GENESIS §3's premise, "all legal states are physically realised together" (NOT DERIVED), so that a zero at any τ
    counts.
  - The word "holomorphic". J vanishes on the CP loci whenever CP is in the law (W113 C3), so the reading cannot cover
    every invariant. The restriction was chosen to avoid that (§5, point 10).
  - The trivial multiplier, for §3.2, as the record's own definition of a source requires (the reading before W48,
    point 1).
- **What it is not.** It is not derived, and not adopted. Under it, a sector's determinant is c·η^{6k}, and the
  product of the two quark sectors' determinants is c·η^{6K}, with K = k_u + k_d. The product is a power of the
  discriminant only up to a multiplier: K/4 is not an integer in any of W114's four compatible assignments (K = 11, 11,
  10, 14).

## 3. What PF1-W would give, on the record (candidates, post hoc, given the frame)

### 3.1 θ̄

- **The count.** Under PF1-W the tuned layer is forced. Counting with W114's rule (dimension − 1 − tuned), plus τ and
  both scales:

| # | up / down | free numbers | quark observables with θ̄ | note |
| --- | --- | --- | --- | --- |
| 11 | mixed 4 / T̄⊗T̄ 7 | 2 + 4 + 2 + 2 = 10 | 11 | exact fit |
| 13 | T̄⊗T̄ 7 / mixed 4 | 4 + 2 + 2 + 2 = 10 | 11 | exact fit |
| 14 | T̄⊗T̄ 3 / T̄⊗T̄ 7 | 2 + 4 + 2 + 2 = 10 | 11 | χ² ≤ 3.84 at a = 0.10 only (9.59 at 0.05); its J misses by a factor of about 9, and W114's χ² does not include J |
| 16 | T̄⊗T̄ 7 / T̄⊗T̄ 7 | 4 + 4 + 2 + 2 = 12 | 11 | nothing derived |

- **So in 11 and 13 the frame would derive one number, θ̄, and predict nothing else.** J at the exact fits is what the
  fitted magnitudes imply (W114).
- **The conditions.**
  - PF1-W makes each g = cΔ^{w/12}.
  - θ̄ is then constant only with the counterterm N = 6K (W101's H-θ). Without it θ̄ = −arg c − 6K·arg η, which
    varies (W113 C2).
  - θ̄ ∈ {0, π} needs real coefficients, that is the swap in the law (GM5c, OPEN).
  - The bit is one sector's sign, chosen by the data.
  - The frame's hypotheses H-T, H-W and H-H hold, at tree level only.
  - The assignment is chosen by the quark data.
  - The weave premise (NOT DERIVED) is needed.
- **The status.** Under all of these, θ̄ would be a candidate for main to bank, post hoc, not a prediction. W113's own
  rule says the count stays 0 until main banks a value, and the goal page counts only "a prediction that is confirmed
  and was not fitted". 0 of 19.
- **The price** (B1670 prices "θ̄ = 0 by a mechanism" as HOLDS, by construction).
  - B1670's routes are a new U(1) and particle; spontaneous CP with vector-like quarks; or CP with SUSY, reducible
    representations and chosen weights.
  - The frame keeps CP, reducible representations and data-chosen weights. It trades SUSY for tree level, so loops
    can regenerate θ̄.
  - It adds H-θ, GM5c, the weave premise, and PF1-W, either as a reading of PF1 or as a new row.

### 3.2 The cusp's dressing (FK10, v1.39)

- **The record's position.**
  - GENESIS v1.39 adopts one unit of end data at the cusp as a tagged working postulate ("given the unit").
  - The reading before W48 (point 4) already says the unit's form, weight −12 with a simple pole at the cusp and no
    zeros on the open surface, is 1/Δ.
- **What PF1-W adds is a reason for that "no zeros on the open surface",** which excludes W48's other dressings:
  - E₄/Δ (count 2) and E₄²/Δ (count 1, the heterotic left-movers) vanish at ω, where E₈'s theta function E₄ does;
  - every Niemeier dressing (count 0) vanishes inside H;
  - 1/η⁸, 1/η¹² and 1/η¹⁶ are zero-free but have non-trivial multipliers;
  - only 1/Δ survives.
- **The general statement.**
  - A dressing zero-free on H with trivial multiplier is g = cΔ^{−n}, so w = −12n.
  - At conditions 0 and L₆ the count is ∓3n (W48 S1), whole triplets. At V2 and V4 it is ∓n.
  - This carries W48's scope: a dictionary beyond Λ, and the simplest dressing.
- **What it does not do.** It does not supply the unit's existence (v1.39's postulate) or its number n.

### 3.3 Where hierarchy can come from

- **PF1-W excludes the listed frames whose determinant vanishes at an interior τ, or identically:**
  - W63 and B1644/B1645: one generation massless by Jacobi.
  - W65 and W67: the second generation massless at ω.
  - W68 and W69, and W112's menu built on them: the δ² : δ : 1 hierarchy near ω, which needs masses that vanish at ω.
- **The data's verdicts on them,** specifically:
  - a massless up quark is excluded at 31σ (B1670);
  - W69's best χ² is 100;
  - W112 is no better than chance (p = 0.139);
  - a second generation massless at ω (W65, W67) contradicts the measured c, s, μ masses at whatever τ the data
    select, and the frames select ω itself.
- **Out of PF1-W's scope:** B1656/W89 (the electron's zero, in the Wilson-line variable with non-holomorphic twisted
  norms, "at this order") and W61 (L² overlaps at one state). They are not claimed.
- **What remains.** PF1-W excludes the near-ω form of the goal page's "flesh". It does not exclude a departure from
  the cusp, or a light quark from coefficients near the rank-two members (det ≡ 0, W113 T1).
  - Of W114's compatible points, 13 and 16 sit at Im τ 1.53 and 1.78. Point 11 sits 0.10 from i.

### 3.4 τ (read-out, not a selection)

- Under PF1-W, a sector's Kähler-normalised |det| is |c|·2^{3k/2}·ψ^{3k}. ψ is largest at ω (R1; Osgood–Phillips–
  Sarnak), the record's tagged state input.
- But CP holds at ω, so J = 0 there, and the compatible fits sit elsewhere.
- So "the state that maximises the masses' product" is ω, and the data are not there. A tension to record.

## 4. Prior art

- **Feruglio, Marrone, Strumia and Titov, arXiv:2505.20395 (2025).**
  - Their abstract: the extension "requires assuming that singularities and zeroes only appear at special points, such
    as decompactification limits".
  - Their quark masses never vanish except at τ = i∞, so det Y ∝ Δ^m, with the weight a multiple of 12. They add a
    dilaton gauge kinetic function, in supersymmetry, which cancels its phase.
  - Their coefficients are adjusted to reach it (nine per matrix), and the fit has as many parameters as observables
    (χ² ≈ 0). That is W114's situation, by a different route: the frame's determinant is c·η^{6K}, with a Dedekind
    counterterm.
  - They give the zeros case no derivation ("perhaps realised in some string compactifications"); for the
    singularities they invoke the distance conjecture.
  - They also fit the leptons at the quark-fixed τ. The minimal choice wanted a different τ, so they needed an extra
    parameter, and they predicted δ_PMNS ≈ 0.94π, m₁ ≈ 10 meV and Σm ≈ 74 meV. Their lepton fit was itself six
    constants for six observables, with δ_PMNS its only prediction. (These details come from a summarised fetch of the
    paper's HTML v1, not a full reading.) That is direct prior art for §6.
- **The record's citations.** The record does not cite the paper. Searched at main 3650f92b0, the audit lane
  17cdad33a and the SM seat 5a9914425 (2026-10-21).
- **The weight-zero route.** Feruglio, Strumia and Titov (arXiv:2305.08908, 2023) and Feruglio, Parriciatu, Strumia
  and Titov (arXiv:2406.01689, 2024) reach a constant determinant through cancelling weights. B1670 and B1674 cite the
  2024 paper.
- **The mathematics is textbook:** the valence formula, the uniqueness of a zero-free level-one form as cΔⁿ, Δ as the
  discriminant of the elliptic curve, and the maximum of ψ at ω.

## 5. A hostile read (each point answered or conceded)

1. **"It is a pun on PF1."** It rests on two named identifications (§2). The record already makes the first once
   (ladder level 7). It stays a reading.
2. **"It was found by looking at W114's tuning, so θ̄ is post hoc."** Conceded. §3.2 was foreseen in the rule (Z4),
   and §3.3 reads record results. Only a test with an outcome not known in advance (§6) can move it.
3. **"The frame does the work."** Largely conceded. PF1-W alone makes each g a power of Δ. θ̄ constant needs H-θ, and
   θ̄ ∈ {0, π} needs GM5c. What PF1-W changes is the status of the two tunings, from chosen to forced.
4. **"Zero-dof fits predict nothing."** Agreed. θ̄ would become a candidate; the count moves only if main banks it.
5. **"Discrete choices: hand, weights, assignment, the sign bit."** Agreed, and chosen by data. θ̄ = π is also
   CP-conserving. Whether the data exclude it independently is not checked here.
6. **"Tree level."** Agreed. Without supersymmetry, loops can regenerate θ̄. That is outside the frame (the goal
   page's third candidate).
7. **"It excludes arcs proved in their frames."** It excludes their frames as the principle's, not their mathematics.
   The data had already refuted them (§3.3).
8. **"The multiplier does part of the work in §3.2."** Conceded.
9. **"PF1-W is a new postulate, so the price does not fall."** That is the owner's question (§3.1, the price).
10. **"'Holomorphic' was chosen to dodge J's zeros on the CP loci."** Conceded. It is the restriction that keeps the
    reading consistent with CP in the law, and it was chosen for that.

## 6. The test that could make it predict, and the collision with W115

- **R2, at a fixed τ** (chat1's assumption A-W: the Weinberg coupling lies in the symmetric part of the (s_L, s_L)
  space).
  - Under PF1-W only w ∈ {0, 12} is admissible up to weight 7. Higher multiples of 12 also admit zero-free members.
  - Excluding the degenerate charged sector (mixed at k = 0) and B1636's sum-rule sector (T⊗T at k = 1), ten
    (charged, Weinberg) pairs remain, with 2 to 6 free numbers each.
  - Every admissible charged sector has at least two free numbers. So PF1-W gives no prediction of the nineteen's own
    lepton ratios at fixed τ. Any prediction must come from the neutrinos, which are outside the nineteen.
- **The sealed test**, `LEPTON_TEST_RULE.md` (2c1e16790); script `lepton_test.py` (2f0379e61); launched before this
  file was committed, output not yet read.
  - Six observables: two charged ratios, three angles and the Δm² ratio; δ is a read-out.
  - Nine pairs have dof 1 to 4; T̄⊗T̄ 7t with symmetric T̄⊗T̄ 7t has dof 0, compatibility only.
  - **A correction to the rule's "Why",** dated here: it says every pair is over-determined with "1 to 5 predictions
    each". That counted seven observables with δ. Under the rule's own six, it is 0 to 4, as just stated. The cells are
    unaffected.
  - FMST 2025's lepton fit at the quark-fixed τ is prior art for this test (§4).
- **W115, the SM seat's next arc** (the owner's choice after W114; rule 5a9914425, committed 11:10:55 UTC).
  - It was not seen before chat1's lepton rule was written: a local fetch at 11:11:01 UTC still returned c9f001d9d;
    chat1's rule was committed at 11:50:17 UTC and its script at 11:50:24 UTC; the local tracking ref first reached
    5a9914425 at 12:00:45 UTC.
  - It tests the charged leptons alone, at the same τ, with the only couplings that leave a free number to spare: T⊗T
    at k = 3 and mixed at k = 2.
  - Both are impossible-class (w = 6): each has a massless point at τ = i for every coupling (Z1). PF1-W forbids them.
  - So a W115 success (p < 0.05 at one degree of freedom, for a coupling PF1-W forbids) would count against PF1-W. A
    W115 failure would be consistent with PF1-W, not evidence for it, since W115's own priors expected failure (80%,
    75%).
  - The two outcomes are not logically exclusive with chat1's test passing, since PF1-W's allowed charged sectors
    always fit the two charged ratios. The runs are complementary, not a decision between them.
  - Assignment 11's τ sits 0.10 from i, where W115's couplings have their forced zero. A light electron there would be
    exactly the interior-zero mechanism PF1-W forbids, which sharpens the collision.

## 7. What this does not do

- It does not derive PF1-W, and it does not adopt it.
- It does not touch W114's numbers.
- It reports no lepton result.
- 0 of 19.

chat1, 2026-10-21. 0 of 19.
