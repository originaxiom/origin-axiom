# B920 — THE REGISTER SWEEP (cc3 loss audit A2 + A5, the mechanical pass)

**Date:** 2026-08-06 · **Seat:** cc computation agent (working-tree edits only; NOTHING committed)
· **Source of record:** `CC3_TO_CC_2026-08-05_LOSS_AUDIT_full_report.md` (branch
`origin/audit/b775-braver-questions`) §A2 + §A5; registered in
`docs/STRUCTURE_TO_NATURE_MASTERPLAN.md` AMENDMENT v6.

Every edit below is the smallest honest one; before/after quotes are abridged to the
load-bearing clause (the full text is in the named file). Verification state at the end of
the sweep: `python3 scripts/gates/gates.py` → **20/20 PASS** (including `chain-locks`,
`law-map-provenance`, `views-generated`); `tests/test_b794_congruence.py` → **5 passed**.

---

## Item 1 — NORMSPLIT: the standing self-contradiction ended

### 1a. The claim, verified in-sandbox (not trusted)

`trace_norm_split.{py,json,txt}` fetched from the cc3 branch
(`frontier/B792_maass_m004_eigenvalues/` there; that directory does not exist on main).
The script was **re-run locally** in a scratch cwd against the branch's two length spectra
(cutoff 6.0; worst ℤ[ω] deviation 2.4e-10 — every trace rounds cleanly, no filter), and the
norm-level split was **recomputed independently** from the trace sets. All of A2's figures
reproduce exactly:

- TRACE level (m004-exclusive traces): **139 traces / 37 distinct norms / exactly one odd
  norm = 7** (via traces 3+ω, 2−ω); classes {0,3} mod 4.
- NORM level (norms achieved by m004 but by no m003 trace):
  **{4, 16, 48, 64, 112, 144, 192, 208, 256, 304, 336, 400} — 12 distinct, zero odd, all
  ≡ 0 mod 4** (the hint's own statement, at the hint's own level).
- **103, 127, 175, 367 are SHARED** (each also achieved by an m003 trace; so is 7 — via
  m003's different traces 1+3ω, 2+3ω). m003-exclusive norms: 43 distinct, all ≡ 1 mod 4.

Verdict: **both seats were right about different objects; the hint survives at the norm
level**, with B794's theorem (N(tr γ) ≡ 0 or 3 mod 4 for all of Γ₄₁) as its mechanism.

### 1b. Artifacts copied

`trace_norm_split.py`, `.json`, `.txt` copied **byte-faithfully** (sha-256 verified equal
to the branch blobs) into `frontier/B794_congruence_level4/` as the reconciling artifact:

- `72b86d382e7368721917ba17800b097caee81d5a4c5907a260bbd9a4fc76c035  trace_norm_split.py`
- `2b8ade501865e5c60940c0a8917496d27c2f5f33f2f6cd02d7e4cf8419edec28  trace_norm_split.json`
- `8ba68b99c49772b11b36c64219902d7eab349e22b50ba95a1a24d18ade84e7e8  trace_norm_split.txt`

(Note: the copied script's `DIR` points at its birth directory `frontier/B792_.../`; it is
preserved byte-faithfully as evidence, not adapted. The rerun used a scratch copy.)

### 1c. `docs/HINT_LEDGER.md` row (7) (~line 579)

BEFORE (abridged): *"(7) H-B788-NORMSPLIT — **RETRACTED 2026-07-28.** The claim … is
REFUTED by B794's proved law … cc's own re-verification appeared to uphold the claim but
was an artifact of a tolerance filter that silently dropped long geodesics — the
disconfirming data. Superseded by a LAW_MAP theorem row."*

AFTER (abridged): *"(7) H-B788-NORMSPLIT — **RETRACTED 2026-07-28; RETRACTION AMENDED
2026-08-06 (B920): the hint SURVIVES AT THE NORM LEVEL — its own level.** … TRACE-level
m004-exclusives are 139 traces / 37 distinct norms / exactly ONE odd (7 …); the NORM-level
m004-exclusives are {4,16,48,64,112,144,192,208,256,304,336,400} — 12 distinct, ZERO odd
… the odd norms 103/127/175/367 are SHARED … Both seats were right about different
objects. B794's theorem … supplies the hint's mechanism … Reconciling artifact:
frontier/B794_congruence_level4/trace_norm_split.{py,json,txt}."*

### 1d. `frontier/B794_congruence_level4/FINDINGS.md` (~line 51)

The two paragraphs ("**REFUTED.** …" and "**And cc's contrary 'verification' was an
artifact.** …") are left in place (append-only record) and a **LEVEL RECONCILIATION**
blockquote is inserted directly after them, dated 2026-08-06 (B920), carrying the figures
of §1a, the survival-at-norm-level statement, the note that "41 with five odd" conflated
the levels, and the artifact pointer.

### 1e. `tests/test_b794_congruence.py`

BEFORE: `test_cc_mod4_hint_is_refuted_by_the_theorem` — asserted only
`x % 4 == 3 and x % 4 != 0` for (7, 103, 127, 175, 367), docstring calling the hint
refuted (treating all five as m004-only).

AFTER: `test_cc_mod4_hint_reconciled_by_level_split` — asserts the mathematics from the
copied `trace_norm_split.json`: 139/37/one-odd-7 at trace level; m003 exclusives ≡ 1
mod 4; the norm-level exclusive set equals the 12 (computed set-theoretically inside the
test, all ≡ 0 mod 4); 103/127/175/367 (and 7) shared at the norm level and outside the
exclusive set; the {0,3} class law. **5/5 tests pass.**

### 1f. `docs/ERROR_LEDGER.md` E28 instance figures (A2's "the E28 instance row still
carries the wrong figures")

BEFORE (abridged): *"…it returned 12 m004-only norms against cc3's 41 … The dropped
geodesics carried exactly the disconfirming odd norms (7,103,127,175,367). cc3's proved
mod-4 theorem settled it against cc.…"*

AFTER: the original text stands, followed by: *"**INSTANCE FIGURES CORRECTED 2026-08-06
(B920 …): cc's 12/zero-odd was in fact the CORRECT NORM-level exclusive set … cc3's
41-with-five-odd conflated trace and norm levels — the reconciled TRACE-level figures are
139/37/one odd (7); 103/127/175/367 are norm-level SHARED. The filter-hygiene class stands
as minted (the filter DID discard without reporting …), but the clause 'the dropped
geodesics carried exactly the disconfirming odd norms' was wrong, and the hint survives at
the norm level …**"*

---

## Item 2 — `docs/ROADMAP.md` Tier-3: the three falsehoods

BEFORE: *"## Tier 3 — the physics walls (all OPEN; the make-or-break)\nNo banked theorem
blocks any of these; no mechanism yet crosses any of them. W5 prices each with one
computable probe."*

AFTER: header re-titled *"the physics walls (the make-or-break)"* + a dated CORRECTED
block (2026-08-06, B920) stating: (1) **the scale no-go IS banked** — the dimensionful /
scale-torsor no-go, LAW_MAP §E wall 10 (B660/B666 cell S), a proved impossibility for
VALUES at WALL 1; (2) **WALL 5 HAS been run once** — B915's sealed crossing returned a
16σ MISS, the confrontation machinery exists and fired; (3) **WALL 4 carries a mechanism
chain at the wall** — the measurement cascade B861–B863 + the SMT (B892/B893,
su(3)⊕su(2)⊕u(1)³ exactly), structure at the wall, not yet a derivation-crossing. The
"W5 prices each with one computable probe" sentence retained.

(The audit's citation "§D.10" for the scale no-go is off by a section letter — the row is
LAW_MAP **§E wall 10**; corrected silently in the inserted text.)

---

## Item 3 — `docs/LAW_MAP.md`: the five orphan rows moved above the footer

The five rows sitting BELOW the maintenance footer (old lines 243–247) were moved into
sections, keeping each table contiguous; nothing deleted:

- **THE mod-4 TRACE LAW / Γ₄₁ CONGRUENCE THEOREM** → §A (the object's arithmetic).
  While moving, its witness clause was reconciled — BEFORE: *"…REFUTES B790's hint
  H-B788-NORMSPLIT"* → AFTER: *"…REFUTES the TRACE-level reading of B790's hint
  H-B788-NORMSPLIT (the hint itself SURVIVES at the NORM level — the 2026-08-06 B920
  level reconciliation; reconciling artifact
  frontier/B794_congruence_level4/trace_norm_split.*)"*.
- **THE METALLIC COMMUTATOR TRACE IDENTITY … (B471)** → §A. Text unchanged.
- **THE TOWER HEIGHT-COUNT CLOSED FORM (B120)** → §A.
- **THE DARK-HYPERBOLA LAWS (B534)** → §C (the chord: the seam observable is
  coupled-object data). Placement is a judgement call — §A was the runner-up.
- **THE √φ PERRON IDENTITY + GL(4,ℤ) RIGIDITY (B533)** → §C (the five coupling types).

In the three rows whose text said "**no row in any registry**" (B534, B533, B120) that
clause now reads "**no row in any other registry** (this row sat below the maintenance
footer until 2026-08-06, B920)". The `law-map-provenance` gate passes after the move.

---

## Item 4 — `docs/COMMS_PROTOCOL.md`: cc3 and the solo seat legalized

- Title: *"the three-seat room (v1.1 …)"* → *"the seat room (v1.2, 2026-08-06: cc3 + the
  solo seat added as named seats — B920 …)"*.
- Seat list now: *"Owner + cc (banking) + cc2 (compute) + chat1 (hypotheses) + cc3
  (audit / genesis; works on its own fetched branch, NEVER merges — cc is the sole merge
  gate) + the solo seat (independent bench: parallel rebuilds and numbered handoffs,
  verified by cc before banking), one room."*
- §1 addressing: `@cc3` and `@solo` added.
- §3 roles: appended *"Added v1.2 (B920): cc3 audits, formalizes, and relays corrections —
  its branch artifacts reach main only by cc's harvest (verify-don't-trust), never by
  merge; the solo seat computes independently and hands off — its results are cross-seat
  claims like any other, reproduced in-sandbox before banking."*

(No claim was made about cc2's closure — the audit asserts it but no banked referent was
found in-sandbox, so the protocol text does not say it.)

---

## Item 5 — the theorem registers: the B8xx/B9xx window rows added

- **`docs/THEOREM_REGISTRY.md`**: new final section *"The B877–B919 window — the
  measurement cascade and the value layer (same-PR catch-up, 2026-08-06, B920)"* — 20
  brief rows (T-FMT, T-SMT, T-MAGIC, T-INTERBREAK, T-CONCORD, T-SIGDICH, T-SIGNLAW,
  T-COCYCLE, T-CSTAB-NOGO, T-ANNIHIL, T-ONECLASS, T-GENSHAPE, T-Z2LAW, T-E62, T-RATATOM,
  T-SIGSPLIT, T-ONENUM, T-UNIMOD, T-38TRACE, and the negative T-CROSSING) mirroring
  LAW_MAP §F, each with its bank and resolvable test lock; lit-status **NEEDS-LIT
  throughout** (no novelty sweep has run on the window); Gate 5 note explicit.
- **`docs/THEOREM_LEDGER.md`** (THE CHAIN): new *"Part V — the measurement cascade and
  the value layer (the B877–B919 window; same-PR catch-up 2026-08-06, B920)"* — links
  **C24–C43**, each labeled ([THEOREM] ×17, [NO-GO] ×2 — the C-stabilizer and the sealed
  crossing, [IDENTITY] ×1 — the 3/8 traces at the one-prime tier), each citing its
  resolvable lock. The **`chain-locks` gate passes** (all 43 links locked). All lock
  files verified to exist before writing the rows.
- **B909's remaining debts** (six-cubic √77 law, the CMT, the invisible-12) are
  **deliberately excluded** from both registers — their locks are still owed (the bank is
  gated on the cpen rerun); a pending note marks them in both files.
- **`tests/test_b758_chain.py` updated in the same pass** (the chain's structural lock
  asserted links == C1–C23 exactly and went red when Part V landed): the range is now
  1–43 with a dated comment, plus a new assertion that Part V admits no AXIOM links.
  BEFORE: `assert [...] == list(range(1, 24))` → AFTER: `list(range(1, 44))` +
  `grades[23:].count("AXIOM") == 0`. All chain tests green (3/3), and the adjacent lock
  tests referencing the edited registers pass (test_b471_harvest, test_b830_masterplan,
  test_b831_retraction_targets, test_b818_retracted_rule, test_roadmap_register,
  test_e21_group_naming_guard, test_public_surface_scan, test_b651_wave3 — 39 tests
  total, all passing).

---

## Item 6 — `docs/RETRACTIONS.md`: the same-PR catch-up rows

A dated CATCH-UP marker row + six rows appended (the ≥5 audit events + today's find):

1. **H-B788-NORMSPLIT** — the 2026-07-28 retraction AND its 2026-08-06 amendment
   (two-stage row; survives at norm level; artifact + E28/E33 pointers).
2. **B471 / Cohn attribution** — the harvest row had omitted the Cohn 1955 attribution
   the arc itself recorded; corrected 2026-07-29 in the LAW_MAP row.
3. **The 5₂ polarity withdrawal** — B438/B440/B443 + CAMPAIGN_STATUS's "{4₁, 5₂} … a
   commensurability class" WITHDRAWN by B855 (2026-08-02): no knot complement is
   commensurable with 4₁ (Reid); the shared property is genericity evidence — the
   opposite polarity; the survivor is 4₁(5,1) ≅ −5₂(5,1) at slope 5 only.
4. **B790's conceded corrections** — all four of Chat-1's challenges conceded in the
   in-FINDINGS ADDENDUM (2026-07-28): non-preregistered null + miscoded Weyl null
   (e^ℓ for e^{2ℓ}); L3 → MISS-earned; tests 1–3 vacuous; scope reading corrected (E29).
5. **B225's relabel** — PROVED → RETRACTED (B831, R35-4; B745's confirmation): the
   "2 = octahedral parent REFUTED" criterion was vacuous; the 5-half survives.
6. **TODAY'S FIND (retraction-propagation failure)** — the solo seat's RETRACTED
   section-LIV septic instrument (`cmt.py`) shipped anyway in solo handoff 6; κ mod 40031
   has NO wall roots (centralizers there read the generic floor 12); caught 2026-08-06 in
   B909 by root-set comparison; corrected instrument `cmt_correct.py` confirms the ledger
   at more (root,prime) pairs; root-set comparison adopted as the wall-instrument sanity
   gate.

---

## Item 7 — `docs/ERROR_LEDGER.md`: the recurrence instances

- **E35 (NEW class row): Oblique-readout violation** — the B881 §3 standing rule
  ("every decomposition readout must be oblique — solve in the full eigenbasis, never a
  projection — unless the basis is provably orthonormal") had NO ledger class despite
  being "earned three times"; the row is minted at the FOURTH violation with all four
  instances: B875 (nearly-parallel sectors), B876 (ill-posed per-sector grading), B881
  (transpose-projections on the non-Hermitian K₁ restriction — the rule minted), **B907
  (2026-08-05, the fourth: Rayleigh quotients on non-normal matrices in the first
  pattern-feasibility census; caught by contradiction with exact automorphisms)**.
- **E36 (NEW class row): Artifact-clobber** — an exec'd foreign frame (the B854 frame is
  the recurring case) writes `results.json` relative to cwd/`__file__` and silently
  clobbers the host arc's artifacts. Instances: **B907** (the banked `results.json`
  contains the frame's verdict, not the selector sweep — clobbered pre-commit; nothing
  load-bearing lost, recorded in-arc) and **B910** (`kappa_class.py` defends against the
  same hazard by design). Standing rule: scratch-cwd + `__file__`-redirect + isolated
  namespace + pre-commit artifact-provenance check.
- **E27 instance appended: the B919 silent-substitution NEAR-MISS** (2026-08-05/06,
  self-caught pre-bank) — a generated two-prime script's silent substitution failure ran
  one prime twice while `two_prime` sat true in `results.json`; the flag was not wired to
  which primes actually ran (E27's exact class); exposed by direct inspection, retracted
  in place within minutes.
- (Plus the E28 instance-figure correction, reported under Item 1f.)

---

## Honest gaps / judgement calls / residuals

1. **B794's frozen run artifacts still carry pre-reconciliation figures**:
   `frontier/B794_congruence_level4/output.txt` (L41/L45) and a comment in
   `verify_congruence.py` (~L98) repeat "12 vs 41" and treat the five odd norms as
   m004-only. They are preserved byte-faithful run records (Working Rule 3 / E7); the
   FINDINGS reconciliation block is the superseding statement. Not edited.
2. **The origin of cc3's "41 with five odd" remains unreconstructed** — the cc3 branch's
   own context sweep (harvested at
   `frontier/B921_branch_harvest/harvested/.../sweep_banked_arcs_B793_B797.md` item 2)
   notes "41 appears nowhere on cc3's branch". The reconciliation does not depend on it;
   recorded as level-conflated, provenance unknown.
3. **LAW_MAP placements of B534 (§C) and B533 (§C)** are judgement calls (the seam
   observable and the coupling-type rigidity read as chord-level); B794/B471/B120 in §A
   are unambiguous.
4. **The masterplan's B920 registration names three more sub-items not in this task's
   mandate** — the CLOSURE_MASTERPLAN unfreeze, the 8 post-banking-commit sealed docs
   adjudication, and the promotion-gate throughput ruling. **Not done here**; they remain
   open B920 obligations.
5. **THEOREM_LEDGER Part V labels** are this sweep's readings of LAW_MAP §F's status
   language (e.g. the 3/8 traces entered as [IDENTITY] at the one-prime tier, not
   [THEOREM]); the chain preamble's "this document is a VIEW of the bank" governs — any
   mislabel is correctable against the arcs without loss.
6. **No claim about cc2's closure** was written anywhere (asserted by the audit, no banked
   referent found).
7. **Nothing was committed**; all edits are working-tree only, awaiting the owner's/cc's
   banking pass (PROGRESS_LOG/CHANGELOG/CAMPAIGN_STATUS rows belong to that pass, per the
   bank-completely rule).
