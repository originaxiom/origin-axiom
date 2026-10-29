# B1809 — WHAT FOUR FRAMES ON RECORD LEAVE FREE (P-406 RE-SCOPED; A CENSUS WITH ONE CLASSICAL LEMMA; DATA-FREE). FOR EVERY DISCRETE CHOICE ON RECORD, EACH OF FOUR FRAMES KEEPS EITHER A CONTINUOUS DATUM NOTHING ON RECORD FIXES, OR AN INFINITE DISCRETE MENU NOTHING ON RECORD SELECTS. AT THE CONFIGURATIONS THE OBJECT'S SYMMETRY FIXES, THE OUTPUTS ARE DEGENERACIES, J = 0, OR NUMBERS SET BY THE DISCRETE CHOICES — TABLE T, WHICH AT B1667's L₂(i) RUNS FROM m₂/m₃ = 0.019 (A HIGGS ∝ R) TO 1. "HIERARCHY" IS NOT DEFINED HERE: THE TABLE IS THE STATEMENT, AND P-432 COMPLETES IT

**Verdict: PROVED, as a census.**
- **Its parts:** a classical lemma, a table of values computed on main, and a per-frame census read from the cited arcs.
  The census's absence claims rest on a sweep ("nothing on record fixes"), not on a theorem.
- **Its history:** P-406's third draft.
  - The first, a "theorem", was withdrawn at its hostile referee: an ill-posed definition, a false Theorem B, a title
    already on record.
  - The second, a census, was blocked at its own referee: (S1) failed at the canonical end radius, (S2) was false for two
    frames, and "V ≡ 1" was misattributed.
- **The record of both:** the referees' reports and main's verification are in `verification/referee/`.

Data-free; none of the 19; no data read. cc (main), 2026-10-29, at the owner's ruling (census, then selection).

**0 of 19.**

## 0. Seen first, and what is new

**Seen first.** The referees' sweeps (88 arcs and 3 rows; 33 arcs and 17 rows) found these antecedents:
- docs/THE_FORCED_AND_THE_FREE.md (2026-08-19: the torsor pattern);
- B1652 THE FRAME TRIBUNAL (2026-10-14: "the only selected vacua, ω and the cusp, have none");
- P-139 with B990's law ("an invariant construction picks only its symmetric points");
- B1667 ("the end supplies no hierarchy");
- B1704 (where τ is held, "no hierarchy");
- B1671, P-194, B213;
- B1670 and docs/THE_PRICE_OF_THE_NINETEEN.md;
- B1750 § 2's typed table;
- docs/THE_DERIVED_STRUCTURE_FOR_REVIEW.md (2026-10-08: "all 19 are free");
- docs/PARAMETER_CLOSURE_MASTERPLAN.md;
- P-224 (the stabiliser no-go);
- B1620; B714; B736; B758; B1123.

**The literature it rests on:**
- the classification of PGL(2, ℝ)'s elements and the elliptic points of PSL(2, ℤ) (standard; e.g. Serre, *A Course in
  Arithmetic*, ch. VII);
- the torsion-freeness of Γ₁(N) for N ≥ 4;
- modular flavour symmetry near fixed points (Novichkov–Penedo–Petcov 2021; Feruglio, Gherardi, Romanino and Titov
  2021), where the residual symmetry fixes exponents;
- Donagi–Wijnholt (arXiv:0904.1218), through B1808.

None states a census of these frames.

**What is new here:**
- τ = i (B1806, B1807);
- the canonical-end table T;
- the configuration-fixed list;
- the census's definition.

The statements at ω and the cusp are not new.

## 1. The definition (the first referee's, sharpened by the second)

- **A frame is (C(d), D, Φ, 𝒦, H):**
  - C(d): the continuous configurations, which may grow with the discrete choice d (the section space grows with the
    weight);
  - D: the discrete choices;
  - Φ: the dimensionless outputs, each named against the 19;
  - 𝒦: the conditions built from the object, each typed (symmetry, canonical construction, variational, arithmetic);
  - H: the tagged hypotheses and the identifications. These are neither derived nor countable choices: H-cov; Λ; the
    cusp unit (FK10, v1.39); GM5b; and B1750's identifications, since "Φ named against the 19" is itself one.
- **The end radius** L = L_h(τ) is in 𝒦 (a canonical construction, B1667). The horocycle h ∈ {max, 2} is in D.
- **A condition** enters 𝒦 only if the record derives it without choosing among alternatives.
- **Fixed outputs.** An output is fixed at d when it is constant on each component of C(d) satisfying 𝒦; the values are
  reported.
- **The counts.** f(d) is the generic rank of Φ on C(d), taken on the open dense set where Φ is analytic (singular values
  cross; L_max(τ) is piecewise). The relations among the outputs number m − f(d).
  - These are relations, not agreement with nature.
  - f(d) is an output rank. P-418 counts inputs. The two are complementary.

## 2. The classical lemma, and the configurations the object's symmetry fixes

**The lemma.** For a nontrivial H ≤ PGL(2, ℤ) acting on ℍ, Fix(H) is one of:
- empty;
- one point in the orbit of i or ω;
- a reflection geodesic.

**Its proof and checks.** By the classification of PGL(2, ℝ)'s elements (in PGL(2, ℤ) the classes ST and (ST)⁻¹ merge).
The subgroup case is the first referee's r5: 31 of 31 meeting pairs of reflection lines meet at i or ω points. The lemma
is generic: every member has the same group (E20).

**The whole configuration's stabiliser must be used** (τ, the line, the section, the reading).
- ±Γ₁(N) is torsion-free for N ≥ 4, so on lines of order ≥ 4 no elliptic element fixes the configuration. A reflection
  geodesic can still be fixed, e.g. (1/N, 0) under the mirror.
- **The configuration-fixed points of the fibre frame are therefore**, up to the group: (i, 0), (ω, 0), (i, (½, ½)) and
  (ω, (⅓, ⅔)).
- The record's lines have every order 1–12 (B1713's 266) and 15–30 (W175, W176). The first referee's r3 values at i on
  (½, 0), (0, ½), (⅓, ⅓) and (⅓, ⅔) are not configuration-fixed.

## 3. Table T — the outputs at the configuration-fixed points (zero line unless stated; B1656's four-channel coupling; B1667's radii at i: L_max(i) = 0.688386, L₂(i) = 2.719258)

(m₁/m₃, m₂/m₃). Computed on main (`verification/values_at_i_main.py`) and by the second referee's c1 and c6, which
regenerate byte-identically on main; the two code paths agree to every printed digit.

| Higgs direction | L-free (L → ∞) | L_max(i) | L₂(i) |
|---|---|---|---|
| DR (k = 3/2; B1697) | (0, 1) | (0, 1) | (0, 1) |
| a₀ = ∂²R − E₄R/48 (k = 7/2; B1697's unique section without end data; equal to F₋₂ at i) | (·, 2/3) | (0.585, 0.731) | (0.0753, 0.658) |
| R, η⁶R (W72's mode), F₂, every section with a(i) on R(i)'s line | (0, 0) | (0, 0.2080) | (0, 0.01907) |
| t = −5/288 (a·a ≡ 0) | (0, 0) | (0, 0.832) | (0, 0.0763) |
| F₆ / F₁₀ / F₁₄ / F₂₂ (B1730, B1742; outside H-cov's proofs) | ≈ (·, 0.667 / 0.300 / 0.643 / 0.532) at L = 2560 | (0.774, 0.966) / (0.092, 0.250) / (0.435, 0.535) / (0.324, 0.443) | (0.0773, 0.675) / (0.0229, 0.281) / (0.0490, 0.624) / (0.0406, 0.513) |
| DR on the S-fixed line (i, (½, ½)) | — | (0.416, 0.708) | (0.0381, 0.519) (the first referee's r3 and r4; exploratory, not yet rerun on main) |
| DR on the ST-fixed line (ω, (⅓, ⅔)) | — | (0, 1) | (0, 1) (the first referee; exploratory) |

- **Not yet computed:** (ω, 0) at the canonical radii; the remaining sections at the fixed lines; the readings (B1790).
  These complete P-432.
- **The radius at L_max(i) is steep.** The k-channel's weight 2πL + c_k there is only 0.446, and it vanishes at
  L ≈ 0.617 (the second referee's c4), so values at L_max(i) change quickly with L.
- **The horocycle is a scale.** Changing it moves R's m₂/m₃(i) by a factor of 11.
- **No data read.** Any comparison is P-432's sealed test (KIND_TABLE, L91).

## 4. The census, frame by frame (renamed: B1652's F1–F5 and GENESIS's F-FC, F-CI, F-HE, F-AP are different frames)

### FR-FIB — B1656's flat fibre frame

**Free and discrete.**
- C(d): τ, and a generic section's coefficients.
- D: the weight class; a shared or per-sector section; h; the line (orders 1–12, 15–30); the reading (eight, B1790);
  c; h₀.
  > *Re-typed 2026-10-29 (P-489): h₀ is a continuous datum set by hand (h₀ = 0), not a discrete choice (the web seat's
  > scoreboard row 1478).*

**Fixed at d.**
- Degeneracies at the special points (Table T).
- J = 0 on mirror-fixed configurations, with mirror-invariant (real-coefficient) sections. With complex coefficients,
  J = 4.4 × 10⁻⁶ on Re τ = 0 (c5).
- With one section and one reading in every sector, V ≡ 1 and the sectors coincide. That is trivial at zero line. With
  the record's reading (S̃, S, S) or with per-sector sections, V varies with τ (c3, c7: ∣V₁₂∣ up to 0.69;
  J = 7 × 10⁻⁷ to 2.9 × 10⁻⁵).
- Isotropic directions (R, η⁶R, t = −5/288): m₁ ≡ 0 at every L. m₂ ≡ 0 only at L = ∞; at the canonical end
  m₂/m₃ = O(1/L).

**Relations among the outputs (to count; P-418).**
- m = 10 (six mass ratios, four CKM parameters). f(d) ≤ 2 with DR at a fixed line.
- "The six are four" holds on α = 2/5 lines (exact for k even; for k odd only with no QI component).
- B1691's m₁/m₃ ∝ Im τ·(m₂/m₃)² is an L-free asymptotic law with a section-dependent coefficient.

**Not reached:** 9 of the 19 — the scale, y_t, y_b, y_τ, λ, θ̄ and the three gauge couplings.

### FR-FLUX — the flux frames (B1800; B1804)

- **Split.** A curve, for every integer flux.
- **Holomorphic.** A countable dense set of CM points chosen by flux integers (B1804). The generation count confines the
  moduli to a curve (B1808), and three or more independent fluxes have no common point. There is no LR-invariant Kähler
  class.
- None of the 19 is computed.

### FR-G2Q — Witten's G₂ frame over Q = m004(p/q) (B1801–B1805; not GENESIS's F-AP, which is the SM seat's apex frame)

- **Free:** the G₂ moduli and the volume. **Discrete:** p/q, the Wilson line, the singularity type, the flux integers.
- **Fixed:** the one-loop sin²θ_W is unchanged by the thresholds (B1801); the generic SU(5) relation is imposed.
  Friedmann–Witten's G_N relation contains an unknown shape a.
- **Not supplied:** matter parity in this frame (B1805, NEGATIVE).
- **Not reached:** the Yukawas, the mixing, θ̄, the Higgs's two parameters.

### FR-DYN — the one-loop potentials

**Cited, not built on.** The SM seat's W51–W176 are READ on main, not recomputed (harvest rows 1452 and 1458 for W175 and
W176).

**Verified on main:**
- B1684 (critical only at i and ω);
- B1686 (the record's content runs to the cusp);
- B1704 (a content holds τ off the cusp only with a negative total cusp coefficient; every content on record is
  positive; adding trivial-sector fermions holds τ on the unit arc between i and ω + 1, y ≈ 0.89–1.00, where there is no
  hierarchy).

**Read only:**
- On the slope-2/5 classes, at each height, Re τ is fixed by partial minimisation in Re τ (W175). The pitchfork at
  Im τ ≈ 2.22 is post hoc.
- W176's least is on the lines (0, 1/N) at Im τ = 4, the top edge of its range, for every order listed. It reports no
  least on any slope-2/5 line.
- Below Im τ = 1.2 on the slope-2/5 classes nothing was checked.

## 5. What survives as statements

- **(S1)** At the configuration-fixed points of FR-FIB — under GM5b and H-cov, with B1667's canonical end L = L_h(τ) and
  h a discrete choice — each output is one of:
  - a degeneracy (m₂/m₃ = 1 or m₁ = 0);
  - J = 0 on mirror-fixed configurations;
  - a number set by the discrete choices: free over a generic section's coefficients, and, for the record's
    parameter-free directions, the values of Table T.

  At L₂(i) those values run from m₂/m₃ = 0.019 (a ∝ R), and m₁/m₃ = 0.023–0.077, up to 1. "Hierarchy" is not defined
  here; Table T is the statement. Near such a point each output is asymptotically r₀ + c·δ^p, with p set by:
  - the residual symmetry;
  - the weight class;
  - at the canonical end, the channel splitting (B1807 §§ 3–4; B1691's S248 note).

  These laws hold within a section- and L-dependent neighbourhood. The cusp is a boundary point (L-free:
  m₁/m₃ ∝ Im τ·∣q∣).
- **(S2)** For every discrete choice on record, each frame keeps one of the following:
  - **A continuous datum nothing on record fixes:**
    - FR-FIB: τ and the section's coefficients;
    - FR-FLUX split: a curve;
    - FR-G2Q: the G₂ moduli and the volume;
    - FR-DYN: Im τ on the computed ranges.
  - **An infinite discrete menu, or a content, nothing on record selects:**
    - FR-FLUX holomorphic: the flux integers (B1804, B1808);
    - FR-DYN with B1704's added fermions: τ held on the unit arc, no hierarchy there.

  The outputs vary with the remaining datum, except those fixed at d and the values in (S1). Swept: the referees'
  sweeps (§ 0). Not checked: FR-DYN below Im τ = 1.2 on the slope-2/5 classes.
- **(S3)** P-406's deliverable, re-scoped. As registered ("frames … with no added moduli"), P-406 is not answered: all
  four frames add moduli. What is delivered is the census's definition, the count f(d) with its m − f(d) relations
  (owed), and Table T.

## 6. The discrete side (labels checked against the record)

**FORCED, generic.**
- The hypercharge direction, given an SM-shaped 15-plet (B1160). B1162's open items are the MSSM witness's, not the
  hypercharge.
- The ℤ₆ global form (B1221: a property of the algebra and its representation).

**Not Standard-Model data.** E₆ across the faces (generic; B727).

**A thread fact (m004), a mathematical fact, not a bridge.** The arithmetic origin ℚ(√−3) (B727). π₁ ↠ 2T is shared by
7₂, 7₃ and 8₁.

**The arrow.** "Forced" in B1750 § 2, with its side a convention (B1662: the side is CHOSEN). Its old home is gone under
GM5b (B1083's addendum).

**Not forced.**
- The hand (FK10 OPEN; B1796 assumes it; B1808: CHOSEN in FR-FLUX).
- "Three" (selected: B1496, B1604).
- Matter parity in FR-G2Q (B1803, B1805).

**Admitted.** The doublet–triplet topology on even fillings (B1802, B1803).

**θ̄.** Not reached by these frames.
- I-18 is UNEARNED.
- Its B1246 sharpening says the type dictionary reaches θ, not θ̄.
- **The row is internally inconsistent:** its 2026-10-22 bracket (P-274) says "the dictionary gives θ̄ ∈ {0, π} …
  θ̄ = 0 holds given the + side", which contradicts the B1246 sharpening. To be reconciled (P-434).

## 7. What the census does not exclude

- **Selection principles:** P-419 (the main line; B1808 closes its flux frame for the generation count), and FK9 / P-139.
- **FR-FIB's values at CM points**, the rigid loci P-419 looks for. Not computed.
- **Contents that hold τ** (B1704's class), or a negative total cusp coefficient.
- **The other open doors:**
  - a forced weight (P-413);
  - a consistency condition on the line (P-411, P-422);
  - the towers in another frame (P-415);
  - a forced holder for the height (FK11).
- **Frames outside these four.**

## 8. Owed

- **P-432:** complete Table T — (ω, 0) at the canonical radii, the fixed lines rerun on main, the readings — then its
  sealed test.
- **P-418:** f(d) per frame as a Jacobian rank.
- **P-434:** reconcile I-18's row.
- **B1697's claim line**, which still reads "m2/m3 → 1/2" (its FINDINGS was corrected by dated note, S245; P-435).
