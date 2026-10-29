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
| **"no closed hyperbolic filling of m004 is arithmetic"** (and "the min-volume closing is non-arithmetic"; "174 closings, still 0 arithmetic") | `frontier/B288_.../FINDINGS.md` (2026-07), extended by B291, B294, B296; docs/THEOREM_LEDGER.md; THE PAPER's filling row | **FALSE, and the test could not have failed (E82).** The criterion applied was the CUSPED one -- imaginary quadratic invariant trace field -- on CLOSED manifolds, where it is never satisfied, so the sweep's zero was guaranteed by construction rather than measured. By the closed criterion (one complex place, integral traces, quaternion algebra ramified at every real place) **six of the 78 fillings in the grid are arithmetic**: m004(+-5,1) (the Meyerhoff manifold, x^4-x-1, disc -283), m004(+-6,1), m004(+-8,1). What survives unchanged: 0 of 174 closings have an imaginary quadratic invariant trace field, which is a different and true statement | `frontier/B1419_the_arithmetic_fillings_corrected/` (2026-09-16), owner-caught; phrases registered in `docs/RETRACTED_PHRASES.md` 2026-09-17 (B1422) |
| **"whose timeout was tuned to an idle machine"** / "failed once under the load of a 146-file run" -- the diagnosis of `test_b1355_geometry_is_exact`'s failure | `frontier/B1424_the_referees_defects/FINDINGS.md` and its verdict (2026-09-17); the lock's own comment | **WRONG DIAGNOSIS, and the fix fixed nothing (E83).** The lock is not load-sensitive: its script solved for the commutant with a SET as the list of unknowns, so sympy's normalisation moved with `PYTHONHASHSEED`. The shipped version passes on seeds 4 and 7 of 0-7 and fails reproducibly on the other six; raising the timeout 600 -> 1800 s would have preserved a lock failing three runs in four. A reproducible failing set is what distinguishes this from flakiness | `frontier/B1425_the_flaky_lock_and_the_hollow_green/` (2026-09-18) + `frontier/B1424_the_referees_defects/ADDENDUM_2026-09-18_THE_DIAGNOSIS_WAS_WRONG.md` |

## Currency note — 2026-09-15, through B1410 (the consolidation merge)

Read at the merge of the two cloud lanes (B1325–B1410; outside-bench memos 185–233) into main; each item from its own record, not from a summary. **Retractions and corrections in the window:** B1410 Addendum 1 (the lane's own headline withdrawn: B871 had already paid the owed definition; the arc's P1 verdict stands, the blocker is now a proved impossibility, B713/B760); B1346 §6 (a document seat's "drill(M(A₁)) = M(A₂)" refuted: the drilled manifold is the two-cusped m129, re-checked on main); B1345 addendum (its F6 refutation WITHDRAWN, E58); B1332 addenda 2–3 (the isotropy reduction needs both V and V*, with a counterexample); B1264's verdict file ("EIGHT measured instances") corrected to its lock's five across 11 live uses; B1401 addendum 1 ("attained in all five" corrected to four of five); B1349 addendum 5 ("four of six" withdrawn to "one of four"). **On main's own side this session:** the paper's family-wide amphichirality sentence (B1181, retracted by B1235) removed from the paper, E53 #30; the "16σ" framing of the crossing withdrawn (B915 addendum); the outside bench's item 2 framing the TOE ledger's "counts 2" against B1321's "3" as different quantities. Nothing here reverses a banked verdict; every item narrows a headline to what its record proves.

## 2026-09-17 (S15, B1422) — "THE PHYSICS CHAPTER IS CLOSED" was never scoped, and the repo held it against itself

**What was carried:** B82/V65 (2026-06-05) banked *"there is no physics here … the physics-probing chapter is
**closed**; future runs should not re-litigate these kills without genuinely new evidence"*, reinforced the next day
by B96. The verdict's own scope is the SL(n)-tower bridges (anyons, quasicrystals, j = 1728, higher-spin, quantum
groups). It was stated **unscoped** on `ROADMAP.md` and `ARCHITECTURE.md` as a standing governance gate and echoed on
about eight further surfaces, with `arc_verdict.json` carrying `superseded_by: null` and this registry carrying no row.

**What happened instead:** the programme ran a different route entirely — E₆ via the McKay door and the 27 — and
`GOVERNANCE.md` §2 was amended with the owner's approval on 2026-08-25 (`b72d87f2`) to *"derives the form of
Standard-Model structure"*. A 51-page paper now rests on that route. **For fifteen months the repository asserted a
no-re-litigation gate and simultaneously litigated past it, and neither surface knew about the other.**

**The correction (not a retraction of B82):** B82's kills stand on B82's routes. The gate is scoped to them, in place,
at both top-level surfaces. Nothing in B82 tested the E₆/27 route, so nothing in B82 licenses or forbids it.

**The lesson, filed:** a verdict that closes a *chapter* must name the routes it closes. An unscoped closure is
unfalsifiable by later work — it cannot be superseded, only ignored, which is what happened.

## Currency read 2026-10-07 (window B1423–B1483; written when the corpus head reached B1483)

Banked-then-corrected statements of the window, each with its correcting locus. Statements that were sealed as
predictions and failed (B1477's first form of the shear law; "a survivor exists ⟺ CS = 0"; B1480's and B1481's failed
predictions) are not here: they were never asserted as results.

| what was asserted | where banked | the correction | where corrected |
|---|---|---|---|
| "the mirror genuinely swaps the geometric spin structure iff 1 ∉ η₀K", K the span of the preserving isometries' sign characters found by a bounded search — stated as a law | B1474 §3 | WITHDRAWN AS A LAW — isometries act on spin structures affinely, a span is not an orbit and a bounded search is not coverage (the audit lane's R92). The seven SWAP verdicts stand on other routes: no real odd torsion (B1476 §2b) and Theorem A (B1477) | B1474 addendum 2026-10-07 |
| "s961: 4 of 8" (and o10_150707: 4 of 8) mirror-invariant spin structures, read as counts | B1475; B1476 C1 | SHARPENED — lower bounds from exhibited witnesses; all 8 (resp. 4) are torsion-real; the exact numbers are not on the record | B1475 addendum 2026-10-07 |
| "Cusped manifolds whose reversing isometry fixes no cusp: ¼ is excluded" (the swap corollary) | B1239 §3 | FALSE AS STATED — the proof fills cusps in swapped pairs; a mirror can fix no cusp and still move some in an odd cycle (o10_150729: a 2-cycle and a 3-cycle, CS = ¼). True when there is no odd cusp-orbit | B1239 addendum 2026-10-06; B1477 (the orbit form) |
| GAP6: "a flat bundle has ch = rk: no index built on it can tell 27 from 27̄ … a statement about curvature … that no flat frame carries", without hypotheses | GENESIS v1.9 (B1466) | NARROWED to its closed-bulk, characteristic-class hypotheses (v1.11, B1476; the audit lane's R89 and the web seat); v1.11's own "cannot reach continuous values" then CORRECTED to "continuous moduli" — a rigid flat point fixes numbers (v1.12, B1478; the web seat's A2) | GENESIS v1.11, v1.12 |
| GM5b: inverse moves are "needed for the signed states" | GENESIS v1.0–v1.13 | CORRECTED — they suffice and are not needed; one central move, −I, is, and positivity (GM5d) is what excludes it | B1482; GENESIS v1.14 |
| "'symmetric phase' occurs nowhere on main (0 of 1337 arcs)" | lead L244, 2026-10-03 | CORRECTED — lead L17, B849's seal and B853's script carry it; an absence read off a tool beyond its domain (found by the SM seat's sm:B1531) | B1467; GENESIS v1.10 |
| "the trace map never reads κ", resting on B37's self-model test | B37 | UNSUPPORTED BY ITS TEST — the predicate cannot fire on any map written in x, y, z (the audit lane's AR3); whether the map reads κ is fork FK12's, open | B1463 |
| "empty k-elimination ⇒ κ free ⇒ no choice" (the inference) | B130 | INFERENCE INVALID, CONCLUSION KEPT on its domain by a valid argument (the audit lane's AR4) | B1463 |
| one sentence of B1455's addendum and GENESIS FK12 (ii) on which symmetry dualises Ballas' family | B1455 addendum; GENESIS FK12 (ii) as it stood before v1.7 | CORRECTED — P is the swap and fixes the family; the dualising symmetry is the strong inversion (sm:B1521 C1, re-derived) | B1462; GENESIS v1.7 |
| "the floor applied to both orders gives \|I(W₁)\| ≤ m_A + b0 on any finite cover" (B1487 T3 as sealed; T-THREE-NEEDS-ENDS; a LAW_MAP row) | B1487 | DOES NOT FOLLOW — the opposite order's dual is W₁ again, so no upper bound comes from the floor; refuted by the SM seat's records (18 readings above m_A + b0); the ceiling is I(W₁) ≤ 2m_A + m_B − b0 (sm:B1545's update). The generation-side conclusions stand | B1487's addendum of 2026-10-07; the SM seat's relay THE ENDS AGREED |
| "the weave's lifts on T form only a projective representation of Mp2(ℤ); χ_{3/2} is fixed only by W41's multiplier, unverified on main" (B1632 C1 as sealed; GENESIS v1.40) | B1632 | REFUTED, COMPUTATION KEPT — the lift helper's sign on S̃; the move matrices are a genuine Mp2(ℤ) representation, exactly the theta constants' multiplier, χ_{3/2} = 0 for it; B1632 stays NEGATIVE as sealed | B1634 (GENESIS v1.41) |
| "m₁ = 0 for a section without a ∂²R component"; "the weight-3/2 section ∂R gives a massless first generation" (B1691's table and first addendum; the S160–S163 status lines) | B1691 | CORRECTED (scope) — B1654's large-L limit; at the canonical end of order one (B1667) the first generation is lifted, m₁/m₃ ∝ 1/L² (found by main, S164) | B1691's correction; B1694 |
| "a flat line splits the sectors' m₂/m₃ by at most four" and "one Higgs is EXCLUDED in this frame" (B1692, B1693 as banked; THE_WEAVE, LAW_MAP) | B1692; B1693 | CORRECTED (scope) — both hold for B1653's point coupling, the large-L limit; at the canonical end of order one the spread reaches 7.7–10.8 and B1695's one-Higgs point fits all six ratios within 1.8 (found by main, S167) | B1692's and B1693's corrections; B1695 |
| "adding trivial-sector Weyl fermions holds τ at i or near ω"; "on Re τ = ½ the gauge contents give saddles" (B1704 as banked; THE_WEAVE) | B1704 | CORRECTED (scope) — Re τ = ½ is not a mirror line once the Higgs's copies are in, so the Re ½ entries were not critical points; the minima lie on the unit arc between i and ω + 1, still far below the band (found by the SM seat, relay 197; checked on main, S180) | B1704's correction |
| "the up and down quarks' [first generation] lifted on every line" (B1712 §2); "the exact first-generation zeros are exactly the law's … and nowhere else" (B1713 §3); "D vanishes exactly where the law says, on every line of order 1–12" (B1716, Z6); "det M = ¼ Σ c_s R_s², independent of L" without its condition | B1712, B1713, B1716 | CORRECTED (scope) — on Re τ = 0 the up and down quarks also vanish on the 16 order-12 lines with 12α odd, a family the zero law does not name (P-292); the whole-grid statements and the law at generic τ stand; the determinant identity holds when no channel is clipped (min 2πL + c_s = 1.24 on the grids); found by main's math referee (the integrity sweep, S188), checked on the stored outputs | dated corrections on B1712, B1713, B1716 |
| *— CATCH-UP (2026-10-28, S235; found by the doc-currency gate at B1802: the same-PR rule lapsed after B1716; six rows owed since B1724) —* | | | |
| "the mixing best (1.203)" (B1720) and "the mixing best (1.51, next to i)" (B1723), read across B1660's three up readings | B1720; B1723 | SHARPENED — both were S* rows, and S* is covariant only under Γ⁰(2), so each was one sheet's value; with the covariant readings they are 1.225 (29.48% of random mixings as good) and 1.851 (40.20%). Every verdict stands (T2 still fails at 1.475%; the mass cells fail) | B1724; the dated addenda of 2026-10-22 on B1720 and B1723 |
| "with τ placed by a rule" — the six reached with τ at a thread's apex, read as the thread rule selecting τ | B1741 | CORRECTED (scope) — the specific rows form one strip (Im τ 2.96–3.11, the order-10 lines (2/5, b)) that any ~100 points in the band find; the specificity is the frame's, with c = 3 and the seat's reading; that the rule places τ is not shown (P-350). Later, neither B1749 nor B1753 is PASSED once c is chosen in the null (B1798) | B1749; B1741's dated note of 2026-10-24; B1798 |
| B1795's preregistration: "two lines' pair values seen before the seal" | B1795's PREREGISTRATION (sealed 24b9e468d) | CORRECTED — the peeked (0, 0) values were the H pair's Dn on 10 lines and the D pair's on 6 (14 distinct lines), since Dn depends on the twist class only; no outcome affected (an E75 instance) | B1795's FINDINGS, the disclosure dated 2026-10-28 (S232) |
| THE_COMPLETION_MAP's gap 3: "one open link … FK10 reduces to FK15" | docs/THE_COMPLETION_MAP.md | CORRECTED — FK10's unit reduces to four links (the field's existence FK15, a type identification, uniform end data, the least remainder), given Λ and the hand, none derived | B1796; B1797 (GENESIS v1.59) |
| L251's status line: "registered, not computed" | docs/OPEN_LEADS.md (L251, 2026-10-13) | STALE — the currency note of 2026-10-15 already records L251 computed in the fibre's point frame (B1642, B1644: a rank-two residue coupling; B1653); B1800 then computed it as stated, as flux-mode bulk overlaps (Y ∝ η^{3/2} θ_r^{−1/2}, not B1636's θ_r²) | B1800 (S233); the dated note on L251 |
| "the retired ruled-branch weave" (B1799 § Seen first) | B1799 | UNSUPPORTED — the record retires τ = ω on the ruled branch (GENESIS v1.35, B1640), not the branch itself | B1800's referee; B1799's dated note of 2026-10-28 (S233) |
| THE_PATTERN_MEDITATION_3 Part I item 4: "the most repeated hatch was never opened: 'a principle that selects the point'" | docs/THE_PATTERN_MEDITATION_3.md (S234) | CORRECTED — selection by the frame's own one-loop potentials was tried on the SM seat's branch (W51, W59, W60, W62, W154, W167, W169) and lands at mirror-fixed points; W175 finds CP-conjugate minima on the mirror-free classes; none holds the height | the SM seat's §325 (harvest row 1454); the meditation's dated note of 2026-10-28 (S236) |
| the six's best rows read as fits 'at L_max', the maximal embedded horoball (B1667's canonical end) | B1726's compute() (L = L_max(Im τ)); B1741, B1749, B1753, B1786 | CORRECTED (scope) — the frame takes the end through the small-cut norm 2πL + c_s; at L_max the exact twisted norms lie 35–38% below it (0.6% at L₂); with the exact norms the down and lepton m₂/m₃ fall 0.47–0.73 in ln and the six fail near the four families' rows (the web seat's sealed look; local refits). The rows are fits of the small-cut formula at L_max's height; the scale's geometric ground is lost (P-421). None was PASSED | the web seat's THE EXACT END (harvest row 1459), reproduced on main (S238); dated notes on B1726, B1741, B1749, B1753, B1786 |
| "∣V_ud∣ ∝ r^½" under the Standard Model's reading (a law); "that reading misses the six (χ² 52.7)" | B1739 §§ 3–4 | CORRECTED (scope) — the slope 0.52 is the median's (quantile slopes 1.24, 1.14, 0.52, 0.22); the 52.7 is the six at the nine's best row, the all-S̃ reading's own least being 22.36; P-345's '∝ r^½' unearned | the web seat's audit (harvest row 1461), verified on main (S242); B1739's dated note |
| "the dichotomy is sealed" (in general); control C1(iii) as a check | B1740 § 2, PREREGISTRATION C1 | CORRECTED (scope) — sealed for F₋₂ only; C1(iii) compares two algebraically identical expressions and tests nothing (an E2 instance) | the web seat's audit, verified on main (S242, by the code); B1740's dated note |
| "two holomorphic Higgs objects cannot do it" (the reading split); "nearly reading-blind" | B1790 § 3 | CORRECTED (scope) — on the mirror lines a holomorphic section (DR with K negated, at τ or τ − 1) reproduces the S̃ reading exactly (Γ⁰(2)-covariant only); off them it does not; 'reading-blind' for the coarse measure only | the web seat's audit, verified on main (S242); B1790's dated note |
| m₂/m₃ "→ ½" / "½ exactly at ω and at i" / "between 0.295 and 0.500 on LR's geodesic"; the t = −5/288 "pole" | B1691 (its ω table, its S163 addendum) | CORRECTED — B1691's at() returns the bounded proxy s₁s₂/(s₁² + s₂²) ≤ ½, not s₂/s₁: its ½ means m₂/m₃ = 1 (an exact degeneracy); the true range on LR's geodesic is [0.536, 0.983] (0.295 a truncation artefact); the 'pole' is a section with a·a ≡ 0; the exponents unaffected | B1806's referee, verified on main (S245); B1691's dated note |
| "a₀ … m₂/m₃ → ½ (0.484, 0.496, 0.499, 0.4998)" | B1697 | CORRECTED — the same proxy; the exact ratio → 1 (0.885, 0.975, 0.9989 at Im τ = 2, 3, 5); the conclusion (no cusp hierarchy for a₀) stands | B1806's referee, verified on main (S245); B1697's dated note |
| near ω, "k ≡ −½ mod 6 (23/2; at −½ and 11/2 m₁ = 0): m₂/m₃ ∝ ∣ε∣², m₁/m₃ ∝ ∣ε∣³" | B1691 (its ω table) | CORRECTED (scope) — B1646's L-free coupling; at the canonical end radius (L = 0.65, 2.5; B1667) m₂/m₃ ∝ ∣ε∣ and m₁/m₃ ∝ ∣ε∣³ at 23/2 and at 11/2 (the channel norms' first-order splitting near ω); the 15/2 and 7/2-class rows stand | P-433, main's own route (S248); B1807's referee; B1691's dated note |
| "the sections without ∂²R at 15/2 and 23/2 give m₂/m₃ ∝ ∣τ − i∣²" | B1806 | CORRECTED (scope) — the L-free coupling; at the canonical end radius m₂/m₃ near i is flat and nonzero (0.272 at L = 0.65, 0.0211 at L = 2.5) and m₁/m₃ ∝ ∣τ − i∣² | P-433, main's own route (S248); B1807 § 4; B1806's dated notes |
| "the residual of that line is ≤ 0.07 everywhere" | B1785 (its § 1) | CORRECTED — 585 of 15 888 three-height fits exceed 0.07 (515 m₁/m₃), 67 exceed 1, max 5.52 (leptons, L₂, S̃, m₁/m₃ on (0, 1/12)): no leading power at those heights | the web seat (THE FRAME NULL relay § 5), recounted on main (S256); B1785's dated note; P-444 |
