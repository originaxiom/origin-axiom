## Preamble — a staleness flag before the rules

Your checkout (`audit/b775-braver-questions`) is **behind `origin/main` on two of the seven documents**, which is exactly the E3 condition:

- `/Users/dri/oa-audit-seat/origin-axiom/docs/ERROR_LEDGER.md` local carries **E1–E26 only** — missing **E4a, E27, E28, E29, E30, E31, E32** and the E27 mechanical-sweep note.
- `/Users/dri/oa-audit-seat/origin-axiom/WORKING_RULES.md` local is missing the **sub-lemma / law-harvest clause of Rule 10**.

Everything below is read from `origin/main`. `docs/RETRACTIONS.md`, `docs/NOVELTY_AUDIT.md`, `docs/COMMS_PROTOCOL.md`, `docs/INPUT_COMPLETENESS_LEDGER.md`, `docs/LISTENING_PROTOCOL.md` are identical local↔main.

---

# (a) THE COMPLETE ERROR-CLASS CATALOGUE

Source: `git show origin/main:docs/ERROR_LEDGER.md`. Header rule: *"One entry per ERROR CLASS, not per incident… The question is always 'what standing rule would have caught this,' never 'who slipped.'"* (GOVERNANCE §13/§15; instituted 2026-07-16). 33 rows.

| id | name | seat(s) that committed / caught it | one-line |
|---|---|---|---|
| **E1** | Undeclared choice drift | cc2 (withdrawn h¹=3, 2026-07-16); program-wide (B637, B601-vs-B238) | A basis/sign/normalization/stage choice made implicitly then read as forced; results silently depend on it. Rule: the conventions block (GOVERNANCE §13); K020 forced-vs-chosen. |
| **E2** | Sealed-criterion vacuity / transcription | B644; L85 sealing errata; **cc's own** (C23 lock, 2026-07-24, self-caught); **cc** (OI-146, B772 audit) | A sealed gate that cannot pass for any genuine object, or a reference table transcribed wrong at sealing. Rule: MB12 covers operations AND criteria; vacuity-check both directions (WORKING_RULES §8). |
| **E3** | Stale-checkout false negative | the Door-2 packet seat (2026-07-16) | "No prior work exists" asserted from a thorough search of an out-of-date clone. Rule: sync-before-computing (WORKING_RULES §1). |
| **E4** | Necessary-read-as-sufficient | B519; Door-2 packet; the C2 design seat; **cc's own ×2** (C23 statement + B775 W4 Z1, both 2026-07-24); **cc** (OI-055) | A necessary/cited/proxied fact treated as the discriminating computation. Rule: compute the discriminating fact in-sandbox (the B525 audit rule); counter-rule GOVERNANCE §16. |
| **E4a** | *(E4 instance, 2026-07-28)* Asymptotic average used as a pointwise predictor | **cc**; refuted by **cc3** | cc predicted r = 8.863405 is the parent's k=2 Maass eigenvalue on a Weyl position 0.18 % from the slot; cc3's projective-line sector test refuted it (dev_min = 1.080; sole parent r = 7.072004 at 3.53e-10). Standing rule: **"Weyl/asymptotic proximity is necessary-ish, never sufficient — the discriminating test must be computed."** Aggravating: cc had argued the *same day* that a 0.344 % Weyl agreement was too weak to verify. |
| **E5** | Precision boundary | B640 first run | Low-precision constants fed into high-precision arithmetic; garbage that looks like structure. Rule: rebuild at target precision from exact sources (B629's 80-dps builder). |
| **E6** | Transcript-grep lock | the pre-audit B632 locks | A test asserting an output string rather than the mathematical fact. Rule: locks assert mathematics (WORKING_RULES §7). |
| **E7** | Overwritten failure record | B632 cell-2 | A failed run's output overwritten by the rerun. Rule: preserve failed outputs byte-faithfully BEFORE rerunning; hash corrected code before the rerun. |
| **E8** | Path assumption | the stray `docs/PROGRESS_LOG.md` (2026-07-16) | Writing to an assumed path (docs/ vs root; cwd drift after cd), creating strays or missing the canonical file. Rule: verify canonical path with `git ls-files`; prefer absolute paths. |
| **E9** | Overstated closure | B638 closure first draft | "Proved/forced" printed for what the solve actually left open (residual dimensions, one-way implications). Rule: state the solution-space dimension with the claim; direction-2 solves before "forced". |
| **E10** | External-verification pretense | "the external audit" phrasings, Review 20 | Phrasing that reads as third-party checking of internal work. Rule: PROVENANCE §0 grounding + review spot-sweep. |
| **E11** | Overextended record | Review 20 (64-hex hash from an 8-hex verified prefix) | Writing a full value where only a prefix/summary was verified. Rule: never transcribe beyond what was computed THIS session. |
| **E12** | Global-state leakage between locks | Review 20; b204; B666 cell 5; landed B676 | A test mutates process-global state (`mp.mp.dps`, caches, cwd) that later tests inherit; order-dependent failures. Mechanism is **collection-time import**. Rule: per-test fixtures (the b204 pattern); conftest collection-finish guard. The earlier "collects after ⇒ exonerated" inference is FALSE and withdrawn. |
| **E13** | Stale artifact text | B649 stage-1/2a; caught by cc2's receipts | Prints/comments describing a superseded method baked into a sealed artifact; the mathematics is right, the record misdescribes it. Rule: pre-seal grep of prints/comments against the method actually executed. |
| **E14** | Noise-band artifact banked as a value | B480's "⟨r⟩ = 0.16"; corrected B666 cell 6 | A float observable on an exactly degenerate spectrum banked as well-defined. Rule: state the convention exactly and verify stability across ≥2 noise realizations / solver scales. |
| **E15** | Exponent-as-base misread (GSWZ eq 2) | B682; corrected B685 | Read denominators 1/3³, 4/3⁵ as "{3,5} = being × hearing"; 3³,3⁵ are POWERS OF 3 — the series is PURE BEING, NO 5. Rule: re-read the source at exponents-vs-bases. |
| **E16** | Chirality over-reading | **cc's own** ("my E-2a/S067 read"); caught by **cc2** | Read opposite Atkin-Lehner signs w₃=+1, w₅=−1 as emergent bifocal chirality; they are FORCED by E₁₅'s even rank — a generic elliptic-curve fact, zero 3-vs-5 content. Owned B695. |
| **E17** | Swap/weld conflation | **cc2** introduced the framing; **cc** banked it; caught by cc2's self-recheck (B702, corrected 2026-07-19) | The "metallic hearing ⇔ real-quadratic SWAP field" law conflated the being-face SWAP (imaginary) with the hearing-face WELD (ℚ(√5)). Rule: a "hearing/tone" claim must name WHICH object (swap=being vs weld=hearing) and its field's real/imaginary type BEFORE the law is stated. |
| **E18** | Workflow-artifact provenance under degradation | B719 (4 API stream-timeouts); caught by a skeptic | A compute agent's saved `_out.txt` contained verdict text not generated by its committed script; a key probe silently never ran. Rule: on ANY degradation signal the banking seat RE-RUNS the load-bearing computation clean in-seat; a probe that did not run is carried OPEN, never inferred. |
| **E19** | Adjudication by cited negative | **cc's own** (courier-seat SEEING, first pass); owner-prompted; corrected B724 | cc dismissed 3 of 5 correspondences by CITING banked negatives as if citation were refutation. On computation C1 was SOUND, C2 OPEN, C4 a CATEGORY ERROR. Rule: **"B-number X refutes this" is a hypothesis to check, not a refutation.** |
| **E20** | Structure-skepticism lagged number-skepticism | program-wide self-audit (B727); cross-verified with cc2 | The flagship structural claim ("E₆ recurs across McKay / Lie / CIZ") never got the base-rate test the numbers got; it came back GENERIC. Rule: before treating a structural recurrence as object-specific ask (a) are the faces canonically linked? (b) how short is the catalogue / birthday problem? (c) does a comparable object share it? |
| **E21** | SL-level over-read before the PSL/center bookkeeping | a research agent AND **cc's first pass** (B731); cc2's guard flagged it | Concluded "m004 congruence at level (4)" from SL image index 12, skipping the SL→PSL center (order 4 at level 4) ⇒ PSL index is 6, not 12. Rule: quotient by the FULL center of SL(2,O/I). |
| **E22** | Premature non-congruence from a shallow level-check | **cc** (B731); corrected by **cc2** computing + **cc** verifying (B734) | Index plateau at 6 through level (4) read as stabilization; it jumps to 12 at (8) — m004 IS congruence. Rule: never infer NON-congruence from a finite plateau; two consecutive powers is not stabilization. |
| **E23** | Level-convention ambiguity | **cc3's proposal, cc's formalization** (adopted 2026-07-22, R27-5) | A "congruence level" silently depends on which filtration (SL-kernel vs PSL/mod-center). Rule: every level claim names its convention; cross-seat comparisons convert to ONE convention before adjudicating. |
| **E24** | Verdict-by-unauthenticated-signal | **cc3's proposal verbatim**; instance = the forged SEAL-READY signal during B742 | A review outcome accepted from a channel without provenance. Rule: verdicts read ONLY from the preserved review artifact; any completion signal lacking metadata is quarantined; **execution never starts inside a review window**. |
| **E25** | Integer-relation false witness — the unbounded-coefficient trap | **cc2's own-goal** (door-1 tool; 20 false CONTAINS verdicts), caught by its own exact factornf cross-check | Numeric lindep/PSLQ witnesses with ~65-digit coefficients beating a naive residual threshold. Rule: thresholds must be coefficient-height-aware AND every verdict-bearing relation gets an exact verification; tool-level look-elsewhere is budgeted. |
| **E26** | Blind-projection negative | **cc** (B766 θ-T6 lesson; B772 adequacy audit) | A "no structure" verdict computed in a cyclic-trace/abelianized projection that is invariant under the sector where the structure is claimed to sit. 4/14 banked negatives flagged TRACE-BLIND-RISK; recomputation launched as B773. |
| **E27** | Disconnected verdict | found at the **B784 audit** (2026-07-24) across cc's arcs B780/B782/C22/CL-LATIN/B781 | The flag that decides the outcome is not wired to any computed quantity — literal booleans, hardcoded truths, a silent except-fallback, a classify() that maps inputs by definition. **4 vacuous locks and 9 documents carrying a false statement traced to this one mode.** Rule: every verdict flag traces to a computed quantity; a sealed two-outcome branch must be REACHABLE. Mechanical sweep 2026-07-25: **20/20 data-connected locks wired; net 0 genuine E27 remaining.** |

## The E28–E32 batch — quoted near-verbatim (banked 2026-07-28)

> **E28 — Silent-discard filter.** *Definition:* "a tolerance/membership filter that drops data **without reporting what it dropped**. Because the dropped items are systematically the hard cases (long geodesics, large norms, poorly-conditioned rows), the filter selects for the author's expectation and manufactures self-vindication."
> *Standing rule:* "**a filter that discards data must report its discards** — count them, report the worst discarded case, and treat a large discard fraction as a failed run, not a clean one."
> *Instance:* "**cc's own instance (B794, 2026-07-28)**: cc's ℤ[ω]-membership filter (tol 1e-7) silently dropped long geodesics while re-checking cc's OWN hint H-B788-NORMSPLIT; it returned 12 m004-only norms against cc3's 41, 'upholding' the claim. The dropped geodesics carried exactly the disconfirming odd norms (7,103,127,175,367). cc3's proved mod-4 theorem settled it against cc. Class named by Chat-1 in relay; **it caught cc within the hour of being proposed**."

> **E29 — Post-hoc analysis-model selection.** *Definition:* "multiple defensible analysis models (nulls, surrogates, tolerances, windows) exist; the one reported is chosen **after seeing outcomes**, and typically the most permissive. The individual computation is correct; the verdict is chosen."
> *Standing rule:* "the pre-registered model is the primary and is named in the prereg; any additional model is reported **alongside** it, never in place of it, with both numbers shown."
> *Instance:* "**cc's own instance (B790, 2026-07-28)**: prereg §2 named the density-matched null as primary; cc reported 'ordinary noise' off a **uniform** null that was never pre-registered. Compounding: cc's 'Weyl-matched' null was itself miscoded (e^ℓ instead of e^{2ℓ}), so **neither** reported model was the committed one. Caught by Chat-1. Corrected verdict (pool-matched, two models agreeing) still MISS, but earned."

> **E30 — Output-verified, derivation-unverified.** *Definition:* "a result's *numbers* are independently reproduced and the result is then called verified — while the *argument* that produced them is never checked. Every table row can be right and the premise still wrong."
> *Standing rule:* "verification names which layer it reached: numbers, derivation, or both. Reproducing a table is not checking its derivation, and a receipt must say which it did."
> *Instance:* "**cc's own instance (B791, 2026-07-28)**: cc re-derived all eight rows of Chat-1's Weyl budget from the L-value and confirmed them exactly — while the derivation behind them divided out a multiplicity that is not there. The arithmetic was right; N_i(T) = dim(V_i)·W(T), not W(T). Consequence: Chat-1's headline 'Gate 9 cannot discharge Gate 5' evaporated once the factor was restored."

> **E31 — Instrument-precondition unchecked.** *Definition:* "a measuring instrument returns a confident, precise number while a *validity condition* of the instrument is unmet — matrix rank, truncation margin, grid resolution, convergence radius. The number is not wrong so much as meaningless."
> *Standing rule:* "before trusting an instrument, assert its preconditions **in code**: overdetermination (rows ≫ cols), truncation margin vs the scale being probed, and a **displaced negative control** that must FAIL."
> *Instance:* "**cc's own instances ×2 (B795, 2026-07-28)**: (a) collocation run at 90 points × 112 modes — nullity ≥ 22 by construction, σ_min ≈ 1e-48 for every r *including controls*; would have 'confirmed' any input. (b) Bessel truncation margin 1.4× at r = 8.86 (needs ≳ 2×); the top two eigenvalues read as ABSENT. **Stopping one run earlier would have published a false negative aimed at another seat's correct result.** Both caught by the displacement controls, not by care."

> **E32 — Unfalsifiable premise (local rigour, global immunity).** *Definition:* "every *cell* carries a pre-registered falsifier and the *campaign premise* carries none. Each cell can fail correctly while the premise survives untouched ('we haven't found the right mechanism yet'). A programme can run to completion, produce nothing, and leave its premise as 'banked' as on day one."
> *Standing rule:* "a campaign states a **campaign-level** falsifier distinguishing its premise from the null-of-no-connection; if none can be written, the campaign is labelled **exploratory-interpretive** and nothing from it banks as *evidence for* the premise — only as mechanism-exclusions."
> *Instance:* "**B796 coupling campaign (2026-07-28, gated pre-launch)**: premise written as 'H0 (banked, now the campaign's **positive target**): values live in the observer–object coupling', justified by the refutation of values-in-the-object. **Refuting the rival does not establish the premise** — every banked null (character variety, rung-1 PSLQ, forced limits, B792 spectral) is predicted *identically* by H2 = 'the object has nothing to do with the SM', which the plan never states. Per-cell falsifiers were added and do **not** fix this."

**Attribution note for cc3:** the ledger's session note says these are "all from cc," but the E32 *instance* is the B796 coupling campaign plan, which per the relays (`/Users/dri/oa-audit-seat/origin-axiom/CC_TO_CC3_2026-07-28_B793_collision_and_a_logical_error.md`, `…_per_cell_falsifiers_are_not_enough.md`) is **cc3-authored and gated pre-launch by cc**. Read E32 as binding on cc3's campaign designs directly.

**The session note, quoted (2026-07-28):**

> "E28–E32 all arose in one session, all from cc, and all share one shape: **a confident, precise output whose preconditions were unchecked** — the filter's discards, the null's provenance, the derivation behind the table, the instrument's rank and margin, the premise's falsifiability. None was a hedge; every one would have been read as a clean result. Of seven instances, **cc self-caught two**; the rest were caught by cc3, by Chat-1, or by a control built for another purpose. The operative lesson is not 'be careful' — it is that **controls built for one purpose catch errors of another**, which is the argument for keeping them when you are sure they are unnecessary."

---

# (b) THE RETRACTIONS INDEX

Source: `git show origin/main:docs/RETRACTIONS.md`. Scope rule: *"DISTINCT from `docs/ARCHIVE.md` (ideas killed at testing) — these were once asserted in the record and later corrected, withdrawn, or superseded; a reader of an old FINDINGS could still act on them."* Maintenance rule: **same-PR — every future retraction adds its row in the PR that banks the correction.** 12 rows:

| # | What was asserted | Banked at | Correction | Corrected at |
|---|---|---|---|---|
| 1 | B519's negative: "no external crossing" (read as sufficient) | B519 FINDINGS | **RETRACTED** — mixed-chain gap-opening is falsifiable; the discriminating fact was never computed in-sandbox | the B525 audit (3/10 banked negatives cracked); the compute-the-discriminating-fact rule |
| 2 | "exponent = rank from Cayley–Hamilton" (SL(4)) | B90/V74 | **REFUTED** — both SL(4) components satisfy L1b with exponents 4 vs 3; L1a was a tautology | the V75 audit; B90 reclassified as reformulation |
| 3 | B95's "forced" principal spectrum read unconditionally; "any 5-dim rep reducible/non-ss 0/120" | B95/V79 | **CORRECTED** — "forced" is conditional on the mult-(n−2) ansatz; non-ss irreducibles exist (2 certificates); n=5 absence holds only for the finite-order/principal family | B153/V142–V145 |
| 4 | PC13's "SL(4) component" claim | PC13 | **REPLACED** — degree=rank is rank-stratified: component@3, slice@4, absent@5 | B153 |
| 5 | The "E₆→SM dictionary" (a cross-seat handoff) | chat-1 handoff, 2026-06 | **VERIFIED-AND-REFUTED** — G₂⊕A₂ mislabeled as E₆; the numerology killed | B347 (replacement: E₆ tangent = 6; θ = E₆→F₄ split) |
| 6 | The trefoil(5,1) trace-field inheritance reading (Tr τ ∈ ℚ(√5)) | B437_child_abelian_book (+B438/B440 foreign controls) | **RETRACTED as inheritance** — numerator-forced, not inherited | PROGRESS_LOG 2026-07 (the (5,1)-filling control) |
| 7 | The "entropy log β" reading of the growth rate | B523_verdict_reexamination + B530_natural_history | **RETRACTED** — primitive subshifts have zero entropy; the quantity is the inflation growth rate | PROGRESS_LOG 2026-07-15 |
| 8 | The quadratic-arrow verdict (all forms) | the L85 campaign | **RETRACTED IN FULL** — longitude convention corrected AND the re-derived form ALSO retracted by the same arc's erratum ("no map was constructed to have an order"; survives only as heuristic expectation). *Row itself corrected 2026-07-21: the earlier "(quadratic stands in corrected form)" contradicted its own cited source — cc2 register crack #3, cc-verified* | B598-P2 + P1_ERRATUM D1–D10 |
| 9 | The Kubota–Leopoldt attribution claim | B507_beta_function + the Review 25 sweep | **RETRACTED** with the discriminating fact computed | REVIEWS (2026-07-15 sweep) |
| 10 | B609's unit-modulus exploratory note | B609 | **SUPERSEDED** — exploratory reading replaced by the exact law | B611; Review 19 (i) |
| 11 | A parallel seat's h¹(D_conjθ) = 3 | a cross-seat packet, 2026-07-16 | **WITHDRAWN by the originating seat** — an assumed λ-sign; the dimension is genuinely open (the object is a fiber pairing, not a rep twist) | B639; L92 re-scoped; the cc2 adjudication note |
| 12 | The B615 amplitude suggestion read at p = 0.078 | B615 | **DISSOLVED** — scheme/scale defect; corrected inputs give 0.145–0.62 across all variants (verdict A) | B615-R (seat 4), integrated B633 |
| 13 | "The naive flip acts on the double" (the L93 candidate as first posed) | L93's design | **REFUTED** — the flip does not act (either J-convention); both outer involution classes broken (partial intertwiner on Sym⁰ only) | B643; LAW_MAP wall 8 |

*(13 rows; note row 8 is itself a retraction-of-a-retraction-row — the index polices itself.)*

**Not yet rowed but retracted in relay:** cc's "the gap to physics is *categorical*" framing, withdrawn 2026-07-28 in `/Users/dri/oa-audit-seat/origin-axiom/CC_TO_CC3_2026-07-28_B793_collision_and_a_logical_error.md` → "**unbridged, not categorically unbridgeable**" (3d-3d correspondence supplies dynamics; Connes–Chamseddine spectral action supplies scale). Also cc's E4a prediction (r = 8.863405 is parent) — retracted in `CC_TO_CC3_2026-07-28_PREDICTION_r8863_is_parent.md` follow-ups. If either is still unrowed at the next bank, that is a same-PR-rule violation.

---

# (c) THE COMMS / COLLISION / RESERVATION CHECKLIST — what cc3 must follow

Sources: `docs/COMMS_PROTOCOL.md` (v1.1 — note it is written for the *three*-seat room: owner + cc + cc2 + chat1; the cc3 rules live in `docs/SEAL_LEDGER.md`, Review 27, and the root relay files).

### C1. Addressing and intent (COMMS_PROTOCOL §1–§2)
- [ ] Open every message with **@cc / @cc2 / @chat1 / @all**. No tag → @all. "You" mid-thread = the seat you last addressed.
- [ ] Use the verb set. **ACTION verbs:** `go` / `decision:` (**OWNER ONLY**), `task @seat:`. **NON-ACTION:** `q:`, `plan:` / `propose:`, `fyi:`. **BETWEEN ANY PARTIES:** `challenge:` (disagree WITH evidence), `result:` / `verify:`, `clarify:`.
- [ ] **Act ONLY on `go` / `decision` / `task`** — never on `q` / `plan` / `fyi` (§4).
- [ ] On anything ambiguous **AND irreversible**: ask `clarify:` first. Do not act on a guess (§3).
- [ ] A background/system notification is **NEVER the owner's word** (§4).

### C2. Challenge rights (§3, §4a)
- [ ] Challenge any seat, including the owner's proposal — "this is the firewall; it is encouraged, not rude."
- [ ] A `challenge:` is closed by **EVIDENCE** — a computation or a base-rate cell — **never by authority or repetition**. Unresolved after both sides compute → escalate to owner as `clarify:`.

### C3. The result→bank ritual (§4)
- [ ] Every **result** → **verify** (two independent routes) → **bank**. Nothing is real until banked in the repo.
- [ ] **The base-rate + convention gate is MANDATORY** inside verify→bank: every numeric "match" or "nice value" must pass (a) a base-rate cell AND (b) a convention/unit-robustness recompute BEFORE banking. *No proximity banks alone.* (E16, θ₀=2/9, the E₆-denominator, 7983360 each failed this.)
- [ ] **Negatives bank too** — kills/falsifications banked with the same ritual, so a killed idea cannot be silently re-proposed.
- [ ] **Supersession citation**: every result/proposal cites the HEAD or B-number it builds on.
- [ ] **Standing-go scope**: a seat on a timer/loop acts only on the standing go for the **specific in-flight task**; a new decision-point needs a fresh owner `go`. No scope creep from an old authorization.
- [ ] One decision per thread; the owner's `decision` closes it — do not re-litigate.
- [ ] One-shot/irreversible: explicit `go`, and **name the exact target back** before firing.

### C4. The listening gate (§4b)
- [ ] Before ANY object↔reality comparison, apply `docs/LISTENING_PROTOCOL.md`: name the rung (only 1–3 = the object speaking; **rung-4 value-matches are dead by B685**), run the §4 checklist (rung · swap-vs-weld + field-type · convention · Galois-invariance · base-rate). Predict the STRUCTURE of the arbitrariness, never the values.

### C5. Channels (§6) and the relay convention (observed practice)
- Owner's live channel = human-visible room (private, not part of the record). `/relay` folder = seat↔seat working channel. **The repo = the durable record; nothing is official until it's here.**
- [ ] **Relay filename convention (in force, root of repo):** `CC_TO_CC3_<YYYY-MM-DD>_<topic>.md` and `CC3_TO_CC_<YYYY-MM-DD>_<topic>.md`. Every relay opens with the seat name + date + the branch/commit it refers to (e.g. `CC3_TO_CC_2026-07-22_p3_complete.md`: "cc3, 2026-07-22. Branch `hunt/p3-depth-exposure`, commit `2817a1b8`").

### C6. Monitor cadence (binding both ways)
- [ ] **`git fetch origin && git log --oneline origin/main -15` at the START of every work block, before choosing what to compute** — the cadence fix adopted 2026-07-28 (`CC_TO_CC3_2026-07-28_MAASS_numbering_and_replication.md` §5: *"The replication was free this time; it will not be next time"*). Restated in `…_B793_collision_and_a_logical_error.md`: *"That cadence rule binds on me too and I have kept it since."*
- [ ] **Commit deliverables.** *"my monitor watches commits, so an uncommitted file is invisible to it (now fixed to watch the working tree too, but commit anyway so the loop is tight)"* — `CC_TO_CC3_2026-07-25_S_gated_and_direction.md`.
- [ ] cc's reciprocal obligation: *"I will relay same-day whenever I bank something in your active area."*

### C7. The RESERVATION PROTOCOL (adopted Review 27, 2026-07-21, after the B742 numbering collisions)
- [ ] **Reserve the B-number BEFORE first use**, by appending a `RESERVED: B<n> (<seat> — <one-line scope>)` row to the **append-only section** of `docs/SEAL_LEDGER.md` ("## Reservation & verdict rows (APPEND-ONLY — the collision protocol; preserved by the generator)", line ~212).
- [ ] The row states **seat, scope, date, and authority** — e.g. `RESERVED: B754 (cc3 — the P2 stratum … branch hunt/p2-spectral; PR-only, cc = merge gate) | — | — | 2026-07-22 | number reservation per the collision protocol (relay CC3_TO_CC_2026-07-22_p2_reservation + cc ACK)`.
- [ ] A cc3 reservation requires a **relay + cc ACK** (the pattern in every cc3 row: B749, B754, B759–B762, B765, B767).
- [ ] Post-hoc regularization is possible but must be **labelled as such** (B765: *"post-hoc regularization: cc3 ran on the R28-5 queue authority before the numbered GO crossed"*).
- [ ] **Never run `scripts/seal_ledger.py` in a way that could clobber the append-only section** — the 2026-07-22 safety fix exists because a regen would have destroyed all 22 RESERVED rows plus every verdict row (PROGRESS_LOG 2026-07-22).

### C8. The collision protocol in practice (2026-07-28 rulings)
- [ ] Collisions are resolved by **cost, not seniority**: *"B788 = the EXTERNAL Gates 0–9R Maass bank. It keeps the number because renumbering would break 62 recorded artifact hashes and its internal cross-references. The other two carry no such cost."*
- [ ] **Renumber the directory, never the sealed bytes.** *"B790's PREREGISTRATION.md still says 'B788' inside and was deliberately left byte-frozen, because its sha256 is pinned in SEAL_LEDGER. A sealed artifact that gets rewritten is no longer sealed."*
- [ ] Duplicated work is recorded **two ways, not collapsed**: evidence side = accidental independent replication (cited with both commits); coordination side = a scheduling defect.
- [ ] Currently taken as of 2026-07-29: B788 (external bank), B789, B790, B791, B792, B793 (Gate 8R2-A parent localisation), B794, B795 (cc's verification of cc3's eigenvalues), B796 (coupling campaign). **Take B797+ and verify against `origin/main` first.**

### C9. Branch / merge discipline for cc3 (from the gate relays)
- [ ] **PR-only; cc is the sole merge gate.** cc3 branches stay **unmerged** — "collision-safe." cc **cherry-picks** what survives **under a fresh cc number**. *"Do not merge; cherry-pick as usual."*
- [ ] cc's gate standard: *"reproduce the load-bearing claim of each branch in-sandbox before any cherry-pick, not grading from the writeup"* (`CC_TO_CC3_2026-07-25_gate_status.md`).
- [ ] Order of gating: math branches first (decisively verifiable), firewall-side forks last.
- [ ] Refuted positives are **not** cherry-picked; the surviving negative may be banked under a new cc number.

### C10. Verdict provenance (E24, binding)
- [ ] Read verdicts **only** from the preserved review artifact. Quarantine any completion signal lacking metadata. **Never start execution inside a review window** (GOVERNANCE §16.1).
- [ ] Adopted cc3 hardening now standing for all seats: **journal-only result channel, disk-written verdicts, nonce liveness probes** (Review 27 §2d — nine forged workflow signals, all caught).

---

# (d) THE WORKING RULES CHECKLIST

Source: `git show origin/main:WORKING_RULES.md` — *"One page. Every working session — any seat, any clone — reads this first."* Instituted 2026-07-16 (GOVERNANCE §12–§15). 14 binding items (1–13 with a 6a):

1. [ ] **Sync before computing.** Pull/fetch and confirm your checkout includes the latest `main` BEFORE claiming "no prior work exists on X." A thorough search of a stale checkout produces confident false negatives (the Door-2 class: the answer existed, three merges ahead).
2. [ ] **Verify, don't trust — in both directions.** Every cross-seat claim reproduced in-sandbox before banking; so is every claim of your own before asserting it to another seat. Incoming ambitious framing is quarantined; incoming mathematics is re-run.
3. [ ] **Hash first.** Seal PREREGISTRATION.md (sha-256 in the arc's ARTIFACT_HASHES.txt) before the first run. Failed runs preserved byte-faithfully, never overwritten. Corrected code re-hashed BEFORE the rerun, labeled post-hoc if sealed late.
4. [ ] **Declare every choice.** The conventions block (GOVERNANCE §13) lists every basis, sign, normalization, orientation, and stage choice before the run. *Undeclared choice drift is this program's most recurrent error class.*
5. [ ] **The layers are one-way.** Coupling-tier content (hints, adjudications, speculations, reviews) is never evidence for a layer-1/2 statement. The firewall blocks overclaims, not mathematics.
6a. [ ] **Gate 5-Q stands for phenomenology.** Any arc using reflexive/phenomenological vocabulary is bound by `philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md` (adopted 2026-07-22): computed-referent vocabulary, non-universality and comparator controls, input identification, stability analysis, no consciousness claims, any-domain empirical constants = value-claims. **Checked at prereg seal and merge.**
6. [ ] **Gate 5 stands.** No SM quantities into `CLAIMS.md`; no recycling structured-null numbers under new labels; physics readings wait on the typed functor (L91). Value comparisons need: **owner directive + sealed design + MB12 + MB13-in-doc + pipeline controls + the INPUT_COMPLETENESS_LEDGER row.**
7. [ ] **Locks assert mathematics.** A test asserts (or re-computes) the mathematical fact, not a transcript string; transcript asserts are the marked fallback.
8. [ ] **Vacuity-check before sealing.** Every sealed criterion must be able to pass AND to fail (MB12 covers operations and criteria); check reference tables/targets for internal consistency before sealing.
9. [ ] **Zero file moves.** Never move or rename banked paths (GOVERNANCE §12). New work = new files. Views and metadata evolve; the substrate is frozen.
10. [ ] **Bank completely.** Every banked arc updates PROGRESS_LOG (append at END) + CHANGELOG + CAMPAIGN_STATUS in the same/next PR; a new law adds its LAW_MAP row in the same PR; new inner terms get TERMINOLOGY.md lines; the atlas regenerates per new B-dir. **This covers SUB-LEMMAS, not just an arc's headline** — any theorem/law-grade result proved along the way gets its own LAW_MAP row. A standing **law-harvest** runs at every review. *(⚠️ This second half is MISSING from your local checkout.)*
11. [ ] **Attribution and privacy.** Commits as `originaxiom`; no AI mentions in anything public-facing; scrub sandbox paths from committed files. After every merge to `main`: `git push codeberg main`.
12. [ ] **Report faithfully.** Negatives bank as computed facts with their discriminating computation in-sandbox (never asserted/cited/proxied); **an unearned negative is as bad as numerology.** Don't stop and celebrate negatives; don't soften positives that passed their gates.
13. [ ] **Instantiated designs get a factual review (GOVERNANCE §16).** Any sealed design whose premises name real-world facts is adversarially fact-checked by a **NON-AUTHORING** reviewer (a fresh subagent under the §16 standing prompt is valid) **between seal and execution**; every empirical predicate carries a live source + access date, never a model prior; **"the premises look wrong" is a stop-condition for every executing seat.** Blinded lanes (predictor/comparator) still require genuinely separated seats — the subagent equivalence is for FACTUAL review only.

---

# (e) THE LISTENING PROTOCOL — the rung ladder and the traps

Source: `git show origin/main:docs/LISTENING_PROTOCOL.md`. Authored by cc2 on the owner's go, 2026-07-19; cc reviewed, refined (§8), banked. Algebraic spine = the B704 seam. **A methodology instrument, not a physics claim.**

### §0 The thesis it enforces
The object forces **FORM, never VALUE** (B685; K020). The measurement torsor is **non-canonical** (phase-2 / B701): the object hands you the Galois **orbit**, never the point. So any bridge to reality must (a) compare STRUCTURE, not numbers, and (b) predict the **structure of the arbitrariness**, not the values. Operational law: *"The object goes silent when we speak for it" — asking for a value is speaking for it.*

### §1 The comparison hierarchy — name the rung BEFORE comparing
*"Only the top rungs are the object SPEAKING; the bottom are speaking FOR it."*

| Rung | Name | Definition (near-verbatim) | Status |
|---|---|---|---|
| **1** | **FIELD / REALITY** | "does the external structure live in the object's field, on an AUDIBLE direction (real quadratic, p≡1 mod 4)? **Most rigid; hardest to fake.**" | May proceed |
| **2** | **TORSOR / GALOIS** | "does the external FREEDOM organize as the object's non-canonical torsor / the B704 𝔽₂ seam (**no canonical origin**)? Falsifiable: a torsor is or isn't there." | May proceed |
| **3** | **FORM / RELATION** | "does the external structure satisfy a relation the object **FORCES** (a sum rule, a selection rule, a factorization), specific enough for a low base rate?" | May proceed |
| **4** | **SINGLE-RATIO** | "number ≈ number. Requires BOTH a base-rate cell AND a forcing mechanism. For THIS object B685 denies the value-forcing mechanism ⇒ **rung-4 value-matches are DEAD ON ARRIVAL, however small the σ-distance.**" | **STOP** |
| **5** | **FIT** | "free parameters tuned to agree. **Meaningless by construction.**" | **Never counts** |

**Gate rule (verbatim):** "rung 1–3 may proceed; rung 4 stops unless it clears base-rate AND a mechanism (it won't, for values); rung 5 never counts."

**§8.1 — Rung 1 is falsifiable-TO-PRECISION.** "Lives in the object's field" is an **ALGEBRAICITY test**, not a yes/no on finite precision: run PSLQ/lattice reduction on the measured, convention-reduced quantity against a basis of the predicted field ℚ(√p*), bounded to degree ≤ d and height ≤ H. **The falsifier is *precision*** — a genuine structural relation survives more digits; a numerological one breaks at the next digit. Report the digit at which it holds and the digit budget; a rung-1 hit is only meaningful **if it survives beyond the digits used to find it**. This is what separates rung 1 (membership in a fixed low-degree lattice = measure-zero, base-rate-immune) from rung 4 (proximity to a fraction = not measure-zero, base-rate-dead).

**§8.2 — Rung 2 is where B704 actually runs (the deepest door).** Take the SM's irreducible, un-derivable freedoms (the flavor parameters), reduce them to their **Galois-invariant field data**, and ask whether that data organizes as the seam's **𝔽₂-multiquadratic structure** (stages = basis, meetings = 𝔽₂-sums, NO canonical origin) — **not** whether any parameter equals a value. A rung-2 result is a statement about the SHAPE of the freedom, and it is falsifiable.

### §2 The structural vocabulary (the only legitimate comparanda)
- **Fields:** ℚ(√5) (hearing, real, **AUDIBLE**), ℚ(√−3) (being, imaginary), ℚ(√−15) (meeting), general stage field ℚ(√p*).
- **The seam (B704):** the 𝔽₂-vector space where STAGES are a basis, MEETINGS are 𝔽₂-sums (the genus bit), with **no canonical origin** (B701). Compare basis vectors and their sums, never coordinates.
- **Audible directions:** p ≡ 1 mod 4 (real quadratic); the fundamental-UNIT tone (p=5 golden, uniquely metallic). Audibility **types** the seam basis.
- **Torsors:** the non-canonical Galois torsors (fiber functor = measurement). The measurement lives in the orbit, never the point.
- **Groups / arithmeticity:** 2I/2T/2O, E₈/E₆, McKay data; torsion-of-shapes (golden = the unique arithmetic bundle).

### §3 The meta-stance — what to predict
Predict the **structure of the arbitrariness**: WHICH external parameters are Galois-related (the form); WHAT field/torsor their freedom forms (the shape of the choice); the AUDIBLE/inaudible dichotomy (what is even hearable). *"The output is NEVER 'the object predicts value X.' It is 'the object forces structure S; the external system has S or it does not.'"* Reduce the external system to its convention-INDEPENDENT (Galois-invariant) invariants FIRST — *"the object only speaks Galois-invariant truth; comparing to human bookkeeping parameters compares to a frame, not to reality."*

### §4 The mandatory gate checklist (before ANY object↔reality comparison)
1. [ ] **NAME the rung** (§1). Rung 4–5 → stop per the gate rule.
2. [ ] **NAME swap-vs-weld and real/imaginary field-type FIRST** (E17 — the B702 lesson).
3. [ ] **Convention / unit-robustness check** (the θ₀ trap; the melody/period trap).
4. [ ] **Galois-invariance**: the compared quantity must be convention-free.
5. [ ] **Base-rate cell** for any numeric coincidence (the 7983360 lesson).
6. [ ] If it survives 1–5, state it as a **FORM match at its rung** — never as a value.

### §5 The traps (worked calibration — every listed case)

| Case | Verdict | What it teaches |
|---|---|---|
| **The golden's 3-way uniqueness** (fundamental-unit tone A; only arithmetic bundle C; hears-because-fibered B) | **GOOD (rung 1–2)** | Each answers "what is the golden's TYPE"; none is a fitted number. *"This is the object speaking."* |
| **θ₀ = 2/9** | **TRAP (rung 4)** | Corrected 7σ → 0.89σ (CONSISTENT) **yet STAYS firewalled** — tautology (Q = 2/3) + no forcing mechanism + convention-dependence. The σ-number was itself a mis-done ratio comparison; the verdict rests on structure. **"Consistent ≠ meaningful."** |
| **B702's silver-SWAP-tone vs golden-WELD-tone** | **CONFLATION-AND-FIX** (why §4.2 exists) | Compared different objects in different (imaginary vs real) fields. Retracted; the audibility law (real weld/character field) is the home. = error class **E17**. |
| **7983360 = \|W(E₆)\|·154** | **BASE-RATE-DEAD** (rung 4 failing §4.5) | A smooth-number coincidence, not structure. |
| **The melody/period trap** | named in §4.3 as a convention/unit-robustness failure mode | Cited alongside the θ₀ trap as the reason step 3 exists. |
| **The E₆-denominator** | named in COMMS_PROTOCOL §4 | One of the four cases (with E16, θ₀=2/9, 7983360) that the mandatory base-rate + convention gate would have caught. *"Automate it, don't rely on vigilance."* |

### §6 The first honest doors (firewalled — each needs a sealed owner-authorized design)
- **Rung-1 door:** does any SM sub-structure live on an AUDIBLE direction (a real-quadratic field the object forces)?
- **Rung-2 door:** does the SM's irreducible FREEDOM organize as a Galois torsor / a B704-seam 𝔽₂ structure with no canonical origin — *"is the SM's arbitrariness the object's non-canonicity?"* — **the deepest falsifiable door.**
- **Rung-3 door:** does any SM relation match a sum-rule / selection-rule the object forces?

*"These are DIRECTIONS for future sealed designs, not results. No SM comparison runs without a sealed owner-authorized design (Gate 5-SM)."*

### §7–§8.3 Firewall + standing status
Methodology only; produces no physics claim. **Adopted as a STANDING GATE**, companion to the mandatory base-rate/convention gate (COMMS_PROTOCOL §4) and the firewall. *"Every object↔reality comparison, any seat, runs the §4 checklist and names its §1 rung first."*

---

# (f) NOVELTY AUDIT — how novelty claims are audited

Source: `git show origin/main:docs/NOVELTY_AUDIT.md` (2026-06-09, B134/V123; R4 appended 2026-06-11; R5–R7 through 2026-07-01).

**Method:** "fan-out web search → fetch → 3-vote verification → cited synthesis." **Purpose:** stop re-deriving known mathematics; locate where the real novelty is; cite prior art.

**Verdict enum:** `KNOWN` / `PARTIALLY-KNOWN` / `APPEARS-NOVEL` / `NEEDS-SPECIALIST`.

**Binding rules about literature-negative claims — this is the part cc3 must not violate:**

1. **Adversarial stance is mandatory:** *"assume known, try hard to find prior art before concluding novel."*
2. **Status:** *"This is a reference note (motivation/provenance), not a claim. Nothing here promotes to `CLAIMS.md`."*
3. **The absence-of-evidence rule (R5 method caveat, binding):** *"the NOVEL/PARTIAL verdicts rest on **absence of a found prior-art match, not a proof of originality** — strictly weaker than the (high-confidence) positive *background* findings, hence **medium** confidence; a specialist could know unpublished or differently-indexed prior art."*
4. **AI reads de-risk but do not close:** R4 — *"it is an AI adversarial literature read … and it **de-risks but does not close**: it finds the *findable* prior art and frames the residue with confidence levels, but a clean APPEARS-NOVEL here is still one same-kind-of-mind verdict — the final close needs a specialist."*
5. **NEEDS-SPECIALIST means zero verified prior art = absence of coverage, not confirmed novelty** (R6 CLAIM 4, explicit).
6. **Method note (this audit):** *"'appears novel' requires an adversarial prior-art search, not absence-of-memory — here it downgraded two of three."* Restated at R6: *"this pass DOWNGRADED the core claim — adversarial search beats absence-of-memory, again."*
7. **Method note (MB6, REPRODUCIBILITY.md):** *"reproduction ≠ interpretation."*
8. **Citation obligation:** the audit ends each pass with an explicit "cite X / do not re-derive them / reserve novelty for Y" instruction. Misattributions found in-audit are banked as corrections (e.g. the Tillmann `math/0508295` mis-specification; the "Qiu via Johnson–Clifford hep-th/0311129" misattribution — *"that arXiv id is a Type-0A string paper; cite FQS/Qiu directly"*).

**Net current standing:** only two genuinely-new candidates survive, both narrow, both pending a specialist close — the block-length palindrome criterion (R1, a GHH-2008 corollary, proved) and the SL(4)/`n≥4` `L=−Mⁿ` figure-eight A-polynomial (R4, established only at n=3,4). *"The project's recurring strength is methodological (verify-don't-trust, firewall, first-class negatives)."*

---

# (g) THE INPUT-COMPLETENESS LEDGER — what it tracks and what's open

Source: `git show origin/main:docs/INPUT_COMPLETENESS_LEDGER.md`. **Mandatory checklist for any SM-facing cell**, filled **in the prereg, before sealing**. *"An unfilled row is a design defect, not a formality."* Referenced as a hard precondition by WORKING_RULES §6.

| # | Item | The question the cell must answer in writing |
|---|---|---|
| 1 | **Scheme** | Which renormalization scheme / mass definition per target (pole, MS-bar, on-shell, effective)? Mixed-scheme ratios are ill-defined (m_t/m_b spans 36–61 across conventions). |
| 2 | **Scale** | At which μ is each running quantity quoted, and why? **The object supplies no scale (I6: ABSENT)** — any single-μ comparison is a human convention; use RG-invariant combinations or scan μ and price the look-elsewhere. |
| 3 | **Uncertainties** | Full 1σ (asymmetric if given), propagated into both the match windows AND the null (2σ inflation both sides, or a likelihood treatment). Point-value windows tighter than the measurement's resolution overstate significance by construction. |
| 4 | **Multi-modal fits** | Octant / mass-ordering / local-minima structure (θ₂₃ flipped octant between NuFIT 6.0 and 6.1 — a central value can move 15 % between releases; run each mode as a sensitivity variant). |
| 5 | **Convention constants** | Any target that is a convention not a measurement (M_GUT, unification scales, "effective" parameters) is flagged in-output and **never drives a verdict**. |
| 6 | **Fit-vs-direct** | Where global-fit and direct measurement differ (\|Vcb\|, \|Vub\|), state which is used and why; note the other. |
| 7 | **Look-elsewhere** | Correction covers ALL grids, tiers, variants, and modes actually examined — including sensitivity variants (Šidák/Bonferroni over the full family, not the headline alone). |
| 8 | **The matched null** | The null draws targets from **the same measure the match criterion uses** — never a narrower one. |
| 9 | **MB13 grep** | Keyword-grep + atlas check that the comparison (or its kill) isn't already banked. |
| 10 | **The firewall question** | Is this cell asking the object for VALUES? The banked theorems (K020 Galois firewall; role-separation law) say values live in the stage. If yes: state which stage-selection assumption is being tested, or reframe. |
| 11 | **Source freshness** | Targets fetched from the **current primary source** (NuFIT/PDG release + date recorded), **not recalled from memory**; the fetch archived in the packet. |
| 12 | **Sealing** | Inputs pasted verbatim BEFORE the seal; design + runner hashed; outputs banked before comparison prose. |

**Open items / the only recorded application.** The ledger's sole worked audit is retrospective, on B615:
- **PASS:** 7, 8 (after two disclosed in-run fixes), 9, 12.
- **FAIL:** 1 (schemes unstated; G3 mixed), 2 (single implicit μ = M_Z / mixed), 3 (point values), 4 (single octant), 11 (values recalled from assistant knowledge, accurate but unarchived).
- **PARTIAL:** 5 (M_GUT carried unflagged in-grid), 6 (CKM source unstated).
- **Outcome:** *"The verdicts survive the audit — B615-R re-ran the failed items and the conclusion strengthened (dissolution). The ledger exists so the next cell passes all twelve at design time."*

**Live relevance to cc3 right now:** items **8** (matched null) and **11** (source freshness) are precisely the two that failed again this session as **E29** (uniform null substituted for the pre-registered density-matched null) and in the 51.014 provenance incident (`CC_TO_CC3_2026-07-28_URGENT_provenance_failure_51014.md` → resolved in `…_B792_gate_51014_resolved_and_a_classification_error.md`). Item **2** ("the object supplies no scale") is the exact ledger row that E32's B796 premise has to argue past.

---

## File index (all absolute, `origin/main` unless noted)

- `origin/main:docs/ERROR_LEDGER.md` — 33 classes, E1–E32 (+E4a) — local copy at `/Users/dri/oa-audit-seat/origin-axiom/docs/ERROR_LEDGER.md` is **stale (E1–E26)**
- `origin/main:docs/RETRACTIONS.md` — 13 rows
- `origin/main:docs/NOVELTY_AUDIT.md` — R1–R7
- `origin/main:docs/COMMS_PROTOCOL.md` — v1.1, six sections + §4a/§4b (three-seat era; predates cc3)
- `origin/main:WORKING_RULES.md` — 14 binding items; local copy at `/Users/dri/oa-audit-seat/origin-axiom/WORKING_RULES.md` is **stale (Rule 10 truncated)**
- `origin/main:docs/INPUT_COMPLETENESS_LEDGER.md` — 12 rows
- `origin/main:docs/LISTENING_PROTOCOL.md` — §0–§8.3
- `origin/main:docs/SEAL_LEDGER.md` line ~212 — **the collision/reservation protocol's append-only section** (22 RESERVED rows)
- `origin/main:docs/progress/REVIEWS.md` lines 1801–1880 — Review 27, where the reservation protocol was adopted
- `origin/main:GOVERNANCE.md` §12–§16 — the constitution behind all of the above
- Relay corpus (working tree, untracked): `/Users/dri/oa-audit-seat/origin-axiom/CC_TO_CC3_*.md` and `/Users/dri/oa-audit-seat/origin-axiom/CC3_TO_CC_*.md` — 20+ files, 2026-07-22 → 2026-07-29; these carry the cc3-binding cadence, numbering, and gate rules that COMMS_PROTOCOL v1.1 has not yet absorbed.

**One structural gap worth flagging to the caller:** `docs/COMMS_PROTOCOL.md` is still v1.1 and describes a room without cc3. The cc3-specific rules (monitor cadence, PR-only/cherry-pick, reservation-with-ACK, collision resolution by hash-cost) exist only in SEAL_LEDGER rows, Review 27 prose, and the untracked root relay files. That is itself a Rule-10 "bank completely" defect: a live protocol governing a live seat is not in the protocol document.