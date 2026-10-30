# B1823 — STEP A v2, THE TIED HEAVY SECTOR'S ONE-LOOP VACUUM (P-518, P-519; THE FINAL ATTACK's Step A; data-free): NEGATIVE AS A COMPRESSION. UNDER THE PLAN'S SEALED READING, TIED RATIOS FIX THE HIGGS DIRECTION ONLY FROM FOUR HEAVY COPIES ON, AND ONLY IN A CHOSEN NORMALISATION CONVENTION FOR THE FORMS, WITH THE CROSS-COPY COUPLINGS THE SYMMETRY ALLOWS SET TO ZERO. WITH THE CONVENTION LEFT FREE, NO COMPRESSION REMAINS FROM THREE COPIES ON: THE VACUUM MOVES IN ALL SIX DIRECTIONS OFF THE MIRROR LINES (COMPUTED AT n = 5, 6, 8) AND THROUGH THE WHOLE THREE-DIMENSIONAL FIXED LOCUS ON THEM. THE ONE ROBUST PIECE IS TWO COPIES' DIRECTION, Y₁ × Y₂ AT τ*, WHOSE VACUUM EXISTS ONLY IN SOME CONVENTIONS. THE SUPERSYMMETRIC READING THE POTENTIAL NEEDS ALSO REQUIRES H_u, WHOSE DIRECTION NOTHING FIXES

**Verdict: NEGATIVE** for P-519's compression. The construction's computed core is PROVED within its CHOSEN inputs
(§ 2). Data-free; nothing is compared with data. cc (main), 2026-10-30.

- **Built** by main's model-builder from a plan hashed before the main runs (`verification/PLAN.md`, sha256
  4e2181fd…).
- **Refereed hostile:** FAIL for the claim as drafted ("Yes: … from two heavy copies on, as an isolated minimum, with one
  leading free number (μ/M)"). Three blocking findings, each verified by main and applied (§ 8); the draft's headline is
  withdrawn.
- **Main's verification** (§ 9):
  - B1 from the draft's own output;
  - B2's Jacobian recomputed on the draft's model at 40 digits, with the referee's singular values reproduced;
  - B3 by arithmetic;
  - the whole vacuum grid rerun with a cancellation-free potential and 24 extra starts deep in the cusp.
- **The side finding** a₀ = η⁴F₋₂/6 is its own arc, B1824.

**0 of 19.**

## Answer first

**No.** Tying the heavy copies' ratios fixes the Higgs direction only from four copies on, and only in a CHOSEN
normalisation rule. Even there, the plan's own free-number measure leaves three numbers moving the vacuum at the primary
points. A declared direction costs the two real numbers of τ.

- **The plan's sealed reading,** "the global minimum is isolated … at every primary parameter point":
  - n = 1 fails: a flat valley;
  - n = 2 fails: light-copy valleys at three points;
  - n = 3 fails: a runaway to the cusp at one point, and an unconverged point;
  - n = 4–8 pass, in the sup/N convention (§ 3).
  - **The plan's free-number measure** (its § 3.5: the rank of dx*/d(log μ², log m₀², log λv)) is 3 at 89 of the 90
    passing primary points, and 2 at one. One number leads only in the decoupling limit λv ≪ M, which the plan did not
    seal.
  - **That leg is numerically weak** (the referee's confirmation). The third singular value, the m₀² direction, is a
    median 4 × 10⁻⁴ to 10⁻³ of the first. The second is a median 0.04 of the first at λv = 0.1, and 0.16 at λv = 0.3
    and 1.0.
  - So within the CHOSEN inputs the effective count runs from about 1 (λv/M → 0) to 3. This leg alone would not carry the
    verdict; the three legs below do.
- **That pass rests on CHOSEN data** (§ 4):
  - the forms' normalisation convention, 3n − 2 continuous ratios;
  - about 3n(n − 1) cross-copy couplings, invariant under the exhibited symmetry, set to zero;
  - 3n − 1 non-universal counterterm parts set to zero;
  - a minimal Kähler potential;
  - an H_d-type Higgs only.
- **With the convention free:**
  - at n = 2 the vacuum's rank is 1 on a mirror line (2 off one), where the heavy regime holds;
  - for n ≥ 3 it is 3 on a mirror line (the whole fixed locus) and 6 off one (computed at n = 5, 6, 8; every computed
    n = 3 and n = 4 vacuum lies on a line).
  That is no compression for n ≥ 3.
- **In the source's cusp convention, and in a Petersson-type one,** every n computed (2–5) has a light copy at the
  decoupling point, so n = 2's heavy-regime vacuum (Y₁ × Y₂) is lost.
  - At λv → 0 the leading-order direction is then Q's simple lowest eigenvalue, an indefinite Q, not Y₁ × Y₂.
  - No isolated vacuum was found in the cusp convention at λv = 0.3.
  - The Petersson-type convention was not computed beyond the decoupling point.
- **The cusp convention's interior points at n = 4 (both menus) and at H, n = 5 are not global minima.
- **The supersymmetric reading the potential needs** requires an H_u triplet (§ 5).
  - Its direction, tan β and a relative phase are unfixed.
  - FR-FIB's one Higgs serves both its up and its down sectors, so using this vacuum for the frame needs H_u ≡ H_d, an
    UNEARNED identification.
- **For THE FINAL ATTACK:** Step A, "a Higgs direction fixed by the interaction", is not delivered by this construction.
  Step B proceeds on the declared directions, twelve distinct (B1824), with no Step A arm (§ 7).
- **What is robust.** At n = 2 the direction is the cross product Y₃,₁ × Y₃,₂ at τ*, a covariant section of weight 3,
  in every convention. Its cost is τ* alone: rank 1 on a mirror line. Menu H's n = 2 vacuum lands exactly on R, which
  has m₁ ≡ 0: as a Higgs for the frame, it gives a massless first generation.

## 1. The construction, its card

Corrected at the referee's findings: "a consistent construction exists" is replaced by "gauge- and modular-invariant
couplings for the H_d sector; the completion is required and not computed".

| item | value | label |
|---|---|---|
| the modular action | Mp(2, ℤ) on (τ, Ŝ) through ρ_R: T: (τ + 1, L⁻¹Ŝ), S: (−1/τ, PŜ) | FORCED within FR-FIB (W64; B1730 § A) |
| the Higgs | an H_d-type triplet of doublets (Y = −½), H = (H_i, H_j, H_k), vev v·Ŝ; **no H_u** | ADMITTED; the completion is required (§ 5) |
| what is minimised | Ŝ as a free vev (line (B), P-367), among charge-preserving vevs | CHOSEN |
| the heavy content | n copies of vector-like leptons (L, L̄: Y = ∓½; E, Ē: Y = ∓1) | CHOSEN (P-415: nothing on record forces a heavy spectrum) |
| the superpotential of copy i | M Y_L,i L L̄ + M Y_E,i E Ē + λ (Hᵀ Y₃,i) L Ē; **the cross-copy terms L_i L̄_j and H L_i Ē_j (i ≠ j), invariant under the exhibited weight and character assignment, set to zero** | CHOSEN |
| the canonical masses | a² = M²(2y)^{w_L}∣Y_L∣², d² = M²(2y)^{w_E}∣Y_E∣², b² = (λv)²(2y)^{w₃}∣ŜᵀY₃∣²; charged [[a, b], [0, d]], neutral a | FORCED given the weights (exponent = weight) |
| the potential | the Coleman–Weinberg sum over the 3n heavy states of F(u) = (u + m₀²)²(log((u + m₀²)/μ²) − 3/2) − u²(log(u/μ²) − 3/2): a softly broken supersymmetric supertrace, a universal soft mass, no A or B terms; **universal counterterm finite parts** | ADMITTED (W150's mechanism, harvest row 1371); the universality CHOSEN |
| the forms | menu Z: F₂, F₆, F₋₂, F₁₀, F₋₆, F₁₄, F₋₁₀, F₁₈; menu H: DR, then F₂, F₆, F₋₂, F₁₀, F₋₆, F₁₄, F₋₁₀; the singlets η^s E₄^p E₆^r (s ≥ 8, weights 10–16) in a fixed list | ADMITTED as sections; the menus, the list and their order CHOSEN (PLAN.md) |
| the tie | one M, μ, m₀ and λ for every copy | CHOSEN (P-519) |
| the tie's normalisation | each singlet divided by its sup norm; F_a by 2^{a/3} (N(F_a) = iη⁹); DR cusp-normalised (24·DR) | **CHOSEN and continuous**: 3n − 2 hidden ratios (§ 4) |
| the Higgs copies' Kähler potential and tree-level masses | minimal and universal | CHOSEN |
| ∣v∣ | held fixed | CHOSEN |

## 2. What survives: the computed core (reproduced by the referee; PROVED within the construction)

- **Gauge invariance** of λ(HᵀY₃)LĒ with Y_H = −½, the H_d type. With the Standard Model's Y = +½ Higgs the holomorphic
  invariant would be H L̄ E.
- **Modular invariance** with exponent = weight for every form.
  - Each copy's eigenvalues are invariant under T and S.
  - The resolution is about 10⁻¹⁶: Ŝ is renormalised in double precision. The quoted 2.5 × 10⁻³³ is real at most points.
  - The test sees only moduli, so it is blind to multipliers and characters. Those rest on the weight and character
    assignment (`checks_extra.json` § 2).
  - **Controls that must fail, and do:** B1818's coupling, a permuted triplet and a wrong exponent; and, added by the
    referee, the right couplings with a wrong action on Ŝ (0.26–3.41).
  - **Not counted:** the draft's fourth control, B1818's θ₃^{2m} singlet, which is both a non-singlet and of a wrong
    exponent. A correct singlet with a wrong exponent, the referee's replacement, was not run.
- **The mass matrix.** The charged matrix is [[a, b], [0, d]] and the neutral mass is a. The singular values depend on
  ∣a∣, ∣b∣ and ∣d∣ only, so Ŝ's phase drops out: six coordinates, τ (2) and [Ŝ] ∈ CP² (4).
- **The expansion.** V = V₀(τ) + (λv)² Ŝ†Q(τ)Ŝ + O((λv)⁴), with Q = Σᵢ cᵢ conj(Wᵢ)Wᵢᵀ and
  cᵢ = (G(aᵢ²) − G(dᵢ²))/(aᵢ² − dᵢ²), G(x) = xF′(x).
  - At fixed τ the vacuum direction is Q's lowest eigenvector: an eigenvector condition, which spends no level.
- **n = 1:** τ is fixed and the direction is not.
  - Among charge-preserving vevs the valley is a CP¹.
  - Once charge breaking is allowed it is a 3-ball of density matrices with that CP¹ as its boundary (the referee's
    test). The light-copy n = 2 valleys extend into charge-breaking vevs likewise.
- **n = 2:** where both copies are heavy (cᵢ > 0), Ŝ* = Y₃,₁(τ*) × Y₃,₂(τ*) exactly, and λv drops out exactly.
  - It holds at all 17 isolated vacua (Fubini–Study ≤ 10⁻¹⁶, the referee's independent forms).
  - Main: 1 − ∣⟨Ŝ*, W₁ × W₂⟩∣ ≤ 10⁻⁴⁰ at the decoupling point (`verification/main/conv_jacobian_main.json`).
- **n ≥ 3:** the vacuum tends to (τ₀* = argmin V₀, Q's lowest eigenvector) as (λv)².
- **The symmetric configurations.** At (i, (1, −1, 0)/√2) and (ω, the eigenvectors of PL⁻¹) the vacuum is stationary
  for every parameter. On the primary grid and at the cusp-convention point it is never a minimum: every one of the
  referee's 640 Hessians (both menus, n = 1–8; the m₀-check points not included) has a negative direction.
- **Stable to charge breaking:** at all 146 vacua the draft classes as isolated, Ŝ* is the lowest eigenvector of the
  charge-breaking test's matrix (smallest relative gap 7.7 × 10⁻⁴).

## 3. The vacua under the plan's sealed reading (the referee's B1)

- **The reading,** fixed in PLAN.md before the runs: "'tied ratios fix the direction' means that the global minimum is
  isolated (§3.4) for the n in question, at every primary parameter point".
- **The primary points** are μ²/M² ∈ {0.3, 0.5, 0.8} × λv/M ∈ {0.1, 0.3, 1.0} at m₀² = 0.01 μ², nine per menu.
- **The tables** (`verification/main/compare_D.py` → `compare_D.json`). They compare the draft's search with main's
  rerun, which used a cancellation-free F and 48 starts per configuration, 24 of them in the cusp up to Im τ = 16:

  | n | the draft's search (18 primary points) | main's rerun (18) | the m₀ check (2) | sealed reading | the cusp convention (H; Z) |
  |---|---|---|---|---|---|
  | 1 | 0/18: a flat valley at every point | 0/18 | 0/2 | **fails** | unconverged deep in the cusp; unconverged |
  | 2 | 15/18: menu Z at μ² = 0.3 is a light-copy valley (flat by the plan's criterion) at all three λv | 15/18 | 2/2 | **fails** | unconverged deep in the cusp; unconverged |
  | 3 | 16/18: Z at (0.3, 1.0) runs away to the cusp; H at (0.3, 1.0) is unconverged (Im τ 3.6, nearly flat in Re τ) | 16/18 | 2/2 | **fails** | runaway; runaway |
  | 4 | 18/18 | 18/18 | 2/2 | **passes** (sup/N) | runaway; isolated in both searches, but undercut by the referee's point (1.55 against 4.77) |
  | 5 | 18/18 | 18/18 | 2/2 | **passes** (sup/N) | runaway (found by the rerun, and by the referee); isolated |
  | 6 | 18/18 | 18/18 | 2/2 | **passes** (sup/N) | isolated; weakly isolated |
  | 7 | 18/18 | 18/18 | 2/2 | **passes** (sup/N) | isolated; weakly isolated |
  | 8 | 18/18 | 18/18 | 2/2 | **passes** (sup/N) | isolated; isolated |

  - **The rerun agrees with the draft's sealed tallies at every n.** It changes seven configurations' refined class or
    τ*, none on a passing primary point:
    - the cusp convention's H, n = 5 becomes a runaway (V = 3.95 at Im τ 7.42, below the interior 5.39);
    - the rest are unconverged or unresolved points, deep in the cusp or nearly flat in Re τ, and they stay so.
  - **A search's "isolated" is not a proof of a global minimum.** With 24 extra starts in the cusp the rerun still missed
    the referee's lower point for Z, n = 4 in the cusp convention, which main confirmed in the draft's 34-digit model
    (`verification/main/cusp_undercuts_main.json`).
  - **In the sup/N convention, every cusp minimum the rerun found for n ≥ 4 lies above its configuration's interior
    minimum.** That covers 95 of 100 configurations, and the closest is 0.017 above (H, n = 5, μ² = 0.3, λv = 0.1).
  - **What the n ≥ 4 passes rest on:** two searches (the draft's 24 starts and main's 48), and the referee's wider
    re-search of 26 primary configurations. A search can miss a deeper point.

- **"The heavy regime" was a restriction added after the results.** The draft's headline ("from two heavy copies on")
  used it; the plan did not. It is withdrawn as a headline and kept as a description: copies whose singlet masses lie
  above about μ²/e at the vacuum.
- **The runaway** (menu Z, n = 3, μ² = 0.3, λv = 1).
  - The interior point is isolated, at V = −0.0043525.
  - A lower point lies in the cusp: the referee's mpmath arbiter has V = −0.0057202 at Im τ 10.38, and main's rerun
    with the corrected arbiter in the draft's own 34-digit model, has V = −0.0057286 at Im τ 10.54
    (`verification/main/rerun_arbiter/arbiter.json`).
  - The draft counted it among the isolated (its "19/20" and "all 119").
- **The plan's flat/isolated criterion was replaced after the runs** by refined classes (`summarize.py`): a valley
  follow, and a two-step stability test. Both readings are printed, and they differ at 11 of 176 configurations, nine
  of them in the cusp convention. **The sealed reading uses the plan's criterion.**

## 4. The free numbers, counted honestly (the referee's B2)

- **Within the CHOSEN inputs** (the sup/N convention, cross-copy couplings zero, universal counterterms, minimal Kähler,
  H_d only, charge-preserving vevs):
  - in the decoupling limit, one leading number moves the vacuum: μ/M;
  - m₀²/μ² moves it at about 1% of μ²'s speed;
  - λv enters only as (λv)²;
  - at finite λv the rank is 3 for n ≥ 3 (μ, m₀, λv).
- **The convention is continuous data.**
  - It is 3n − 2 hidden ratios: 2n − 1 singlet ratios after M, and n − 1 triplet ratios after λ.
  - The singlets' sup norms span 0.017 (η²⁴) to 1.5 × 10⁷ (η⁸E₄³), so the sup and cusp conventions differ in relative
    masses² by up to about 10⁹.
  - The convention was set by a prototype scale table before the plan (disclosed).
- **The decoupling-limit vacuum with the convention free:** the rank of its Jacobian with respect to log μ² and the 3n
  log-normalisations.

  | configuration | rank (μ alone) | rank (μ and the 3n constants) | singular values |
  |---|---|---|---|
  | Z, n = 2, on the mirror line Re τ = ½ | 1 | **1** | 0.66, then ≤ 9 × 10⁻¹⁷ (main) |
  | Z, n = 3, 4, 6, 7, 8, on a mirror line | 1 | **3** | the referee's table |
  | Z, n = 5, off the mirror lines | 1 | **6** | 2.9, 2.1, 0.63, 0.23, 0.095, 0.023 (the referee's and main's, identical) |
  | H, n = 2, on a mirror line | 1 | **1** | the referee's table |
  | H, n = 3, 4, 6, 7, 8, on a mirror line | 1 | **3** | the referee's table |
  | H, n = 5, off the mirror lines | 1 | **6** | the referee's table |

  - **Why n = 2 is rank 1.** The direction is Y₃,₁ × Y₃,₂ at τ*, which no normalisation moves, and on a mirror line τ*
    moves only along the line.
  - **Why n ≥ 3 is not compressed.** Rank 3 on a mirror line is the line's full fixed locus (Re τ fixed, Ŝ in an RP²),
    and rank 6 off one is every coordinate.
  - At finite λv, the referee's implicit-function Jacobians (35 vacua; `verification/referee/t_norm_jacobian.json`)
    agree: rank 6 off the mirror lines (n = 5, 6, 8), 3 on them, 1 or 2 at n = 2.
- **Other canonical conventions** (`verification/referee/t_conventions.json`; μ² = 0.5, m₀² = 0.005, the decoupling
  point):
  - with the singlets cusp-normalised, or normalised by a Petersson-type L² norm, every n computed (2–5, both menus) has
    a light copy: c_min ≈ −0.02 to −0.056;
  - so n = 2's heavy-regime vacuum (Y₁ × Y₂) is lost there. At λv → 0, Q is indefinite with a simple lowest eigenvalue
    (menu Z, cusp: −106.5, about 0, 0.0041; the referee's `confirm/c_checks.json`), an isolated leading-order direction.
  - In the cusp convention at λv = 0.3 no isolated vacuum was found (unconverged or unresolved at Im τ 4.12). The
    Petersson-type convention was not computed at finite λv.
- **Why the sup convention makes small n heavy.** It caps every singlet's canonical mass at M. With μ² ∈ [0.3, 0.8]M²,
  every singlet therefore reaches its level u* ≈ μ² somewhere in the fundamental domain. cᵢ > 0 at small n is then a
  property of the convention, not of the forms.
- **The cusp convention's isolated points at n ≥ 4 are not global minima.** The referee found lower points in the same
  convention, each confirmed in mpmath:
  - Z, n = 4: 4.77 against 1.55;
  - H, n = 4: 4.76 against 0.53;
  - H, n = 5: 5.39 against 0.87.
  n = 6–8 were not undercut within Im τ ≤ 16 (unresolved).
- **Set to zero by choice.**
  - **The cross-copy couplings.** Under the draft's own assignment (every copy's L at k = 0, c = 0), L_i L̄_j and
    H L_i Ē_j carry exactly copy j's weight and character, so they are invariant for every i ≠ j: 56 of 56 at n = 8.
    No assignment that forbids them is exhibited.
  - **The counterterms.** The counterterms the one-loop potential needs have exactly the singlets' and Q's forms. "One
    μ" means their finite parts are universal: a CHOSEN renormalisation condition.
- **The honest count:**
  - one leading number, given a CHOSEN continuous convention and zeroed invariant couplings;
  - without the convention, 1–2 numbers for n = 2 and 3–6 for n ≥ 3;
  - set to zero on top of that: about 3n(n − 1) couplings and 3n − 1 counterterm parts;
  - plus H_u's direction, unfixed (§ 5).

## 5. The field content (the referee's B3)

- **The reading is supersymmetric.**
  - F is the softly broken supersymmetric supertrace: two complex scalars at mass² u + m₀² per Dirac fermion at u.
  - H is written in a superpotential.
- **A lone Y = −½ triplet is anomalous.** Its Higgsinos (three doublets) give Tr Y³ = 3 · 2 · (−½)³ = −3/4,
  Tr(Y T²) = −3/4 and Tr Y = −3. The count of SU(2) doublets is odd (the Standard Model's 12, plus 2n vector-like, plus
  3), which is Witten's global anomaly.
- **An H_u triplet (Y = +½) is required.**
  - It brings its own CP² direction (4 real coordinates), tan β and a relative phase. None is fixed here.
  - H_u has no coupling in the construction. H_u L̄ E is gauge-invariant, and its modular status is not examined.
- **FR-FIB's single Higgs serves its up and its down sectors** (B1656; B1703). Using this vacuum for the frame needs
  H_u's direction identified with H_d's: an UNEARNED identification.
- **In a non-supersymmetric reading,** F's form needs scalar quartics tuned to the Yukawa coupling, which is not
  RG-stable. The tree-level quartics invariant under ρ_R's signed-permutation image (e.g. Σ_α (H_α†H_α)²) depend on Ŝ at
  tree level and would dominate the one-loop selection unless CHOSEN zero.
- **The completion is registered** (P-536).

## 6. Does not establish

- **That the object, or FR-FIB, contains this heavy sector,** or its menu, copy count, tie or convention. All are CHOSEN
  (P-415).
- **That Ŝ* is our world's Higgs direction.** Nothing is compared. Reading the minimised vev as the frame's Higgs, and
  the singular values as masses, is UNEARNED.
- **That the direction is the heavy sector's.** The light fields' own loops also give Ŝ-dependent terms, of order
  y⁴v⁴ log, against the heavy sector's (λv)²m₀² log. The direction is the heavy sector's only if m₀ ≫ yv.
- **The extra doublets.** The two non-vacuum Higgs combinations are physical doublets, with masses² set by Q's other
  eigenvalues (about λ²m₀² × 0.01–1/16π²).
- **The scales.** No relation is derived between M, the scale at which FR-FIB is read, and v. ∣v∣ is fixed by hand, and
  v ≪ M is assumed.
- **Stability beyond one loop,** and robustness to non-minimal Kähler terms. Tree-level terms such as
  κ(2y)^w∣Y(τ)ᵀH∣² are allowed by the same symmetry. The literature's Kähler ambiguity of modular flavour models is the
  general form of this gap (Seen first).
- **Fragile cases.** Where Q's gap ratio is small (0.008 at H, n = 3), a perturbation of about 1% of Q's spread rotates
  the direction by O(1). The decoupling-limit Jacobian gives up to 2.8 per e-fold of a singlet constant there.
- **Menu H's n = 2 vacuum lies on R,** an isotropic direction with m₁ ≡ 0 (B1809). As a Higgs for the frame it gives a
  massless first generation. That is an outcome.
- **Any description length** (P-418).

## 7. What it means for THE FINAL ATTACK

- **Step A** (P-495: a Higgs direction fixed by the interaction) is not delivered by this construction. It is NEGATIVE as
  a compression: the inputs it needs (a continuous convention, zeroed invariant couplings and counterterms, an H_u
  sector) cost more than the six coordinates they fix.
- **Step B** keeps the declared directions, twelve distinct (B1824), and gets no Step A arm. The prior THE FINAL ATTACK
  attached to Step A's vacuum (PASS ≤ 10%) is not used.
- **What it teaches,** kept as structure:
  - B1818's count ("each condition a level, each level a free number") holds for τ's conditions and for light copies.
  - The direction is fixed by an eigenvector condition, which spends no level.
  - The freedom returns through the normalisations, which are continuous.
  - A construction that fixed them (a canonical normalisation the object forces) would have to beat the light-copy
    regime that the canonical conventions computed here fall into (P-537).

## 8. The referee (hostile, read-only; every finding checked by main)

| item | verdict | applied |
|---|---|---|
| B1: the headline against the plan's sealed reading; "the heavy regime" post hoc; the runaway counted as isolated | BLOCKING | the sealed verdict leads (§ 3); the regime labelled post hoc; the tallies corrected |
| B2: "one leading free number" rests on a post-hoc continuous convention and on couplings set to zero; other conventions lose the small-n result; the cusp convention's n ≥ 4–5 is refuted | BLOCKING | the convention in the headline; the convention-free count (§ 4); the cross terms and counterterms counted as CHOSEN |
| B3: the field content is anomalous in the supersymmetric reading; H_u required; H_u ≡ H_d UNEARNED | BLOCKING | the reading declared; the completion registered (§ 5, P-536) |
| N1: charge-preserving vevs only | non-blocking | the restriction stated; the test passes; the n = 1 valley corrected (§ 2) |
| N2: the double-precision F is exactly 0 for u ≳ 10¹⁴ | non-blocking | the whole grid rerun by main with the stable form (§ 3) |
| N3: the symmetric points were computed at one parameter point | non-blocking | extended to the grid (§ 2) |
| N4: the invariance test's resolution and blindness to characters; one control doubly wrong | non-blocking | stated, and the S-action controls added (§ 2) |
| N5: overstated wording | non-blocking | removed ("the interaction's", "one leading number plus a discrete menu", "all 119", the cusp convention's "isolated") |
| N6: four gaps to list | non-blocking | listed (§ 6) |
| N7: why sup makes small n heavy; the literature leg; the criterion's replacement | non-blocking | § 4, Seen first, § 3 |
| N8: what survives | — | § 2 |
| **The confirmation pass** (the referee, on this page and main's reruns; `verification/referee/confirm/CONFIRM.json`) | FAITHFUL overall; the label NEGATIVE fair | applied: four statements narrowed to what was computed ("all six directions" off the lines only; n = 2's vacuum "lost", not "none"; the symmetric points on the primary grid; n = 2's rank 1 local to the heavy regime); N1's light-copy valley and N7's mechanism added; the weak leg's strengths quoted |

## 9. Main's verification

- **B1, from the draft's own output** (`verification/summary.txt`, `step_a_v2.json`):
  - menu Z, n = 2, μ² = 0.3 is FLAT(1) at all three λv;
  - menu Z, n = 3, μ² = 0.3, λv = 1 is flagged RUNAWAY by the draft;
  - menu H, n = 3, μ² = 0.3, λv = 1 is unconverged (gradient 10⁻³).
  PLAN.md's hash matches ARTIFACT_HASHES.txt.
- **B2, on the draft's model** (`verification/main/conv_jacobian_main.py` → `.json`).
  - τ₀* is found by Newton in mpmath at 40 digits, and Q's eigenvector by mpmath; the derivatives are central
    differences.
  - Menu Z, n = 2: rank 1, singular values 0.66 then ≤ 9 × 10⁻¹⁷. n = 5: rank 6, singular values 2.9, 2.1, 0.63, 0.23,
    0.095 and 0.023, identical to the referee's.
  - V₀ in mpmath equals the draft's numpy V₀ to 12 digits.
  - **Disclosed:** a first version minimised with Nelder–Mead in double precision. It stalled at its iteration cap (about
    10⁻⁹ in τ, too coarse for a rank) and was stopped before it printed.
- **B3** by arithmetic (§ 5).
- **The grid rerun** (`verification/main/rerun_stableF/`: `patch_stableF.py`, the patched copies, the log and
  `step_a_v2.json`).
  - The changes are four asserted replacements on copies of the draft's code:
    - F and its mpmath twin in the cancellation-free form (2u m₀² + m₀⁴)(log(u/μ²) − 3/2) + (u + m₀²)² log1p(m₀²/u), equal
      to the draft's form algebraically and to 50-digit values to about 2.5 × 10⁻¹⁶ from u = 10⁻⁴ to 10¹⁷ (main's ten
      points and the referee's 85);
    - the draft's 24 starts reproduced, plus 24 in the cusp;
    - an arbiter between the lowest interior and the lowest cusp point.
  - **Disclosed:** the arbiter's first version called model.py's module-level mp_V, which omits the sup constants and DR's
    scale. Its values were discarded, and the arbiter was rerun with the draft's own 34-digit model
    (`verification/main/rerun_arbiter/`).
  - Results: § 3.

## 10. Disclosed

- **Before the plan:** prototypes, during which mpmath's jtheta(2, 0, q) branch defect was met (θ₂ is summed in τ),
  the scale table that set the normalisation convention, and one exploratory search (menu Z, n = 1–4, one point).
- **After the plan, before the main runs,** each change re-hashed in ARTIFACT_HASHES.txt:
  - the discriminant written non-negatively;
  - per-copy levels for the untied control;
  - the invariant Jacobian;
  - the valley follow;
  - the mirror check at Re τ = −½;
  - the phase test in mpmath.
- **The first launch of the grid crashed** (an overflow deep in the cusp) before any output. It was fixed with a soft wall
  at Im τ > 40 and per-start error trapping, then rerun from scratch.
  - Its log is kept as `step_a_v2_run_D_crashed_overflow_paths_redacted.txt`, with the machine paths replaced by
    `<root>/` and `<python>/`.
  - The original's sha256 is c811b78c50978c5d7a8e62930d5cbdb08e8b31a9eaf405f5a8d6e13bc3151f52, as hashed in
    ARTIFACT_HASHES.txt.
- **The criterion was replaced after the runs** (§ 3).
- **`analysis_leading.py` ran three times,** and `analysis_points.py` had three versions. The superseded outputs are
  kept.
- **The draft as refereed** is kept as `verification/DRAFT_DESIGN_AS_REFEREED.md`; this page replaces its claims.

## Seen first

- `VERDICT topic-sweep /vector.like|vectorlike|heavy (lepton|copy|copies|state).{0,60}(Higgs|direction|mixing)|Higgs direction.{0,40}(fix|vacuum|minim)|minimi[sz]ed vev|Coleman.Weinberg.{0,60}(Higgs|direction|section)|cross product.{0,30}(section|F_)/: 25 of 1568 arcs on main match (NEGATIVE 3, PROVED 22); 6 register rows match (DONE 2, QUEUED 4); 13 other lanes match` (the draft's sweep).
  - The arcs it lists (B865, B895, B944, B953, B978) concern E₆ content and vector-like matter in the 27, not a heavy
    sector selecting a Higgs direction.
  - The rows are P-139, P-325, P-367, P-377, P-495 and P-518.
- `VERDICT topic-sweep /tied (ratio|heavy)|heavy (copies|sector).{0,40}(vacuum|Higgs|direction)|normali[sz]ation convention|K[äa]hler ambiguity|\bH_u\b|Coleman.Weinberg/ (full text): 26 of 1568 arcs on main match (NEGATIVE 5, OPEN 3, PROVED 18); 8 register rows match (DONE 3, QUEUED 5)` (main's, at landing).
  - Its two-Higgs matches (B1742, B1757, P-370) fit pairs of declared directions to data as two-Higgs readings. None
    builds a vacuum for H_u.
  - B1646 (the direction is the mass matrix), B1795 (the doublet–triplet split) and B1805 answer other questions.
- **Read:**
  - B1818's held draft, its referee, and the withdrawal note on STEP_A_DESIGN;
  - main's W150 verification (harvest row 1371);
  - B1730, B1809 and B1810;
  - TERMINOLOGY's H-cov;
  - THE_FINAL_ATTACK § 4;
  - P-139, P-367, P-415, P-495 and P-518–P-535.
- **The literature.**
  - The heavy-state mechanism is W150's source (arXiv:2402.02071), verified on main at harvest row 1371.
  - That the Kähler potential of modular flavour models is not fixed by the modular symmetry is known: Chen, Ramos-Sánchez
    and Ratz, arXiv:1909.06910. It is the general form of § 6's Kähler gap and of § 4's normalisation freedom.
  - Vector-like lepton mass matrices and the Coleman–Weinberg supertrace with universal soft masses are standard.
  - No novelty is claimed for the directions found. The draft's "new" is withdrawn.
