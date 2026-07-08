# The decadal repo reviews — ledger (GOVERNANCE §11)

Every ~10 merges on `main`, a whole-repo review fires: full suite + all gates +
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
