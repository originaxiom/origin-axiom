# The retractions index (GOVERNANCE §12–§14 companion; instituted 2026-07-16)

*One row per banked-then-corrected statement. This index is DISTINCT from
`docs/ARCHIVE.md` (ideas killed at testing) — these were once asserted in
the record and later corrected, withdrawn, or superseded; a reader of an
old FINDINGS could still act on them. Curated, not exhaustive at
inception; maintenance rule (same-PR, like LAW_MAP): every future
retraction/withdrawal adds its row in the PR that banks the correction.
Rows cite the banked locus and the correcting locus.*

| what was asserted | where banked | the correction | where corrected |
|---|---|---|---|
| B519's negative: "no external crossing" (read as sufficient) | B519 FINDINGS | RETRACTED — mixed-chain gap-opening is falsifiable; the discriminating fact was never computed in-sandbox | the B525 audit (3/10 banked negatives cracked); the compute-the-discriminating-fact rule |
| "exponent = rank from Cayley–Hamilton" (SL(4)) | B90/V74 | REFUTED — both SL(4) components satisfy L1b with exponents 4 vs 3; L1a was a tautology | the V75 audit; B90 reclassified as reformulation |
| B95's "forced" principal spectrum read unconditionally; "any 5-dim rep reducible/non-ss 0/120" | B95/V79 | CORRECTED — "forced" is conditional on the mult-(n−2) ansatz; non-ss irreducibles exist (2 certificates); the n=5 absence holds for the finite-order/principal family | B153/V142–V145 (the det-t=0 drift found) |
| PC13's "SL(4) component" claim | PC13 | REPLACED — degree=rank is rank-stratified: component@3, slice@4, absent@5 | B153 |
| The "E₆→SM dictionary" (a cross-seat handoff) | chat-1 handoff, 2026-06 | VERIFIED-AND-REFUTED — G₂⊕A₂ mislabeled as E₆; the numerology killed | B347 (the correct replacement: E₆ tangent = 6; θ = E₆→F₄ split) |
| The trefoil(5,1) trace-field inheritance reading (Tr τ ∈ ℚ(√5)) | the child-transfer thread — frontier/B437_child_abelian_book (+ B438/B440 foreign controls) | RETRACTED as inheritance — numerator-forced, not inherited | PROGRESS_LOG 2026-07 (the (5,1)-filling control) |
| The "entropy log β" reading of the growth rate | the criticality thread — frontier/B523_verdict_reexamination + frontier/B530_natural_history | RETRACTED — primitive subshifts have zero entropy; the quantity is the inflation growth rate | PROGRESS_LOG 2026-07-15 |
| The quadratic-arrow verdict (all forms) | the L85 campaign | RETRACTED IN FULL — the longitude convention corrected AND the re-derived form ALSO retracted by the same arc's erratum (P1_ERRATUM D2: "no map was constructed to have an order"; survives only as a heuristic expectation). [Row corrected 2026-07-21: the earlier "(quadratic stands in corrected form)" contradicted its own cited source — cc2 register crack #3, cc-verified] | B598-P2 + P1_ERRATUM D1–D10 |
| The Kubota–Leopoldt attribution claim | the dictionary thread — frontier/B507_beta_function + the Review 25 sweep (docs/progress/REVIEWS.md, 2026-07-15) | RETRACTED with the discriminating fact computed | REVIEWS (the 2026-07-15 sweep) |
| B609's unit-modulus exploratory note | B609 | SUPERSEDED — the exploratory reading replaced by the exact law | B611; Review 19 (i) |
| A parallel seat's h¹(D_conjθ) = 3 | a cross-seat packet, 2026-07-16 | WITHDRAWN by the originating seat — an assumed λ-sign; the dimension is genuinely open (the object is a fiber pairing, not a rep twist) | B639; L92 re-scoped; the cc2 adjudication note |
| The B615 amplitude suggestion read at p = 0.078 | B615 | DISSOLVED — scheme/scale defect; corrected inputs give 0.145–0.62 across all variants (verdict A) | B615-R (seat 4), integrated B633 |
| "The naive flip acts on the double" (the L93 candidate as first posed) | L93's design | REFUTED — the flip does not act (either J-convention); both outer involution classes broken (partial intertwiner on Sym⁰ only) | B643; LAW_MAP wall 8 |
| *— CATCH-UP BLOCK (2026-08-06, B920; cc3 loss audit A5: the same-PR rule above was broken — no rows since 2026-07-22 despite the events below) —* | | | |
| H-B788-NORMSPLIT ("m004-only trace norms all ≡0 mod 4") — hint retracted 2026-07-28 as "REFUTED by B794's law" | docs/HINT_LEDGER.md row (7); frontier/B794_congruence_level4/FINDINGS.md | TWO-STAGE: the 07-28 retraction itself was then AMENDED 2026-08-06 — the refutation holds only at the TRACE level; at the NORM level (the hint's own level) the hint SURVIVES: norm-level m004-exclusives = 12 norms, all ≡0 mod 4; 103/127/175/367 are shared; B794's theorem is the mechanism | B920 (the cc3 level reconciliation, rerun in-sandbox); reconciling artifact frontier/B794_congruence_level4/trace_norm_split.* ; E28/E33 instance rows |
| B471's Fricke/commutator harvest row read as the programme's own result (the Cohn 1955 attribution omitted at harvest) | docs/LAW_MAP.md (the R32-9 harvest row, first form) | ATTRIBUTION CORRECTED 2026-07-29 — classical territory (Cohn 1955, Markov, Fricke), cited not claimed; the programme's own content is the metallic-body specialisation only | the LAW_MAP B471 row (⚠ block); tests/test_b471_harvest.py |
| "{4₁, 5₂} form a commensurability class" / "the forced child inherits its parent's commensurability class" | B438, B440, B443; docs/CAMPAIGN_STATUS.md | WITHDRAWN (polarity inverted) — no knot complement is commensurable with 4₁ (Reid: the unique arithmetic knot); a property shared with 5₂ is shared across NON-commensurable manifolds, i.e. genericity evidence, the opposite of "commensurability-forced"; what survives is narrower: 4₁(5,1) ≅ −5₂(5,1) at slope 5 only | B855 (the wrong-null audit, 2026-08-02) §2; its carried-forward correction list |
| B790's Maass-adjudication first pass: the "ordinary noise" null verdict + three supporting readings | frontier/B790_maass_adjudication/FINDINGS.md (first pass) | FOUR CORRECTIONS CONCEDED (Chat-1's challenges, all four) — the reported null was never the pre-registered one AND the "Weyl-matched" null was miscoded (e^ℓ for e^{2ℓ}); L3 re-verdicted MISS-earned; tests 1–3 vacuous; the B713–B716 scope reading corrected | the B790 ADDENDUM (2026-07-28, in-FINDINGS); ERROR_LEDGER E29 |
| B225's "2 = octahedral parent REFUTED" verdict carried as PROVED | frontier/B225* (own file); the arc-verdict register | RELABELED PROVED → RETRACTED — the criterion was vacuous (the bad-prime extraction reports 2 for EVERY monic-in-z input; specificity zero); the octahedral-parent question returns to OPEN; the 5-half survives (5 in conductor 40 = the golden branch point x²=5) | B745 (confirmation); B831 (the relabel, R35-4); CHANGELOG 2026-08 |
| The section-LIV septic wall-root instrument (cmt.py), retracted by the solo seat, SHIPPED ANYWAY in solo handoff 6 — a stale pre-retraction artifact (κ mod 40031 has NO wall roots; centralizers there read the generic floor 12) | solo handoff 6 §XLIX–LVIII (the shipped cmt.py) | CAUGHT AT VERIFICATION 2026-08-06 — root-set comparison against κ exposed the phantom roots; the corrected instrument (cmt_correct.py) confirms the ledger at MORE (root,prime) pairs; adopted as the wall-instrument sanity gate; the retraction-propagation failure (a retracted instrument surviving into a handoff) is the sharpest retraction-hygiene datum owned | B909 (frontier/B909_frame_arc/FINDINGS.md, cmt_correct.py); routed to B920 (this catch-up) |
| Theorem (classify): a 27-dimensional assembly "exists only for $A_4$ and $2T$" | `papers/structure_paper/arxiv/main.tex` §classification | **REFUTED** — all six admit one (block-sum lemma; witnesses `9×3`, `3×4+3×5`, `27×`linear). 2O and 2I survive and are binary, so `cor:onlybinary` cannot absorb it; the entrance stands on the arithmetic surjection instead | B8080; `verify/check_assembly.py`; theorem restated and `sc:assembly` rewritten |

## 2026-08-08 — B964: two VEV claims withdrawn
1. **"The object does not supply a VEV"** (B952, B959, B960, echoed B962) — **FALSE.** An
   adjoint VEV's unbroken group *is* the centralizer of that element, so the measurement
   cascade **is** an adjoint Higgs mechanism. The object supplies the rank-preserving half;
   it lacks the rank-reducing 27 half.
2. **"The 27-VEV route provably stops one step short"** (B962) — **scope error.** True for
   **27-only** breaking; false in general, since the 78 contains a 24.

**Untouched:** B952/B959/B960's rank obstruction (it was always about *centralizer /
adjoint* constructions), the 27 branching, the F₄=generic-VEV unification, and L138.
**Cause:** using "VEV" loosely to mean "27 VEV". **Rule adopted: name the representation
every time.** Caught by the owner's challenge, not by a gate.

## Currency read 2026-08-13 (the register joins the doc-currency watch; head B1066)

Four retractions this window, each banked in the PR of its correction per the
maintenance rule:

- **"cubic-cyclic K"** (the banking seat) — retracted same-day, proven wrong
  on-bench (a cyclic cubic has square discriminant; disc μ's part is 77);
  corrected to the S₃ cubic with resolvent ℚ(√77). Carried in
  `docs/NOVELTY_SWEEP_LEDGER.md`'s ONE-K block and RETRACTED_PHRASES.
- **"all 18 roots loxodromic" as x-only typing** (the relay audit seat,
  their bdbc4267) — withdrawn under the full-triple rule they authored;
  A5 subsequently certified properly (18/18, deterministic, 60-digit).
  Carried in B1062's M5 addendum.
- **The debt-metric headline** (the consolidation seat, their branch §8) —
  "blind to 191/48%" retracted to the scoped finding (OPEN+RETRACTED
  outside both registers; 20 of 41 uncited); their retraction re-verified
  on this bench (qB1054's checks re-run). Carried in the digest row 4.8.
- **B1066 execution 1's residue** (the banking seat) — the wide-window
  firing on PMNS column 1 and the "armed-for-the-future" framing were
  stale-release artifacts (NuFIT 6.0 vs the current 6.1); withdrawn in the
  arc's own FINDINGS with the two-execution history side by side.

- **B8070's rank descent** (2026-08-17, self-retracted the same day it was written) —
  the claim that anomaly cancellation carries `su(3)⊕su(2)⊕u(1)³` (Lie rank 6) to
  `su(3)⊕su(2)⊕u(1)_Y` (Lie rank 4) and so escapes the `GUT_REQUIREMENTS_LEDGER` §D rank
  obstruction. **Withdrawn in full:** the headline was an f-string literal, not a
  computation; the one quantity actually computed (Killing rank) is 11 on both sides; the
  "before" algebra was degenerate (its three u(1) generators do not commute with
  su(3)⊕su(2)); and the controls tested quantities adjacent to the claim. Independently,
  **B971 had already closed the question NEGATIVE nine days earlier** — on the object's own
  complete 27 every anomaly condition is identically zero. Banked as `frontier/B8070_anomaly_rank_descent`
  (verdict `RETRACTED`), error classes **E843** (new) and **E2** (instance).
- **B864's uniqueness, scope restored** (2026-08-17, B8070; **a sharpening, not a retraction**)
  — *"hypercharge is the unique gaugeable U(1)"* is uniqueness **inside the chosen 3-plane**
  `span(Y, χ, ψ)`, which B864 §3 states and which most downstream rows carry as "in the chain's
  abelian sector". Two facts re-derived: the coefficient `a` drops out identically (`A(Y) = 0`
  is the textbook fact, so the computation says nothing about `Y`), and over the full
  5-dimensional charge space the cubic factors into **three** anomaly-free lines. The unscoped
  phrasing in `docs/OPEN_LEADS.md` L144 has been corrected; B864 carries a banner.
- **The 254-case reality negative, argument re-scoped** (2026-08-17, B8073) — the conclusion
  (*`su(5)` is not real by this route*) **survives**; the argument does not. It measured
  `Stab(s)` (dim 61) rather than the composed `A = (34,24)`, and its τ was the 2-torsion sign
  slice with **no intertwining check**. B8073 tested the right object with a gated τ
  (2106/2106 at three primes) and found Killing rank **3**, with no character in the swept
  family giving 24. Recorded as a true-conclusion-wrong-argument, the pattern B971 already
  carries once. `frontier/B8068_j2t_charge_field/CELL_ITEM1_FINDINGS.md` carries the banner;
  `cell16_reality.py`, `cell18_realforms.py` and `cell20_outer.py` carry the ungated-τ note.
