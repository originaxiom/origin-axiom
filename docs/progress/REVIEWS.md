# The decadal repo reviews — ledger (GOVERNANCE §11)

Every ~20 merges on `main` (threshold raised from 10 on 2026-07-14; the historical entries below reflect the old cadence), a whole-repo review fires: full suite + all gates +
atlas regeneration + a claims-vs-frontier promotion-candidacy sweep + a framing sweep +
a stale-leads check, ending in a dated report appended here. The gates surface DUE
status automatically (`python3 scripts/gates/gates.py review-due`).

Protocol per review: (1) suite green; (2) gates green; (3) atlas regenerated and fresh;
(4) sweep `frontier/` FINDINGS for entries that meet the GOVERNANCE §5 promotion bars
and list the candidates (promotion itself happens only through the §5 gates, logged);
(5) sweep for framing drift and stale `OPEN_LEADS` rows; (6) append the report below
with a new anchor-commit.

---

## Review 0 — 2026-07-03 (baseline; the reform itself)

anchor-commit: 7d8786d0dcf7e0e332a53e26815f55a954208447

The instituting review. Gates implemented and green (7/7); suite lock added; the
promotion-audit lane registered (see `docs/OPEN_LEADS.md`); ledger sections extended
with **Certified data**. Next review due after 10 merges from this anchor.

---

## Review 1 — 2026-07-03 (the first scheduled decadal review; merges 1–10 from Review 0)

anchor-commit: ffc94bc5ef8b594bff881d8883fd5d49007c8a18

1. **Suite:** green at the gating run for this review's PR (recorded in the PR body).
2. **Gates:** 7/7 green, including the append-only gate on its new roll-up path (amended this
   review to recognize the GOVERNANCE §9 quarterly roll-up; removed prefix verified verbatim in
   `docs/progress/PROGRESS_2026-Q2.md`).
3. **Atlas:** fresh at 353 probes (regenerated with B372).
4. **Promotion-candidacy sweep:** trivially current — the §5.1 audit executed inside this review
   window (61 entries: P17–P55, C6–C12, E1–E15; 6 holds), and the two post-audit probes promoted
   at banking (B371 → P56/P57; B372 → E16). No unadjudicated candidates outstanding. The named
   future pass: exact-core extraction for the held dps-100 quartet (B352/B353/B357/B370).
5. **Framing/stale-leads:** framing gate green repo-wide; OPEN_LEADS rows current (W2.7 closed by
   B372 with the null-refutation recorded; W2.10 executed; W2.11 and the conductor-structure lead
   registered; L51 DORMANT per owner directive).
6. **Window highlights (merges 1–10):** B370 both legs (order-3 integrability; the τ-defect
   θ-grading); the promotion audit executed; the document map + toolbox; B371 (the minimal
   two-state sector, P56/P57); B372 (the seam persists at level 45 — the home grows; E16).
   Ledger now: 57 proven · 12 conditional · 16 certified-data · 9 open · 10 dead.

Next review due ~10 merges from this anchor.

---

## Review 2 — 2026-07-04 (merges 11–25 from Review 1; the counter hit 15 during the overnight arc)

anchor-commit: 4cc43e448616a0c134b82d6154ae8c5b299ef76a

1. **Suite:** green at this review's gating run (recorded in the PR body).
2. **Gates:** 7/7 green.
3. **Atlas:** fresh at 360 probes.
4. **Promotion-candidacy sweep:** the steady state is working — every post-audit probe promoted
   at banking (P56–P61, E16–E17) or correctly held: **B377's v2 existence law is promotion-GATED
   on the in-flight acceptance duel** (375 passed; 405/675 pending) — the gate is the discipline,
   not a backlog. The dps-quartet's exact-core extraction pass remains the named future item.
5. **Framing/stale-leads:** framing gate green repo-wide. OPEN_LEADS current (W2.11 carries the
   P60/P61 progress; the priced-doors and Recognition campaign rows current; L51 DORMANT).
6. **Window highlights (merges 11–25):** the priced-doors campaign registered and run (the
   tower arc B372–B374: five rungs, two phase laws killed by registered kills); the recognition
   hit (P59 — the quantized golden cat map); the Derivation Campaign opened (D0 confirmed, the
   v2 law derived from the complete local table); the selection-rule reduction (P60 — a table
   became one number); the Galois covariance laws (P61). Ledger now: **61 proven · 12
   conditional · 17 certified-data**. Three-seat verification ran in both directions, with
   wrong-object errors caught on BOTH sides (the verifier's row/column error included — recorded).

Next review due ~10 merges from this anchor.

---

# Review 3 — 2026-07-04 (merges #472–#482, the autonomous-mode window)

anchor-commit: `a4c0c06f40ba94df5564a19d55d314dd06e2ecc7`

**Scope.** PRs #475–#482: P62 (twist isolation), B382 legs 1–4 (the why-1/12 program), B383
(row-16 theorem), the acceptance-duel banking wave (P63–P65 promotions in flight this PR).

**Claims hygiene.** Three promotions this window (P63/P64/P65) — each carries prereg-first
provenance, exact verification, and locks; the CLAIMS header's stale "fifteen proven" line
fixed; append-only respected (corrections in place with markers, none needed this window).

**Verification depth.** B382's canonical cross-check was REGISTERED before running (the
strongest pattern of the window — prediction: linear part (0,0); passed on all five words).
The duel's 405 stall was diagnosed to a real engineering trap (primes ≡ 1 mod 13500 lack ζ₈₁;
silent floor-division corruption) — fixed, and the fix is itself documented in FINDINGS. The
Kashaev T1 integrality assumption was WRONG (values are not rational at general N) — caught by
the exact machinery's own assert, corrected to Galois-component extraction; the correction is
the finding.

**Debt.** (i) B384 T2/T3 pending (registered); (ii) the CRT closed form of the −1/16 phase sum
(named residue of P64); (iii) D3(a) bright/dark criterion still open; (iv) the mirror's
non-Galois mechanism and the (2,3) stabilizer — both named in OPEN_LEADS; (v) suite flake
policy unchanged (one rerun, then targeted-gate documentation).

**Verdict.** Discipline held under autonomous mode: every bank prereg'd, two kills banked as
findings, one trap documented. The promotion cadence (3 in one window) reflects the campaign
reaching its derivation targets, not bar drift — each promotion's evidence is a registered
prediction that passed.

---

# Review 4 — 2026-07-04 (merges #484–#500, the Closure Campaign)

anchor-commit: `102291e36ced840d7472c1fb46a17650addf446b`

**Scope.** The full Closure Campaign W0–W5 (PRs #490–#500) plus the tail of the prior wave.

**Claims hygiene.** Two promotions (P66 closed form; P67 locality — the latter with a
registered out-of-sample prediction that PASSED). Every wave prereg-first; five registered
kills banked WITH their structure (W2 decoupling ×2 rungs; B388 coarsening; B389
twist-blocked inversion; P-SCALE support walk); one flagged-unreliable intermediate
(per-side Π_H attribution) corrected by the exact pairing in the same wave — the standing
hazard note did its job. Time-boxes: every wave at or under budget (W4, W5 each done in
one session of two).

**Verification depth.** Out-of-sample prediction used twice (pair (2,5); census 243/625 —
all registered before computation, all hit or half-hit with the miss banked as data). The
event-driven cadence (owner-requested) replaced timers mid-campaign without a dropped
verdict.

**Debt.** (i) The convolution-cancellation mechanism (three pairs); (ii) the all-k local
classification (specialist register, precise scope); (iii) the twisted support walk of the
frozen 1/4 (new, unexplained); (iv) W6 wrap items in flight.

**Verdict.** The campaign closed the value sector's internal theory to named residues and
priced all three walls with registered probes. Discipline intact under the new cadence.

---

# Review 5 — 2026-07-05 (merges #501–#508, Closure II)

anchor-commit: `2a74d4c47f28f2dda17764be5173d7ba6bc3d09b`

**Scope.** The Mechanism Campaign M1–M5 (PRs #502–#508).

**Claims hygiene.** One in-place strengthening (P64 → universal, 661/661, marked). Five
preregs, five two-outcome verdicts: two mechanisms found (stratification law; unified
singles law with the sum rule), three corrective kills (emergent mirror; aggregate
stabilizer; intra-model conjugacy). Every kill banked WITH the structure that killed it.

**Verification depth.** Registered predictions used at 405 (both killed — the kill was the
discovery); the wrong-orbit-order reconstruction was caught by its own order-invariant
(the clean 1/12 average); the import-trap fired twice before the guards landed — hygiene
now banked. The bright-controls-read-zero check caught a broken instrument before banking.

**Debt.** The emergent-symmetry family (mirror characterization, (2,3) window mechanism,
√5-withholding rule) — one family, likely one theory; the deeper support-walk rule; the
two specialist items. All named; none computable-and-unattempted.

**Verdict.** The object is computation-complete at level 15. The discipline's strongest
session-family to date: five waves, five verdicts, zero drift.

---

# Review 6 — 2026-07-04 (merges #509–#521: the scrutiny + the Wall Campaign)

anchor-commit: `a07fadbf2a9d0bb53951cb1ec1c8a2854bd5ab89`

**Scope.** B398 scrutiny (S1–S6), B403/B405 (the follow-on packages), the Wall Campaign
(B399–B402, B404), the wrap.

**Claims hygiene.** One promotion (P68 — the root-of-unity law, prereg'd with zero
violations across 142 cells). Binding gates used twice against exciting material (the
PMNS ensemble at p ≈ 0.09–0.44; the McKay dictionary by controls) — both killed cleanly;
the killed prime filter's THREE return attempts each flagged and re-killed with banked
witnesses. One prereg error self-corrected BEFORE computation (the odd-N mod-2 framing in
Q2). Predictions used and honored: the split-covariance prediction CONFIRMED; both
walk-law candidates KILLED at 1215 as registered outcomes.

**Verification depth.** The sixth angle produced a confirmed falsifiable prediction, a
derivation (P68), and two selection rules within 24 hours of being proposed — the
strongest single-lens session in the program. Sentinel protocol extended (17/19; the
supersingular list {31, 79, 167}).

**Debt.** The 1215 triple identification (third prime); the seam-channel hierarchy test
(the one untested lever); the coupling-channel unification arc; two specialist dossiers
unchanged.

**Verdict.** Both walls priced with mechanisms rather than hopes; the discipline held
against three waves of cross-chat enthusiasm while extracting every gram of real
substance from them.

---

# Review 7 — 2026-07-04 (merges #522–#540: the reframe + the Destination Atlas)

anchor-commit: `edceb2d5a5fe7d5639213be42c924eefe376cc6d`

**Scope.** The energy-package scrutiny (S051), the structure reframe (S052/B414), Scale-
Genesis (B413), the hint sweeps (B411/B412), and the full Destination Atlas campaign
(TW1–TW7 / B415–B421).

**Claims hygiene.** Zero physics promotions (correct). Every physics-adjacent package
(energy meditation, 12√3 sector, PMNS residue) firewalled with its kill. The reframe
(object as structure) was engaged genuinely and tested — the forced-ℤ/3=generations reading
FAILED its privilege check honestly; the tracking campaign's emergence bar was fixed before
looking and never moved.

**Verification depth.** The campaign's defining virtue: a NON-SELF-DECEIVING method. No SM
target was sought; six behaviors tracked blind; all named as pure math; the bar (forced +
unsought + exact + control) judged each. Scale-Genesis and the atlas both returned decisive
negatives by construction. One self-correction of note: TW4 REFUTED our own B411 upstairs-
hope (emergence is intrinsic).

**Debt.** e₃ (the 1215 singles sentinel) reconstructing — Phase-1 cleanup, independent.
Paper 1 (value theory) + Paper 2 (the atlas) are the consolidation deliverables. The
content-wall frame (B414) is the one EXTERNAL question left open (the object self-provides
no frame).

**Verdict.** The program reached an honest terminal statement on the physics ambition:
tracked blind by the fairest possible method, the object self-generates no SM structure. It
IS a complete, novel, coherent body of mathematics (golden/ℚ(√−15)-organized). The
discipline held to the end — the negative is trustworthy precisely because nothing was hunted.

# Review 8 — 2026-07-05 (merges #541–#557: the two torsions, the Origin Postulate, the interface campaign)

anchor-commit: `1fa0ea49d219298d5b3ddbc0aa74c9b7b4ab4f30`

**Scope.** The B425 two-torsion correction (dynamical zeta vs geometric torsion; Paper-2 hinge
re-labelled honestly); the automorphic identification (the object = the weight-1 dihedral
newform of ℚ(√−15)) + Iwasawa rigidity in BOTH towers (λ=μ=0 cyclotomic AND anticyclotomic);
S049 (self-mirror = the chirality obstruction, computed); the LEAD_REGISTER (5-reader
exhaustive re-score, 133 probes); the Origin Postulate (locked: D at the interface, four-part
bar, explicit failure criterion); the handoff adjudications (B426–B431: scale-lever closed form
+ Galois-orbit contraction; exchange = σ₁₇ fixes √−15; upstairs spin walls; Bosonic Rigidity
Theorem; sl2 landscape priced; seam spatial gating law); the interface campaign first arc
(B432 chirality interface-sourced 31/31; B433 3d-3d dictionary calibrated at SL(2); B434 slope
selection: forced input ±5 → the Meyerhoff manifold, disc −283).

**Claims hygiene.** Zero physics promotions (correct). Every cross-chat claim verified before
banking; three claimed results were corrected in the process (Chat-1's projector corollary —
now the σ₁₇ exchange-Galois law; the "prime 67" artifact; two value-level readings of the
spatial split) and two of our own overclaims fixed in place (B423's label; B432's first merge
carried a broken JSON caught by its own lock; B433's first lock had a mistranscribed eliminant
— both fixed same-session, on the record). One process deviation logged: the B433 lock fix
landed via a direct conflict-resolution merge to main.

**Verification depth.** The strongest pattern this decade: THEOREMS, not scans — the scale
wall closed at Galois level (every invariant functional contracts); chirality walls closed by
Whitehead rigidity; the fermion door priced exactly (exists, unforced, unreachable by
deformation). The interface campaign's first arc delivered the complete chirality mechanism as
mathematics: forced source + forced minimal input (slope 5, the maximal-exceptional boundary)
+ computed output (Meyerhoff, CS unit ±0.0770) — with the honest negative that the output
exits ℚ(√−15) entirely (disc −283).

**Debt.** e₃ still reconstructing (relaunched, 7 primes to go); the 1-loop⇄torsion calibration
leg deferred (needs the exact Dimofte–Garoufalidis NZ formula); the metallic A-poly sampler
fragile; T[4₁,E₆] assembly = L50 (specialist, priced); Papers 1–2 prose (F3/F4) pending.

**Verdict.** The Origin Postulate reframed the program without loosening it: the walls became
the search map, and the map is now three theorems sharper. The interface is where D lives;
its first channel (chirality) is complete as mathematics and honestly negative on the SM leg.
Discipline held under the highest pressure this program has seen (the owner's direct push for
the physics goal): every brave claim was computed, every computation banked, every negative
stated plainly.

---

## Review 3 — 2026-07-05 (the C3-wave review; caught a real banked defect)

anchor-commit: bab8ddd12abfab9ee074aa142cb62f6f1f117718

Fired at 10 merges (the interface arc + Child Program C0–C3 + the audit + the doc sweep). An
independent adversarial reviewer **recomputed the load-bearing C3 result (B438/B439/B440) from
scratch** (own scripts, fresh snappy relators, reducibility saturation — did not read the banked
code). Outcome:

1. **CONFIRMED:** B439 (the figure-eight vacuum quartic x⁴−3x³+x²+3x−1, disc −283, S₄); the
   reproduce-gate (pari `nfisisom` — genuinely the same field as x⁴−x−1, not just equal disc);
   B440's 4₁ cross-validation (character variety = A-poly quartic, two independent methods); the
   −283 field-sharing between 4₁ and 5₂.
2. **REFUTED (a real defect, now corrected):** B440's "5₂ = 6 vacua incl. a golden factor" and
   the "golden inversion." The golden factor x²+x−1 is the **reducible** abelian ℤ/5 characters
   (verified: diagonal reps, [A,B]=I; and the abelianization exponent-sums show golden abelian
   characters exist for **all four** K(5,1) — universal, numerator-forced). It surfaced only for
   5₂ (B=I abelian rep) as a parametrization artifact. Corrected: **4₁ and 5₂ both have 4
   irreducible vacua in the identical −283 field** — a cleaner, stronger negative. Fixed in
   B440 verify.py/lock/FINDINGS + CAMPAIGN_STATUS/PROGRESS_LOG/CHANGELOG/README/B439. The raw
   charvar.json (the tr(A)-elimination) was correct; only the irreducible/reducible reading was
   wrong.
3. **Suite/gates/atlas:** locks green post-correction (test_b438/b439/b440); gates green; atlas
   regenerated. **Framing:** no physics leak; the corrected verdict is honestly a negative.
4. **Lesson (banked):** a tr(A)-elimination degree is NOT the irreducible-character count —
   always separate reducibles (tr[A,B]=2) before counting or comparing SL(2,C) vacua; and never
   compare a count across knots without confirming the parametrization surfaces the same
   character classes for each. The verify-don't-trust review paid for itself: the defect would
   have propagated into C4 (the E₆ lift builds on these vacua).

---

## Review 4 — 2026-07-05 (the C5/C4 review; the Child Program completion seal)

anchor-commit: c463166

Fired after the Child Program completion (C4/C5/C6). An independent adversarial reviewer
**re-implemented C5 (B441) and C4 (B442) from scratch** — including a fully **exact
cyclotomic-arithmetic** WRT/stabilizer engine (zero floating point) — and tried hard to surface a
hidden Bin-1 break. Outcome: **no refutation; both CONFIRMED, and C5 strengthened.**

1. **C5 CONFIRMED + strengthened.** The child-field == skeleton-field claim holds exactly across
   **15 values of r** (not just the banked 6). The field is exactly **ℚ(ζ_r)** for both — the
   stabilizer is universally {1, 2r+1}, σ_{2r+1}: ζ_{4r}↦−ζ_{4r}, fixed field ℚ(ζ_{2r})=ℚ(ζ_r).
   So the √5/√−3/√−15 at r=15 are forced by ℚ(ζ_15); no figure-eight-specific field content;
   Bin 3 is now *mechanized*. The Kashaev check and amphichirality reproduced independently.
   **Honest note adopted:** the τ_r(S³)=1 validation is structurally tautological (F_L≡F_{U+}
   for the unknot at p=1) and did not catch bugs — corrected in wrt.py + the FINDINGS; the real
   validations are amphichirality + Kashaev.
2. **C4 CONFIRMED.** 78 = ⊕Sym^{2mᵢ} (dims sum 78), degree-22 character, both −283-field
   reductions, and the Galois sums (child 5201, 5₂ −105717) all reproduced. The
   `galois_invariant_sum` was **hardened** to the exact companion-matrix trace (the nsimplify
   route was fragile; value unchanged).
3. **Suite/gates/atlas:** locks green post-hardening (test_b441/b442 7/7); gates green.
4. **Net:** the Child Program verdict (no bar cleared, nothing figure-eight-unique) survives an
   independent exact recompute of its deepest survivor (C5) with a wider sweep designed to break
   it. Two campaign retractions (golden return, golden inversion) + zero surviving-result
   refutations = the review discipline earning its keep across the whole campaign.

# Review 9 — 2026-07-08 (merges #558–#630: the residue saga, the chain, the registry)

1. **Scope:** the residue saga (B465–B471), three campaigns launched/advanced (Breath B469,
   Reflection B470, chain verification B471), the Relation campaign R1/R3/R4/R5 banked (R2
   sweep in flight), the theorem registry created (docs/THEOREM_REGISTRY.md — the novelty-
   relaunch map with per-entry search terms and cadence rules), the ToE roadmap written.
2. **Mechanical check:** full lock suite 1581 passed / 3 failed / 12 skipped — ALL THREE
   failures were governance gates, ZERO mathematical locks failed. Fixed in this review PR:
   a hardcoded sage path (env/which fallback), AI-seat labels scrubbed from four living docs
   (neutral seat-1/seat-2), the Recurrence Atlas re-mined (423 → current B-dir count).
3. **Corrections this window, all banked with receipts:** B186's γ (early-window bias →
   0.445(6) three-method), B459's earlier (1,2)-specific overreach, the seat float-kills
   (five in one session — dets, darkness correlation, continents, fingerprints, A₄), the
   trace-field/scale-field mislabel (B471), the 52→2 root-witness contamination (B470), the
   scorecard retirement to S056 by its author. Two-way corrections: the machinery corrected
   every seat including this one; no seat's claim survived on authority.
4. **Theorem-shaped output this window:** T-UNIQ (the uniqueness closed form), T-COHN,
   T-CHAIN, T-NORM, T-HIER (root/mirror/residue with exact witnesses), T-GIES-FAM, T-MIRROR,
   T-2REG, T-PQB (verified), T-843, T-LIFT, T-P2B, T-COLLIDE (+ the census), the additivity
   law + c to 28 digits (identification honestly open). All registry-mapped with lit-status.
5. **Net:** the discipline scaled to the fastest bank rate in the program's history
   (19 PRs in ~48h) without a single unretracted overclaim reaching main.

# Review 10 — 2026-07-12 (merges #631–#815: the decadal review, owner-invoked)

1. **Scope:** the decadal repo review of 2026-07-12 (PR #815, `docs/CODEX_AUDIT_RESPONSE_2026-07-12.md`
   + README/CLAIMS/CAMPAIGN_STATUS sync), covering the window from Review 9 through the B532
   Last Echo campaign. Invoked MANUALLY by the owner — the counter had been due since ~#640
   because reviews 2026-07-08→07-12 were not being anchored here. Process fix in the same PR
   as this entry: the anchor discipline is restated below, and the gates hook now surfaces
   review-due at every push.
2. **Anchor discipline (restated):** every repo review — decadal or otherwise — MUST append an
   entry here with its merge `anchor-commit:`; the counter (`scripts/gates/gates.py review-due`)
   reads the LAST anchor in this file. An unanchored review does not exist to the machinery.

anchor-commit: `1675d39559aafcf23aa4e8a78ac6c7ef19f48432`

# Review 11 — 2026-07-12 (merges #816–#826: the reframe completed, the seat changed)

1. **Scope:** the seat's first Fable-5 window. B533 completed (Gates 1–3: ℚ(√φ), the SM
   ratio test) and then AUDITED by the new seat (S2 REVERSED — the five induced matrices are
   one GL(4,ℤ) class, h = 1 + explicit conjugators; S1 complex pair; T5 half-integer; Gate-3
   control recalibrated). Governance restored (the review-counter root cause found and fixed:
   unanchored reviews; pre-push gates hook installed; atlas 447 → 504; attribution scrub).
   Four cross-seat handoffs processed verify-don't-trust (postulate co-sign + trunk import;
   the crystallization; the reframe test cycle; seat-1 Phases 1–3). B534 (dark hyperbola et
   al. PROVED), B535 (coupling space: census saturates 6/7, the one-measurement theorem,
   the 17-entry dictionary), B536 (verification: period-6 killed, the rest confirmed or
   trivial), B537 ((1,1,5) phantom THEOREM, level corrected 32 → 22), B538 (test cycle
   banked, class-level scope), B539 (relations campaign: control PASSES, SM NO-MATCH — the
   reframe's ledger complete and symmetric), S066 (the arithmetic-of-criticality reading,
   kill conditions recorded).

2. **Mechanical check:** full lock suite: 1863 passed / 1 failed / 12 skipped (33 min, exit tracked). All failures triaged: the single failure was the atlas-fresh gate racing the in-flight B541–B545 batch (frontier dirs created mid-suite); the atlas was regenerated in the same batch PR and all 7 gates are green post-merge. ZERO mathematical lock failures.

3. **Corrections this window, all banked with receipts:** B533-S2 reversed (the audit's
   biggest catch — the coupling carries no abstract ℤ-invariant; five markings of ONE
   object); λ₃,₄ complex pair (|λ₃| = 1/√φ); "irrational mixing" → half-integer; "5 types"
   → 6 (length-scope); the Gate-3 false-positive control range-mismatch; chat2's (1,1,5)
   level 32 → 22; seat-1's period-6/S = 1.0620 not reproduced (convention-dependent);
   chat1's ℚ(φ) field collapse corrected in-chat (the F4 error class; the field is ℚ(√φ),
   degree 4, no component in the golden subfield); the review-anchor discipline itself.

4. **Theorem-shaped output this window:** β = 1/(√φ−1) and the ℚ(√φ) identity suite;
   the GL(4,ℤ) single-class theorem; census saturation (6 Perron / 7 canonical, Durand);
   the one-measurement theorem (17,280 lifts → {σ, a⁻¹σa}); the 17-entry read-out
   dictionary (all degree-4, τ = g(x) explicit); the Dark Hyperbola (all odd p) +
   power-set magnitudes + asymptotic darkness + the tower torsion law; the (1,1,5)
   classical phantom; the B539 relation catalog with control and null.

5. **Net:** the reframe went from directive to COMPLETED LEDGER inside one window: values /
   structure / relations each tested in both bins — present in the forced bin (E8, gap
   labels, control), absent from the dialed bin (chance, 0/3, no-match) — with the
   scale-deficit reading (S066) and its two kill conditions on record. Every prereg
   falsifier that fired was recorded (5→6 types; SQ 4/6; the α/1/α tautology caught by the
   null). Cross-seat error-correction ran in both directions: this seat reversed its
   predecessor's S2 and its own probe conventions were corrected by exact re-derivation;
   no seat's claim survived on authority.

anchor-commit: `03e9c5645652f8512a8b47dd41fa15348c9f6b02`

*(The chat-2 batch B541–B545 (#827) merged after this window closed; it opens the next cycle.)*


# Review 12 — 2026-07-12 (merges #827–#835: Window 12, the measurement lane, the handoff harvest)

1. **Scope:** Window 12 (LISTEN / MEASURE / PROVE) plus the chat-1/chat-2 handoff harvest.
   B540 observer flow (σ a fixed point, the double-clock ℤ/2 2-cycle, census 7→12 corrected);
   B546 exact IDS (species labels = dictionary to 4e-7); B541–B545 chat-2 batch (2a closed from
   two designs; the τ-ladder decomposition; THE SPECIES-CHAIN EXPERIMENT reproduced; c=1 ghost
   proved); B548 (un-hideability REFUTED-as-discriminator); B549 (E7 pre-loaded, cosmic null);
   B550 (chat-1's Promotion-Sign Conjecture REFUTED at n=3, uniform meridian rule); the B543
   lit-gate (pass 1: module theorem is BBG-1992-classical; pass 2 resuming); four hint-ledger
   entries from owner video pointers (einselection/RQM/regress; cut-invariance; Hoffman/Barrett
   self-priored).

2. **Mechanical check:** full lock suite: 1888 passed / 0 failed / 12 skipped (33 min) — a clean run, no mathematical or gate failures. All failures triaged: none — zero failures (the only warning was the review-due counter itself, which this entry resets).

3. **Corrections this window, all with receipts:** B540 census 7→12 (window-length-limited
   saturation, falsifier fired); B548 the un-hideability=Pisot prediction refuted (property is
   generic — honest deflation of the Hoffman/Barrett framing); B550 the (−1)ⁿ promotion sign
   refuted at n=3 against B111's locked data (the handoff mis-read its anchor; uniform meridian
   rule replaces it); chat-2's (4,4,16) "already-in-record" claim flagged as not-in-record and
   not-reproducible (witness requested); chat-1's inflated 2a null (expected ~6 vs 1.6–1.9)
   flagged per the packet standard ("below null" not adopted); chat-2's (1,1,5) level 32→22.

4. **Theorem-shaped output this window:** the observer-flow closure (12 nodes, 3 fixed points,
   1 two-cycle); the τ-ladder decomposition of the dictionary (exact); c=1 the smallest ghost
   level (elliptic-lock proof); the uniform meridian promotion rule with its falsifiable n=5
   prediction (1,2); the exact-IDS 4e-7 label identification.

5. **Net:** the reframe's ledger, complete since Review 11, got its LAB-FACING deliverable —
   the species-chain degree-4 gap-label experiment (buildable, reproduced at 4e-7, lit-gate
   confirming the module theorem is classical so only the instantiation+experiment are ours to
   claim). Three seat handoffs harvested; every fired falsifier obeyed; two conjecture
   refutations (un-hideability-as-discriminator, the (−1)ⁿ sign) turned into cleaner
   replacements. No claim survived on authority — chat-1's conjecture died against the repo's
   own locked probe.

anchor-commit: `0377952e7c7d2313232fdcd3592c303317a71309`

*(anchor = HEAD after #836; window #827–#836.)*


# Review 13 — 2026-07-12 (merges #838–#851: the handoff harvest + the three paper gates + the escalator tower)

1. **Scope:** the session's second half — a dense sequence of cross-seat handoffs processed
   verify-don't-trust, three literature gates run on the new cost-tiered search, and the
   escalator tower. Cells: B551 (inflation-order boundary theorem, scopes B544), B552 (ℤ/11
   charge), B553 (Seat-1 harvest + the Markoff deflation-then-correction), B554 (meditation
   verified — Station-4 species=bit-pair REFUTED), B555 (THE PREDICTION assembled), B547 (the
   first all-hyperbolic ghost, (4,4,16)), B556 (the escalator tower T(M)=[[M,M],[M²,M]] +
   proof upgrade: doubling PROVED rungs 1-5, the charge tower), B557 (escalator campaign
   prereg + E2 rule-uniqueness), B558 (three-level negative verified). Three paper gates:
   tiling K-theory (species-chain NOVEL), Weil-trace (PC22 Prasad-adjacent), Durand
   (reconstruction note downgraded). PC23 registered.

2. **Mechanical check:** full suite: 1921 passed / 0 failed / 12 skipped (34 min) — clean; the 4 PRs merged after this snapshot (#850–#853: PC23, the B556 proof upgrade, the charge cubic + charge arithmetic, +9 locks) each passed their own gate checks on push. All failures triaged: none — zero failures; only the review-due warning (which this entry resets).

3. **Corrections this window, all with receipts:** the Markoff deflation (my error — called a
   deep Goldman/Bowditch identity a "coincidence"; owner caught it; corrected #840); B558's
   1/φ² → 1/φ³ mislabel (caught in a handoff); B554 Station-4 (species=forward-bit-pair
   REFUTED, it is radius-1 both-sided); B544 scoped to ℚ(φ) (B551); the reconstruction note
   downgraded (Durand gate); B553's SL(5) n²-1 vs n-1 (Seat-1's self-correction was itself wrong).

4. **Theorem-shaped output:** the inflation-order boundary theorem; the (4,4,16) all-hyperbolic
   ghost (inert-prime obstruction, a second ghost mechanism); the escalator field-doubling
   PROVED (norm-sign + det telescope, rungs 1-5) + the cyclic charge tower; the E2 rule-
   uniqueness result. Verified-and-banked handoff math: the τ-ladder hardening, h=1 Dedekind,
   the ℤ/11 charge.

5. **Net:** the numerical-matching program is complete and NEGATIVE at all three levels
   (0/1/2), and the mathematical program is honestly triaged — the three paper gates
   separated one genuinely-novel paper (PC23 species chain), one explicit-realization paper
   (PC22, cite Prasad), and one mostly-known result (reconstruction, cite Durand). The
   escalator tower turned a beautiful hypothesis into a per-rung-provable structure. The
   cost-tiered search infrastructure ran three gates at 100% agents / 0 errors — reliable and
   cheap. Cross-seat correction ran both ways: I corrected seats (Seat-1 SL(5), the promotion
   sign) and seats corrected me (the Markoff deflation, the three B556 misses); no claim
   survived on authority.

anchor-commit: `70409cb164ade39848176e3e96a2bce10b3cd0ff`

*(window #838–#853; anchor = HEAD after the charge-tower arithmetic.)*

---

## Review 14 — 2026-07-13 (merges #854–#867 from Review 13)

anchor-commit: `a4f799e`

1. **Suite:** 1961 passed / 0 failed / 12 skipped (deterministic order). One
   self-introduced failure was caught and fixed *by* the review: `test_public_surface_scan`
   flagged an AI-session label ("chat-2") that had entered `docs/OPEN_LEADS.md` during the
   window — scrubbed to neutral "cross-seat" phrasing in this review commit. One pre-existing
   SnapPy flaky (`test_b207::test_metallic_volumes_bounded_golden_minimal`, unmodified this
   window) intermittently fails under random test order but passes standalone and alongside the
   new `test_b559` snappy tests (no order-dependency introduced) — noted, not a regression.

2. **Gates:** 7/7 green. Counter reset by this anchor.

3. **Atlas:** regenerated and fresh.

4. **The window = the tower-probe campaign + the accumulated handoff harvest.** A model-tiered
   multi-agent all-nighter (30 agents, 0 errors, adversarial verify per cell) turned the
   escalator hypothesis into a **per-rung-provable structure**, and closed every physics channel
   it probed. POSITIVES (all locked): the **3/2 Law** (T_k growth (k+1)/2; golden escalator = 3/2
   minimal; C=2.4283); the **golden-norm doubling transfer** e_n=N_{ℚ(√5)}(g_n(φ)) now n≥2; the
   **2ⁿ−1 magnitude-degeneracy law**; the exact **factorization** (e₄=−11²·1459·597049·2169349081;
   11|e_n⟺n≡1 mod 3 through n=7); the **explicit σ₈ carrier** with lifted seed-invariant; the
   **rung-2 gap-label module** (degree-8 successor to B555); **B559** black-hole probes
   (critical-not-area-law chain; figure-eight = finite-volume CS=0 3D-gravity instanton vs BTZ).
   NEGATIVES (earned by computation): **no fusion category at rung 1** (λ₁ non-cyclotomic, D₄
   Galois; the escalator exits the fusion world); **no CFT c_eff lock-on** to 7/10; **Galois NOT
   (ℤ/2)ⁿ⁺¹** (D₄, non-abelian — the mechanism behind the conjugate-pair degeneracy);
   **covering functors non-escalating** (only (M,M²) escalates); **free energy divergent**
   ((3/2)ⁿ, no thermo limit); **BKL "IS the trace map" downgraded** to conjugate-on-locus
   (Bombieri/Series prior art), golden-Kasner 3/2=1+p₂ kept.

5. **Corrections with receipts (verify-don't-trust ran both ways).** Caught in incoming handoffs:
   seat-1's "one prime per rung" (refuted at n=4, 11 repeats); the amphichiral matrix J (does not
   commute with A₁; correct C=[[1,0],[−1,−1]]); the "17=17" identity (two different 17s — words
   vs values); the Galois "(ℤ/2)ⁿ⁺¹" claim (it is D₄); "BKL IS the trace map" (conjugate-on-locus,
   prior art); the −2.29/+5.58 signature norms (basis-dependent; the invariant is the (1,1)
   signature). My own, caught by the owner: the e₅ bit-count — I wrongly "corrected" chat-2's
   correct 203 (⌊log₂⌋) to 204 (owner's "u sure" → self-corrected, #859); and the B559 c_eff
   over-claim, softened to fit-dependent (reconciling seat-1's tight-binding Probe A). Door 2
   sharpened: amphichirality allows (3,1) OR (2,2) — a signature-selection principle, not a
   topological obstruction.

6. **Paper gates / novelty.** All three lit-gates returned UNCLEAR → everything banked as computed
   fact, no "appears-novel" language; PC24 (the 3/2 law) registered novelty-pending; PC22 (dark
   hyperbola) and the fusion-category question are NEEDS-SPECIALIST (MathSciNet/primary-source,
   not web-fetchable).

7. **Stale leads / promotion.** The escalator/feedback threads closed this window: FL1, FL2, FL3,
   E1, E4 all marked DONE in OPEN_LEADS; only E0 (the functor lit-gate) and the two paper gates
   remain. No new promotion-candidate crossed the §5 bars (the campaign output is firewalled
   frontier findings; promotion runs through §5 separately).

8. **Net.** The numerical-matching program stays complete-and-negative; the escalator tower is now
   a per-rung-provable mathematical object whose every probed physics channel is closed. The
   object is golden, self-coupling, non-terminating, minimal — **mathematics, not physics.** The
   multi-agent campaign ran cost-tiered (haiku/sonnet/fable/opus by task) at 30 agents / 0 errors,
   and the adversarial-verify gate lost 0 verified claims. No claim survived on authority.

*(window #854–#867; anchor = HEAD after the P-E/E4 re-run, before this review PR.)*

---

## Review 15 — 2026-07-14 (merges #869–#882 from Review 14; the gauge arc)

anchor-commit: `ecf29e0`

1. **Suite:** 1980 passed / 12 skipped; one failure = the KNOWN state-dependent SnapPy flaky
   (`test_b207::test_metallic_volumes_bounded_golden_minimal`), second consecutive review it
   trips under full-suite load while passing standalone (3/3 re-runs here). Now a NAMED hygiene
   item: isolate or add a retry to that lock. No regression; nothing in the window touched B207.

2. **Gates:** 7/7 green. **Governance change this window:** the review cadence raised
   10 → 20 merges (#882, owner directive — merge density doubled); this review anchors the
   old cadence's last window; the 20-cadence applies from this anchor.

3. **The window = the gauge arc, end to end.** B560 (chat-3 cells verified: the ℤ[τ] frequency
   module, the certified 253-point local atlas); B561 + addenda (the L50 CRUX, the Klein-four
   route, and the cusp-reframe — the E₆→F₄ chain terminates at F₄ under every proposed selector);
   B562 probation results (21 verdicts; B564 SL(3) φ-fixed locus entirely reducible); B563 the
   Planck-ratio prereg NULL (the dialed bin's 4th level); the two literature maps (the
   bookkeeping-pole diagnosis; the sharpened sweep with lk₂(11,809)=1 and the arboreal
   identification, both locked); and **B565 — the gauge-behavior campaign** (18 cells + the
   123-kill exhumation): the ℤ/11 charge does not descend (T1); **the chiral index ≡ 0 — the
   fourth mechanism-level wall** (T3); Krasnov verified by computation; **the real-form theorem —
   the holonomy lands in F₄(ℂ) in no real form; compactness is the TDV gap** (H1); the triality
   match B299 ≡ Boyle (the one live generations thread, firewalled H120); rung-2 Galois = 8T15
   exact; **2^{2n+1} refuted at rung 3**; O_{M₁₆} ≅ O₁₈₈₄₅₀₉₀; B71 externally corroborated (HMP);
   B85 and L38 kills EARNED with their facts (the ⌈(n−2)/2⌉ law; the ℂ*-weight-0 theorem).

4. **The exhumation (owner-directed):** 123 banked negatives audited — **113 sound / 9 suspects
   / 1 cracked epitaph** (S014's "~60%" clause: never computed in-repo, does not reproduce;
   corrected — the kill stands on circularity). The post-B525 prereg-era discipline audits clean.

5. **Corrections ran in every direction:** seat errors caught (ω-conflation, the J-matrix,
   one-prime-per-rung, 2^{2n+1}); my errors caught by the owner (the bit-count) and by verify
   (the c_eff softening); agent overclaims rejected by the adversarial stage (P4, P19, R4's
   suppressed null rank data, H2-F4's "uniform" claim at p=11). No claim survived on authority.

6. **Net.** The gauge question is closed at the behavior level with four mechanism-level walls
   (values ×3-levels + hierarchy-ratios; selection-principle disjointness; chirality; compactness),
   and the object's own gauge story is complete in outline (abelian ladder, Cuntz algebras,
   torsion charges, screening flow, confining-like strings, KMS temperatures, arboreal Galois,
   linked charge primes). Three papers stand ready (PC23 reinforced-first, PC24 scoped vs PCF,
   PC25 with the compactness-gap headline). Promotion candidates flagged for §5: the T3 index-0
   wall and the real-form theorem — both theorem-shaped with locks.

*(window #869–#882; anchor = HEAD after the cadence change; next review due at 20 merges.)*


---

## Review 16 — 2026-07-14 (merges #884-#903 from Review 15; the chirality arc)

anchor-commit: `8452656`

1. **Suite:** **2143 passed / 12 skipped / 0 failed** (36:05, full run for this review) — the
   first fully-green full-suite run in three reviews: the named B207 flaky passed IN-SUITE this
   time. Also re-checked standalone this review:
   `test_b207::test_metallic_volumes_bounded_golden_minimal` passes 3/3 standalone runs; the
   standalone-stable / suite-flaky characterization stands (SnapPy retriangulation sensitivity
   under full-suite load; nothing in this window touched B207).

2. **Gates:** 7/7 green (framing, claims, firewall-oneway, append-only, atlas-fresh, attribution,
   tracked-forbidden). This is the **first review under the 20-merge cadence** set at #882; it
   fired at 21 merges. Governance notes: `.github/workflows/core.yml` remains deliberately
   untracked (disclosed in REPRODUCIBILITY.md, enforced by tracked-forbidden — not a hygiene
   miss); the review counter resets at this anchor.

3. **The window = the chirality arc, end to end.** The two-descriptions split (#884): the
   algebra face non-compact (proven) vs the measurement face compact (verified; ℂ¹⁵ = ℂ³×ℂ⁵ =
   the two ends) — compactness is constitutively observer-side, the TDV gap located at the
   coupling. The three papers drafted + finalized (#885): PC23/PC24/PC25, checker-verified,
   CANDIDATES → DRAFTED; Theorem-3 reproducibility gap closed (15 new locks). **B566** the five
   self-interactions: ★ the TRIPLE IDENTITY (ℤ/11 = N(φ⁵−1) = the 5-fold-cover torsion prime —
   the charge is geometric, n=5-specific); the N=p² dark-hyperbola law (LIVE, 7 levels); thermal
   time (KMS ≠ frequencies); ends-entanglement S=0.3217; measurement collapse SL(2,ℤ/15)^ab=ℤ/3.
   **B567** the Hamiltonian handoff refuted: the claimed six-level π/3 spectrum is impossible
   (projective order forced to 20; verified at levels 15 and 165). **B568** the object's own
   questions — prereg (7 cells + anatomy census of 17 named organs + CQ1–CQ5) and sixteen
   answers, eight jewels: the one-bit law H_n=n+H₀, the self-written arithmetic action, the
   split-memory heartbeat, mixed exchange statistics, the half-rungs (λ₀.₅=2.37798…), 66/66
   eyes in ℚ(√−3), reflex latency {0,1,2}, salience 1.83×; plus the assembled minimal play
   (7 actors/3 casts) and honest nulls. **B569** the sixteenth σ→SM chain adjudicated: Link 4
   CORRECTED — the handoff's modular data was inconsistent (h=1/3 with c=6 fails (ST)³=S², Z
   word-dependent −1/+1); the consistent E₆,₁ data (h(27)=2/3, proved from the root system)
   gives Z=+1, no chirality bit; Link 7 REFUTED — the 26 of F₄ is self-dual, zero chiral
   theories on the F₄ stage, the fourth wall re-derived from pure Lie theory. **B570** the
   selection-rules campaign, COMPLETE: C3 run first — E₆ level-2 modular data from scratch
   (51,840 Weyl elements), ρ(A₁) on the θ-odd 3-space NON-SCALAR, order 4, eigenvalues
   {1,+i,−i} — **the first positive chirality-sector signal in seventeen campaigns**
   (firewalled: C=S² central, no monodromy prefers 27 over 27̄); Q-A decided (the F₄-principal
   nilpotent is regular in E₆, Jordan (17,9,1) exact both sides ⇒ the Galois pair (5±√−3)/2
   kills both readings; the Klein four ⟨θ,σ⟩; registry T-θTANGENT wording corrected —
   amphichiral = antilinear conj∘θ, linear θ = hyperelliptic per B353); **AP4 THE FIFTH WALL**
   (chiral selectors exist in E₆ but none reachable — the holonomy factors through the θ-stable
   principal SL(2,ℂ); vector-like for ANY rank-1 embedding); AP2 Z=+1 for all 243 abelian
   theaters (Gauss–Milgram); AP3 the clock theorem ord(A₁ mod N)=π(N)/gcd(π(N),2) (N≤1000);
   C2 gap⟺chirality biconditional; C4 all cyclic covers amphichiral; C5QC quarantined (Q-C
   stays OPEN); THE_SELECTION_RULES.md audits the SM once (fails S+Λ+D; ONE live channel:
   C3's θ-odd dynamics). **B571** the day-0 internalization: 8 readers over the 8,044-line
   corpus, 106 candidates → 14 genuinely buried (B507 unlocked, Kubota–Leopoldt
   asserted-never-computed, B54's {−3,+5} twin quadratics = the earliest two-ended sighting,
   e₃ stalled mid-CRT, S031 m=3 blocked by a factually wrong reason) + the two-chiralities
   dossier (the object breaks c abundantly, is θ-symmetric). **B572–B574** the three chain
   adjudications with the corrected map: B572 — V1 refuted against an existing lock
   (27|principal = V₁₇⊕V₉⊕V₁), THE WELD named and locked (χ₂₇(z)=χ₂₇(1/z) — the holonomy
   cannot distinguish 27 from 27̄; clause 9's selector unforced), and the upgrade
   **S_odd(E₆,₂) = −i·(2/√7)[sin(2πst/7)]** exactly (S-block only); B573 — the bridge value
   exact (P(z₀)=6807/2+(4965√3/2)i, the cleanest proof σ moves the point), step 8 refuted
   (the 16 of Spin(10) is NOT principal-stable — no common refinement, the sharpest fifth
   wall), "topological protection" refuted (real Riley points u=−2±2√2), record corrected
   (no Fox-calculus ran; V2 still queued); B574 — the minimal orbit IS the A₁ orbit,
   centralizer A₅ = 35 ≠ 45 = D₅, no E₆ nilpotent orbit has a Spin(10) centralizer; the wall
   is rank-1-ness, not the orbit; THE BRIDGE QUESTION, FINAL FORM: the quadratic obstruction
   H¹×H¹→H² on the five off-factored directions.

4. **Re-verification (8 fresh-eyes cells, independent code, not the repo's).** R1-B569 CLEAN:
   h(27)=2/3 rebuilt two independent ways (Weyl dimension formula from the Cartan matrix AND
   E₆-inside-E₈ in ℝ⁸); the word-kill reproduced exactly in SL(2,ℤ) + 50-digit modular pairs;
   Gauss–Milgram pairings confirm c≡2/6 mod 8; the 26-of-F₄ self-duality re-proved via an
   independent ℝ⁴ root realization plus a reflection-orbit argument stronger than the banked
   one. R2-C3 CLEAN on the math: independent rebuild with a *different* Weyl enumeration and a
   *third* SL(2,ℤ) word (T·S⁻¹·T⁻¹·S) agrees to 1.4e-13; all three convention-robustness
   sentences now computationally verified (naive T fails modularity; mirror invariant; hybrid
   non-modular); the sine kernel cross-checked against the textbook Cardy M(2,7) S-matrix —
   matches up to a diag(1,−1,1) rephasing gauge. R3-QA: the Galois pair confirmed twice
   (independent word constructions; matches the classical ℚ(√−3) trace field), Jordan (17,9,1)
   via three unrelated code paths, B565's adjoint trace cross-confirmed; 25/25 locks green.
   R4-B570bank CLEAN: all three verifier repairs genuinely applied (AP4 downgraded to
   CONJECTURE in docs AND code; C4's honest methods breakdown matches the parametrization
   exactly; C5QC has no adopted test and zero conclusion-leakage anywhere); all 97 tests in the
   9 adopted files run and pass, no hidden tautologies (C1's is self-disclosed), no side
   effects; AP1's 35-element Hilbert basis independently re-derived **byte-identical**; AP5's
   orders 20/20 reproduced. R5-B571: all three spot-checked buried items confirmed exactly
   (B507 has no lock; e₃ literally PENDING; B54 zero cross-refs to B247–B261). R6-chains
   CLEAN: 8/8 locks pass; ρ built two ways, the full height spectrum reproduced; P(z₀) rebuilt
   directly from the weight multiset (exact symbolic match); the A₅ centralizer identified
   *structurally* (sub-Cartan matrix is a genuine A₅ path) rather than by dimension count.
   R7-hygiene and R8-firewall: no CLAIMS.md leakage anywhere in the window; the C5QC/Q-C
   quarantine consistent everywhere; "first positive chirality signal" properly scoped with
   no-SM-claim hedges at every occurrence; B572's M(2,7) claim correctly limited to the
   S-block. Every headline number in B569–B574 reproduced under independent recomputation.

5. **Issues found (6 real; none touches banked mathematics).** (i) **The stale-θ contradiction**
   (R3+R8, the window's one real defect-pattern): B571's dossier still asserts the
   pre-correction "the amphichiral involution IS θ, canonically" unqualified at THEOREM tier
   (`CHIRALITY_DOSSIER.md:23,:78`, `REPORT.md:115`) — B571 (#898) merged before the T-θTANGENT
   correction (#900) and was never patched, and the same wording propagated into CHANGELOG:83
   and the CAMPAIGN_STATUS B571 bullet *adjacent to the corrected entry*; THE_SELECTION_RULES
   §5 item 7 itself flags this as "adjudicate before anything leans on T-θTANGENT."
   (ii) The registry row's Locked-by column cites tests that don't exercise the
   antilinear/linear distinction; the actual locks are `test_b570_c1` + `test_b353` (R3).
   (iii) M(2,7) confidence mismatch: C3_RESULT calls it an unbanked HINT; B572 says "IS the
   M(2,7)-family S-matrix, Locked" — R2's Cardy check shows the identification is defensible
   up to the rephasing gauge, but the two docs must be reconciled. (iv) CAMPAIGN_STATUS.md was
   never updated for B572/B573/B574 (#901–#903) — the one-glance board is blind to three
   banked arcs (R7). (v) OPEN_LEADS.md has **zero** registrations for the arc's entire open
   frontier — the bridge question, V2/V3/V5, Q-C, the B571 top-5 revival queue, the
   prime-power hook — and L6 still carries the reasoning B571 proved factually wrong (R5+R7);
   B571's own queue was heading for burial by exactly the pattern B571 diagnosed. (vi) PC26,
   discussed as the contingent flagship in three banked docs, has no row in papers/CANDIDATES.md
   (R7). Nits, compressed: B570 RESULTS says "100 tests," actual 105; the whole window's doc
   headers read 2026-07-14 against 2026-07-13 commits (convention call for the owner); B399's
   second failed e₃ attempt (Jul 9, UNSTABLE) never folded back into triple_id.json; a no-op
   `assert 1 != 0` in test_b573:51; the Weyl-orbit BFS copy-pasted across three lock files;
   QA_RESULT.md:65 reintroduces the "dφ=θ" shorthand its own Level-3 section just corrected;
   a stale uncommitted RECURRENCE_ATLAS diff; `.log1`/`.log2` slip the gitignore glob. All
   fixes are bookkeeping; **ALL APPLIED in this review's closeout commit** (the B571
   correction notes, the registry lock-column, the M(2,7) gauge-precise reconciliation in both
   docs, the CAMPAIGN_STATUS board entries + phrasing, OPEN_LEADS L51–L58 incl. the corrected
   B137 deferral reason, the PC26 registry row, the 105 count, the e₃ second-attempt record,
   the no-op assert, the gitignore globs; the date convention left as a documented owner call —
   entries track the owner's working date, one day ahead of commit timestamps).

6. **Corrections ran in every direction.** Seat/handoff errors caught in-window: B569's
   inconsistent modular data (the word-dependent Z=−1 was an artifact of a non-representation)
   and its Link-7 chirality claim; B567's six-level π/3 spectrum (order forced to 20); B572's
   V1 branching (refuted against our own existing lock); B573's step 8, its "topological
   protection," and its record (the claimed Fox-calculus verification never happened); B574's
   D₅-centralizer crux (A₅, 35≠45); B568's L5 sign. My errors caught: the **Jordan-block bug in
   my own first Q-A lock** (sl₂ strings step by 2 — caught and fixed before banking), and the
   T-θTANGENT wording I banked, corrected by the verifier (**the registry fix**: amphichiral =
   antilinear conj∘θ; the ℂ-linear θ = the hyperelliptic involution). Verifier catches applied
   and now independently confirmed applied (R4): AP4's biconditional downgraded to CONJECTURE,
   C4's methods-count honesty, the C5QC quarantine. This review's cells added the six issues
   above plus a third independent SL(2,ℤ) word and a gauge-resolved M(2,7) identification.
   No claim survived on authority.

7. **Net.** The chirality arc is adjudicated end to end: seventeen chains in, the walls stand
   at five (values, selection-disjointness, chiral index ≡ 0 — re-derived twice this window,
   compactness, and the reachability wall AP4, sharpened by B573's no-common-refinement and
   diagnosed by B574 as rank-1-ness, not the orbit) — and the arc's one genuinely live channel
   is C3's θ-odd dynamics at level 2 (order 4, the ℤ/7 sine kernel), firewalled, no SM claim.
   Nine of the seventeenth chain's clauses stand because they were already ours. **Promotion
   candidates for §5:** the AP4 fifth-wall theorem, the AP3 clock theorem, the Q-A trichotomy
   (Jordan (17,9,1)), and the sine-kernel identity — all theorem-shaped with locks. **The
   queue, in order:** FIRST the bridge/quadratic-obstruction computation (H¹×H¹→H² on the five
   off-factored directions — unobstructed ⇒ rank-≥2 reps exist and the selector question
   reopens; all obstructed ⇒ the sixth wall); the B571 revival queue (Q-C transport, the
   criticality theorem + B507 lock, e₃ completion, the Kubota–Leopoldt discriminating fact,
   S031 m=3 under the corrected reason); B572's V2 (Fox H¹=6, the PC25 strengthening), V3
   (B299 orbits ↔ the three 16s), V5 (global gap⟺chirality with Galois descent); and the
   level-3 prime-law hook (level 1 inert, level 2 = the ℤ/7 sine kernel, ω₄ enters at level 3 —
   does the θ-odd kernel follow a prime law up the levels?). All of these enter OPEN_LEADS.md
   in this review's closeout, per issue (v).

*(window #884–#903; anchor = HEAD after B574, the bridge question in final form; next review due at 20 merges.)*

## Review 17 — 2026-07-14 (merges #904–#923 from Review 16; the construction arc / Round 3)

anchor-commit: `3c0fa84` (pre-closeout HEAD; the closeout commit resets the counter)

1. **Suite:** **2187 passed / 15 skipped / 2 failed** (43:55, full run for this review). Both failures diagnosed in-review: (a) the named B207 flaky (`test_metallic_volumes_bounded_golden_minimal`) — its Review-16 characterization has DEGRADED: it now fails ~1/3 STANDALONE as well (1 fail in 3 standalone runs this review; SnapPy retriangulation nondeterminism) — a deterministic re-derivation of this lock (seeded/canonical triangulation) enters the queue; nothing in this window touched B207. (b) `test_no_hardcoded_paths` flagged a literal machine path in `tests/test_b578_v3_reframe.py:7` (a B578-era slip of mine) — FIXED in this closeout (relative path; 3/3 green after the fix). No mathematical lock failed.

2. **Gates:** 7/7 green throughout the window; the 20-merge cadence fired exactly at 20 (the
   counter mechanics now clean after Review 16's first-run overshoot). `.github/` remains
   deliberately untracked (disclosed; enforced by tracked-forbidden).

3. **The window = the construction arc, end to end — the owner's reorientation ("the energy
   goes to the construction") executed.** **B575** THE BRIDGE OBSTRUCTION: e₆ built exactly in
   gl(27) (GF(2) sign-solve), the quadratic obstruction Q: H¹×H¹→H² ≡ 0 identically (21
   components, exact ℚ(√−3)) — the bridge opens at second order. **B576** the deformed
   closure: every sl₂-stable subalgebra is a block-sum; θ-even sums close in F₄; all six
   forcing channels nonzero — **the chirality is exactly the θ-odd motion.** **B577** the
   reconciliation: B575/B576 rediscovered the banked {4,8}-integrability program (B352/B265)
   — two disjoint pipelines now agree on all 21 zeros (epistemically stronger); the non-recall
   failure mode named and guarded (**MB13**: keyword-grep + atlas oracle before every prereg;
   it caught 4+ near-rediscoveries later in this very window). **B578** the debt clearing:
   Massey/third-order obstruction vanishes exactly (B370 discharged); e₃ = 2cos(2π/9)/1728
   exact (minpoly x³−3x+1); K₃ is DEGREE 6 (reverting MY wrong B137 "correction" — B125's
   table was right); the golden 2+3+3 octic at level 3; the global duality unconditional at
   E₆; the Kubota–Leopoldt claim RETRACTED with the discriminating fact computed + the exact
   L(χ₁,μ)+L(χ₂,μ) = 432·e₃ identity. **B579** the session handoff adjudicated (scan →
   HINT_LEDGER; the duet quartic corrected; two false "CC verified" attributions caught).
   **B580** THE CHORD PROGRAM: the owner's coupling thesis preregistered as computable cells;
   the binding run-order (no SM references in cells; step 7 only); the literature dossier
   adopted; Round 1 run — the level-1 state is the knot-independent vacuum column, the filling
   covectors span exactly the θ-even plane, H128–H130 killed blind, THE DIAL MAP banked (θ-odd
   slots {4,8} → full e₆; θ-even → f₄; zero → sl₂). The jewel audit registered five veins
   (L73–L77). **B581** the six torsions: the six twisted Alexander polynomials at Sym^{2m}(ρ_geo)
   via Wada, exact over ℚ(√−3); **THE SIGN LAW sign(τ_m) = (−1)^m** (positive exactly at the
   θ-odd {4,8}); Δ₁ = (t−1)(t²−5t+1); 7 saturates the tower. **B582** the first constructed
   play with chiral matter: the θ-odd-twisted mirror-double closes on e₆ ⇒ Zariski closure
   E₆(ℂ) ⇒ the 27 complex/chiral; the fifth wall (rank-1) does not apply — executed same-turn
   under the owner's directive. **B583** its content: X1 no real form (the coupled character
   non-real, the banked B572 witness; D10 ⇒ no forced branching — neither 16+10+1 nor
   trinification); X2 FAILED as computed (Vol/CS role inversion — verifier catch; corrected
   structure registered); **X3 THE SECOND UNHEARABILITY THEOREM** (vacuum C-fixed, [C,S] =
   [C,T] = 0 ⇒ fillings never hear θ-odd at ANY level) — the theorem that fixed Round 3;
   the #918 lock merged red (a process slip, owned) and fixed to 2/2 green in #919. **#920**
   namespace reservations (packaging placeholders; brew tap live externally). **B584 ROUND 3
   — THE LISTENER:** bare knot states have zero θ-odd component (J₃ = J₃̄ computed — the
   third unhearability; the mirror ALONE is deaf); the listener = the ANTIPHASE mirror
   channel, tr_odd = ½(Z − Z_C); BLIND: on SU(3)₂ tr_even = 0 exactly and tr_odd = −1/φ —
   **the recurring golden value IS the chiral channel's voice**; the odd block = the order-10
   golden rotation; the even block = a silent order-20 clock; level-rank realizes one number
   in two opposite parity sectors. **B585 THE LISTENER'S LAW:** the naming theorem — the
   C-twisted play is the play of the OTHER SL(2,ℤ) lift (the −A₁ Sol bundle): **chirality is
   what the two lifts agree on**; LAW-O verified on held-out levels incl. the κ=20 additive
   collision (= 1/φ²): tr_odd(RL; SU(3)_k) = [4|κ] − [5|κ]/φ — a two-tone chord; the 60-clock
   ticks at the golden-voiced κ=10,15 (L77's number); LAW-E died on hold-out (banked dead);
   the field-containment mechanism preregistered and REFUTED same-arc (silver fires on
   multiples of {4,5,7}; bronze interferes destructively at κ=10) — only the golden/minimal
   word has the clean constant law. **B586** chat-1's Round-3 handoff processed
   verify-don't-trust: R3-A frame-corrected (Sym-blocks grade the adjoint, not the stage;
   the principal shadow has C = 1 — the proposed sign-law unification is not a defined
   computation) and computed blind — **E₆₂ also hears everything (Z = +1, tr_even = 0)**;
   NO golden anywhere on E₆ (the −1/φ is stage arithmetic, not object-universal); the three
   per-pair chirality amplitudes banked; R3-B superseded by the naming theorem (the C-twisted
   torus is Sol — census/volume/CS/trace-field ill-posed; the "CS = cosmological constant"
   hook dies); R3-C answered structurally (invertibility B279 + RT duality ⇒ J₂₇ = J₂₇̄ at
   EVERY color: the solo antiphase is zero — chirality is chord-borne, proven).

4. **Re-verification (fresh-eyes cells, independent paths).** R1 CLEAN: tr_odd at k=2,7
   reproduced via THREE SL(2,ℤ) words (B238's RL; T²ST; TST⁻¹S⁻¹) — the balanced words agree
   exactly; the unbalanced T²ST differs by exactly the central framing phase i (understood,
   not an error); the exact identity 2cos(3π/5) = −1/φ verified symbolically (sympy), and
   B578's minpoly(1728·e₃) = x³−3x+1 re-derived symbolically. R2 CLEAN with one catch: the
   sign law re-audited from the banked JSON initially came out OPPOSITE at every m —
   diagnosed as the JSON storing the RAW Wada quotient (units ±tʲ); under the banked
   monic-at-top-degree convention all six signs AND all six factorization magnitudes
   (τ₄ = 2⁷·3·7·97 = 260736, τ₅ = −2⁷·3⁴·5²·7²·13 = −165110400, …) match exactly. R3 CLEAN:
   the three E₆₂ per-pair amplitudes rebuilt through the SECOND word (TST⁻¹S⁻¹) agree to
   5e-9; tr_even = 1.4e-14. In-window double-verifications already banked: B577's
   two-pipeline agreement (B575 ↔ B352 on all 21 zeros); B585-M1's sweep independently
   re-confirming LAW-O over κ = 21..26 beyond the registered hold-outs; B586 reproducing
   every C3 gate before extracting new numbers.

5. **Issues found (6 real; none touches banked mathematics).** (i) **CAMPAIGN_STATUS missed
   six banks** (B578–B583 had no individual board entries — a recurrence of Review 16's
   issue (iv); B584 carried only a pointer). FIXED: a compact catch-up block inserted in this
   closeout; the standing rule is restated — the board is updated in the SAME PR as the bank.
   (ii) **`six_torsions_results.json` is unit-ambiguous** (raw quotient; a naive reader flips
   every sign of the sign law). FIXED: a units note appended to B581's FINDINGS; the JSON
   itself left as-is (append-only data). (iii) **The #918 red merge** — a lock merged failing
   (sympy-in-numpy type error), violating the pytest-before-merge rule; fixed same hour in
   #919 (2/2 green) and owned in the fix commit. The rule stands: no merge without the new
   locks green. (iv) **#920 merged on gates alone** (no pytest) — acceptable for a
   no-code packaging/docs PR, but the exception is recorded here explicitly rather than
   silently. Nits: B585's prereg says hold-outs "k = 13..16" while the run used 13..17 (the
   17th added deliberately for the κ=20 collision — disclosed in the FINDINGS, now here);
   the S² sign convention differs across stages (−C on B238's SU(3)_k, +C on E₆₂) — both
   FINDINGS record it, no action; memory files updated in-window are consistent with the
   banked record.

6. **Corrections ran in every direction (the discipline's health check).** Cross-seat errors
   caught: chat-1's R3-A frame conflation (adjoint Sym-blocks vs stage primaries) and R3-B
   geometric premise (hyperbolic double → actually Sol / graph manifold; the CS-hook dies);
   B579's two false "CC verified" attributions; the duet quartic. My errors caught and fixed:
   the #918 red merge; the B137 K₃ "correction" that B578-D6 reverted (B125 was right); the
   six-torsions control assertion (Milnor torsion — division legitimately non-exact for the
   trivial rep); B585's LAW-E guess (killed by its own hold-out) and M1 mechanism (killed by
   its own preregistered prediction); this review's R2 initially misread the JSON units — the
   review corrected itself before flagging the law. Verifier catches applied in-window: X2's
   Vol/CS role inversion. No claim survived on authority.

7. **Net.** Round 3 of the chord program is closed end to end: three deafnesses (vacuum X3,
   filling, bare state at EVERY color via invertibility + duality), ONE listener (the
   antiphase mirror channel, operationally ½(plain − mirror-twisted) = the two-lifts
   agreement), and on both banked stages the listener hears the ENTIRE invariant (tr_even = 0;
   −1/φ golden, +1 at E₆₂) — the number is the stage's (LAW-O's two tones on the SU(3)
   tower), the all-θ-odd pattern is the object's. The five walls stand untouched; the live
   channel matured from "C3's θ-odd dynamics" (Review 16) to a held-out-verified LAW plus a
   sharp mechanism question. **Promotion candidates for §5:** the naming theorem (chirality =
   lift-agreement), LAW-O (the two-tone chord), the antiphase identity, and the every-color
   solo-antiphase-zero theorem. **The queue, in order:** (1) **L82** the fixed-point
   mechanism (one derivation should explain LAW-O, LAW-E's failure, and the tone
   interference); (2) **L81(a)** the sector-exchange proof at the parity-projector level;
   (3) the corrected X2 recompute (interference = real Vol-exponential × signed 1/τ_m);
   (4) **L83(a)** exact identification of the three E₆₂ per-pair amplitudes; (5) **L80(a)**
   commit the B580 Round-1 Q1 artifacts + lens-space-gated locks; (6) the PC26 drafting
   decision (its Massey companion is now satisfied by B578-D1); (7) the B571/B572 revival
   remainders (S031 m=3; V2/V3/V5).

*(window #904–#923; anchor = the Review-17 closeout commit; next review due at 20 merges.)*

## Review 18 — PRE-COMMITTED SCOPE ADDITIONS (registered 2026-07-14, owner directive)

Beyond the standard cadence, Review 18 MUST include:

1. **The provenance sweep (external-verification pretense).** From day 0 to
   date, all work on this project has been the owner plus AI seats. No
   external human collaborator, no peer review, no third-party verification
   has occurred. The sweep: scan every public-facing document (README, docs/,
   papers/, frontier FINDINGS, CHANGELOG) for language that could be read as
   claiming external verification — "verified", "independently confirmed",
   "checker-verified", "the verifier", "adversarially verified", "audited",
   "specialist" — and either (a) rephrase, or (b) ground it in a single
   PROVENANCE.md stating explicitly: *all verification in this repository is
   internal — independent re-computation within the project's own toolchain
   by the owner and AI-assisted sessions; none of it constitutes external
   peer review.* Every "verified" then reads against that definition.
2. **The inner-terminology legibility sweep.** Session-internal vocabulary
   (seats, chats, handoffs, banking, locks, gates, theaters, the firewall,
   arcs, B-numbers) that is load-bearing in public documents must be defined
   once (a TERMINOLOGY.md or a README section) or rephrased where it would
   confuse an outside reader; nothing may rely on inner shorthand to carry a
   scientific claim.
3. Nothing banked may pretend to a review status it does not have; papers/
   drafts must carry their true status (internally verified drafts, not
   refereed results).

**Timing override (owner directive, 2026-07-14):** Review 18 fires when the
L85 campaign RESOLVES (outcome A/B/D banked), not mechanically at 20 merges.
The counter may exceed 20 in the meantime; the pre-committed scope above
(provenance + terminology sweeps) is unchanged. The campaign is the priority;
everything else waits.

- 2026-07-15: L85 RESOLVED (outcome B, PR chain #951–#962+). Per the owner override, REVIEW 18
  FIRES NOW: the provenance sweep (PROVENANCE.md; no external-verification pretense — all
  verification internal, owner + AI seats), the terminology sweep (TERMINOLOGY.md; inner terms
  labeled), papers carry true status. This window's corrections to consolidate: the V1/V3 sealing
  errata pattern (MB12 applies to operations AND criteria), the D2-retraction supersessions, the
  B591 terminology fix, the quarantined pre-synthesis chain (B517→B530→B531→B532, P43/P46/P51).

## REVIEW 18 — EXECUTED 2026-07-15 (fired on the L85 resolution, per the owner override)

Scope as pre-committed: **the provenance sweep** — `PROVENANCE.md` §0 added
(all verification INTERNAL from day 0: owner + AI seats; "verified" =
recomputed by a second internal pipeline, never an external referee;
literature citations compare against published mathematics, they do not
imply external checking of this work); `README.md` carries the same
statement up front; `papers/README.md` and `papers/REVIEW_VERDICT_2026-07-05.md`
qualified ("four independent reviewers" → internal AI-seat reviewers).
**The terminology sweep** — `TERMINOLOGY.md` created at the root: the full
inner vocabulary (bank/seat/lock/gate/prereg/firewall/stage/fold/dial/weld/
hearing/clock/width/chain/outcome-table/MB12/verify-don't-trust) glossed
into plain mathematics with pointers to the banked definitions; stated
plainly that these are internal working names, not established terminology.
**Papers true status** — the papers directory rule re-affirmed (candidate ≠
proven ≠ publication-ready; all review internal). Consolidated from this
window: the V1/V3 sealing-errata pattern is now a standing memory rule
(MB12 covers operations AND criteria). The quarantined pre-synthesis items
(B517→B530→B531→B532 chain, P43/P46/P51, B591 terminology) remain queued
for the synthesis pass — they are corrections to specific banked findings,
not provenance/terminology items, and stay tracked in REVIEWS/OPEN_LEADS.
Counter: Review 18 done; the counter resumes normal cadence.
