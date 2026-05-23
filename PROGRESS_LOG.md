# Origin Axiom — Progress Log

Append-only, chronological. Never edit past entries. Each working session adds a dated
entry. When this file grows large, older entries roll into `docs/progress/` by quarter.
Governed by `GOVERNANCE.md` §9.

---

## 2026-05-22 — Consolidation: audit + Phase 0 governance

**Context.** The project had scattered across four GitHub repositories
(`origin-axiom-framework`, `origin-axiom-theta-star`, `origin-axiom-obstruction`,
`00_origin-axiom`) and a large local archive of May-2026 AI-assisted sessions. This
repository was created as the single canonical home.

**Done:**

- **Full audit** of all prior work. Produced `PROVENANCE.md` (artifact map) and
  `AUDIT_REPORT.md` (reconciled status).
  - Key finding: two contemporaneous 2026-05-21 self-assessments disagree — an optimistic
    one (`handoff.md`) and a disciplined one (Reality Check v1 + V4 paper).
    The disciplined line was adopted as canonical.
  - Reconciled the status of all results into a ledger: 10 `proven`, 4 `conditional`,
    9 `open`, 10 `dead`.
- **Phase 0 governance scaffolding** built: `GOVERNANCE.md` (constitution),
  `CLAIMS.md` (living ledger), `README.md`, `ROADMAP.md`, this log, `CHANGELOG.md`,
  `REPRODUCIBILITY.md`, `docs/ARCHIVE.md`, `.gitignore`.
- **Framing locked** to the V4 / Reality-Check line (`GOVERNANCE.md` §2): the project is a
  candidate classical/statistical transfer-matrix framework, not a physics theory.

**Decisions (with the project owner):**

- New canonical repo to live in the `originaxiom` GitHub org; the four old repos to be
  archived (read-only) with "superseded by" pointers — pending GitHub admin authentication.
- Governance: framework-grade but right-sized.
- Plan: Phase A (tested foundation) first, then Phase B (frontier).

**Blocked:** GitHub reorganization — the available `gh` login (`edhe-dev`) has no admin
rights on the `originaxiom` org. Awaiting owner authentication.

**Next:** reorganize `old/` into `legacy/`; then Phase A — build `src/origin_axiom/` and the
test suite locking claims P1–P10.

---

## 2026-05-22 — Legacy reorganization & repository consolidation

**Done:**

- `old/` → `legacy/raw/old/` (git-ignored). Curated text extracted to
  `legacy/reports/` (V4 paper, Reality Check, G1–G5 gate reports) and
  `legacy/reports/session_md/`. Added `legacy/README.md`, `legacy/github-repos.md`.
- the hand-off document → `legacy/handoff/handoff.md` (historical record only, per
  `GOVERNANCE.md` §2).
- A genesis-era folder `e_origin axiom` (~3.6 GB, ~Oct 2025 — the original
  "Non-Cancelling Principle" work) was discovered during the move. Git-ignored
  under `legacy/raw/`, recorded in `PROVENANCE.md` §3.0; **not yet audited in
  detail** — flagged for a later pass.
- GitHub: `gh` authenticated as `originaxiom` (a user account, not an org; the
  four prior repositories belong to it). Confirmed `origin-axiom` was a former
  name of `origin-axiom-framework` (stale redirect).
- Canonical repository `originaxiom/origin-axiom` created (public); Phase 0
  committed, pushed, and tagged `phase0-governance-freeze`.
- The four prior repositories — `origin-axiom-framework`, `origin-axiom-theta-star`,
  `origin-axiom-obstruction`, `00_origin-axiom` — each received a "superseded by"
  pointer commit on its README and was archived (read-only). They are kept, not
  deleted: their commit history is the project's record of progression.

**Next:** Phase A — build `src/origin_axiom/` and the test suite locking P1–P10.

---

## 2026-05-22 — Phase A: tested foundation

**Done:**

- Built the `origin_axiom` package under `src/`: modules `constants`, `algebra`,
  `statistics`, `gluing`, `topology`.
- Built `tests/` — one test file per proven claim P1–P10, plus `test_conditional.py`
  covering the computable conditional claims C2–C3.
- Test suite **green: 33 passed, 1 skipped** (the skipped test is the optional
  SnapPy live cross-check; the figure-eight constants are also hard-coded and
  tested without SnapPy).
- One test was corrected mid-run: the mapping-torus torsion growth rate approaches
  `log(φ²)` from *below*, not above — the test now asserts the correct property.
  (Logged per `GOVERNANCE.md` §6: the red-team lens caught a wrong assumption.)
- `CLAIMS.md` evidence column updated — every P-claim now points to its passing test.
- Packaging: `pyproject.toml` (pytest `pythonpath=src`, no install step needed),
  `requirements.txt`.

**Phase A gate:** passed — suite green, all ten P-claims locked behind tests.
Tagged `phaseA-foundation-freeze`.

**Next:** Phase B — the frontier. First probe (B1): does the gluing identity
`W = S_L − F_R + ms` map onto the discrete Chern–Simons flatness condition `F=0`?
See `ROADMAP.md`. Phase B is quarantined in `frontier/` and gated.

---

## 2026-05-22 — Phase B / probe B1: gluing vs. Chern-Simons flatness

**This is frontier work — observations, not claims.** (`GOVERNANCE.md` §5.)

- Ran the first frontier probe, `frontier/B1_gluing_chern_simons/probe.py`.
- **Exact results:** `log(A) = (log φ²/√5)·(H + 2(E+F))` — verified against
  `scipy.linalg.logm` to 2.8e-16; frame-to-spin-connection ratio `d/a = 2`
  exactly; torsion component (antisymmetric `E−F` part) exactly 0 — the discrete
  connection is torsion-free. The gluing identity is re-read as the holonomy
  composition law (shared edge `m=q, s=Q−q`).
- **Verdict — qualified yes, bounded:** the gluing reproduces the holonomy-level
  structure that discrete flatness encodes, and `log(A)` splits cleanly into a
  torsion-free frame + spin connection. It does **not** produce the Chern-Simons
  action, its level `k`, or anything distinguishing 2+1 *gravity* from a generic
  flat-connection theory. See `frontier/B1_gluing_chern_simons/README.md`.
- **No claim promoted.** O1–O5 remain `open`. The real open problem — pinning a
  Chern-Simons gauge in which the gluing variables *are* `(ω, e)` and checking
  whether a level `k` is forced — is not closed.

---

## 2026-05-22 — Phase B / probe B2: monodromy action on the moduli space

**Frontier work — observations, not claims.** (`GOVERNANCE.md` §5.)

- Ran `frontier/B2_moduli_evolution/probe.py`.
- **Solid:** the monodromy acts on `(log M, log L)` as the linear map `A`;
  hyperbolic dynamics with multipliers `φ²`, `φ⁻²`; fixed point = complete
  structure; continuum limit = the flow `exp(t·log A)` (returns `A` at `t=1`).
- **Negative result:** the handoff document's claim that *"A acts on the
  A-polynomial curve as (M,L)→(M²L,ML)"* is **falsified** — that substitution
  does not leave the figure-eight A-polynomial curve invariant (nonzero
  remainder). The handoff conflated the fiber character variety with the knot
  exterior's `(M,L)` coordinates. Consistent with the 2026-05-22 audit's warning
  that the handoff over-reaches.
- **No claim promoted.** O1–O5 remain `open`. See
  `frontier/B2_moduli_evolution/README.md`.

---

## 2026-05-22 — Phase B / probe B3: figure-eight triangulation & the 4D Regge question

**Frontier work — observations, not claims.** (`GOVERNANCE.md` §5.)

- Ran `frontier/B3_regge_complex/probe.py`.
- **Solid:** the figure-eight's 3D ideal triangulation (2 regular ideal
  tetrahedra, 2 edges, 4 faces, 1 cusp) and its Regge edge check — six `π/3`
  dihedral angles meet at each edge, sum `2π`, **deficit 0**: the complete
  hyperbolic structure is the zero-deficit Regge solution. Exact.
- **Clarifying negative:** the handoff's "Step 5A" — *build a 4D Regge complex by
  stacking figure-eight slices by A* — is **not a defined construction**. It
  supplies no 4-manifold and no 4-simplices. The path 5A→5C→Einstein has an
  undefined first step.
- **Pattern across B1–B3:** in each probe the well-defined content is exact and
  real, while the bridge to 3+1 gravity rests on a step asserted but not
  constructed. That is the genuine open problem (O1–O3) — not a computation away.
- **No claim promoted.** O1–O9 remain `open`. See `frontier/B3_regge_complex/README.md`.

---

## 2026-05-22 — Session-3 integration: P11–P13 promoted, probes B4–B5 added

A review from the prior session proposed promoting more computational results.
Each was evaluated against the promotion gate (`GOVERNANCE.md` §5) rather than
bulk-imported.

**Promoted to the proven core** (exact algebra, gate passed):

- **P11** — exact sl(2,ℝ) decomposition `log(A) = (log φ²/√5)(H + 2(E+F))`;
  ratio `d/a = 2`, antisymmetric `(E−F)` component exactly 0.
- **P12** — the figure-eight gluing equation factors as (Eisenstein)(golden),
  discriminants −3 and 5.
- **P13** — `[[1,2],[2,−1]]` (the shape of `log A`) and `G` are isospectral;
  elementary corollary of P11 + P6.

**Declined for the proven core:** the review's proposed "P14" (Kasner exponents
at `u = φ`). The Kasner conditions hold for *every* `u`; the only φ-specific
fact — the golden geometric progression of exponents — is downstream of a
frontier claim. It belongs in probe B4, not `src/`. Promoting it would smuggle
an unproven selection into the proven core.

**Added as frontier probes** (observations, not claims):

- **B4** — BKL billiard / Gutzwiller / golden Kasner. The figure-eight orbit is
  the shortest primitive modular-billiard orbit; the leading Gutzwiller term
  (37.8% — modest); golden Kasner exponents at `u = φ`. Heavily caveated.
- **B5** — Wheeler-DeWitt constraint and a `Λ = 2π²/Vol` estimate. The estimate
  is ~10¹²⁰ off observation and dead-adjacent (cf. D1, D2) — recorded as a
  documented warning so the path is not silently re-attempted.

Test suite: **39 passed, 1 skipped.** Ledger now: **13 proven, 4 conditional,
9 open, 10 dead.**

---

## 2026-05-23 — Phase C kickoff: exhaustive survey of emergence-paths

**Reframe.** The project's posture shifts from validating one mechanism (the L/R/A
record system → figure-eight → φ) to **systematically surveying** the space of
mechanisms by which "nothing being unstable" could produce reality. The deliverable
becomes the *map of attempted paths* — most of which are expected to `STALLED` at
the same wall Phase B probes hit. The user's *"if reality emerges at all"* is the
honest framing.

**Done in this kickoff:**

- Scaffolded `paths/` (a new top-level directory parallel to `frontier/`):
  - `paths/README.md` — scope, ground rules, verdict labels (carried from
    `GOVERNANCE.md`).
  - `paths/PATHS.md` — the 25-row registry: 20 mathematizable paths (E1–E20) and
    5 philosophical paths (P1–P5), with status per path.
  - `paths/MECHANISM_CLASSES.md` — the 12 mechanism classes (A–L) with rationale.
  - `paths/philosophical/PHILOSOPHICAL_PATHS.md` — the P1–P5 register, cleanly
    separated.
- Cross-linked the existing `frontier/B1`–`B5` work to the paths it partially
  explored (E1, E2, E3, E6) — not duplicated.
- Updated `ROADMAP.md` with a Phase C section; `README.md` status table gains a
  Phase C row.

**First batch (selected to span maximally different mechanism classes):**

| Probe | Class | Question |
|---|---|---|
| E14 | Formal | Does "nothing" admit a precise definition (initial object / empty type)? |
| E11 | Statistical | Does counting alone force something? |
| E5 | Quantum-physical | Does Vilenkin tunneling-from-nothing actually produce a universe? |

**Next:** Run the three first-batch probes. Each ends with one of `PRODUCES-OBSERVABLE`,
`STALLED`, `DEAD`, `NEEDS-EXPERTISE`. Re-plan the second batch after all three
verdicts are in.

---

## 2026-05-23 — Phase C / probe E14 (categorical / initial-object): `STALLED`

**Frontier observation, not a claim.** (`GOVERNANCE.md` §5.)

- Formal analysis only (no probe.py — the path is conceptual). See
  `paths/E14_categorical_initial_object/{README,FINDINGS}.md`.
- All four standard formal characterizations of "nothing" (set theory, category
  theory, type theory, HoTT) are well-defined and unique up to canonical
  isomorphism. **None of them, by itself, forces emergence.** Each is defined
  by having minimal structure.
- The mathematizable conclusion mirrors the philosophical path P1:
  characterising "nothing" presupposes a containing framework; the framework is
  not empty, but the object inside it is. The categorical level supplies the
  *target* of the question, not the *force*.
- **Verdict:** **`STALLED`** — the unconstructed step is identified precisely:
  every other E* probe must supply a *dynamical or physical* principle
  external to the formalism. Pure formal characterization is necessary but
  insufficient.
- This finding *bounds the rest of the program*: appeals to pure formalism
  cannot supply the emergence ingredient. The other first-batch probes (E11
  entropic, E5 Vilenkin) are precisely tests of two different candidate
  ingredients (counting and quantum tunneling). E14's verdict makes their
  responsibility clear.

---

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->
