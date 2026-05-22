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

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->
