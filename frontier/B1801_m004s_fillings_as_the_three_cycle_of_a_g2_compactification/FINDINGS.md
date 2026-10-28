# B1801 — m004'S FILLINGS AS THE 3-CYCLE Q OF A G₂ COMPACTIFICATION (THE MEDITATION'S ANGLE A, IN FRIEDMANN–WITTEN'S FRAME; DATA-FREE): THE ORDER-3 REIDEMEISTER TORSION OF EVERY HYPERBOLIC FILLING m004(p/q) WITH 3 ∣ p IS 4/3 (∣Δ₄₁(ω)∣ = 4; THREE INDEPENDENT ROUTES), SO FRIEDMANN–WITTEN'S L(Q) = 3∣H₁∣/4. THEIR THRESHOLDS ARE OF THE FORM x·k_a + y·b_a, SO THEY LEAVE THE ONE-LOOP sin²θ_W UNCHANGED FOR ANY Q: THE TORSION RELATES MODULI TO M_GUT AND FIXES NONE OF THE 19. THE DOUBLET–TRIPLET SPLIT FIRST CLAIMED IS WITHDRAWN

**Verdict: PROVED** for the torsion, the acyclicity and the breaking pattern, which are exact. **NEGATIVE** for "the torsion
predicts a gauge coupling": Friedmann–Witten's identity, computed on the bench, holds for every Q in their frame. Data-free.

cc (main), 2026-10-28, from THE_PATTERN_MEDITATION_3. Corrected before landing at its hostile referee (§ 5). The draft's
doublet–triplet claim, and the meditation's α_s hope, are withdrawn. **0 of 19.**

## 1. The frame, and what it assumes

**Friedmann–Witten** (hep-th/0211269): M-theory on a G₂ manifold X with the GUT group on a 3-cycle Q. SU(5) is broken to
the Standard Model by a flat H-bundle (Wilson lines) on Q. The one-loop threshold corrections are Q's Ray–Singer torsions.

**Here Q is a hyperbolic Dehn filling of m004** (B1794: H₁ = ℤ/∣p∣, torsion only). This needs several hypotheses beyond the
paper:
- **Infinite π₁.** Friedmann–Witten assume finite π₁ for "no zero modes". Here acyclicity is computed instead: the order-3
  character gives H⁰ = H¹ = 0 on m004(3, 2), (6, 1) and (9, 2), because Δ(ω) = −4 ≠ 0 (the twisted Fox Jacobian's singular
  values are (4, 0); `verification/bench_checks.py`). Trivial coefficients give H⁰ = 1, H¹ = 0.
- **The abelian vacuum is isolated,** H¹(Q; ad) = 0 for the abelian bundle. It is one of many flat SU(5) connections.
- **Existence.** That a G₂ manifold exists with such a Q as its A₄ locus is open: Acharya asks it, and Witten cites "the
  difficult problem of what singular manifolds of G₂ holonomy actually exist". Friedmann–Witten's examples are S³ quotients.
  The identification Q = m004(p/q) is therefore UNEARNED (IDENTIFICATION_LEDGER, I-36).
- **No rigidity is used.** The torsion is a topological invariant, Q's metric is the induced G₂ metric, and V_Q stays a
  modulus. Mostow rigidity plays no role here.

## 2. Computed

**The Wilson line.**
- U = exp(2πi·6Y/3) = diag(ω, ω, ω, 1, 1) has det 1. It is Friedmann–Witten's U_γ (their 3.28) at (q, w) = (3, 2).
- Its commutant is S(U(3) × U(2)), the Standard Model's group (centraliser dimension 12; the referee's `r3`).
- **This is not new.** Every SU(5) → SM breaking has that commutant (B1221).
- U is the generator of Z(SU(3)). In S(U(3) × U(2)) it coincides with exp(4πiY), and that identification is the ℤ₆ quotient
  (B862, B1221). So each field sees ω^(triality): the record's B1684 M5 ("at a nonzero 3-torsion line exactly Q, u^c, d^c are
  twisted") and P-100 ("the Standard Model's ℤ₆ … standard").
- SU(5) → SM breaking does not need 3 ∣ p: every filling with ∣H₁∣ ∉ {1, 5} admits a breaking line (e.g. m004(2, 3), ℤ/2,
  ∣τ∣ = 5/4).

**The order-3 torsion is 4/3 on every hyperbolic filling with 3 ∣ p, independent of the slope.**
- **(a) Turaev's surgery formula:** ∣τ∣ = ∣Δ(ζ)∣ / (∣ζ − 1∣∣ζ^r − 1∣), with the figure-eight's Δ(t) = t − 3 + t⁻¹ (Fox calculus
  on the knot group, a relator whose homomorphism counts match m004's group; the referee's `r1`). ∣Δ(ω)∣ = 4; the
  record's ∣Δ(ω)∣² = 16 is B350's, re-deriving B326.
- **(b) The referee's Fox calculus on SnapPy's own presentation,** with the core class from SnapPy's peripheral words:
  1.333333333333 on 12 fillings × 2 characters, without Δ or r.
- **(c) Without Turaev:** H₁ of the 3-fold cyclic cover has order 16p/3 on every filling checked — main's six by SnapPy's
  covers (`bench_checks.py`), and the referee's nine by Reidemeister–Schreier and Smith form. Then ∣τ∣² = ∣H₁(Q̃)∣/(3p) =
  16/9.

**The normalisation.**
- ∣τ∣ is Turaev's (τ(S¹) = (t − 1)⁻¹). Friedmann–Witten's e^T is its inverse, the Ray/Franz torsion (their footnote 5). This
  is checked on their lens space for both characters.
- For a rational homology sphere the trivial-coefficient torsion is ∣H₁∣; Friedmann–Witten give only the lens value −log q.
- So T_ω = log(3/4), T_O = −log∣H₁∣, and **L(Q) = exp(T_ω − T_O) = 3∣H₁∣/4**: 9/4 for ℤ/3 and 9/2 for ℤ/6. Their lens space
  at q = 3 gives 9, a ratio of ∣Δ(ω)∣ = 4.
- The lowest volumes with 3 ∣ p (the referee's scan over p ≤ 60, ∣q∣ ≤ 40) are m004(6, ±1) at 1.284485 and m004(3, ±2) at
  1.440699.

## 3. Why none of the 19 follows (computed on the bench)

- **The thresholds' form.** Friedmann–Witten's traces give S′_a = (50T_ω/3, 4T_O + 6T_ω, 6T_O + 4T_ω). The bench verifies
  their identity S′_a = −(2/3) b_a (T_O − T_ω) + 10 k_a T_ω (`bench_checks.py` (1)). The thresholds are therefore of the form
  x·k_a + y·b_a, and det[16π²/g_a², k_a, b_a] = 0 identically: **no one-loop correction to sin²θ_W, for any Q in this frame.**
  In their words: "the massive Kaluza-Klein harmonics have made no correction at all to the prediction of the theory for
  sin²θ_W".
- **What L(Q) does enter:**
  - V_Q = L(Q)/M_GUT³ (their 3.25);
  - κ₁₁² = α³_GUT L(Q)³/(4π M⁹_GUT) (4.13), and M₁₁ = 2πM_GUT/(α^{1/3}_GUT L^{1/3}) (4.14);
  - G_N = α³_GUT L(Q)^{2/3}/(32π² a M²_GUT), with the G₂ space's unknown shape a (4.12);
  - the p → π⁰e⁺_L coefficient, ∝ L^{2/3} (5.14). Given the same unknown constant, the rate scales as L^{4/3}: a
    model-to-model ratio, not one of the 19.
- **The Standard Model's 19 are untouched.** The meditation's α_s hope is withdrawn.

## 4. Withdrawn, and open

- **Withdrawn:** the draft's "the ℤ/3 Wilson line splits the Higgs doublet from its colour triplet: the doublet keeps its zero
  mode and the triplet is lifted".
  - In Friedmann–Witten's frame the Higgs 5 and 5̄ are chiral superfields at conical points P_i: complete SU(5) multiplets.
  - The bulk 7d vector multiplet is adjoint-only. Its untwisted components give H⁰ = 1, a 4d vector multiplet, and H¹ = 0, no
    chiral multiplet. Its twisted components are acyclic.
  - So the Wilson line does not split the Higgs.
  - Witten's mechanism (hep-ph/0201018) instead needs a discrete symmetry F of Q (and of X) with two fixed circles, the Higgs
    5 and 5̄ placed on them, and the gauge transformation acting at one. Witten: "the special points in Q support complete
    SU(5) multiplets".
  - The draft's reading would also have lifted the quarks.
- **Open:**
  - SnapPy gives Sym(m004(3, 2)) = Sym(m004(6, 1)) = ℤ/2 + ℤ/2. Whether an involution has fixed circles and lifts with a gauge
    transformation that separates doublet from triplet is registered as P-408, not claimed.
  - Witten's mechanism works for any breaking order, so P-408 is not tied to 3 ∣ p.

## 5. The referee (hostile, read-only; `audit/referee_b1801/`, scripts kept in `verification/referee/`)

**Passed:**
- the Wilson line, its commutant and every row of the holonomy table;
- the relator, by homomorphism counts into S₃, S₄, A₅, S₅ and PSL(2, 7) against SnapPy's group;
- ∣τ∣ = 4/3 by three routes;
- Friedmann–Witten's normalisation on their lens space;
- the (3.21) identity and the vanishing determinant;
- the scan;
- the acyclicity.

**One blocking finding, applied:** the doublet–triplet split (§ 4).

**Corrections, applied:**
- the triality table is B1684's M5 and P-100's; ∣Δ(ω)∣² is B350's;
- the B862 link stated exactly;
- the thresholds' form, not "universal";
- the negative computed on the bench, and scoped to every Q in this frame;
- the unstated hypotheses (infinite π₁, isolation, existence), with Mostow removed;
- the attributions, and the torsion convention declared;
- "one" non-numerological route, not "the";
- the post hoc L^{2/3} remark removed. It selected both the filling and the scenario, set a at Friedmann–Witten's
  conjectured bound, and used data-derived numbers;
- "the object" replaced by "m004's fillings";
- the verdict file and the identification row added.

**Notes:**
- the script's loop and the lock are strengthened;
- P-405 is reframed: membrane-instanton actions are calibrated volumes, which depend on the moduli, not hyperbolic volumes;
- the meditation's SYNTHESIS annotated.

## Seen first

`VERDICT topic-sweep /G2|G_2|M-theory|Friedmann|Witten.{0,20}(doublet|Wilson)|Ray.Singer|Reidemeister|analytic torsion|Wilson line.{0,30}(SU\(5\)|break)|doublet.triplet|discrete Wilson|torsion homology|rational homology sphere/ (full text): 120 of 1548 arcs on main match (NEGATIVE 27, OPEN 7, PROVED 86); 3 register rows match (DONE 3)`.
The referee added "triality", "3-torsion" and "cyclic cover".
- **Bearing on it:**
  - B98, B622: adjoint torsions;
  - B326 and B350: ∣Δ(ω)∣² = 16;
  - B862 and B1221: the ℤ₆ quotient, and why every SU(5) → SM breaking has this commutant;
  - B955 and B956: Wilson lines on the knot complement;
  - B1484;
  - B1684 M5: the triality table;
  - B1794, B1795;
  - P-100.
- **Literature:**
  - Friedmann and Witten (hep-th/0211269), read for 3.1–3.31, 4.10–4.14 and 5.14;
  - Witten (hep-ph/0201018), read by the referee;
  - Acharya (hep-th/0212294);
  - Turaev on the torsion of surgeries;
  - Ray–Singer and Cheeger–Müller.

## Files

- `verification/torsion.py` → `torsion_run.txt`.
- `verification/bench_checks.py` → `bench_checks_run.txt`.
- `verification/referee/`: `r1_relator_and_torsion.py`, `r2_cover_check.py`, `r3_group_theory_and_fw.py`, and their runs.

The lock: `tests/test_b1801_m004s_fillings_as_the_three_cycle_of_a_g2_compactification.py`.
