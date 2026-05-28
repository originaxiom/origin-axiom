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

## 2026-05-27 — Phase C / probe E11 (statistical / entropic): `STALLED`

**Frontier observation, not a claim.** (`GOVERNANCE.md` §5.)

- Ran `paths/E11_entropic_emergence/probe.py`. Saved
  `entropy_multiplicity.png` (log-scale multiplicity vs occupancy, n = 64).
- **Exact combinatorics:** `P(empty) = 2⁻ⁿ`; peak multiplicity `C(n, n/2) ∼
  2ⁿ/√(nπ/2)`; entropic pull `log(peak/1) ∼ n·log 2 − ½·log(nπ/2)`. For
  n = 128: P(empty) = 2.9 × 10⁻³⁹, pull ≈ 86.07. No free parameters.
- **Verdict — `STALLED`:** counting works as a *selection* mechanism inside a
  pre-existing configuration space + measure; it does not *construct* either.
  The empty measure space (no σ-algebra, no measure) does not even support
  the inequality `1 ≪ 2ⁿ`. The Boltzmann pull computes "empty is rare *given*
  something," not "something emerges from nothing."
- **Pattern with E14:** two stalls, same shape — E14 had a clean *target*
  (initial object / empty type) without a *force*; E11 has a clean *force*
  (entropy) only when the *target* (phase space) is already given. Neither
  alone supplies the missing piece. Raises the prior that Phase C's missing
  ingredient is genuinely external to both formalism and statistics — it
  lives in physics (E5, E9, E20) or in a structural primitive yet unnamed.
- The measure-theoretic refinement ("does the *absence* of a measure carry
  information?") belongs to **E13**, not E11.
- See `paths/E11_entropic_emergence/FINDINGS.md`. Registry updated.

**Next:** the first batch's third probe, **E5 (Vilenkin tunneling)** — the
quantum-physical candidate. E14 + E11 sharpen the question E5 must answer:
the Wheeler-DeWitt setup must specify both the Hilbert space of "nothing"
and a non-zero amplitude out of it without smuggling either in as a prior.

---

## 2026-05-27 — Phase C / probe E5 (quantum-physical / Vilenkin tunneling): `STALLED`

**Frontier observation, not a claim.** (`GOVERNANCE.md` §5.)

- Ran `paths/E5_vilenkin_tunneling/probe.py`. Saved `vilenkin_barrier.png`
  (`V(a) = a² − (Λ/3)a⁴` for several `Λ`) and `vilenkin_psi.png` (WKB
  `|ψ(a)|` for `Λ = 1`).
- **Exact result:** `B(Λ) = ∫₀^{a_max} √V(a) da = 1/Λ` in natural units
  (closed-form, via the substitution `u = (Λ/3)a²`); analytic vs numeric
  `quad` agree to ~1.8 × 10⁻¹⁴. Amplitude `exp(−2B)` is non-zero for any
  `Λ > 0`.
- **Verdict — `STALLED`:** condition (a) "non-zero amplitude" is met, but
  (b) "generic" fails — the result is artefactual to the FRW topology
  choice, the minisuperspace truncation, the operator-ordering /
  integration-measure choice, the boundary-condition choice
  (Vilenkin/Hartle–Hawking/DeWitt all well-defined and giving different
  answers), and `Λ` is consumed as input, not derived. (c) fails — the
  "probability of a universe" requires a meta-measure the framework does
  not supply. The "nothing" in this setup is the `a = 0` corner of a
  Hilbert space already built on FRW cosmology — the framework the
  mechanism claims to produce is the framework it presupposes.

**First batch closed: E14 + E11 + E5 → three STALLs across three orthogonal
mechanism classes (formal F, statistical E, quantum-physical B).** Each
identifies the specific input it smuggles:

| Probe | Supplies | Smuggles |
|---|---|---|
| E14 | clean *target* (initial object / empty type) | the meta-framework that characterises |
| E11 | exponential *force* toward populated states | the configuration space and measure |
| E5  | non-zero tunneling *amplitude* | FRW topology, truncation, `Λ`, ordering, boundary choice |

The kickoff hypothesis — that most paths would `STALL` at the same wall and
that recognising the wall as universal would itself be a finding — is now
supported with `n = 3`. The wall has a consistent shape: **every candidate
mechanism is well-defined *as a function on* its inputs and does not derive
its inputs.** *Force-vs-target asymmetry.*

**Next batch — selection rule:** prefer paths that target the *framework*
rather than mechanisms inside one. Candidates:

- **E18** (bootstrap / self-consistency, Class I) — consistency as a
  framework-level selector.
- **E15** (boundary / holographic, Class G) — framework as boundary data.
- **E16** (RG flow, Class H) — framework itself is scale-dependent.

Likely additional stalls (recorded for honesty, not as plan):
- **E20** is an E5 variant (inherits the smuggled-Λ problem).
- **E9** is textbook SSB inside an assumed Hilbert space (target-without-
  force, like E11).

A *failed* `STALLED` in the second batch — a probe that does not stall and
does derive its framework — would be the program's first
`PRODUCES-OBSERVABLE` candidate.

---

## 2026-05-27 — Session 3 synthesis: 2025 field theory ↔ 2026 algebraic skeleton; P15, P16 promoted; B6–B9 added

**Two new proven claims (exact algebra about A), four new frontier probes.**

A synthesis handoff (`docs/SESSION3_SYNTHESIS.md`, scripts in `scripts/`)
reconnected the original 2025 field-theory line (non-cancellation potential,
driven scalar) to the algebraic skeleton (A, figure-eight, φ). All five scripts
were run on this machine and independently re-verified symbolically before any
promotion.

**Verified before promotion (independent sympy re-derivation, not the scripts):**

- The Möbius action of `A=[[2,1],[1,1]]` on `H` is `τ→(2τ+1)/(τ+1)`; fixed-point
  equation `τ²−τ−1=0`, roots `φ`, `−1/φ`. Exact.
- Generating vector field from `log A` (P11): `v(τ)=−κ(τ²−τ−1)`,
  `κ=2·log(φ²)/√5≈0.860818`. Both derivations (entries of `log A`; factored form)
  agree symbolically. `v(φ)=v(−1/φ)=0`, `v(0)=κ≠0`. Exact.
- Potential `V(τ)=κ(τ³/3−τ²/2−τ)`; `V′(τ)=κ(τ²−τ−1)`; min at `φ` (`V″=+κ√5`),
  max at `−1/φ` (`V″=−κ√5`), `τ=0` not a critical point (`V′(0)=−κ`). Exact.

**Promoted to the proven core (analogous to P11/P12 — exact algebra about A):**

- **P15** — the Möbius generating vector field. `tests/test_mobius_vector_field.py`
  (9 tests).
- **P16** — the derived potential. `tests/test_derived_potential.py` (9 tests).
- New module `src/origin_axiom/mobius.py`. (P14 left intentionally unused, per the
  synthesis numbering.)

**Added as frontier probes (interpretation; each carries the synthesis caveat):**

- **B6** — field equation `□τ+κ(τ²−τ−1)=0`. Caveat: the potential is derived;
  the kinetic term / dimension / field interpretation are inserted. `STALLED`.
- **B7** — Fisher–KPP creation wave. Reaction `1+τ−τ²` is exact (`=−V′/κ`); seed
  at 0 converges to `φ` (`|⟨τ⟩−φ|≈3.6e−11`), front speed `2√D`. Caveat:
  dissipative gradient flow not the wave eq.; `D` inserted. `STALLED`.
- **B8** — particle spectrum. `mass²=κ√5`, `g=κ` exact; `m/g=√(5/(4logφ))≈1.6117`
  is an **honest near-miss, explicitly NOT φ** (Δ≈0.0063) — recorded under
  disclaimer so it is not later mistaken for a result (cf. D-class numerology).
  `STALLED`.
- **B9** — fusion–scattering. The cubic vertex (`κ/3`) and Fibonacci fusion (P2)
  share `τ²−τ−1`, but no functor: "analogous to" ≠ "derived from". `STALLED`.

**"Six faces" audit.** The synthesis claims `τ²−τ−1` appears in six independent
contexts (`scripts/six_faces.py`). Audited each: **1 defining** (the golden-ratio
equation itself), **4 genuinely independent** (charpoly of `F=[[1,1],[1,0]]`; the
Möbius force law P15/P16; Fibonacci fusion `τ²=1+τ`; the attractor `x=1+1/x`),
**1 via discriminant** (the Markov/Hurwitz optimal constant `√5=√disc`). The
synthesis claim stands with Face 1 as anchor and Face 5 reported as a
discriminant link. **Correction to a too-strong reading:** the Möbius
fixed-point polynomial is a *based* invariant of A, **not** a conjugacy-class
invariant — `K=LAL⁻¹` gives `τ²−3τ+1` (roots `φ²,φ⁻²`), a different polynomial.
So Face 3 is specific to the representative `A=LR`, consistent with R51. The
synthesis's Step 1 uses `A` explicitly, so this is sound.

**Connection to the 2025 genesis.** The derived cubic `V` has its minimum at `φ`
(not zero) and `V′(0)=−κ≠0`, so "nothing" is unstable — the correct shape for the
non-cancellation intuition. This *closes the search* opened in the Oct-2025
conceptual document: the original guess (a cosine potential with its minimum at
zero) had the wrong shape; the potential is now **derived** from the monodromy
A acting on moduli space, not guessed. Four genesis documents were filed under
`legacy/reports/genesis/` (historical only; no claims extracted — see that
directory's README and `PROVENANCE.md` §3.0). The cosine-potential simulations
of `02/03_Master*.txt` are superseded by P16's cubic.

**Honest status.** P15/P16 are *exact algebra about an already-proven object* —
the same kind of result as P11–P13, not a derivation of physics from nothing.
The field theory (B6–B9) remains a natural-but-inserted lift; the force-vs-target
asymmetry of Phase C still holds, with the one genuine advance that the
*potential* (the "force") is no longer inserted. Ledger now: **15 proven**, 4
conditional, 9 open, 10 dead.

---

## 2026-05-28 — Conditional uniqueness theorem (formalizes C1)

**A conditional result, properly labeled — not a promotion.**

Following the Session-3 synthesis and the "minimal substrate" question it raised,
wrote the precise statement and machine-checked the algebra of the conditional
uniqueness theorem: **A1–A7 ⟹ A = LR ⟹ P1–P16.**

- `docs/UNIQUENESS_THEOREM.md` — seven explicit axioms (two-record substrate;
  reversible integer transfer; orientation-preserving; primitive one-channel
  update; torsion-free closure; minimality; **order convention LR vs RL**). The
  first mixed closure `B(a,b) = LₐR_b = [[1+ab,a],[b,1]]` has `det=1`,
  `trace=2+ab`, `det(B−I)=−ab`; torsion-free closure (or minimal hyperbolic trace)
  forces `ab=1`, hence `a=b=1`, hence `A`. The 12×12 grid shows **144 hyperbolic
  positives → 1** under the torsion-free filter.
- `tests/test_uniqueness_theorem.py` (9 tests) locks every numeric assertion in
  the doc: the closure form, det/trace/torsion formulas, torsion order = `ab`, the
  144→1 collapse, trace-3 minimality, `A` and its `φ²,φ⁻²` spectrum.
- **The order choice (A7) is load-bearing, not cosmetic.** `LR` and `RL` are
  `SL(2,ℤ)`-conjugate (same trace/eigenvalues) but give *different* Möbius
  fixed-point polynomials: `LR → τ²−τ−1` (roots `φ,−1/φ`), `RL → τ²+τ−1`
  (`1/φ,−φ`), `K=LAL⁻¹ → τ²−3τ+1` (`φ²,φ⁻²`). The golden polynomial — the one
  driving P15/P16 and the "six faces" — is a **based** invariant of `A=LR` with
  this order, not a conjugacy-class invariant. The uniqueness is honestly *up to
  order*, and that single binary choice is the minimal inserted structure that
  selects the golden vacuum `φ` over its mirror. (This is the same based-invariant
  fact caught in the Session-3 audit, now shown to be structural in the theorem.)
- **C1 updated** in `CLAIMS.md`: evidence upgraded from prose (V4 §2) to a
  machine-checked computation, and extended from "L,R forced" to "A forced up to
  order." **C1 stays `conditional`** — the axioms are motivated, not derived; only
  the axioms→A step is conditional, the A→P1–P16 step is already proven.
- **Scope discipline:** the document stops before the field-theoretic lift
  (`frontier/B6`–`B9`), which carries further inserted choices (kinetic term,
  dimension). This is the exact, finite, conditional statement — the "wall A"
  (derive the substrate from nothing) is untouched and remains mapped-dead.

Ledger unchanged: 15 proven, 4 conditional, 9 open, 10 dead. (Suite: 66 passed,
1 skipped.)

---

## 2026-05-28 — Atlas/paper roadmap integration manifest

**Migration control before content migration.**

After the Session-3 freeze, compared the canonical repository with the private
staging workspace to determine what can be safely integrated without bulk-copying
exploratory work. Added `docs/atlas/INTEGRATION_MANIFEST.md` as the first public
artifact on branch `roadmap/atlas-paper-integration`.

- Local delta audit found: 116 comparable canonical files, 2,995 comparable staging
  files, 8,069 excluded private/cache/raw artifacts, 36 same-hash overlaps, 23
  same-path differences, and 2,936 staging-only files.
- The manifest establishes the migration policy: copy sanitized paper registry
  material, rewrite public atlas docs, summarize campaign/source outputs, keep raw
  inventories and local run artifacts private, and avoid bulk overwrites of
  canonical files such as `CLAIMS.md`, `PROGRESS_LOG.md`, `README.md`, and
  `ROADMAP.md`.
- Planned batches: R1 atlas skeleton; R2 paper-candidate registry; R3 quantum
  selector campaign synthesis; R4 PC02 external-review packet; R5 noncommutative
  residue dossier; R6 state-integral selector dossier.
- No claims changed. This is process infrastructure only.

Verification: staged manifest content passed the private public-safety scan; suite
green with 66 passed, 1 skipped. Pytest emitted a cache-write warning in the
sandboxed execution environment only.

---

## 2026-05-28 — Research Atlas skeleton (R1)

**Public navigation layer, not new claims.**

Implemented the first atlas batch from the integration manifest on branch
`roadmap/atlas-paper-integration`. The goal is to make the work reviewable
without bulk-copying exploratory material into the canonical repository.

- Added `docs/atlas/README.md` as the atlas entry point and source-of-truth
  boundary. It states that `CLAIMS.md`, `GOVERNANCE.md`, `PROGRESS_LOG.md`,
  `frontier/`, `paths/`, and `docs/ARCHIVE.md` remain authoritative.
- Added `docs/atlas/RESEARCH_TREE.md`, mapping the main route from the original
  question through source-free zero failure, cancellation, noncommutative
  residue, the `A = LR` spine, topology host, and the still-open physics bridge.
- Added `docs/atlas/REVIEWER_GUIDE.md`, with separate routes for new readers,
  mathematicians, physicists, and reproducibility checkers.
- Added `docs/atlas/FAILURE_ATLAS.md`, classifying repeated obstructions:
  source law missing, commutative cancellation, selector insertion, measure
  insertion, unit bridge missing, gauge/particle dictionaries missing, 3+1D
  bridge missing, observable missing, and numerology killed by controls.
- Added `docs/atlas/SUCCESS_ATLAS.md`, summarizing the safe surviving structures:
  the proven core, the conditional uniqueness theorem, and the exact internal
  dynamics from the Session-3 synthesis, while keeping physics claims unpromoted.
- Added `docs/atlas/GLOSSARY.md`, a first reader-facing vocabulary for the core
  math, topology, and physics-bridge terms.
- Added `docs/atlas/SIMULATOR_ECOSYSTEM_MAP.md`, establishing that future
  interactive tools must reproduce calculations, expose assumptions, or make
  failures inspectable. Decorative visualizations are explicitly excluded.

No claims changed. The atlas is a map over existing governed evidence.

Verification target for this batch: staged public-safety scan and full test
suite before commit.

---

## 2026-05-28 — Paper-candidate registry (R2)

**Candidate tracking, not claim promotion.**

Implemented the second integration batch on branch
`roadmap/atlas-paper-integration`: a public-safe paper registry that turns
candidate result clusters into auditable cards without presenting them as
finished papers.

- Added `papers/README.md`, defining the rule that a paper candidate is not a
  proven claim and not publication-ready until it passes its own draft gate.
- Added `papers/CANDIDATES.md`, tracking ten candidate outputs with type,
  readiness, core value, and main risk. PC02 is marked as the first ship target;
  PC04 and PC06 are the next structured candidates.
- Added `papers/ARTIFACT_MANIFEST.md`, establishing provenance/checksum rules for
  future PDFs, source files, generated reports, figures, data, and bundles. No
  artifacts were copied in this batch.
- Added `papers/candidates/PC02_conditional_uniqueness/PAPER_CARD.md`, focused on
  the conditional theorem `A1-A7 -> A = LR` up to order, its evidence files,
  controls, and the missing paper-grade mapping-torus homology lemma.
- Added `papers/candidates/PC04_noncommutative_residue/PAPER_CARD.md`, focused on
  the residue program: commutative inverse cancellation leaves no residue, while
  distinguishable ordered inverse operations can leave a noncommutative residue.
- Added `papers/candidates/PC06_quantum_selector_bridge/PAPER_CARD.md`, focused on
  the state-integral route as a serious host whose missing object is a nonzero
  contour/thimble/relative-homology selector theorem.

No claims changed. The registry is a routing layer from atlas nodes and evidence
clusters to possible papers, review packets, or archives.

Verification target for this batch: staged public-safety scan and full test
suite before commit.

---

## 2026-05-28 — Quantum selector campaign synthesis (R3)

**Campaign summary only; raw artifacts stay private.**

Implemented the third integration batch on branch
`roadmap/atlas-paper-integration`: a public-safe synthesis of the completed
`quantum_selector_v1` campaign.

- Added `docs/atlas/campaigns/quantum_selector_v1.md`, summarizing the campaign
  without copying raw JSONL, scoreboards, source downloads, local path
  inventories, or run logs.
- Recorded the stable run facts: 232 cycles, 50 unique mechanisms evaluated, 80
  source-derived questions, and verdicts of 6 survives, 28 stalled, 8 killed, and
  8 needs-expertise.
- Preserved the main positive lesson: the strongest Origin-side survivor is
  ordered noncommutative cancellation residue. The campaign reinforces the
  conditional `A = LR` direction but does not produce a physics bridge.
- Preserved killed-route lessons: source-free zero-birth fails in the tested
  deterministic classes; commutative cancellation leaves no residue; dimensionless
  structure cannot become physics without units, source law, or measurement map;
  direct measured-input leakage kills the tested CKM route.
- Preserved stalled-route lessons: state integrals recover a host curve but not a
  contour/thimble selector; boundary counts do not select a category; finite
  symmetries do not construct gauge connections; trace 3, discriminant 5, and word
  count 16 do not by themselves construct matter content.
- Routed campaign impact to paper candidates: PC02 strengthened indirectly, PC04
  strengthened directly, PC06 sharpened into a selector theorem question, and PC01
  strengthened as an obstruction map candidate.

No claims changed. This batch converts private campaign output into a public
atlas summary and keeps the raw run material out of the repository.

Verification target for this batch: staged public-safety scan and full test
suite before commit.

---

## 2026-05-28 — PC02 external-review packet (R4)

**Review handoff, not new theorem content.**

Implemented the fourth integration batch on branch
`roadmap/atlas-paper-integration`: a concise external-review packet for the
conditional uniqueness paper candidate.

- Added `papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md`.
- The packet gives a reviewer the target statement, files to read, reproduction
  commands, algebra to check, order caveat, non-claims, draft-readiness checklist,
  and review questions.
- The packet isolates the paper-grade missing lemma:
  `H1(mapping torus of B) = Z plus coker(B - I)`, with torsion order
  `|det(B - I)|` when the determinant is nonzero.
- The packet enforces the no-overclaim boundary: C1 stays conditional; A1-A7 are
  not derived from nothing; LR/RL order is not forced from weaker data; B6-B9
  physical lifts are not proven.

No claims changed. This batch prepares PC02 for external mathematical review.

Verification target for this batch: staged public-safety scan and full test
suite before commit.

---

## 2026-05-28 — Noncommutative residue dossier (R5)

**PC04 atlas node; still frontier, not physics.**

Implemented the fifth integration batch on branch
`roadmap/atlas-paper-integration`: a public atlas node for the noncommutative
cancellation residue path.

- Added `docs/atlas/nodes/noncommutative_cancellation_residue.md`, organizing the
  core residue branch: commutative inverse cancellation leaves no residue, while
  distinguishable ordered inverse operations can leave a nontrivial residue.
- Linked the node to R27, R40, R42, the quantum-selector campaign synthesis, and
  the PC04 paper card.
- Recorded the strict result: `LR - RL != 0` and `L R L^-1 R^-1 != I`; in the
  commutative quotient the residue disappears.
- Recorded the no-overclaim boundary: the two operations, order loop, substrate,
  field dictionary, unit scale, source law, and observable are not derived.
- Updated `papers/candidates/PC04_noncommutative_residue/PAPER_CARD.md` with the
  new atlas node and concrete reproduction commands for R27, R40, R42, and the
  full test suite.

No claims changed. PC04 remains a paper candidate whose missing theorem is the
formal distinguishability/order/residue statement.

Verification target for this batch: staged public-safety scan and full test
suite before commit. The private staging probes behind the R5 summary are not
yet migrated as canonical public reproducers.

---

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->
