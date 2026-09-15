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
- **B1123's forcedness DOORWAY** (banking seat, harvested from cc3
  27d9ceb9) — *"E₆ is what level 15 = 3·5 factors into (SL(2,ℤ/15) ≅
  SL(2,3)×SL(2,5) = 2T×2I by CRT → McKay → E₆/E₈)"* is **WITHDRAWN**:
  level 15 is IRREDUCIBLE, not factored (B695/E-3 — the being/hearing
  faces interfere, 59/60 primes falsify L-factorization); the CRT
  conflated the *level* with the *group*; Part III makes no such chain.
  cc3 self-caught it (commit 1a0b5a90); cc had propagated it to ~8
  surfaces (error **E37**). The forced CENSUS (39/43, C6→C17 axiom-free)
  is independent of the doorway and STANDS; E₆ arrives at the object's
  hyperbolic ℚ(√−3) curvature end (2T→E₆ via McKay; B981/B248). Corrected
  in place across all surfaces in the B1127 PR. *(banked: B1123 · corrected: B1127 / E37 / cc3 1a0b5a90)*

## 2026-08-28 (B1188) — the L190 direction-word correction

B1187 banked the Ω-DAG per-level null result with the interpretation "excess transitive reach."
The direction was wrong (higher d_MM = lower ordering fraction = reach DEFICIT); the 11σ number,
the per-level z-trend, and the non-genericity verdict all stand unchanged. Corrected in
B1188/FINDINGS, the GRAND_COMPUTATION_LEDGER, and L190's row; the phrase row added to
RETRACTED_PHRASES. Class: E52-adjacent (an interpretation word passing both bank and review) —
caught by the retrieval sweep's clock/4d lens cross-reading B189's own earlier correction.

## 2026-09-05 (B1248) — "the class restricts to c" (B1192) is REFUTED, not merely unsupported

**B1192**'s headline read *"X₀ induces the nontrivial Galois element on BOTH spectral fields
simultaneously: **the class restricts to c**"*, and described ε as **mirror-odd**. **B1216**'s
addendum already retracted the *eigenline evidence* for that clause as MB12-vacuous (every
anti-conjugator swaps the eigenlines, by construction) while leaving the clause itself standing on
the det = −1 sign.

**The clause itself now falls.** B1248 shows `det X ≡ 2 − κ (mod squares)` with `κ = tr[A,M]` the
Fricke–Vogt invariant, and κ is a function of the Fricke coordinates `(tr A, tr M, tr AM)` — **all
three mirror-invariant**, so `κ(A,M) − κ(A⁻¹,M⁻¹) = 0` identically (Gröbner residue exactly 0). The
class is therefore **MIRROR-EVEN for every pair**, and by **B1161**'s free-orbit theorem a
mirror/Galois-invariant object quantity is constant across branches: **it cannot be c.**

**What stands:** ε = −1 is a well-defined, dimensionless, non-vacuous ℤ/2-valued datum of the pair
(B1248's trichotomy exhibits all four branches and reproduces −1 as `2 − κ = 2 − 3`). **What falls:**
its identification with the orientation bit, and the word *mirror-odd*. Rows F2/H1 keep their
"first realized instance" content with the restriction-to-c clause struck.

**Also corrected here (E60), same arc, self-caught:** B1248's own first draft wrote the
Maclachlan–Reid quaternion algebra as `(tr²A − 4, 2 − κ)`, identifying ε *itself* with the second
Hilbert slot. The true algebra is `(tr²A − 4, (2 − κ)/(tr²A − 4))` — they differ by the first slot.
Caught by computing **2T**: the Q8 pair gives the **Hurwitz quaternions (−1,−1)**, the known answer,
against the wrong form's split `(−1,+1)`. `det X₀ = squarefree(2 − κ)` is unaffected, and the arc's
lock already encoded the correct formula — the test was right while the prose was false. The 2T
control is now permanent. Class: **E60** (a wrong statement whose downstream conclusion happened to
be right, so nothing red).

Corrected at source in `frontier/B1192_close_loop_batch4/FINDINGS.md` (Addendum 2, per E53), in
`frontier/B1248_norm_classification/`, THEOREM_REGISTRY, IDENTIFICATION_LEDGER, CHANGELOG and
CAMPAIGN_STATUS.

## 2026-09-14 (B921-9b) — the seven retractions that never got a row

**The gap, and why every gate was right to be green.** Twelve arcs carry
`"verdict": "RETRACTED"` in their `arc_verdict.json`; **five had a row here.** The
other seven were corrected properly — each arc's own `FINDINGS.md` carries a
correction banner written at the time, so nothing in the corpus was ever wrong — but
the correction never reached *this* index, and this index is what a reader consults
who never opens that arc's file. `retraction-sweep` did not notice, and **that is
correct behaviour**: its rule is *"registered retracted phrases must not appear as
live claims"* — it polices the content of rows that exist. The comment that
introduced `relay-debt` in `scripts/gates/gates.py` had already named the shape:
*"`lawmap-scope` and `retraction-sweep` police the CONTENT of rows that exist;
neither notices a row that was NEVER WRITTEN."* That comment built the third gate for
exactly this failure — **for relays. Nothing did it for retractions.** So this is not
a new discovery; it is **L143's gap, still open on a second surface**, found by a lead
row (B921-9) that had been sitting on it since August.

Closed two ways: the seven rows below, each quoting the arc's **own** stated reason
from its **own** banked record (no reason invented), and `scripts/checks/retraction_debt.py`,
wired as the `retraction-debt` gate — **shown reporting 7 before these rows and 0 after**
(MB12: a check that cannot fail is not a check).

**A note on how the quotes were verified, because the first method failed.** Fourteen quotes
were grepped in their sources **before the rows were written** — and then writing them broke
three, silently: a backtick added inside `M.is_isometric_to(mirror)`, an emphasis marker dropped
from `only the *conclusion* is`, a `"gate"` re-typed with single quotes. Every one still *read*
correctly; none was any longer the source's text. **Verifying the intended quote is not verifying
the shipped one** — the same proxy substitution this window has now named five times. The rows
below are checked by re-extracting all 16 quotes **from this file as it stands** and grepping each
in its own arc's record, resolving the arc by its verdict file's `id` rather than by directory name
(a glob picks `frontier/B58_stage1`, NEGATIVE, over `frontier/B58_sl4_tower_test` — the
grandfathered B58 collision). **16 of 16 verbatim.**

| what was asserted | where banked | the correction | where corrected |
|---|---|---|---|
| B192's metallic Lyapunov-spectrum **parity law** — the SL(n) transfer cocycle's spectrum is symmetric iff `n` is even, realizing V29, and **special to the metallic cocycle** (163× a generic SL(n)) | `frontier/B192_sln_higher_rank/FINDINGS.md` (2026-06-22, ledger V185) | **REFUTED** — *"an artifact of cherry-picked energies"* plus a *"rigged control"*: on a fair broad energy grid the defect grows monotonically with `n` (no alternation; n=4 is *more* asymmetric than n=3), and a **random potential in the same companion** matches metallic (n=4: 0.337 vs 0.344). The 163× compared metallic-at-cherry-energy against a dense-Gaussian matrix with no transfer structure. **Survives:** D1 (spectrum sums to 0) and B166's own results | the same arc, corrected in place 2026-06-23 after independent adversarial verification; its reproducer's checks now *verify the refutation*; third verify-don't-trust self-correction |
| B216's verdict that the `f≥8` class-field period-law split is **genus-theoretic / NEEDS-SPECIALIST** | `frontier/B216_period_law_f8_boundary/FINDINGS.md` (2026-06-26, ledger V219) | **OVERTURNED** — *"an artifact of testing"* `γ≡±I` (only the scalars ±1). The correct invariant is elementary: the form **content** `gcd(b,c,a−d)`; at `f=8` mod 8 has extra square-roots of 1, so `GAMMA_A ≡ 5·I (mod 8)` has content **8**, not the ±I-depth 4 — which was the entire "obstruction". Period is genus-**independent**. **Survives:** *"The validated general-WRT tool built here is correct and reused by B219"*; only the conclusion is overturned | B219 (V222, 2026-06-26), `frontier/B219_period_content_law/`; banner in B216's own FINDINGS |
| B58's headline **"the prediction cannot be tested numerically"** (the SL(4) 7-factor tower), verdict NEEDS-EXPERTISE | `frontier/B58_sl4_tower_test/FINDINGS.md` | **NEGATED** — the ε-extrapolated pinv-ratio route computes the ambient SL(4) 15×15 fixed-line Jacobian, validated against the exact SL(3) anchor and B65's exact symbolic J(1); the spectrum reproduces B59's banked factorization. **Survives:** the fixed-line point *is* the identity representation, where the rep-to-trace map is first-order degenerate, so the naive at-the-point route is genuinely dead — *"What flips: only the impossibility headline."* | B742 (the negatives hunt) + B745 (five independent exact checks, ALL PASS), 2026-07-21; relabeled PROVED → RETRACTED by B831 (R35-4) |
| B702's law **"metallic hearing ⇔ real-quadratic SWAP field"** | `frontier/B702_metallic_hearing_law/FINDINGS.md` (2026-07-19, verifying cc2's E-Q1/E-Q2) | **RETRACTED** — it *"conflated the being-face SWAP with the hearing-face WELD"*: the golden swap's eigenvalues are roots of unity in ℚ(√−3) with **rational** tones, while φ = 2cos108° is the order-10 **weld** in ℚ(√5). So *"both swap fields are IMAGINARY"* and there is no reality asymmetry in the swap at all. **Survives:** E-Q1's exact ℚ(i) silver core ratio, unaffected; E-Q2 corrected to **torsion vs non-torsion**; and the correct hearing statement, at the weld/character field — ℚ(√p\*) real ⟺ p ≡ 1 mod 4 | the same arc's RETRACTION + CORRECTION block (cc2 self-correction, cc-verified, 2026-07-19) |
| B731's headline **"the figure-eight knot group is NON-CONGRUENCE"** — the knot has no finite congruence observer (a NO-GO) | `frontier/B731_object_observer_noncongruence/FINDINGS.md` (2026-07-20) | **RETRACTED** — the arc inferred the 2-adic index had stabilized at 6 from levels 2–6 alone; *"It had NOT"*: the index jumps to 12 at level (2)³=(8), so **m004 IS a congruence subgroup, at level (8)**, and the object-level observer exists for the knot too. **Survives:** the level-2 and level-4 index-6 computations, and the E21 SL/PSL-center lesson | B734 (2026-07-20; cc2 computed, cc verified), later B794; *"the error is logged as E22"* |
| B780's **c-versus-θ gate** — "the gate is VERIFIED" and "applying it halves cc3's enumeration 8→4" | `frontier/B780_galois_reversal_gate/FINDINGS.md` (2026-07-24) | **RETRACTED AS VACUOUS** — `c_sig=(True,True,True)` and `theta_sig=(False,False,False)` *"are LITERALS, not wired to any computed boolean"*, and `classify()` maps them to 'c' and 'θ' by definition, so "the gate rejects the swap" *"cannot fail"*. **Survives (upstream, already banked elsewhere):** c and θ genuinely differ on SL(2) rank-onset, on action type (diagonal vs the permutation (1 4)(2 5)(3 8)(6 7)), and on the B766 solo axis — *"Those differences are real"*, and the gate built on top of them added nothing | the B784 adversarial audit, 2026-07-24; banner in B780's own FINDINGS |
| B1181's amphichirality closure — the family is **83 of 83 amphichiral**, zero exceptions, spot-verified 5/5 | `frontier/B1181_amphichirality_closure/` (banked 2026-08-27, `37e1521c`; FINDINGS authored 2026-08-29 under R52-4) | **RETRACTED 2026-09-02** — *"the closure was measured by M.is_isometric_to(mirror), which is orientation-blind"*; by `symmetry_group().is_amphicheiral()` the family is **38/112 amphichiral**, and `o10_150700` — *this arc's own spot-check witness* — is **CHIRAL** at CS = −1/12. **Survives:** THE ONE-WAY FAMILY TEST method-law minted here stands, and this retraction is its second instance | B1235, 2026-09-02; recorded in the arc's own `arc_verdict.json` `retracted` block with its stale phrases, which `RETRACTED_PHRASES` and the `retraction-sweep` gate already carry |

## Currency note — 2026-09-15, through B1410 (the consolidation merge)

Read at the merge of the two cloud lanes (B1325–B1410; outside-bench memos 185–233) into main; each item from its own record, not from a summary. **Retractions and corrections in the window:** B1410 Addendum 1 (the lane's own headline withdrawn: B871 had already paid the owed definition; the arc's P1 verdict stands, the blocker is now a proved impossibility, B713/B760); B1346 §6 (a document seat's "drill(M(A₁)) = M(A₂)" refuted: the drilled manifold is the two-cusped m129, re-checked on main); B1345 addendum (its F6 refutation WITHDRAWN, E58); B1332 addenda 2–3 (the isotropy reduction needs both V and V*, with a counterexample); B1264's verdict file ("EIGHT measured instances") corrected to its lock's five across 11 live uses; B1401 addendum 1 ("attained in all five" corrected to four of five); B1349 addendum 5 ("four of six" withdrawn to "one of four"). **On main's own side this session:** the paper's family-wide amphichirality sentence (B1181, retracted by B1235) removed from the paper, E53 #30; the "16σ" framing of the crossing withdrawn (B915 addendum); the outside bench's item 2 framing the TOE ledger's "counts 2" against B1321's "3" as different quantities. Nothing here reverses a banked verdict; every item narrows a headline to what its record proves.
