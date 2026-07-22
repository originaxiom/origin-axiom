# S16 REVIEW 1 — B754 p2 spectral (pre-execution design review)

Reviewer: fresh, non-authoring §16 seat (oa-audit-seat)
NONCE: B754R1-LIVE-6e9d2a17
Date: Wed Jul 22 08:16:29 CEST 2026
Branch under review: hunt/p2-spectral
Sealed design: frontier/B754_p2_spectral/PREREGISTRATION.md + TARGETS.json per ARTIFACT_HASHES.txt v1

Protocol: incremental disk — each check's finding appended immediately after it is run.
Final line will be exactly "VERDICT: SEAL-READY" or "VERDICT: STOP — <failing premises>".

---

## CHECK 1 — Seal integrity: PASS
- Recomputed sha-256, working tree AND `git show HEAD:` blobs:
  - PREREGISTRATION.md = f326adbb5a7b471c32cb7365bdeb85687bd98b5955254ab8b31d533011ddb262 — matches ARTIFACT_HASHES.txt v1 line.
  - TARGETS.json = fbca26c178dd1ee4d96ecc3e2e2675edeab6ce0379344a17735b25108fe40d8d — matches ARTIFACT_HASHES.txt v1 line.
- `git diff HEAD` on both sealed files: empty (byte-identical to branch HEAD 4e401310).
- Base commit: seal records "base 870d8cc3; reservation #1250". merge-base(HEAD, main) = 870d8cc3 (B753 commit, parent of the seal commit). Matches.

## CHECK 2 — Authorization: PASS (with one hygiene note)
- Reservation: NOT visible on stale local `main` (870d8cc3); after `git fetch`, origin/main (0147a753) contains commit efaa0181 "B754 reserved (cc3 P2 spectral stratum) (#1250)". docs/SEAL_LEDGER.md line 283 on origin/main:
  "RESERVED: B754 (cc3 — the P2 stratum: spectral-face re-adjudication of 19 sealed targets from bprime_annotations.json; branch hunt/p2-spectral; PR-only, cc = merge gate)" — names THIS stratum (P2 spectral-face, 19 sealed targets) and THIS seat (cc3), and the exact branch under review.
- cc ack relay (<cc2-seat>/seat-work/relay/CC_TO_CC3_2026-07-22_p2_ack.md): confirms B754 RESERVED (#1250, on main, mirrored); ACKs branch `hunt/p2-spectral`; freezes the consumable spectral surface to EXACTLY B737 + B739 + B746 + B753, with a stability promise (nothing else spectral lands during the stratum unless owner opens the discrete-spectrum door, relay-before-bank).
- Prereg frozen-surface list = B737 (zeta-quotient voice, residue, CM/palette) · B739 (character-rigidity) · B746 (two-column law) · B753 (unitary θ-odd block, eigenphases ±72°, kind-correct mixing matrix, one-number pin). Set AND per-arc characterizations match the ack EXACTLY. No fifth source anywhere in the prereg.
- Hygiene note (non-blocking): seal base 870d8cc3 predates the reservation commit efaa0181 on main; reservation was made via relay + ledger mirror per the collision protocol, so sequencing is proper. merge-base(HEAD, origin/main) = 870d8cc3 as sealed.

## CHECK 3 — TARGETS integrity: PASS
- TARGETS.json = list of exactly 19 entries; keys per entry: {id, record, exposure_note}.
- Selection RECOMPUTED independently from frontier/B742_negatives_hunt_p1/stageA/bprime_annotations.json (30 annotations): filter anatomy_exposure==true AND anatomy_note matching /spectral|spectrum|emittance|B735/i → 19 ids. Set difference vs TARGETS both directions: EMPTY. (Narrower pattern without "spectrum" gives the identical set — selection is robust to pattern choice.) 29/30 annotations have anatomy_exposure=true; the 10 exposed-but-unselected ids (B146, B437, B489, B685, TOMB-L255/L293/L310/L34/L74/L9) have no spectral mention — correctly excluded.
- Selected set: B107, B285, B516, TOMB-L241, TOMB-L247, TOMB-L252, TOMB-L258, TOMB-L267, TOMB-L277, TOMB-L30, TOMB-L334, TOMB-L339, TOMB-L57, TOMB-L63, TOMB-L67, TOMB-L70, TOMB-L77, WALL-1, WALL-7. WALL-1 and WALL-7 PRESENT.
- Every entry carries its full kill record (claim_killed, kill_form, is_negative=true, faces_consulted, fact_basis, evidence_quote, citation_chain, source path) with record.id == entry id, plus a non-empty exposure_note that is byte-identical to the banked anatomy_note (19/19).

## CHECK 4 — Design adequacy (MB12 on the three-outcome enum): PASS (one convention note for executors)
- MB12 (WORKING_RULES §8: every sealed criterion must be able to pass AND to fail) applied to each outcome:
  - KILL-EXTENDS: reachable (e.g. B107's single-scale kill vs B746 F3/F5 banked golden-power spectra and B753's exact unitary block — computable in-cell extensions exist); failable (no computation, or the computed fact does not uphold).
  - FACE-OPENS: gap-demonstration is EXECUTABLE against the frozen corpus because the corpus is finite, enumerable, and scope-explicit — all four FINDINGS exist and are readable in the tree (B737_candidate_zero, B739_character_rigidity, B746_golden_ledger, B753_mixing_structure, each with FINDINGS.md + PREREGISTRATION.md + outputs). A concrete gap demonstration looks like: state the {operator, input, discriminator, what-an-answer-would-change} 4-tuple, then walk the four arcs' explicit scope boundaries (B739 is expressly "weight-0 scalar scope" and redirects the level's new arithmetic to the DISCRETE newform spectrum; B746's own verdict is GAPPED 10/12 with the gap = the voice; B737 queues open leads L1/L2; B753 computes exactly one 2x2 θ-odd block) showing none computes the needed object. The cc ack independently confirms the discrete-spectrum door is OWNER-GATED and outside the frozen surface — so demonstrable gaps exist; the outcome is non-vacuous. Failable: skeptic shows the surface does answer, or the question is ill-posed/not computable.
  - FACE-IRRELEVANT: earnable-with-argument, failable (skeptic defeats the irrelevance argument). By CONSTRUCTION every FACE-IRRELEVANT contradicts a banked annotation (all 19 targets carry anatomy_exposure=true), and the mandatory-skeptic trigger is stated twice and consistently: prereg line 27 ("contradicts a banked annotation → skeptic mandatory") and the Skeptic rule ("Every FACE-OPENS and every FACE-IRRELEVANT gets one adversarial skeptic"). No gap between trigger and rule.
- Exclusivity/exhaustiveness: with the natural precedence (computed uphold → KILL-EXTENDS; provable no-touch → FACE-IRRELEVANT; otherwise → FACE-OPENS queue entry), the three outcomes partition the per-target question. Declared exceptions: depth/E22 items OUT OF SCOPE (deferred to P3), and revival ADJUDICATION excluded from this arc ("NOT a revival" — a revival-shaped in-cell computation routes to the next arc's queue as a demonstrated-live FACE-OPENS question, matching the B742→B745 precedent where revivals get their own cross-verify arc; nothing banks from this arc, cc is the gate).
- CONVENTION NOTE (non-blocking, for executors + harness): a target that both earns a computed extension AND surfaces a residual gap should record KILL-EXTENDS as the verdict and still queue the gap question; the prereg implies but does not state this precedence. Record it in the journal at first occurrence.

## CHECK 5 — Gate 5-Q compliance of the DESIGN: PASS
- philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md read from origin/main (status ADOPTED 2026-07-22, owner-approved, #1248 = ffeabbde in branch history). Each rule the prereg invokes exists and is correctly characterized:
  - Q1 (computed referent): prereg binds all face vocabulary to the four frozen arcs — matches the firewall's own bindings (voice = continuous-spectrum channel B737/B739; gait-vs-name = two-column law B746). Correct.
  - Q2 (non-universality control): prereg states any consultation operator "must FIRST show it discriminates the object from a generic input" with stop-there on failure and names the B752 lesson — this is the firewall's Q2 verbatim in substance, and it IS stated as MANDATORY-FIRST for consultation operators (the specific thing this check demanded). cc's ack independently concurs on exactly this point.
  - Q3 (input identification): "inputs identified against banked exact sources" — correct compression of the firewall's cite-and-verify-invariants rule.
  - Q5 (no consciousness claims): prereg is STRICTER than the firewall ("no experience vocabulary anywhere" vs Q1-bound labels allowed) — compliant.
  - Q6 (specialness budget): prereg attaches the E20 look-elsewhere budget to any "face specially touches THIS claim" with the sister/comparator question named in-cell — correctly folds in Q6 plus the Q2b comparator-object control.
  - Q7 (falsification edge): "each cell's prereg'd headline states what would kill it" — matches.
- Not invoked and not needed at design level: Q4 (no fixed-point/convergence claims in the prereg; applies per-cell if one arises), Q5b (no empirical constants anywhere in the design; Gate 5 proper declared absolute, WALL-1's cell explicitly forbidden to hunt values). Q8's standing machinery is present in fact: hash-first seal (Check 1), reservation #1250 (Check 2), banking-seat re-run on skeptic-surviving FACE-OPENS (E18), stopping rule respected (B753 pin language untouched).
- Per-target three-outcome enum sits within repo precedent for per-item grading enums (B742 kill/revival, B746 12-floor grading, B750 class enum); the arc-level gates (count-gate 19/19, journal-only verdicts, PR to cc) are the Q8-standard ones.

## CHECK 6 — The four frozen arcs on main: PASS (headline anchors for executors)
All four exist on origin/main under frontier/, each with a readable FINDINGS.md, byte-identical to the branch copies (git diff origin/main..HEAD empty on all four):
- B737_candidate_zero (58 lines): OUTCOME B at the crux — the voice carries ζ_K whole via φ(s)=Λ_K(s−1)/Λ_K(s) with the one-cusp exact-transfer lemma (φ_m004 = φ_orbifold identically, Res φ = 2√3/vol(m004)), plus object-specific data (conductor-4 CM cusp torus; Hecke palette 1/2/8) — but the ζ is the FIELD's voice; Candidate Zero killed; leads L1/L2 queued.
- B739_character_rigidity (51 lines): OUTCOME A 0/3 — the continuous spectrum is CHARACTER-RIGID: single channel, multiplicity 1, scattering exactly Λ_K(s−1)/Λ_K(s); NO conductor-(4)/(8) character appears in the continuous spectrum; the level's new arithmetic lives ONLY in the discrete newform spectrum. Weight-0 scalar scope.
- B746_golden_ledger (77 lines): GAPPED 10/12 — every structural floor FORCED-golden; the one gap is the voice (pure being-field/Eisenstein); the two-column law: golden is how the object MOVES, ℚ(√−3) is what it SAYS.
- B753_mixing_structure (50 lines): the 2x2 θ-odd weld block is exactly UNITARY with eigenphases ±72° (chat-1's 108° false; the Re λ = Re B₀₀ = 1/(2φ) distinction provably empty); the kind-correct mixing matrix is golden-exact with |B₀₀|² = 1/(φ√5); one-number pin co-signed; no SM comparison.

## CHECK 7 — Directory sweep: PASS
- find over frontier/B754_p2_spectral/: exactly ARTIFACT_HASHES.txt + PREREGISTRATION.md + TARGETS.json + reviews/S16_REVIEW_1.md (this file). Nothing else — no stray cells, drafts, caches, or dotfiles.
- git ls-tree at HEAD: only the three sealed files tracked. git status in the arc dir: only reviews/ untracked (this review, by design the reviewer's channel). No pre-staged execution work exists before the review verdict.

## CHECK 8 — Two independent anchors: RECORDED
Both values verified ABSENT from every file in the arc before this write (grep over frontier/B754_p2_spectral/ returned nothing for either prefix); they anchor this review to the live tree and are re-runnable by any auditor:
- ANCHOR 1 (the selection source this review recomputed from):
  `shasum -a 256 frontier/B742_negatives_hunt_p1/stageA/bprime_annotations.json`
  = ae250d22937bb6a7b7918e06c4411f44f409eaec9f77391ff721cc1156f96b47
- ANCHOR 2 (the authorization ledger as fetched today):
  `git rev-parse origin/main:docs/SEAL_LEDGER.md` (origin/main = 0147a753)
  = 18a34b382dd250702333cf72d62d1acb644de141

---

## SUMMARY
1. Seal integrity — PASS. 2. Authorization (#1250 + cc ack; frozen surface matches exactly) — PASS. 3. TARGETS (19/19, selection recomputed, sets identical, WALL-1/WALL-7 present, records + notes complete) — PASS. 4. MB12 design adequacy (all three outcomes reachable; FACE-OPENS gap-demonstration executable; FACE-IRRELEVANT skeptic trigger sound) — PASS with one non-blocking convention note (KILL-EXTENDS precedence over residual gaps: record in journal at first occurrence). 5. Gate 5-Q design compliance (Q1/Q2/Q3/Q5/Q6/Q7 all real and correctly characterized; Q2 mandatory-first confirmed) — PASS. 6. Four frozen arcs on main with readable FINDINGS, anchors noted — PASS. 7. Directory sweep clean — PASS. 8. Anchors recorded — DONE.

VERDICT: SEAL-READY
