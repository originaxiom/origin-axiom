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

## Currency sweep of the SM seat's range, B1249–B1370 (2026-09-16)

*The register lagged the corpus by 61 arcs (doc-currency). Read against the seat's PROGRESS_LOG entries for B1267–B1370: the
banked-then-corrected statements of that range, in the table's own format. None is a retraction in full; each is a correction of
scope, of a prediction, or of a wording that a reader of the original FINDINGS could still act on. Later arcs of the range
(B1369, B1370) banked no correction of an earlier banked claim — B1369's first run's hard-coded sentence about the one-cusped
members was corrected before banking and never entered the record.*

| what was asserted | where banked | the correction | where corrected |
|---|---|---|---|
| B1267 §1's transport scope (the golden E₈ along Q read wider than the object supports) | B1267 | CORRECTED by addendum (E66) — the transport is the two faces' (ALE Γ = 2I, holonomy = 2T); I-26 note corrected | B1268 |
| B1270's "θ" named as the outer automorphism of the fork | B1270 | CORRECTED (E69) — the involution is the inversion (conjugation): outer, 2 fixed roots, signature 1/5 | B1272 |
| B1301's prediction of new odd support at Y₂₀ and Y₂₂ | B1301 | WITHDRAWN — the law corrected: new odd support only at odd levels (Y₂₀: nothing at 41; Y₂₁: 48 947) | B1303 |
| B1281 §2D's caveat: the exact product mode sin(4πx)·cos(2πy) on the object's cusp giving χ(∂⁺) = ±4 | B1281 | SCOPED — that mode's zero set is non-transverse (eight crossings), where ∂⁺M is not a surface and χ is undefined rather than non-zero; adding 0.05 of a generic odd mode resolves the crossings and gives 0 (verified on main, B1417) | B1281's scoping note (2026-09-16), main's B1417 |
| B1351 §2 (ii)'s "torus acyclic ⇒ N = 0", read as convention-free | B1351 | SCOPED — holds under the whole-torus and annular conventions of ∂⁺M (rows A–C of the I-26 table), not under the disc conventions (rows D–F), where the bridge lane reads a conditional net three (the audit lane's R23) | B1351's currency note (main's B1413 harvest, 2026-09-15) |
| B1363's "eleven order-4 classes" of the descent's lines | B1363 | CORRECTED in wording — eleven classes, eight of exact order 4 | the harvest of main's B1415 (2026-09-16) |
| B1365's L215 remedy with a "quartic cap" (a Planck-suppressed term capping ⟨N⟩) | B1365 | CORRECTED — M-theory supplies no such term; every term joining apex fields is instantonic, so the cap is a hierarchy of cycle actions the object does not fix; the remedy itself then excluded by the pincer | B1367 (and the letter's postscript, 2026-09-16) |

*Standing since then: B1368, B1369 and B1370 are negatives and an open narrowing with nothing retracted; fc R71's region-swap
lemma was generalised (B1369 §3 (ii)), not corrected.*
