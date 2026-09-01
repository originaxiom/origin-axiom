# S4b — CHANGELOG.md DIGEST (internalization sweep)

**Sweep date:** 2026-09-01. **Reader role:** digest-and-flag only; no claim is adjudicated dead or
proved here — that is the evaluating seat's job.

## Coverage modulus (exact)

- **File:** `CHANGELOG.md`, 12,956 lines, ~1.2 MB, 774 `##` entries spanning 2026-06-03 → 2026-09-01.
- **Read END-TO-END this session, every line, in 37 contiguous chunks** (lines 1–12,956, no gaps),
  newest-first in priority: the full heading map (all 774 headings) was extracted first and used as
  a completeness check; chunk offsets were tracked so no range was skipped.
- **Provenance note:** a prior draft of this digest was found already on disk (evidently from an
  interrupted earlier run of the same sweep). It was NOT trusted: every claim in it was re-checked
  against this session's own full read; the coverage section was rewritten to this run's actual
  bookkeeping; one red flag was softened (Γ₄₁ level — the record does hold a "different
  filtrations" disposition) and one new red flag was added (B152 → B1012, found only by reading the
  June tail).
- Depth was uniform-in-lines but not uniform-in-attention: the newest band (B1216–B1232, lines
  1–860) and the paper-facing band (2026-08-29 → 08-31) were read closely against the live board;
  the July trace-map/monoid era and the `[Unreleased]` tail (June 2026, B48–B352) were read fully
  but digested at arc-level granularity.
- **Live surfaces consulted:** `docs/CAMPAIGN_STATUS.md` top ~110 lines (through the B1225
  paragraph — enough to verify the stacked-LATEST contradiction claims verbatim) and
  `papers/P3_THE_PAPER/SPEC.md` (first ~60 lines + a grep for the "one bit" claim). **Not done
  here:** no cross-check against `PROGRESS_LOG.md`, arc directories, or test locks. Any claim below
  about "the paper" is about the paper *as the changelog and SPEC describe it*.

## Structural facts about the file itself (version-boundary mechanics)

1. **The file is append-only-with-exceptions and format-broken mid-file.** The Keep-a-Changelog
   preamble ("All notable changes… Format follows…") sits stranded at **line 7538**, below ~7,500
   lines of newer entries; a `## [Unreleased]` section at line 10,899 holds the *oldest* material
   (June–July 2026, B48–B352). Anyone diffing "released vs unreleased" gets the inverse of the truth.
2. **Ordering is only roughly chronological.** Within days, entries appear in bank order, not
   B-number order (e.g. B981/B980/B979 appear *after* the B982–B987 block; B975/B969 interleave).
3. **Correction conventions are inconsistent across eras.** Some entries carry in-place dated
   correction notes (e.g. the Gate C entry's "*Corrected 2026-08-30: this entry first said cell 2 is
   queued and unrun…*"); most later retractions are recorded only as **new entries above**, leaving
   the superseded entry reading as live when hit in isolation (see Red flags).
4. **Numbering constitution events** (invisible on live surfaces except via the alias table):
   cloud collision B1025–B1044 → permanent `CLOUD_ALIAS_TABLE.md`, main reserves B1045–B1059
   never-assigned and jumps to B1060 (2026-08-12); reserved bands ruling (audit seat mints
   B8000+/E800+, cloud keeps qL; 2026-08-18); B788/B790/B791 renumber (external Maass bank keeps
   B788); B347→B350; Ω-handoff "B206" ≡ repo B155, and the Ω program's own B206–B907 numbering is
   *disjoint* from the repo's; S042–S044 → S050–S052; L51–L61 → L62–L71; "L165+" → "L185+".
   B1001: the atlas regex was capped at 3 digits, so **B1000 was invisible** the day four-digit
   arcs began.
5. **Cadence/constitution changes:** decadal review 10 → 20 merges (2026-07-14); GOVERNANCE §12–§16
   (claims-as-units, review loop, factual-review lane) 2026-07-16/17; the certification envelope
   (Sec.CE) 2026-08-20; OA_SLOW slow lane created at B1177 and *first ever run* at B1207
   (2026-08-29) — i.e., ~50 gated test files were unexecuted from creation until three days before
   the sweep date.

## The top of the file: a three-stage self-demolition of the "consistency turn" (B1228 → B1232)

This is the single most important arc for the evaluating seat, because the live board stacks all
five stages and the changelog contains **no in-place banners** on the superseded stages:

- **B1228 (08-31):** S1 run; σ = 1 *retracted in-session* (geometric CS boundary WZW is A₁, not
  E₆); but banks "**k = 1 forced by inventory** — the object supplies J and provably no k" and
  "the wall is the mechanism that pins σ."
- **B1229 (08-31):** the consistency turn. Banks the "robust core" σ ∈ ℚ (via Anderson–Moore/Vafa
  + c = 6σ) and the "sharp" **σ ∈ {1/3, 1} — one bit** via MMS two-character classification + the
  object's ℤ/3.
- **B1230 (08-31):** C-5 **refutes B1229's stated support** (c = 6 has FOUR level-1 solutions —
  A₂@9, A₆, D₆, E₆; at level 1 c = rank); C-5b "recovers on a better footing": primary counts
  55/7/4/3, "the object's own ℤ/3 cuts four to one, restriction-free."
- **B1231 (09-01):** the identification discipline. Names **C-5b's ℤ/3 identification itself as one
  of the bench's two unearned identifications**; parameter counts become LOWER BOUNDS; citation
  debt discharged and it *deflated the headline*: **MMS seven-value list is ℓ = 0 only**, and
  **Anderson–Moore/Vafa was never read** — grade PHYSICS-ARGUMENT with an *unestablished*
  finiteness-of-primaries hypothesis. "σ's headline carries three conditionals, none stated when
  banked."
- **B1232 (09-01, top of file):** three retractions — (1) **σ ∈ ℚ establishes nothing (ℚ dense in
  ℝ): B1229's core was not weakly grounded, it was EMPTY**; (2) **B1228's "no receiver for k ⇒
  k = 1" is a default from absence — retracted** (adopted law: absence of a typed receiver means
  quotient-invariance or underdetermination, never a default); (3) C-2 resolves to Outcome A
  (B₀ is a ℚ-module, K-rank 4; the "dim 4 = φ(12)" tell was exactly the B1231 error class); plus
  Correction 4: part of I-7 **conflated a ℤ/2 with a ℤ/3** (Gal(ℚ(ζ₃)/ℚ) has order 2; C-5b listed
  the trace field as a ℤ/3 source). The positive: representational choices that vanish from
  observables — three columns, not two; ℙ³ closes by quotient invariance without the naming wall
  falling. **Fenced:** the (3,4,1)/lepton-block computations are codex's, *still running*; only the
  algebra and two retrieval certs were verified on this bench.

**Net state per the record itself:** σ is "not deleted, nothing exhibited, σ = 1 still retracted";
the k = 1 forcing is retracted; the ℤ/3 menu cut is under indictment (the changelog never states
explicitly whether C-5b's four→one cut survives Correction 4 — it retracts the *trace-field ℤ/3
source*, and B1231 flags the *boundary-module identification*; the surviving basis for the cut, if
any, is not restated). **This is an open question the digest hands to the evaluating seat.**

## Decisions / events NOT visible (or under-visible) on live surfaces

- **Owner directives recorded only in prose:** all specialist sends HOLD, per-item owner approval
  (B1179/B1181); "the paper will be crafted owner+cc after the math is exhausted"; privacy rule —
  owner's name/email never in tracked files (author block deliberately placeholder at submission
  prep, submission campaign S3); cc3's branch carries the owner's personal email on
  `SUBMISSION_METADATA.md` — surfaced to owner, deliberately untouched (B1152).
- **The D2/LEAP-1 authority question is still the owner's**: cloud downgraded the payment to
  PROVISIONAL because the owner's "go" may have been a general continue; "owed to the owner: one
  binary decision" (B1212). No later changelog entry records that decision.
- **The θ-even crossing (the last licensed value crossing) is RELEASED and UNSPENT** (B1217): the
  hold was owner-authorized, released, and deliberately not fired — the licensed row remains
  unspent. Easy to lose; it is a live one-shot resource.
- **Paper genealogy:** P1–P3 (old generation) frozen as internal notes after three non-converging
  scrutiny rounds (2026-07-08/10); **P5 monoid paper WITHDRAWN** — its spine is
  Baake–Grimm–Joseph 1993 (Kolář–Ali 1990 / Peyrière 1991), found only after the outline's own
  lit-gate had "named the right person and asked the wrong question"; P4 is the one
  arXiv-candidate, owner-gated; PC13 deflated; PC12 downgraded to computational report. The
  current "P3 — THE PAPER" (owner+cc, spec 2026-08-29, main.tex 2026-08-30/31) is a *different
  object* from the frozen P3; the PDFs in `papers/tex/` and `papers/flagship/` are the superseded
  June/July generation.
- **The submission campaign found the paper's bibliography was decorative** (12 of 13 bibitems
  never cited; fixed to 14/14, gated) — a fact about the paper's history a referee-facing surface
  will not show.
- **Instrument-era systemic findings** that shape how much to trust any single banked line:
  E53 (finished-but-forgotten; ~10 instances incl. inside the ledger recording it), B1004 (a
  retracted clause live in five places; three gates told to look away), B1207 (the slow lane's
  first-ever run: 9 failures incl. a verifier that had never executed since banking, and a PSLQ
  grid silently tripled by append-mode), B1216 (second MB12-vacuity in a fortnight, *both in
  supporting clauses* — "the headlines are getting checked; the sentences propping them up are
  not"), B1231's own instrument "would NOT have caught the error it was built for."

## Contradictions / tensions with the current live board (B1216–B1232 era)

1. **Stacked LATEST entries preserve superseded headlines without inline strikes** (verified
   verbatim on the board this sweep). The board's B1229 paragraph still displays "σ ∈ {1/3, 1} —
   ONE BIT. ℝ⁺ → 7 → 2" and B1228's "the level is **forced by inventory**… the **mechanism that
   pins σ**"; both are retracted two paragraphs above (B1231/B1232). Same for B1230's "C-5b
   recovery… the object's own ℤ/3 cuts four to one — stronger than what B1229 claimed," which
   B1231/B1232 indict (unearned identification; ℤ/2-as-ℤ/3 conflation). The board is newest-first
   so a full read is safe, but any citation of the B1228/B1229/B1230 paragraphs in isolation
   propagates retracted content. This mirrors the repo's own E53/RETRACTED_PHRASES failure mode,
   now on its most prominent surface.
2. **B1216's "C4 delivered as predicted" (σ one-bridge-missing with a runnable gate at χ_∂, c = 6)**
   is quietly hollowed by B1231's citation-debt finding (the c = 6 gate leaned on MMS-at-ℓ=0 and
   an unread Anderson–Moore/Vafa). The board does not annotate the B1216 paragraph.
3. **Congruence level of Γ₄₁ / m004 — dispositioned but never closed by name:** B734 banked "m004
   IS congruence at level (2)³ = (8), correcting B731" (with a "Serre-defying… pending external
   literature cross-check" caveat never seen discharged); B794 later banked "Γ₄₁ is congruence of
   level **exactly (4)**" (Γ(4) ⊆ Γ₄₁, Γ(2) ⊄ Γ₄₁). The record *does* hold a disposition: the
   owner-directed context re-read (2026-07-30 era) records the three answers as "different
   filtrations" per E23 and flags a "DISCREPANCY REQUIRING RESOLUTION"; Chat-1's review then
   resolved the *index* arithmetic (Z ∩ H = {±I}; PSL-index 6 and SL/{±I}-index 12 both correct in
   their own groups; E23 strengthened to a three-group rule). What the changelog never carries is a
   single by-name statement that "(8) in the PSL filtration" and "(4) in the SL-kernel filtration"
   are both final and compatible — the two PROVED-grade level claims still read as contradicting
   each other when hit in isolation.
4. **B1012's "blind-to-k ⟺ CS = 0 ⟺ amphichiral"** was refuted at its second link by B1226
   (m003/m135/m207: amphichiral, CS = ¼; m208: chiral, CS = 0; corrected law: blind-to-k ⟺ complex
   volume real). Six surfaces were corrected, but the B1012 changelog entry itself (and every
   intermediate entry that quotes "relocated beyond the object's reach in principle" — e.g. B1228's
   own text) carries no banner. See also red flag 6 below: the refuting counterexample was already
   banked in June.

## Staleness / divergence vs the P3 paper (as of its last recorded touch, 2026-08-31)

The paper's last changelog-recorded state is the submission campaign (17 pages, S0–S6,
2026-08-31) — i.e., it **predates B1231 and B1232 entirely**. Specific exposure:

- **"Prices the observer at exactly one bit"** (SPEC §0 one-sentence claim; verified in the SPEC
  this sweep). The record around it: B1164 census = 2 discrete + 1 continuous bits (V₄, not one
  bit); B1015/B1188/B1191 end-state = one unit ℓ + bits + finite labels; and B1231 now makes every
  parameter count a **lower bound** until identifications are earned. Whether the paper's "one bit"
  is the defensible c-bit-only reading or an overclaim is for the evaluating seat; the spec
  sentence as written is in tension with the record's own later typing.
- **The ℙ³ row.** Paper (per B1220/B1230-era corrections): "closed permanently, one named datum
  outstanding, blocked on codex R030." B1232 now claims the row dissolves *differently* — the
  three coordinates are representational, spread-0 under an annihilating coupling, "count the
  image, not the source" — which, if it survives verification (codex computations still running),
  makes the paper's ℙ³ row stale in the *favorable* direction but factually wrong in mechanism.
- **σ / the freedom ledger.** If the paper's σ row absorbed anything from the
  B1228–B1230 band (level-1 forcing, the one-bit menu, the ℤ/3 cut), it now carries three
  unstated conditionals per B1231 and two outright retractions per B1232. The changelog does not
  record a post-B1232 paper pass.
- Historical paper corrections that DID land and should be checked as still present: the
  A₂+A₁-Levi deflation (B951/B1210 — "the landing" moved to the recognition table; the SPEC carries
  the ⚠-corrected block, verified this sweep), arena/content split (252/222/2, zero object tokens —
  B1170), B862+B1080 dual citation for ℤ₆, λ external-by-theorem (B721/GC-22), Gieseking covering
  direction (got backwards twice in one day; "now assume we get wrong by default").

## Red flags (each: locus + why suspicious)

1. **CHANGELOG lines 1–186 (B1232 vs B1229/B1228):** retracted headlines ("σ one bit";
   "k = 1 forced") stand un-bannered in their original entries and on the live board's
   corresponding paragraphs — the repo's own named failure mode (E53 / retraction-not-propagated,
   B1004) recurring at the record's very top, in its highest-visibility band.
2. **Anderson–Moore/Vafa (B1229 entry):** a load-bearing literature step that was
   **cited, never read** ("neither paper could be read" — B1231), underpinning the entire σ∈ℚ
   move. Asserted-not-computed in the strict sense; now fenced, but every intermediate surface
   that repeated "σ is rational" between 08-31 and 09-01 inherited an unread citation.
3. **C-5b's surviving content is undefined:** B1232 retracts the ℤ/3's *trace-field source* and
   B1231 flags its *boundary-module identification*, but no entry states whether the 4→1 cut of the
   c = 6 menu retains any earned basis. The changelog leaves the σ candidate set in an undeclared
   state (four solutions? one? menu withdrawn?).
4. **B1232's positive lemma rests on computations "still running" on another bench** (codex
   (3,4,1) sequence, lepton connecting block) — the board and changelog both fence this, but the
   "first closure mechanism that does not require the naming wall to fall" headline is currently
   supported on this bench by algebra + two retrieval certs only.
5. **Γ₄₁ congruence level (8) vs (4)** — two PROVED-grade banked entries that contradict each other
   on their face; dispositioned as "different filtrations" (E23 + the context re-read + Chat-1's
   index reconciliation) but never closed by a by-name statement reconciling both *level* values;
   B734's own "pending external literature cross-check" caveat was never seen discharged (see
   Contradictions item 3).
6. **NEW (from the June tail): B1012's equivalence was refutable from the corpus's own banked data
   2.5 months before it fell.** **B152 (2026-06-11)** ran a 240-manifold census and banked "exactly
   one converse counterexample (**m208, chiral with CS = 0**) — CS-2-torsion is **necessary but not
   sufficient**." **B1012 (2026-08-10)** then banked "blind-to-k ⟺ CS = 0 ⟺ amphichirality" as an
   equivalence, and it stood — quoted upward into H11's "relocated beyond the object's reach in
   principle" and into B1228 — until **B1226 (2026-08-31)** re-exhibited m208 (plus m003/m135/m207
   at CS = ¼) via B1224's undrawn consequence. B1226 credits B1224, not B152: the record itself has
   not named this as an E53/lost-edge instance, though it is one — the killing datum sat banked in
   the June tail the whole time.
7. **B1217 evidence-contract gap:** cloud's V-NEG *headline* run is "not reproducible as
   committed" (typed CITED, artifact missing). If any live surface treats the extended V-NEG as
   verified, it overstates.
8. **The B653 JUNO "OUTCOME A" (sin²θ₁₂ = 1/(2φ))** was later reclassified
   VALID-AS-LETTER / **VOID-AS-HELD-OUT-CONFIRMATION** and B1066 then *exhausted* the licensed
   contact surface with a 4.7σ exclusion of sin²θ₁₂ and 3.4σ on |U_e1| = φ/2. Any narrative reuse
   of the B653 "hit" without the void reclassification is a live hazard (the changelog handles it
   correctly; downstream summaries may not).
9. **The record's own meta-warning generalizes:** B1216 — MB12-vacuities are migrating into
   *supporting clauses*; B1231 — the detection instrument for the dominant error mode misses the
   bare "X IS Y" phrasing by design. The evaluating seat should treat one-line verdict summaries
   (the exact genre of this file) as the least-audited layer, per B1220's own finding that "the
   one-liner is what downstream surfaces quote" and can contradict its own cell (B1196/GC-27
   instance).
10. **Format break + [Unreleased] inversion** (lines 7538, 10899): mechanical, but it means any
    tooling or reader that parses the file by Keep-a-Changelog conventions silently mis-orders two
    months of history.
11. **Unspent one-shots and undischarged owner decisions live only in prose:** the θ-even crossing
    (released, unfired), the D2 signature confirmation, the L192 bit-level box-D license
    (registered, not banked). None of these are contradictions, but they are decisions/dispositions
    a live board reader would not reconstruct.

## Era map (for orientation, one line each)

- **Jun 2026 ([Unreleased] tail, B48–B352):** metallic trace maps, SL(n) tower, A-polynomials;
  founding refutations kept visible (cotangent formulas, B192 parity law, PC13); B152's CS census.
- **Jul 1–14:** commensurability/class-level deflation (B727/B803 lineage), P5 withdrawal, the
  E₆ 27 built (B883/B904), measurement theorems (B874–B897), the cascade (B859–B873).
- **Jul 15–19:** θ-odd sector, chiral play, hearing law, fiber-functor torsors (B700s), Kim/
  arithmetic-CS meet (B707/B708).
- **Jul 20–Aug 9:** observer spine (B713–B733), instrument/audit era (B799–B860 governance
  band), value-wall consolidation.
- **Aug 10–22:** the claim ledger (B1014), anchors, crossings all-miss (B1027/B1063/B1066/B1075),
  closing campaign (B1083–B1140), value campaign exhaustively closed (B1126–B1137).
- **Aug 25–28:** cloud memo harvests (structure forced / values withheld across the visible
  sector), W₀/amphichirality/parity law (B1163–B1168), grand computation (B1188–B1196).
- **Aug 29–31:** THE PAPER (spec → 17pp), publication+submission campaigns, family = 112,
  identification-era corrections (B1201–B1226), β-odd box, consistency turn.
- **Sep 1:** identification discipline + the three retractions (B1231/B1232).
