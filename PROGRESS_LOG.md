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
- Added `docs/atlas/AUDITOR_GUIDE.md`, with separate routes for new readers,
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

**Validation handoff, not new theorem content.**

Implemented the fourth integration batch on branch
`roadmap/atlas-paper-integration`: a concise validation packet for the
conditional uniqueness paper candidate.

- Added `papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md`.
- The packet gives a reader the target statement, files to read, reproduction
  commands, algebra to check, order caveat, non-claims, draft-readiness checklist,
  and validation questions.
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

## 2026-05-28 — State-integral selector-gap dossier (R6)

**PC06 atlas node; theorem question, not solved selector.**

Implemented the sixth integration batch on branch
`roadmap/atlas-paper-integration`: a public atlas node for the state-integral
selector gap.

- Added `docs/atlas/nodes/state_integral_selector_gap.md`, organizing the
  quantum-topology bridge as a precise missing-selector problem.
- Updated `papers/candidates/PC06_quantum_selector_bridge/PAPER_CARD.md` to point
  at canonical atlas evidence rather than private staging paths.
- Recorded what survives: quantum-dilog/state-integral hosts, figure-eight
  A-polynomial asymptotics, Picard-Lefschetz/Stokes language, and nontrivial
  monodromy-residue structure.
- Recorded what fails locally: zero winding remains allowed, multiple primitive
  windings remain allowed, nontrivial kernel windings exist, orientation remains
  unforced, and no source-normalized thimble-intersection vector was constructed.
- Stated the needed theorem: a source-normalized quantum-dilog /
  Picard-Lefschetz result forcing a nonzero relative-homology or
  thimble-intersection class for the figure-eight state integral.

No claims changed. PC06 remains `NEEDS_VALIDATION` and expertise-bound.

Verification target for this batch: staged public-safety scan and full test
suite before commit.

---

## 2026-05-29 — Atlas/paper integration closure (R7)

**Roadmap closure and merge gate.**

Closed the public-safe atlas/paper integration roadmap on branch
`roadmap/atlas-paper-integration`.

- Updated `docs/atlas/INTEGRATION_MANIFEST.md` so it no longer points to the old
  "R0 only" decision. The manifest now marks R0-R6 complete and records R7 as
  the closure batch.
- Recorded the merge gate: clean integration branch, full test suite, branch-wide
  public-safety scan, diff hygiene, no raw/private artifacts, and public log
  entries.
- Planned final integrated tag: `atlas-paper-integration-v1`.

No claims changed. This is roadmap closure for already-curated documentation and
paper-candidate infrastructure.

Verification target for this batch: staged public-safety scan, diff hygiene,
full test suite, branch-wide private-material check, merge to `main`, and tag if
clean.

---

## 2026-05-29 — Post-merge integration manifest cleanup

**Cleanup after `atlas-paper-integration-v1`; no tag movement.**

After merging `roadmap/atlas-paper-integration` into `main` and pushing tag
`atlas-paper-integration-v1`, cleaned the manifest wording so the public roadmap
matches repository reality.

- `docs/atlas/INTEGRATION_MANIFEST.md` now marks R7 complete.
- Removed stale "R0 only / atlas skeleton" residue from the manifest's current
  decision section.
- Recorded that future work should proceed on new focused branches, beginning
  with PC02 conditional uniqueness.

No claims changed. The existing `atlas-paper-integration-v1` tag remains
unchanged.

---

## 2026-05-29 — PC02 mapping-torus torsion lemma

**Paper-support proof, not claim promotion.**

Started the PC02 conditional-uniqueness review track on branch
`paper/pc02-conditional-uniqueness`.

- Added `papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md`.
- Linked the lemma from `docs/UNIQUENESS_THEOREM.md`.
- The note proves the standard mapping-torus homology step using the Wang exact
  sequence:
  `H1(M_B; Z) = Z plus coker(B - I)`.
- It also proves that if `det(B - I) != 0`, then the torsion order is
  `|det(B - I)|`, via Smith normal form.
- For `B(a,b) = L_a R_b = [[1+ab,a],[b,1]]`, this gives
  `det(B(a,b)-I) = -ab`, so the torsion-free filter forces `ab = 1`, hence
  `a = b = 1` over positive integers.
- Updated the PC02 paper card and review packet from "missing lemma" to "lemma
  written; ready for external mathematical review after final wording pass."

No claims changed. C1 remains conditional; this only supplies a paper-grade proof
of the topology step already used by the theorem document and tests.

---

## 2026-05-29 — PC02 validation brief

**Validation-ready handoff, not public draft.**

Completed the final PC02 wording pass on branch
`paper/pc02-conditional-uniqueness`.

- Added `papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md`.
- Tightened the PC02 paper card and review packet so the current state is
  "ready for mathematical validation," not publication-ready.
- Advanced PC02 readiness from `EVIDENCE_EXISTS` to `NEEDS_VALIDATION` in both
  `papers/CANDIDATES.md` and the paper card, reflecting that the evidence and
  proof packet exist but still need independent mathematical validation before becoming
  `DRAFTABLE`.

No claims changed. C1 remains conditional.

---

## 2026-05-29 — B13 trace-map character-variety probe

**Exploration branch probe; exact algebra, no claim promotion.**

Started the trace-map exploration track on branch
`explore/trace-map-character-variety`.

- Added `frontier/B13_trace_map_character_variety/` with `README.md`,
  `probe.py`, and `FINDINGS.md`.
- The probe computes the punctured-torus trace map
  `T(x,y,z) = (z,x,2xz-y)` and the Fricke-Vogt invariant
  `I = x^2+y^2+z^2-2xyz-1`.
- Exact result: the Jacobian at `(1,1,1)` has characteristic polynomial
  `(t+1)(t^2-3t+1)`. On an invariant rank-2 lattice, the quadratic sector is
  represented by `M=[[0,1],[-1,3]]`, a `GL(2,Z)` conjugate of
  `A=[[2,1],[1,1]]`; the full parity-plus-rank-2 block basis has determinant
  `5`.
- Additional checks: `I` is preserved exactly; the `I=0` singular points form a
  regular tetrahedron; the Hessian at `(1,1,1)` has eigenvalues `-2,4,4`; the
  local `x=z=1+eps` Jacobian family preserves the `-1` parity eigenvalue while
  splitting the two golden modes.
- Control: the `x=z=1+eps` family is **not** a fixed-point branch. The only
  fixed points of the trace map are `(0,0,0)` and `(1,1,1)`.
- Genericity control: the `A`-sector is the symmetric-square trace lift of the
  primitive orientation-reversing Fibonacci half-step `F=[[1,1],[1,0]]`, not of
  the direct monodromy `A=F^2`. Direct `A` gives `(t-1)(t^2-7t+1)`, i.e. the
  `A^2` sector. The `A` quadratic in a `GL(2,Z)` symmetric-square lift occurs
  exactly for `det=-1`, `trace=+/-1`.
- Caveat: all readings in terms of physical `3+1`, particle masses,
  gauge-protection, Kasner/BKL gravity, or awareness remain interpretive
  dictionaries, not derived physics.

Verdict: `STALLED` at the dictionary from trace-character coordinates to
physical or cognitive interpretation. No claims changed.

---

## 2026-05-29 — B14 half-step square-root selector

**Continuation of the trace-map controls; exact algebra, no claim promotion.**

Added `frontier/B14_half_step_square_root_selector/` on branch
`explore/trace-map-character-variety`.

- The probe checks the half-step behind B13. With record swap
  `P=[[0,1],[1,0]]`, `F=L P=[[1,1],[1,0]]` satisfies `F^2=A`.
- Exact result: the only `GL(2,Z)` square roots of `A` are `F` and `-F`. The
  proof uses eigenvalue trace constraints plus Cayley-Hamilton:
  if `X^2=A`, then `det(X)=-1`, `tr(X)=+/-1`, and
  `X=tr(X)(A-I)`.
- General mixed-closure result: for
  `B(a,b)=L_a R_b=[[1+ab,a],[b,1]]`, an integer orientation-reversing square
  root exists iff `a=b`; then `B(k,k)=(L_k P)^2`.
- Consequence: the half-step requirement is a symmetry/balance selector. It does
  not by itself select `k=1`; combined with the existing torsion-free/minimality
  condition `ab=1`, it yields `F=L P` and `F^2=A`.
- Caveat: this shifts the live question to the status of the record-swap `P`.
  If `P` is a legitimate pre-dynamical symmetry of the two-record substrate, the
  half-step is forced up to sign. If not, it remains inserted.

Verdict: `STALLED` at deriving the record-swap symmetry. No claims changed.

---

## 2026-05-29 — B15 trace-map invariant controls

**Part C2 trace-map audit; exact controls plus one normalization correction.**

Added `frontier/B15_trace_map_invariant_controls/` on branch
`explore/trace-map-character-variety`.

- Exact result: for the naive vector-field proxy `V=T-id`, the Jacobian on the
  diagonal `(c,c,c)` has characteristic polynomial
  `(mu+2)(mu^2+(1-2c)mu+(1-2c))`; the quadratic discriminant is
  `(2c-1)(2c+3)`, giving Eisenstein at `c=0`, nilpotent at `c=1/2`, and golden
  at `c=1`.
- Control: only `c=0` and `c=1` are actual trace-map fixed points; `c=1/2` is
  a linearization checkpoint, not a fixed point.
- Exact result: the discrete trace map preserves the Fricke-Vogt invariant
  `I=x^2+y^2+z^2-2xyz-1`; the naive continuum proxy fails this at
  `(3/2,1,3/2)` on `I=0`, where `dI/dt=-5/4`.
- Correction: using the usual Fibonacci initial-line normalization with
  hopping `h=1`, `x=(E-lambda)/2`, `y=E/2`, `z=1`, the invariant is
  `I=lambda^2/4`. More generally, `I=(lambda/h)^2/4`. Therefore
  `I(1,1,3/2)=1/4` gives dimensionless `lambda/h=+/-1`, not `sqrt(5)`. The
  proposed `sqrt(5)` coupling requires a shifted convention and is not accepted
  here.
- Caveat: labels such as "nothing", "awareness", or "existence" for different
  `I`-surfaces remain semantic overlays; the exact result is only invariant
  separation.

Verdict: `STALLED` at the interpretive dictionary. No claims changed.

---

## 2026-05-29 — B16 record-swap symmetry status

**Testing whether the B14 half-step assumption is forced or inserted.**

Added `frontier/B16_record_swap_status/` on branch
`explore/trace-map-character-variety`.

- Exact result: the involutions in `GL(2,Z)` that exchange the primitive shears
  satisfy `X^2=I` and `X L X^-1=R`; bounded exact search finds only
  `P=[[0,1],[1,0]]` and `-P`.
- Exact result: the bounded automorphism group of the primitive pair `{L,R}` is
  `{I,-I,P,-P}`, where `P` and `-P` swap the pair.
- Relation to order: `P A P = RL`, so `P` exchanges the two based order choices.
- Relation to half-step: `F=L P` and `F^2=A`; the sign ambiguity gives only
  `+/-F`.
- Caveat: A1-A6 do not derive the exchange-symmetry requirement. `P` is forced
  only after adding a plausible but additional substrate-exchange axiom.
- Minimality addendum: several weaker conditions were tested. Plain
  orientation-reversing involution is too weak. The operational half-step
  condition `(L X)^2=A` is sufficient and gives exactly `X=+/-P`; so does
  requiring `X A X^-1=RL`. By contrast, generic orientation-reversing
  time-reversal of `A` leaves many candidates.

Verdict: `STALLED` at deriving exchange/half-step symmetry. No claims changed.

---

## 2026-05-29 — Trace-map/spectrum checkpoint and review-note package

**Checkpoint packaging; no claim promotion.**

Prepared the current `explore/trace-map-character-variety` branch for external
review without merging it to `main`:

- Added `papers/candidates/PC02_conditional_uniqueness/DRAFT_NOTE.md` as a
  compact review note centered on the conditional uniqueness theorem. B13-B25
  appear only as appendices and motivated frontier extensions.
- Added `papers/candidates/PC11_trace_map_spectrum_bridge/PAPER_CARD.md` to
  track the half-step trace lift / Fibonacci spectrum bridge separately from
  PC02.
- Added and executed `frontier/B26_lambda1_derivation_attempt/`. Exact algebra
  confirms the proposed selector:
  `char(DT^3 at (0,0,c))=(t+1)(t^2-(4c^2-2)t+1)`, so matching the `A`
  quadratic forces `c^2=5/4`, hence `I=1/4` and positive dimensionless
  `lambda/h=1`.
- Control: `(0,0,c)` is not a literal period-3 orbit of the signed trace map;
  `T^3(0,0,c)=(0,0,-c)` and the literal `T^6` return gives
  `t^2-27t+1` at `I=1/4`, not `A`'s polynomial.
- Verdict: B26 strengthens B25 from "shared invariant surface" to "unique
  projective half-return self-similarity surface," but this still depends on a
  projective/sign-quotient criterion that is not derived from A1-A7.
- Extension: the same projective criterion gives an exact Lucas hierarchy for
  even `n`: `char(F^n)=t^2-L_n t+1`, so
  `I=(L_n-2)/4` and `(lambda/h)^2=L_n-2 = 1,5,16,45,121,...`.
  This is exact algebra under the criterion, not yet a physical spectrum.
- Full-return control: literal `T^6` matching of the `A` sector selects real
  `c^2=1/4`, hence `I=-3/4` and `(lambda/h)^2=-3` under the B25 normalization.
  The projective half-return distinction is therefore material.

Ledger unchanged: B13-B26 remain frontier-only; `lambda/h=1` remains motivated
by a sharper selector, not unconditionally derived.

---

## 2026-05-29 — B27-B29 higher-rank and selector controls

**Extended the trace-map campaign; no claim promotion.**

Added B27-B29 as controlled follow-ups to the B26 selector:

- **B27 `SL(3)` Fibonacci trace lift:** derived and verified the
  eight-coordinate `SL(3)` trace lift of `sigma(a)=ab, sigma(b)=a`. At the
  trivial representation, the Jacobian factors as
  `(t-1)(t+1)(t^2-4t-1)(t^2-3t+1)(t^2+t-1)`, with eigenvalues
  `phi^3, phi^2, -phi, 1, -1, 1/phi, 1/phi^2, -1/phi^3`. The `A` quadratic
  survives, but the fixed-point decomposition is symmetric/antisymmetric under
  inverse-trace pairing; direct/inverse trace distinctions are not promoted to
  particle/antiparticle physics.
- **B28 projective quotient legitimacy:** proved the central sign action
  `S(sa,sb)(x,y,z)=(sa*x,sb*y,sa*sb*z)` is compatible with the half-step trace
  map via `T(S(sa,sb)p)=S(sa*sb,sa)T(p)`. Thus the B26
  `T^3(0,0,c)=(0,0,-c)` identification is legitimate after passing to
  central-sign / `PSL` data. The remaining gap is still the selector: choosing
  that quotient as the self-similarity criterion is not derived from A1-A7.
- **B29 hierarchy and normalization controls:** separated absolute `lambda`
  from the dimensionless ratio `lambda/h`. Under the B26 projective criterion,
  even `n` gives `(lambda/h)^2=L_n-2 = 1,5,16,45,121,320,...`; literal
  full-return matching gives a different hierarchy
  `(lambda/h)^2=sqrt(L_n-2)-4`. Finite spectra at the first projective values
  `lambda/h=1,sqrt(5),4` pass top-gap labeling controls, validating the
  computation but not deriving a physical spectrum.

Verdict unchanged: B25-B29 strengthen the trace-map/spectrum bridge as exact
and reproducible frontier evidence. They do not promote `lambda/h=1`, a
physical dictionary, or any awareness/particle/spacetime interpretation into
the core.

---

## 2026-05-29 — B30-B37 selector-first campaign

**Executed the selector-first campaign; no claim promotion.**

Added B30-B37 to test every current route toward the missing `lambda/h=1`
selector.

- **B30 projective state space:** the central-sign quotient is canonical once
  the state space is lift-independent `PSL` trace-character data. Quotient
  coordinates `u=x^2,v=y^2,w=z^2,r=xyz` obey `r^2=uvw`, and the trace map
  descends polynomially. The B26 sign-flipping half-return is literal period 3
  in the quotient, but it leaves `I=c^2-1` free.
- **B31 primitive projective return:** primitive projective return alone exists
  for every `c`. Matching the return linearization to the original `A`
  quadratic selects `c^2=5/4`, `I=1/4`, `lambda/h=1`, but this is an additional
  `A`-sector matching rule.
- **B32 selector axiom audit:** isolated the missing object as **S1**: "the
  primitive projective return linearization must contain the original
  `A` quadratic sector `t^2-3t+1`." A1-A7 plus exchange get the trace-map
  setting; they do not derive S1.
- **B33-B36 extension routes:** `SL(2)`/`SL(3)` spectra fit a symmetric-power
  tower, Goldman/WP structure descends to the quotient, sign topology explains
  the order-3 projective behavior, and Fibonacci spectral controls remain
  compatible with `lambda/h=1`. None independently derives S1.
- **B37 operational feedback quarantine:** feedback and invariant language are
  restricted to computable predicates. The trace map has nonlinear feedback and
  a preserved invariant, but it does not satisfy an operational self-model
  criterion; awareness/religion/metaphysics-adjacent language remains outside
  the claims system.

Net result: the frontier is narrower, not solved. The projective quotient is
well-supported; the selector is now precisely S1 and remains `STALLED`.

---

## 2026-05-29 — B38-B47 deep S1 campaign

**Deepened the selector search; no claim promotion.**

Added B38-B47 to test whether S1 can be derived from arithmetic, topology,
renormalization, or higher-rank stability.

- **B38 tangent arithmetic filter:** for the primitive projective return, the
  tangent trace is `mu=4c^2-2=4I+2`. If this tangent return inherits integer
  hyperbolic trace plus minimality, or the tangent analogue of torsion-one
  closure, then `mu=3`, hence `I=1/4` and `lambda/h=1`.
- **B39-B40 filter inheritance audit:** integrality gives a discrete family
  `c^2=(m+2)/4`, not a unique value. The missing assumption is **T1**: the
  primitive projective tangent return inherits the original arithmetic
  persistence filters. With T1, S1 follows; without T1, `I` remains free.
- **B41-B42 controls:** the coordinate-axis projective 3-cycle is the simplest
  nontrivial one-parameter family, but still leaves `I=c^2-1`; simple
  variational quantities are monotone or boundary-selected and do not pick
  `I=1/4` unless the target is built into the functional.
- **B43-B45 supporting conditional routes:** minimal positive nonsquare
  discriminant gives `Delta=5`, torsion-one closure gives `mu=3`, and the
  primitive Lucas hierarchy member gives `(lambda/h)^2=1`; each route requires
  the tangent arithmetic/filter inheritance assumption.
- **B46 rank stability:** the selected `A` sector divides the known `SL(3)`
  trace-lift Jacobian, while a nearby tangent quadratic does not. This supports
  stability of the selected sector but does not derive it.
- **B47 verdict ledger:** S1 is **conditional**, not derived. The strongest
  honest dependency is `T1 -> S1 -> I=1/4 -> lambda/h=1`.

Net result: the missing object moved one level deeper. S1 can be justified by a
named tangent-filter inheritance assumption T1, but T1 itself is not derived
from A1-A7 plus exchange.

---

## 2026-05-29 — Conditional trace selector theorem (formalizes C5)

**Packaged the B38-B47 selector result as conditional claim C5; no proven-claim
promotion.**

Added `docs/TRACE_SELECTOR_THEOREM.md`, a theorem-style note that states the
current strongest trace-map selector result:

```text
T1 -> S1 -> I=1/4 -> lambda/h=1
```

- **C5 added to `CLAIMS.md`:** the primitive projective tangent return selects
  the `A` sector `t²−3t+1`, hence `I=1/4` and dimensionless `lambda/h=1`, only
  under **T1**: the tangent return inherits the original arithmetic persistence
  filters.
- **The algebra after T1 is exact:** B38 locks `mu=4c²−2=4I+2`; minimal positive
  integer hyperbolic trace or tangent torsion-one closure gives `mu=3`, hence
  `I=1/4`; B25's normalization gives `(lambda/h)²=4I=1`.
- **The open object is now precise:** B39-B47 show that T1 itself is not derived
  from A1-A7 plus exchange. Validation should ask whether T1 is a theorem,
  a standard naturality/filter-inheritance principle, or an extra axiom.
- **Documentation synchronized:** `README.md`, `docs/atlas/README.md`,
  `docs/atlas/AUDITOR_GUIDE.md`, and PC11 now point to the C5 package and keep
  the spectrum bridge conditional, not predictive.

Ledger update: 15 proven, **5 conditional**, 9 open, 10 dead. Proven test suite
unchanged.

---

## 2026-05-30 — PC11 validation packet and freeze preparation

**Prepared the trace-selector branch for validation and freeze.**

Added a Markdown-only validation layer for the now-narrowed mathematical question:

```text
Is T1 natural, standard, derivable, or inserted?
```

- `papers/REVIEWABILITY_INDEX.md` routes readers to the two ready packets:
  PC02 (conditional uniqueness) and PC11 (half-step trace lift / C5 selector).
- `papers/candidates/PC11_trace_map_spectrum_bridge/VALIDATION_BRIEF.md`
  gives a compact validation handoff focused on the trace lift, projective quotient,
  tangent return quadratic, and T1.
- `papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md` gives the
  full audit path, reproduction commands, controls, non-claims, and outcome
  labels.
- PC11 readiness advanced from `EVIDENCE_EXISTS` to `NEEDS_VALIDATION`; it is
  blocked from stronger status until independent validation of T1.
- `REPRODUCIBILITY.md` now records the planned freeze tag
  `trace-selector-c5-freeze`.

No claims changed. Ledger remains 15 proven, 5 conditional, 9 open, 10 dead.

---

## 2026-05-30 — Reviewability and falsifiability workflow

**Refocused the paper layer toward reviewability; no claims changed.**

Replaced the communication-oriented packet layer with repo-native validation
artifacts:

- `papers/VALIDATION_WORKFLOW.md` — process for selecting a packet, running
  reproduction checks, recording findings, assigning outcome labels, and
  deciding repository actions.
- `papers/VALIDATION_LEDGER.md` — public-safe ledger template for actionable
  technical findings, with allowed decisions (`ACCEPT_FIX`, `ACCEPT_CLARIFY`,
  `NEEDS_REPRO`, `DISPUTE_WITH_REASON`, `OUT_OF_SCOPE`, `KILL_OR_RESCOPE`).
- `papers/REVIEWABILITY_INDEX.md` — router for PC02 and PC11 validation packets.
- `papers/candidates/PC02_conditional_uniqueness/REVIEWABILITY_CHECKLIST.md` —
  PC02 audit path, falsification questions, and non-claims.
- PC02 and PC11 validation briefs replace communication/review labels.
- `docs/atlas/AUDITOR_GUIDE.md` replaces the previous reader-role guide.

The repo now tracks reviewability, falsifiability, and validation decisions. It
does not track specific people, private correspondence, private identity data,
or private logistics.

Ledger unchanged: 15 proven, 5 conditional, 9 open, 10 dead.

---

## 2026-05-30 — Falsifiability matrix and public-surface QA

**Closed the consolidation loop with explicit kill/rescope criteria; no claims changed.**

Added `papers/FALSIFIABILITY_MATRIX.md` as the next audit stop after
`CLAIMS.md` and `papers/REVIEWABILITY_INDEX.md`. It maps PC02, PC04, PC06,
PC07, and PC11 to:

- current status;
- claim boundary;
- missing object;
- reproduction or proof path;
- validation question;
- kill/rescope condition.

Added `papers/candidates/PC07_mobius_flow_potential/PAPER_CARD.md` because PC07
was listed in the registry but did not yet have a candidate card. The card keeps
P15/P16 as exact algebra and quarantines B6-B9 as a field-theory lift requiring
inserted kinetic/carrier/unit choices.

Added `tests/test_public_surface_scan.py` to lock the public documentation
surface against stale communication artifacts, email-shaped strings, reviewer
placeholder labels, and raw transcript markers.

Updated the validation router, paper registry, paper cards, and auditor guide to
point at the matrix before any status change. Ledger unchanged: 15 proven, 5
conditional, 9 open, 10 dead.

---

## 2026-05-29 — B25 Fibonacci spectrum anchor

**Curated finite-approximant probe; no claim promotion.**

Added `frontier/B25_fibonacci_spectrum_anchor/` as a controlled replacement for
the local exploratory spectrum scripts. The probe uses tridiagonal
diagonalization of finite Fibonacci Hamiltonian approximants at dimensionless
`lambda/h=1` with `h=1`, not brute-force random energy sampling.

- Gap-labeling control: largest finite-approximant gaps match Fibonacci
  gap-label residuals below `5e-4` in the default run. This validates the
  implementation against known Fibonacci-Hamiltonian mathematics; it is not
  claimed as new.
- Dimension control: reports mid/wide/late finite-approximant box-counting
  slopes. The mid-scale slope is near `0.75`, but the result is explicitly not
  promoted to an exact Hausdorff dimension. Window sensitivity and finite-size
  saturation are part of the output.
- Bridge status: `I0=(lambda/h)^2/4`, so `lambda/h=1` gives `I0=1/4`. This is
  the same invariant surface used in the figure-eight trace-map normalization,
  but B18 functoriality holds for all invariant surfaces. The status of
  `lambda/h=1` is therefore **MOTIVATED**, not derived.
- Verdict: `STALLED` at deriving the coupling. If `lambda/h=1` is accepted as an
  additional motivated input, the spectrum is a useful empirical/numerical
  anchor. Without a derivation, it is not a falsifiable prediction of the core.

No claims changed.

---

## 2026-05-29 — B17-B24 half-step kernel campaign

**Executed in modified dependency order; no claim promotion.**

Added B17-B24 on branch `explore/trace-map-character-variety`, following the
half-step kernel thesis:

```text
exchange/half-step symmetry -> trace lift -> recursive A-sector
```

- **B18 first:** the trace map is the functorial half-trace lift of
  `F: a->ab, b->a`; `T_F^2` is the `A=F^2` trace lift. This passes the
  canonicality gate but remains `STALLED` at the physical/semantic dictionary.
- **B19:** plain exchange/order-conjugacy are too weak; adding `X^2=I`, or
  using the operational half-step condition `(L X)^2=A`, isolates `P` up to
  sign in bounded exact `GL(2,Z)` search. Generic orientation-reversing
  involution and time reversal are too weak.
- **B17:** same-record repetition stays parabolic; original A1-A6 filters
  already select `LR/RL`; `LPLP=A` is a half-step refactorization, not a new
  uniqueness theorem without the half-step condition.
- **B22:** the `-1` parity sector is generic for orientation-reversing
  symmetric-square lifts; the special object is the `A` quadratic sector
  (`det=-1`, `trace=+/-1`), not parity alone.
- **B20:** operational invariant-memory and feedback are present, but the trace
  map does not explicitly read `I`; awareness/self-model language remains
  quarantined.
- **B21:** the half-step trace map is anti-Poisson for the
  Goldman/Weil-Petersson bracket and `T^2` is Poisson; this gives a natural
  character-variety symplectic structure, not spacetime.
- **B23:** the perturbation map near `(1,1,1)` has unique nonlinear term
  `2uw`; no BKL/Misner variable dictionary is derived.
- **B24:** `SU(2)_3` is compatible because `2cos(pi/(k+2))=phi` only at `k=3`,
  but the level-selection rule remains inserted.

All new probes are frontier-only and end `STALLED`. No claims changed.

---

## 2026-06-01 — B48 / PC12 metallic SL(3) trace-map intake

**Curated side-work intake; no claim promotion.**

Integrated the reproducible mathematical payload of the private SL3 metallic
trace-map work as a governed repository artifact:

- **B48 `SL(3)` metallic trace maps:** adds a sanitized certificate probe for
  the family `phi_m(a)=a^m b, phi_m(b)=a`, extending B27's `m=1` Fibonacci lift
  to all `m>=1`. The probe checks the trace-map recurrence, direct exact
  `SL(3,Z)` matrix traces, entropy recurrences, fixed-line Jacobian blocks,
  integer splitting classification, and compact `SU(3)` diagonal-slice
  representatives.
- **PC12 paper candidate:** adds `Metallic SL(3) Trace-Map Arithmetic` as a
  standalone `NEEDS_VALIDATION` candidate. It supports the trace-map ecosystem
  but does not change PC11's `T1 -> S1 -> I=1/4 -> lambda/h=1` conditional
  status.
- **Governance boundary:** raw side-work bundles, coordination artifacts, and
  private working notes were not copied. The public repo records only distilled
  B48/PC12 material plus a private-source checksum in the artifact manifest.

New strategic insight: B27 was not an isolated `m=1` accident; the higher-rank
trace-lift route has a systematic metallic family with its own commutator
invariants, entropy, and arithmetic fixed-line structure. The missing selector
for PC11 remains missing. The next useful path is proof hardening: convert the
certificate-assisted PC12 splitting classification into a compact reviewable
proof architecture.

---

## 2026-06-01 — B49 PC12 proof-hardening

**Proof architecture extracted; no claim promotion.**

Added `frontier/B49_sl3_certificate_proof_hardening/` to decompose the PC12
fixed-line integer splitting classification into reviewable proof modules:

- universal discriminant/parity splitting criterion;
- direct positive families and isolated negative split cases;
- square-gap propagation lemma;
- finite positive-strip exclusions for `4 <= c <= 14`;
- negative strip and boundary exclusions for `-11 <= c <= -2`.

The B49 probe checks the finite proof tables and recurrence propagation
mechanism against the B48 arithmetic. This strengthens PC12 by narrowing the
remaining task from "trust a broad certificate scan" to "write polished proof
text, especially for global coefficient-positivity exclusions." PC12 stays
`NEEDS_VALIDATION`; no Origin-core claim changes.

---

## 2026-06-01 — B50 PC12 proof-draft assembly

**Internal theorem-note skeleton; no public draft.**

Added `papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE_SKELETON.md`
and `frontier/B50_pc12_proof_draft_assembly/` to organize B48/B49 into five
theorem blocks:

- metallic `SL(3)` trace-map formula;
- commutator trace-pair invariant;
- algebraic entropy;
- fixed-line integer splitting classification;
- compact diagonal `SU(3)` slice.

The skeleton records proof status for each block, required reproduction
commands, and non-claim boundaries. It makes PC12 structurally ready for proof
drafting, but not `DRAFTABLE`: global `c>=15` / `c<=-12` exclusions, entropy
no-cancellation prose, literature positioning, and compact `SU(3)` wording still
need validation.

---

## 2026-06-01 — B51 symbolic-m factorization and B52 bridge control

**PC12 proof strengthened; naive physics bridge ruled out.**

Integrated the cross-platform review packet into governed repo evidence:

- **B51 `SL(3)` symbolic-`m` factorization:** the `c=3` fixed-line Jacobian
  block factorization is now verified with `m` formal, not only checked over
  bounded integer values. At `c=3`, the Cayley-Hamilton derivative recurrence
  has characteristic equation `(r-1)^3=0`, giving polynomial derivative rows in
  `k`. The symbolic `8x8` Jacobian commutes with the exchange involution and
  block diagonalizes into symmetric and antisymmetric sectors with characteristic
  polynomials `(t-1)(t+1)(t^2-(m^2+2)t+1)` and
  `(t^2+mt-1)(t^2-(m^3+3m)t-1)`.
- **B52 multichannel Fibonacci bridge control:** the simplest three-channel
  Fibonacci tight-binding model was tested directly. Its site transfer matrices
  are `6x6` determinant-one symplectic matrices on doubled phase space. In the
  commuting control they decompose into three independent `SL(2)` channels. In
  the generic control the PC12 third-order `SL(3)` trace recursion fails, while
  the expected order-six Cayley-Hamilton recursion holds.
- **Literature scan:** scalar and Jacobi Fibonacci Hamiltonian work remains
  `SL(2)`/trace-map spectral theory; matrix-valued or multichannel models use
  doubled `2L x 2L` transfer matrices. No source found in this scan supplies the
  PC12 `SL(3)` physical dictionary.

Net result: PC12 is stronger as standalone trace-map mathematics, but the
physics bridge remains missing. The naive multichannel bridge is now a recorded
negative result rather than an open ambiguity. No claims promoted; PC12 remains
`NEEDS_VALIDATION`.

---

## 2026-06-01 — B53 literature screen, B54 general-c structure, PC12 rescale, E21 quarantine

**Curated cross-session intake; no claim promotion.**

- **B53 literature screen** (`papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md`):
  classified PC12's blocks against the `SL(3,C)` character-variety and
  substitution-trace-map literature. Verdict: Thm 1-3, the exchange
  decomposition, and the symbolic-`m` factorization are `STANDARD_REPACKAGE`
  (Lawton minimal `SL(3,C)` coordinates; Baake-Grimm-Roberts substitution trace
  maps; Bellon-Viallet algebraic entropy = log of the metallic-mean Perron
  root); only the fixed-line integer splitting (Thm 4) is `APPARENTLY_NEW`, and
  it is elementary. PC12 rescaled `THEOREM_NOTE` -> `COMPUTATIONAL_REPORT`; still
  `NEEDS_VALIDATION`. This is a screening pass, not specialist review.
- **B54 general-c exchange structure** (`frontier/B54_general_c_exchange_structure/`):
  proves `[J(m,c),P]=0` for symbolic `c` (m=1,2,3), generalizing B51's `c=3`
  block-diagonalization to the whole fixed line; the reason is structural
  (`P`-equivariance at the `P`-invariant fixed line). Records the `c=1` twin
  polynomials — symmetric Eisenstein `t^2-t+1`, antisymmetric golden `t^2-t-1`,
  discriminants -3 and 5, the same pair as the P12 figure-eight gluing equation —
  and the `m=1` cyclotomic sweep `Phi_3, Phi_4, Phi_6, (t-1)^2, char(A)` at
  `c=-1..3`. Locked by `tests/test_general_c_exchange_structure.py`. Standalone
  trace-map math; no claim promoted.
- **E21 self-evidencing closure quarantine** (`paths/E21_self_evidencing_closure/`):
  an ambitious cross-session framing mapped the trace-map coupling `lambda=m`
  onto a variational free energy. Verified the one exact fact (the half-return
  characteristic polynomial equals `char(M^2)` at `I=m^2/4`) and recorded that it
  is the single identity `4c^2-2=m^2+2`; `D(I)=(4I-m^2)^2` is a relabeled squared
  residual; the free-energy mapping is structural analogy, not derivation; no
  observable is predicted. Verdict `STALLED` (instantiates E18). Kept out of
  PC12. The first-order `SL(3)` bridge tautology is noted in
  `docs/atlas/FAILURE_ATLAS.md`.
- **Not imported:** an external 9-page draft (self-evidencing framing; its
  acknowledgments name AI platforms) was kept out of the repo pending a decision
  reconciling acknowledgments with the repository privacy rule.

Proven/conditional/open/dead ledger unchanged; no claim promoted.

---

## 2026-06-02 — PC02 draft-note reconciliation

**Editorial consolidation; no claim promotion.**

- Reconciled two parallel 2026-05-29 PC02 draft notes into one canonical
  `papers/candidates/PC02_conditional_uniqueness/DRAFT_NOTE.md`. Adopted the
  formal theorem-note structure from the unmerged `paper/pc02-draft-note` branch
  (numbered sections; axiom table A1-A7; mapping-torus torsion lemma via the Wang
  exact sequence; minimal-trace route; explicit Theorem + proof; the LR/RL
  based-invariant table; non-claims; review questions) in place of the earlier
  review-brief version. The half-step, trace-map, and conditional spectral-anchor
  (`T1 -> I=1/4 -> lambda/h=1`, C5) material is retained as an explicitly
  non-theorem Appendix A, with the Damanik-Gorodetski-Yessen citation
  (arXiv:1403.7823). Updated the reproduction counts to the current suite
  (83 passed, 1 skipped). PC02 stays `CONDITIONAL_THEOREM` / `NEEDS_VALIDATION`;
  this is editorial, not a status change. The superseded `paper/pc02-draft-note`
  branch can now be deleted.

---

## 2026-06-02 — B55 c=1 general-m structure, B56 figure-eight kill, B57 splitting classification

**Standalone trace-map math; no claim promotion.**

- **B55** (`frontier/B55_c1_fixed_line_structure/`): completes the c=1 fixed-line
  sector structure for general m. Symmetric sector is **mod 4** — `Φ₆` (m≡1,3),
  `Φ₄` (m≡2), degenerate `(t−1)²` (m≡0); antisymmetric is
  `(t−1)(t+1)(t²−mt−1) = char(M)` for all m. Proved per residue class (symbolic m)
  via the c=1 closed forms (roots `{1,i,−i}` + a resonant linear term in `x1,x4`),
  cross-checked m=1..12; m=1 reproduces B54's twins. This corrects the earlier
  "odd→Φ₆ / even→Φ₄" reading (m≡0 mod 4 degenerates, not Φ₄). Locked by
  `tests/test_c1_fixed_line_structure.py`.
- **B56** (`frontier/B56_figure_eight_invariant_surface/`): negative control. The
  diagonal SL(2,C) reps `w³−2w²−2w+1=(w+1)(w²−3w+1)`, roots `{−1,φ²,φ⁻²}`, give
  Fricke–Vogt `I = 3w²−2w³−1 ∈ {4, −17/2 ± 7√5/2}`, none = `1/4`. The
  figure-eight ↔ `I=1/4` (self-evidencing) bridge is **DEAD**; the c=1 Eisenstein
  resemblance to the figure-eight tetrahedron shape (`z²−z+1`, complex, `Q(√−3)`)
  is a cyclotomic coincidence. Scope guard: the separate P12 gluing-equation
  discriminant echo `(−3, 5)` is unaffected. Locked by
  `tests/test_figure_eight_invariant_surface.py`.
- **B57** (`frontier/B57_general_m_splitting/`): classifies integer splitting of
  the antisymmetric quartic for m=1..6. `{c=1, c=3}` universal; m-dependent extras
  `m=1:{−11,−9}`, `m=2:{−3,−1}`, `m=3:{−3,0}`, `m=4:{−1}`, `m=5:{}`,
  `m=6:{−1,0,2}`; counts vary `[4,4,4,3,2,5]`. The Hilbert-class-field coincidence
  (`h(−15)=2` vs m=1) is killed for m≥2. Locked by
  `tests/test_general_m_splitting.py`.
- PC12 (a `COMPUTATIONAL_REPORT`) gains the general-m c=1 structure (B55) and the
  splitting classification (B57); B56 enters as an explicit boundary. The
  self-evidencing/FEP framing stays quarantined in `paths/E21`. Suite: 91 passed,
  1 skipped (83 prior + 8 new). No claim promoted; proven ledger unchanged.

---

## 2026-06-02 — E21 self-evidencing controls (Weil–Petersson identity, Aubry-duality kill)

**Quarantine controls; no claim promotion.**

Integrated two further session results into the E21 self-evidencing quarantine
(`paths/E21_self_evidencing_closure/`), both verified before integration:

- **Fisher information = Weil–Petersson coefficient (exact, elementary).**
  `F(m) = 16/(m²(m²+4)) = 16/disc(char(M²)) = 16·g_WP(m²+2) = (4/Δ_eig)²`, with
  `g_WP(α)=1/(α²−4)`. Exact (verified symbolically) but it is the chain rule on
  `LE(I)=arccosh(2I+1)` plus `disc(t²−αt+1)=α²−4=1/g_WP(α)`. The session itself
  flags the Weil–Petersson reading as possibly "just calculus"; recorded, **not
  promoted**.
- **Aubry self-duality at `λ=m` killed.** `λ=m` is the trivial fixed point of the
  duality map `λ→m²/λ`, so the apparent self-duality is vacuous; the off-diagonal
  m-metallic model has no genuine Aubry self-duality at `λ=m` for `m≥2` (session
  IPR test). No metal–insulator observable. Recorded in
  `docs/atlas/FAILURE_ATLAS.md`.

Both strengthen E21's `STALLED` verdict (one exact-but-elementary identity in
geometric dress; one dead physical reading). The E21 probe now carries 5 checks.
Kept out of PC12; no Origin-core claim changes; proven ledger unchanged.

---

## 2026-06-02 — Handoff triage; SL(n) factor-count tower recorded as a prediction

**No claim promotion.**

Triaged a pre-computed handoff of four items. Three were already integrated and
were **not** re-done (no duplication):

- Weil–Petersson identity — already integrated (E21, ledger V6, PR #11).
- Off-diagonal Aubry-duality kill — already integrated (E21, FAILURE_ATLAS,
  ledger V7, PR #11).
- c=1 mod-4 correction — already integrated as B55 (PR #10).

The one new item, the **SL(n) factor-count tower**, is recorded as an **untested
prediction** in `papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE_SKELETON.md`
("Open Prediction" section): at the identity representation, the rank-two
`SL(n,C)` Jacobian is conjectured to factor into a parity block plus
`(n²−1−parity)/2` degree-2 `char(M^k)` factors (`parity = 2` odd n, `1` even n).
Confirmed only at `n=2` (1 factor) and `n=3` (3 factors, powers {−1,2,3}); `n≥4`
(SL(4): 7 factors) is untested and requires building the `SL(4)` trace map — a
candidate future probe (B58+), explicitly not a claim. Proven ledger unchanged.

---

## 2026-06-02 — B58 SL(4) factor-count tower test (attempt; NEEDS-EXPERTISE)

**Frontier attempt; no claim promotion.**

Attempted the SL(n) tower prediction at `n=4` (`frontier/B58_sl4_tower_test/`).
Confirmed the mechanism — the SL(4) identity forward recursion is `(r-1)^4`, so
the fixed-line derivative sequences are cubic in `k` (degree `n-1`; SL(3) was
`(r-1)^3`/quadratic) — and the obstruction: the fixed-line point (all traces
`= n`) is the degenerate identity representation, where traces are second-order
(`d tr(W)=0`), so a representation-based numerical Jacobian cannot recover the
ambient fixed-line trace map that factors into `char(M^k)` (B54/B55). Testing the
7-factor prediction requires the ambient 15-coordinate SL(4,C) trace map (Procesi
generating set + substitution action via the SL(4) trace identities), not built
here. Verdict **NEEDS-EXPERTISE**: the `n=4` prediction is untested (neither
confirmed nor refuted) and stays a prediction in PC12. Locked by
`tests/test_sl4_tower_test.py`. Suite: 93 passed, 1 skipped. Proven ledger
unchanged.

---

## 2026-06-02 — B59 SL(4) fixed-line factorization (numerical; tower prediction refuted)

**Frontier evidence (numerical, method-validated); no claim promotion.**

Resolved the SL(4) tower prediction that B58 left as `NEEDS-EXPERTISE`, by a
method that sidesteps B58's obstruction: at a perturbed rep `A=exp(eps P)`,
`B=exp(eps Q)` the trace-coordinate differential is full rank, so the ambient
Jacobian `DT(eps)=D[tr W_i(AB,A)]·pinv(D[tr W_j(A,B)])` is computable, and
`x(eps)→(n,..,n)` as `eps→0`; extrapolating gives the fixed-line Jacobian. The
method reproduces B55's SL(3) `c=3` spectrum to ~4 digits (the credibility
anchor). The SL(4) (15×15) spectrum factors as

```text
char(M^-1) · char(M) · char(M^2) · char(M^3) · char(M^4) · char(-M^2) · (t-1)^2(t+1)
```

— five clean `char(M^k)` (`k=-1,1,2,3,4`; powers climb to 4), one sign sector
`char(-M^2)` (`-φ²,-φ⁻²`, no SL(3) analog), and a degree-3 parity block. This
**REFUTES** the naive "7 `char(M^k)` + 1 parity" prediction (actual:
`3 parity + 5 char(M^k) + 2 from char(-M^2)`). Numerical (~3-4 digits),
method-validated — **not a symbolic proof**; symbolic confirmation still needs
the ambient SL(4,C) trace ring (B58). PC12's "Open Prediction" updated to
`REFUTED`. Locked by `tests/test_sl4_factorization.py`. Suite: 95 passed, 1
skipped. Proven ledger unchanged.

## 2026-06-02 — B60 SL(n) tower: cross-n structure map (n=3,4) + SL(5) barrier

**Frontier evidence (numerical, method-validated for n=3,4); no claim promotion.**

Generalized the B59 extrapolation method to arbitrary `n` and built the corrected
cross-n structure map:

```text
n   char(M^k) powers      sign sectors   parity block          n^2-1 check
3   {-1, 2, 3}            none           (t-1)(t+1)   [deg 2]   2 + 3*2 = 8
4   {-1, 1, 2, 3, 4}      char(-M^2)     (t-1)^2(t+1) [deg 3]   3 + 5*2 + 2 = 15
```

From `n=3` to `n=4`: the `M`-powers climb and densify, a sign sector `char(-M^2)`
appears, and the parity block grows. This empirical map replaces the refuted
`(n^2-1-parity)/2` all-`char(M^k)` conjecture. Validated on SL(3) ground truth
(`max match 0.0000`); SL(4) reproduces B59 (`0.0101`).

**SL(5) is unresolved.** Its trace-coordinate differential has `cond ~1e11`,
beyond double-precision extrapolation; five attempts failed (finite-diff,
row-balanced, exact-diff at double precision; `mpmath` single-`eps` and multi-`eps`
normal-equations pinv, which squares the conditioning to `~1e22` and goes
numerically singular at `dps=45`). The barrier is documented as a reproducible
conditioning fact. The next step is a stable high-precision SVD-based pinv (with
multi-`eps` extrapolation) or the symbolic ambient SL(5,C) trace ring. Locked by
`tests/test_sln_tower.py`. Suite: 97 passed, 1 skipped. Proven ledger unchanged.

---

## 2026-06-02 — B61 SL(5) high-precision factorization (barrier re-diagnosed; 22/24 resolved)

**Frontier evidence (numerical, high-precision; method-validated on SL(3)/SL(4));
no claim promotion.**

Ported the method to `mpmath` (dps 60) with a stable SVD-based pseudoinverse
(`pinv` via the tall-orientation SVD, losing only `~log10(cond)` digits vs
`2 log10(cond)` for normal equations). Two findings:

1. **B60's "SL(5) conditioning wall" was a misdiagnosis.** At dps 60 the SVD
   shows the forward-only word set's 24th singular value is the dps zero-floor
   (`~1e-40`): it is **rank 23**, not 24. Double precision read the rounding floor
   as `cond ~1e11`. Switching to **inverse-word coordinates**
   (`A,B,A^-1,B^-1`, len `<=4`) gives a genuine rank-24 system at `cond ~1e4`.
   (Confirmed by a parallel computation; integrated here.)

2. **22 of 24 SL(5) multipliers resolve** to the Cayley-Hamilton catalog:

   ```text
   char(M^-1)·char(M)^2·char(M^2)·char(M^3)·char(M^4)·char(M^5)
            ·char(-M^2)·char(-M^3)·(t-1)^2(t+1)^2          [22 of 24]
   ```

   The n=5 tower row: powers climb to 5, sign sectors `-2,-3`, parity deg 4.
   SL(3)/SL(4) reproduce to `~4e-14`/`~3e-9` (vs B60's `~1e-3` double floor).

The remaining **2-dimensional sector is a method limit**, not a numerical
artifact: it ties to the directions where `Dx` loses rank at the fixed line
(the `(r-1)^n` degeneracy), where `pinv` is discontinuous, so the `eps->0` limit
is **gauge-dependent** -- the residual scatters across seeds (verified
20/22/24/26/28). Stable across extrapolation degree 5-9 and integer/half-integer
power bases; `cond` at the relevant `eps` is only `~1e6-1e8` (trivial at dps 60).
SL(3) (8/8) and SL(4) (15/15) had no such residual; `n=5` is where this
representation-perturbation method first runs out. The last 2 need the symbolic
ambient SL(5,C) trace ring (still open, cf. B58). Locked by
`tests/test_b61_sl5.py`. Proven ledger unchanged.

---

## 2026-06-02 — PC12 made review-ready for an external specialist

**Packaging / governance; no claim promotion.**

With the SL(n) line in good shape, prepared PC12 (metallic `SL(3)` trace maps)
for an outside specialist read — the project's standing single-highest-value
move. PC12 already had a thorough literature screen, validation brief, and
skeleton, but lacked the review packet and checklist that PC02 has.

**Done:**

- **Polished, self-contained `DRAFT_NOTE.md`** built from the skeleton: setup +
  Lawton coordinates; Thm 1-3 and the exchange-sector factorization stated with
  citations (Lawton; Horowitz; Procesi; Baake-Grimm-Roberts; Bellon-Viallet) and
  not re-proved; the apparently-new fixed-line integer-splitting classification
  (Section 6); the compact `SU(3)` slice; and the numerical cross-n tower
  (B59/B60/B61) as a clearly-labeled Appendix A. Pure computational mathematics —
  no project, physics, or foundational framing (reads cold for a specialist).
- **`REVIEW_PACKET.md` + `REVIEWABILITY_CHECKLIST.md`** mirroring PC02, with the
  five sharpened questions (Q1 Sec-6 novelty; Q2 sector factorization vs BGR;
  Q3 cross-n tower derivability; Q4 the SL(5) rank-loss obstruction; Q5
  terminology).
- **Bounded literature refresh** (web): confirmed the 2026-06-01 screen, added
  the algebraic-entropy = spectral-radius citation (arXiv:0812.0853) directly
  supporting the entropy value, and found no prior art for the Sec-6 splitting or
  the cross-n tower. Folded into `LITERATURE_POSITIONING.md`,
  `VALIDATION_BRIEF.md`, and `REVIEWABILITY_INDEX.md`.
- **Status:** `PAPER_CARD` readiness `NEEDS_VALIDATION -> READY_FOR_REVIEW`
  (specialist read pending); ledger row **V12**. The actual specialist read is
  the user's hand-off and remains the open step. Suite unchanged: 102 passed,
  1 skipped. Proven ledger unchanged.

---

## 2026-06-02 — B62 opposition involution: the 2 unresolved SL(5) modes

**Frontier evidence (exact root-system structure; validated on SL(3)/SL(4);
numerically corroborated); recorded as a live structural result; no claim
promotion.**

Tested a falsifiable prediction for B61's 2 unresolved SL(5) fixed-line modes.

- **The numerics genuinely cannot decide them.** Re-verified: `tr(DT0)` and
  `det(DT0)` from the B61 representation-perturbation method scatter across seeds
  (tr = 22.8 / 20.8 / 14.5; det complex, varying). The 2-mode block's spectral
  invariants are gauge-dependent, so no flavor of that numerics resolves them.
- **The opposition involution does.** Identifying the exchange involution
  (`tr W <-> tr W^-1`) with the opposition involution `theta = -w0` on the
  `sl(n)` root system, the `theta`-eigenspace split on the height-2 root space is
  exact (pure root-system combinatorics): `(+1,-1)` dims are `(2,0)` for `n=3`,
  `(2,2)` for `n=4`, `(4,2)` for `n=5`. The first two reproduce the known SL(3)
  (`char(M^2)`) and SL(4) (`char(M^2).char(-M^2)`) towers exactly; SL(5) is
  `char(M^2)^2 . char(-M^2)`. Since B61 resolved 4 of those 6 dimensions as
  `char(M^2).char(-M^2)`, the **2 unresolved modes are a second `char(M^2)`**:
  eigenvalues `phi^2 = 2.618...` and `1/phi^2 = 0.382...` (sum +3, product +1).
  Corroborated: the gauge-perturbed residual modes are positive (seed 20:
  ~2.89, ~0.90), ruling out the negative-rooted `char(-M^2)`.

This completes the SL(5) fixed-line row (22 numerical + 2 structural):
`char(M^-1) char(M)^2 char(M^2)^2 char(M^3) char(M^4) char(M^5) char(-M^2)
char(-M^3) (t-1)^2(t+1)^2`. Recorded as a **live structural result** -- the split
is exact and validated, but a symbolic proof of the height decomposition needs
the ambient SL(5,C) trace ring (B58's open task). Locked by
`tests/test_b62_opposition_involution.py` (suite 107 passed, 1 skipped). Proven
ledger unchanged.

---

## 2026-06-02 — B63 SL(4) fixed-line factorization over Z[m] (computer-assisted)

**Frontier evidence (computer-assisted symbolic: high-precision multi-m numerics
+ exact polynomial interpolation); validated vs B59 at m=1; no claim promotion.**

Targeted B58's open task -- build the symbolic SL(4) Procesi trace ring -- and
report two things honestly.

- **The hand-built trace ring is harder than "one depth level deeper."** SL(3)'s
  coordinates all have single-block substitution images `tr(A^k B^±)` (B54). SL(4)
  needs `e_2(A)`, and there is no single-block-only coordinate system: it forces
  either the 6-dim exterior-square representation `Lambda^2 V` (depth-6 recursion,
  chain rule through `e_i(Lambda^2 A)(e(A))`) or genuine two-/three-block words
  `tr((A^m B)^2 A)=tr(A^{m+1}B A^m B)`. That multi-block Procesi machinery is the
  real reason B58 is open. Documented, not built.
- **The result is established by a reliable computer-assisted route.** SL(4) has
  no fixed-line rank-loss (unlike SL(5); B61/B62), so the rep-perturbation
  Jacobian is clean at high precision for every `m`. Computing the 15 multipliers
  for `m=1..6`, extracting each factor's eigenvalue sum (= exact integer
  `tr(M^k)`), and interpolating it as a polynomial in `m` gives, over `Z[m]`:

  ```text
  char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1)
  L_2=m^2+2,  L_3=m^3+3m,  L_4=m^4+4m^2+2,  L_{±1}=±m
  ```

  PROVING (a) the SL(4) factorization over `Z[m]` (stronger than B59's m=1) and
  (b) that the M-power set `{-1,1,2,3,4}`, the sign sector `{-M^2}`, and the
  parity block are **m-independent** (only `L_k(m)` moves). m=1 reproduces B59
  (max-match `3.4e-7`). The explicit `k(alpha)` root map is supplied structurally
  by B62; the from-first-principles trace-ring proof (and symbolic `n>=5`) remain
  open. Locked by `tests/test_b63_sl4_symbolic_m.py`. Proven core P1-P16
  unchanged.

---

## 2026-06-02 — B64 parity mechanism: proof of the tower's k(α) sector assignment

**Frontier evidence (exact symbolic algebra; SL(3) full, SL(4) sector
assignment); no claim promotion.**

Recorded and proved the structural mechanism behind B62's opposition-involution
identification. `M=[[m,1],[1,0]]`, `L_k=tr(M^k)`. At the fixed line the trace-map
Jacobian commutes with the exchange involution `P` (B54), so it block-diagonalizes
into P-symmetric/antisymmetric sectors. Three facts fix the assignment:

1. depth-n Cayley-Hamilton ⇒ `J(m)` entries are polynomials in `m` (derivative
   sequences `∂τ_k/∂x_j` polynomial in `k`, evaluated at `k=m,m±1,…`);
2. `P` = contragredient (`A↔A^-1`) sends `φ_m → φ_{-m}`, i.e. `m → -m`;
3. Dickson parity `L_k(-m) = (-1)^k L_k(m)`.

⇒ the symmetric sector char poly is **even in `m`**, the antisymmetric carries
the **odd-in-`m`** content; so **`char(M^k)` with even `|k|` is P-symmetric, odd
`|k|` P-antisymmetric** — the root-height split.

- **SL(3), full symbolic `m`:** the depth-3 derivative sequences give
  symmetric = `(t-1)(t+1)char(M^2)` (even in `m`, `k=2`), antisymmetric =
  `char(M^-1)char(M^3)` (`k=-1,3`) — exact identities.
- **SL(4):** the mechanism splits B63's factorization into P-symmetric
  `{M^2,M^4,-M^2}` (even `|k|`) and P-antisymmetric `{M^-1,M,M^3}` (odd `|k|`),
  verified by Dickson parity. The depth-4 derivative sequences are built (seed
  degree 3 "cubic" + forced degree 4).
- **Obstruction localized:** a full symbolic SL(4) Jacobian needs more than the
  fundamental rep at exactly one place — `e_2 = tr(A^2)`, whose image
  `tr((A^m B)^2) = (tr A^m B)^2 - 2 tr(Λ^2(A^m B))` needs the single-block
  `Λ^2 V` (6-dim, depth-6). That is the even-`k` sector and the residual core of
  B58.

Net: the tower's structural theory now has which factors (B59-B62), which sector
each lives in (B64, proven `k(α)`), and the `m`-dependence `L_k=tr(M^k)` (B63);
one from-first-principles symbolic proof for all `n` (the `Λ^2`/multi-block trace
ring, B58) remains. Locked by `tests/test_b64_parity_mechanism.py`. Proven core
P1-P16 unchanged.

---

## 2026-06-02 — B65 symbolic SL(4) Jacobian J(m), char poly factored over Z[m]

**Frontier evidence (computer-assisted entries + exact symbolic factorization);
no claim promotion.**

Closed the SL(4) symbolic factorization by the entry-interpolation route (chosen
over the hand-built trace ring after a rank check showed single-block V+`Lambda^2`
traces span only **12 of 15** dimensions — genuine mixed two-block words are
unavoidable, sharpening B64's even-k/`Lambda^2` obstruction).

- The fixed-line Jacobian entries in the B59 word basis are **canonical
  (seed-independent) rationals of degree 4 in m** (verified seed-independent to
  extrapolation precision).
- Computed `DT(0)` at high precision (mpmath dps 50, tight eps-ladder; SL(4) is
  gauge-clean) for `m=1..7`, reconstructed each entry as an exact rational
  (worst error ~7e-5 at m=7), and interpolated to degree-4 polynomials in m,
  **over-determined** (degree 4 fixed by 5 points, verified on 7). This fixes
  `J(m)` rigorously (`jacobian_m.json`).
- `sympy.factor(char(J(m)))` over `Z[m]` gives, exactly:

  ```text
  char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1)
  ```

  Matches B63/B64; `m=1` reproduces B59.

This is the SL(4) factorization as a **direct symbolic factorization of the full
Jacobian** — factorization derived, not matched (the strongest form). Honest
status: computer-assisted in the entry determination (high-precision numerics +
exact over-determined reconstruction); the factorization is exact symbolic
algebra. The purist from-first-principles Procesi trace ring (B58; the mixed
two-block machinery) remains the open item. Locked by
`tests/test_b65_sl4_symbolic_jacobian.py`. Proven core P1-P16 unchanged.

---

## 2026-06-02 — B66 SL(6) numerical tower: the |k|=3 multiplicity test (= 2)

**Frontier evidence (numerical, high-precision); no claim promotion.**

Computed the `n=6` row of the metallic fixed-line tower (35-dim SL(6,C) character
variety) by the inverse-word method (B61), to settle the tower's open
multiplicity formula: does the odd-`k`, degree-`d=3` factor multiplicity follow
`max(n-d,1)` (=> 3 at n=6) or saturate at 2? SL(6) is the smallest `n` where the
two predictions differ — SL(5) gives `max(5-3,1)=2`, already equal to the
alternative.

**Result.** The opposition-involution theta-split sector structure is exact:
9 odd-k + 6 even-k quadratics + 5 parity = 35 (`sector_prediction`; validated
SL(3)=8, SL(4)=15, SL(5)=24). The numerics resolve the |k|=3 region cleanly —
all four roots of `char(M^3)`={4.236,-0.236} and `char(-M^3)`={-4.236,0.236} land
on the catalog (dist <= 4e-4), exactly TWO quadratics. The only extra big-root
mode (-4.434, dist 0.198) has no small-root partner, so it is gauge-corrupted, not
a third factor. Hence **|k|=3 multiplicity = 2, the same as SL(5) — it does NOT
grow with `n`, refuting `max(n-d,1)`.**

**Honest limit.** The SL(6) fixed-line rank-loss is far more severe than SL(5)'s:
26/35 multipliers resolve, 9 are gauge-corrupted (3 complex-conjugate pairs + 3
real outliers — the B62 trivial-rep mechanism amplified from SL(5)'s 2 modes). The
full 15-quadratic profile is therefore not completely determined, but the |k|=3
quadratics have moderate roots, resolve cleanly, and number 2 — which is the test.
A symbolic proof for `n>=5` still needs the ambient SL(n,C) Procesi trace ring
(B58, open). Ledger V17. Structure locked by `tests/test_b66_sl6_tower.py`;
spectrum reproduced by `frontier/B66_sl6_tower/probe.py` (~30 min). Proven core
P1-P16 unchanged.

---

## 2026-06-02 — Tower verification pass: SL(2) parity correction + B66 relabel

**Verification prompted by review; corrections, no result change.**

Re-verified the trace-map tower and caught two issues (Ledger V18).

**(1) SL(2)/n=2 parity correction.** The identity-fixed-point trace-map Jacobian
for `SL(2)` factors as `(t+1)·char(M^2)` for ALL `m` (verified symbolically:
coords `x=trA, y=trB, z=trAB`, `p_k=tr(A^k B)` with `p_k=x p_{k-1}-p_{k-2}`,
substitution `A->A^m B, B->A`). The parity eigenvalue is `det(M) = -1`, so the
parity factor is `(t+1)`, **not** `(t-1)`. Confirmed three ways: the direct
Jacobian, `det(M)=-1`, and the `Sym^2(F)` decomposition (eigenvalues `phi^2`,
`phi*psi=-1`, `psi^2` — the `-1` is the cross-term `det(M)`). The `DRAFT_NOTE.md`
cross-`n` tower table had listed the `n=2` parity block as `none` (under-counting
the 3-dim variety by the degree-1 factor); corrected to `(t+1)`. (B33's probe
already had `(t+1)(t^2-3t+1)`.)

**(2) Dickson backbone, independent confirmation through `L_8`.**
`char(-M^k) = char(M^{-k})` iff `k` is odd (true k=1,3,5,7; false k=2,4,6,8), and
`L_k(-m) = (-1)^k L_k(m)` — an independent instance of the B64 parity mechanism.

**(3) B66 labeling clarified.** `sector_prediction` bins quadratics by root-HEIGHT
parity; this equals the `char(M^k)` |k|-parity count only for ODD `n`. At even `n`
they differ (SL(4): height `(4,2)` vs |k|-parity `(3,3)`), because `|k|` runs past
the maximal root height, so a `char(M^even)` factor lands in an odd-height space.
So the B66 "9 odd-k + 6 even-k" is a root-HEIGHT count, relabeled "odd/even-height"
in the B66 docs and Ledger V17. The B66 `|k|=3 multiplicity = 2` result comes from
direct root-matching and is unaffected; the `35` total is unchanged.

All three facts locked in `tests/test_b66_sl6_tower.py` (now 11 tests). Proven core
P1-P16 unchanged.

---

## 2026-06-02 — B66 validation campaign: mult(|k|=3)=2 stress-tested four ways

**Validation prompted by review; the B66 result holds. Numerical, no claim change.**

Four independent checks of the B66 key result (mult(|k|=3) = 2 for SL(6), so
`max(n-d,1)=3` is refuted). Ledger V19; report in
`frontier/B66_sl6_tower/VALIDATION.md`; scripts `validate.py`, `second_m.py`,
`gauge.py`.

**1. Identical pipeline on SL(3..6)** (`validate.py`). The same pipeline (automatic
QR-pivot inverse-word selection -> `DT(eps)=DX.pinv(Dx)` extrapolation -> Dickson
identification) gives mult(|k|=3) = **1, 1, 2, 2**. SL(5)=2 is recovered under the
*same* gauge-handling SL(6) uses (the load-bearing check), with auto-selected words
(a word-set change from the hardcoded `SL6_WORDS`).

**2. Second/third m** (`second_m.py`). m=2 and m=3 both give mult 2, with the |k|=3
big root tracking `L_3(m)` (14.0710678 = 7+sqrt(50); 36.0277564 = 18+sqrt(327)) --
not a golden-ratio coincidence at m=1.

**3. Gauge subspace** (`gauge.py`). Computing the 35x35 Jacobian at two base points
(seeds 20, 24): the |k|=3 eigenvalues are seed-STABLE (1e-7..1e-4) and
well-conditioned (kappa 15-108), while the 8 gauge modes SCATTER across base points
(up to 3.8, several going complex<->real). mult=2 on the clean complement. (Two
metrics in the first pass were the wrong tools -- an orthogonal "overlap" is
meaningless for a non-normal matrix; replaced by eigenvalue condition number, and
seed-stability is the decisive discriminator.)

**4. Exact-over-Q (honest negative).** The numerical Jacobian is NOT canonical
(`||dt0(seed20)-dt0(seed24)|| ~ 7e3`; the pinv amplifies error without bound in the
gauge directions), so there is no exact rational matrix to reconstruct -- unlike
gauge-clean SL(4) (B65). The intrinsic character-variety Jacobian is canonical, but
computing it exactly is the ambient SL(6,C) Procesi trace ring -- B58, still open.

**Net:** mult(|k|=3) = 2 is robust across 2 word sets x 2 seeds x 3 m values, and
the method exactly recovers the proven SL(3)/SL(4) (B63/B65) and SL(5) tower. The
from-first-principles exact proof for n>=5 remains B58. Validation machinery locked
in `tests/test_b66_sl6_tower.py` (now 13 tests; suite 131 passed). Proven core
P1-P16 unchanged.

---

## 2026-06-02 — B67: figure-eight A-polynomial from the trace-map fixed-point set

**Frontier evidence (exact derivation); cross-validation, no claim promotion.**

Derived the figure-eight knot's A-polynomial -- a published invariant of algebraic
topology (Cooper-Long 1996) -- **exactly** from the metallic SL(2,C) trace map's
fixed-point set. Ledger V20; report in `frontier/B67_figure_eight_apolynomial/`.

**Setup.** The figure-eight complement is the once-punctured-torus bundle with
monodromy `phi = [[2,1],[1,1]] = M^2` (Fibonacci-squared), realized on `F_2=<a,b>`
by `phi(a)=a^2 b, phi(b)=ab`; its SL(2,C) trace map is `T_1^2(x,y,z)=(xz-y, z,
xz^2-x-yz)`. A fiber representation extends over the bundle iff its character is a
**fixed point of `T_1^2`** (then it is conjugate to its phi-image, so a monodromy `t`
exists) -- so the trace-map fixed locus `y=z=x/(x-1)` IS the A-polynomial curve.

**Computation.** At each fixed point: explicit `A=[[x,-1],[1,0]]`,
`B=[[0,b],[-1/b,x/(x-1)]]` (`b+1/b=x/(x-1)`); solve the linear system
`tAt^-1=A^2B, tBt^-1=AB` for `t in SL(2,C)` (1-dim null space; `t` unique up to sign;
monodromy verified to ~1e-15). Meridian `M=eig(t)`, longitude `L=eig[B,A]` (fiber
boundary = Seifert/0-framed longitude). Then `tr(t)^2=(x^2+x-1)/(x-1)` (confirmed to
50 digits at seven x) and `kappa=tr[A,B]=(x^4-3x^3+x^2+4x-2)/(x-1)^2`, giving the
**meridian<->longitude trace identity** `kappa = tr(t)^4 - 5 tr(t)^2 + 2`. Eliminating
`x` in eigenvalue coordinates yields, exactly,

    A(M,L) = M^4 L^2 + (-M^8 + M^6 + 2M^4 + M^2 - 1) L + M^4    (= Cooper-Long 1996).

`derived - Cooper-Long = 0` (literal equality). The raw eliminant is `A_CL^2` (a
quadratic-in-`x` parametrization squares it); the squarefree part is the A-polynomial.

**Significance.** First derivation of the figure-eight A-polynomial from a trace-map
computation -- an independent cross-check connecting the SL(n) trace-map tower
(B59-B66) to A-polynomials / character-variety knot invariants. The natural next step
is **SL(3)**: the SL(3) figure-eight A-polynomial (Garoufalidis-Thurston-Zickert 2011,
via ideal triangulations) from the SL(3) trace map -- open, not attempted. Locked by
`tests/test_b67_figure_eight_apolynomial.py` (suite 136 passed). Proven core P1-P16
unchanged.

---

## 2026-06-03 — Closing the exploratory phase: B58 Stage 1 + overnight consolidation

**Consolidation commit. Honest history: a corrected misconception is recorded, not deleted.**

**Corrected misconception (Ledger V21).** A scoping guess that the cotangent dimension is
`3n^2-10n+11` (=8,19,36) and the excess `2(n-2)(n-3)` (=0,4,12) was **never validated and is
REFUTED** by the Đoković cross-check; kept visible so it is not re-derived. The cotangent
spectrum (`d-sigma` on `m/m^2` of the two-traceless-matrix trace algebra, computed modular over
F_p, prime-stable over 3 primes) is the genuine Teranishi/Đoković minimal-generator spectrum:
**9** (n=3 = Teranishi 11 GL − 2), **30** (n=4 = Đoković, exact per-degree distribution
3,4,6,2,4,2,4,4,1), and **>= 111** (n=5, PARTIAL lower bound at deg<=11, single prime, K=1100 --
NOT a validated count). Excess = cotangent − `(n^2-1)` Jacobian = **1, 15, >= 87**.

**Cotangent route to `a_d`: CLOSED** (FAILURE_ATLAS). The excess is the *secondary* trace
invariants (n=3: `det[X,Y] = tr([X,Y]^3)/3`, sigma-eigenvalue −1; n=4: high-degree Đoković
generators); primary-vs-secondary is module/syzygy structure, not sigma-weight, so no degree or
factor rule separates the Jacobian primaries from the cotangent. Sharp at n=3: the tower's `(t+1)`
and the excess's `(t+1)` share one 2-dim sigma-eigenspace. **B58 Step 2** killed the
symmetric-power shortcut from the multiplicity side too (`sl(n)=+Sym^{2k}`: bare = even-only
overshoot, coupled = odd-only; neither = tower; B64's parity split is a sorting, not a formula).
Net: `a_d` needs the exterior-power Cayley-Hamilton hand proof (B58 proper).

**Overnight consolidation (Ledger V22/V23).** Job 1 time-reversal promoted as a Dickson-parity
COROLLARY (`charpoly(J^-1)=charpoly(J)` under even-k fixed / odd-k `char(+M^k)<->char(-M^k)`;
"arrow of time" is a label only). Job 4 SL(7): CONSTRAINTS not conclusions (`char(M^3)=a_3=1` is
the positive-power multiplicity at n=7, not total mult(3); `char(M^2)=3` weak; sign sector/`b_3`
unreached; INCONCLUSIVE). Job 2 SL(3) A-poly: NO-GO (principal Sym^2 is the wrong component;
geometric one is boundary-unipotent = the GTZ target). Job 3 cross-m m=2: census **m136**, B67
framing does not transfer (residual ~6e-3), left OPEN. Job 5: correctly skipped. Job 6 AJ: NOT
promoted, shelved in frontier (order-2 recursion match is below B67's exact-identity bar; q=1
limit unresolved). Literature review folded in (`frontier/literature_search.md`: principal-SL(2),
adjoint Reidemeister torsion, Kozai's fibered-3-manifold reducible deformations).

**Forward guard:** no entropy/"spectral-weight" probe exists in the repo; if one is added later,
it computes `Σ|k|` spectral weight, NOT topological entropy (= `n·log mu`, linear) -- no `n^2`
scaling, no fixed "antisymmetric fraction" (those oscillate). **arXiv check:** 2603.00816
(Ishibashi-Mizuno) confirmed real; Kozai 1509.07487 and 2411.04431 pre-2026. Suite green; locked
by `tests/test_b58_stage1.py`. Proven core P1-P16 unchanged.

---

## 2026-06-03 — Punch-list closeout (post-reaudit) + tracked PC12-refresh deferral

Closed the consolidation+audit arc (REPO_STATE.md). Applied the three trivially-safe punch-list
items: (1) Ledger **V15 (B64)** status requalified `PROVEN (symbolic)` ->
`PROVEN (symbolic, SL(3)); SECTOR-ASSIGNMENT (SL(4)); STRUCTURAL MECHANISM (general n)` to match
the honest B64 README (full SL(3) symbolic proof; SL(4) sector-assignment; general-n is the
mechanism -- not "general-n settled"). (2) `CLAIMS.md` date refreshed to 2026-06-03 with a note
that the proven core P1-P16 is unchanged through all B58-B68 frontier work. (3) `CLAIMS.md`
P7/P9 provenance footnote added (P7 sympy-verified-exact; P9 SnapPy/census + literature).

**TRACKED DEFERRAL (do BEFORE any external PC12 specialist hand-off):** the PC12 candidate docs
(`DRAFT_NOTE.md`, `PAPER_CARD.md`, `FALSIFIABILITY_MATRIX.md`, `LITERATURE_POSITIONING.md`)
predate B58/B66/B67 and do not mention the SL(6) multiplicity result (`|k|=3 = 2`, `max(n-d,1)`
refuted, B66), the figure-eight A-polynomial derived from the trace map (B67), or the
cotangent-route closure (B58). They are **stale, not contradictory.** Fold these into the
PC12 appendix/positioning before the specialist read. Deferred and tracked (also noted in
`papers/candidates/PC12_sl3_metallic_trace_maps/PAPER_CARD.md`). Proven core P1-P16 unchanged.

---

## 2026-06-04 — B58 Phase A consolidation: merge, honest relabel, candidate `a_d` pinned

Merged the Phase A branch (`frontier/b58-phaseA`) and consolidated the doc surfaces to the honest
current state. **No new research direction started — the strategic fork is held for human decision.**

**What Phase A established.** An EXACT `(n^2-1)` fixed-line Jacobian engine (eps-series dual numbers
over F_p; the least-squares form of B66's pinv limit) — VALIDATED at n=4 (reproduces B65's
`a_d=(1,1,1,1)` exactly, prime-stable). At n=5 it returns `a_2=1`, not the true 2.

**The exact-`Q` "fix" hypothesis was WRONG and is kept visible.** I had hypothesised the n=5
shortfall was finite-field non-canonicity, fixable over exact `Q` with `S=I`. Refuted: three
realizations — F_p random metric; F_p `S=I` prime-stable (`= Q` mod p); real positive-definite
mpmath — ALL give `a_2=1`. The cause is the pinv-limit CONSTRUCTION: the `eps->0` least-squares
limit is non-canonical at the degenerate `char(M^2)^2/(t+1)^2` collision, returning a defective
non-Dickson cubic `{-0.734,-0.734,2.695}`. **Headline: the pinv / ambient-Jacobian construction
(B59–B66 + this engine) UNDER-COUNTS degenerate multiplicities — wrong, not merely ceilinged, from
n=5 in every field/precision** (FAILURE_ATLAS sharpened; Ledger V24).

**B62 clarified (Ledger V25, `B62_STATUS.md`).** Not a theorem: State 3 for the full `a_d`, State 2
(verified candidate) for height-2 only. The θ-eigenspace dims are exact Lie theory; the unproven
step is the IDENTIFICATION with the Jacobian multiplicities (needs the ambient SL(n,C) trace ring,
B58 proper). B64 proved the SECTOR (SL(3)), not the COUNT.

**Candidate `a_d` formula recorded (Ledger V26, `CANDIDATE_A_D.md`).** θ-split extended to all
heights: `a_h=⌈(n-h)/2⌉`, `b_h=⌊(n-h)/2⌋` for `h=2..n-1`; plus an OBSERVED height-1/wrap piece
(`char(M^1)^{n-3}·char(M^-1)·char(M^n)`) and parity. Reproduces the n=3,4,5 towers EXACTLY
(integer-valid + dimension-sum `=n^2-1`, n=3..7). Three gaps: UNPROVEN (trace-ring identification),
INCOMPLETE (height-1/wrap + parity observed not derived), and one CONFLICT at its first new
prediction (below).

**`b_d` and `a_3(n=6)` downgraded to OPEN.** `b_d=[d<=n-2]` is an n<=5 match only — it diverges
from the θ-split at n=6 (`b_2`: 1 vs 2). `a_3(n=6)`: B66 numerical `1` is now understood as the
pinv under-count at a degenerate collision (V17 annotated); the candidate predicts `2`
(better-supported, NOT asserted). Both OPEN for n>=6.

**Strategic state (deferred, human decision).** The pinv / ambient-Jacobian route is EXHAUSTED as a
path to *degenerate* `a_d`. The B58 trace ring (structural form + identification proof) is the sole
remaining route that both computes degenerate `a_d` reliably and proves it. The fork — bank the
candidate + structural finding as a written result, vs commit to the multi-session B58 trace-ring
proof — is HELD. Proven core P1-P16 unchanged.

---

## 2026-06-04 — Phase 8: physics-paths sweep (robustly negative) + B68/B69/B70 + the trace-ring attack

After the B58 Phase-A consolidation, ran the deferred Phase-8 program: a systematic sweep of every
reachable physics anchor, the metallic A-polynomial family, and the trace-ring proof attack on `a_d`.
All exploratory, all banked with honest labels; proven core P1–P16 untouched. Ledger **V28–V42**.

**Physics-paths sweep — no crossing (V28–V39, `frontier/physics_probes/`).** The honest headline: the
framework produces real mathematics (low-dim topology / number theory / 1D condensed matter) but has
**no crossing into fundamental — or even new quantum — physics**; every reachable anchor is special to
`n=2`/`m=1` and does not generalize. The two genuinely-open real-physics targets are **closed
negative**: metallic anyons (V28 — `τ²=1+mτ` categorifiable only at `m=1`, Ostrik rank-2) and SL(n)
quasicrystal spectra (V29 — the **symplectic obstruction**: self-adjoint 1D transfer matrices are
`Sp(2p,R)`, and `SL(n)=Sp` only at `n=2`). The Chern–Simons/torsion family (V30) is genuine topology
with no clean pattern (corrected at the real geometric rep `κ=−2`: `τ₁=−3∈Q(√−3)`, `τ₂=−16`; trace
field degree 2→4→8); `τ_m` is identified (V31) as **Porti's adjoint Reidemeister torsion form**
(Fried–Milnor), the peripheral-deformation direction. The `j=1728` / CM-by-`Z[i]` spectral-curve
thread (V32–V34) and the emergent-geometry/area-law probes (V36/V37) are banked; the `m136`/`m=2`
A-polynomial framing is **RESOLVED** — the m=2 trace-map eliminant `M²L²−(M⁴−4M²+1)L+M²` IS the
census-m136 A-polynomial, confirmed both by holonomy-match (V32 Gate-0) and an independent from-scratch
null-space-dim-1 fit (V38, no Sage). See `PHYSICS_PROBES_SUMMARY.md`.

**B69 — metallic A-polynomial family + cusp-torsion law (V35/V39/V40).** The trace-relation curve
`F_m(x,κ)=0` (projection of the `T_m²` fixed locus) extends the figure-eight (m=1) to the metallic
family, VERIFIED m=1..4. **Cusp-torsion law:** cusps (poles of κ) at elliptic-torsion values
`x=2cos(π/k)`, `k∈{3..m+2}`, `k≡m (mod 2)`. Banked the "breakthrough-chat" handoff after independent
re-derivation + a line-by-line audit (caught a `κ`-sign diagnostic bug — the complete structure is
`κ=−2`, not `+2`). **Novelty check: STANDARD_REPACKAGE** — the cusp law is the known Baker–Petersen
ideal-point structure of once-punctured-torus bundles (arXiv:1211.4479), not new.

**B68 — AJ-conjecture probe (shelved, no claim).** The figure-eight colored Jones is q-holonomic with
minimal recursion order 2 (= the B67 A-polynomial's L-degree), annihilating `J_N` for `N=2..5`; but
the exact `recursion|_{q=1}=A` identity does not resolve (convention `M_rec=q^N=meridian²` +
ill-conditioned `q→1`), below B67's exact-identity bar. Order-match only.

**B70 — the trace-ring attack on `a_d` (Phase-8 Track A; V41/V42).** The candidate `a_d` formula
(B62 θ-split) is unproven; the proof needs the ambient SL(n,ℂ) trace ring, whose barrier is the
even-k / `e₂=tr(Λ²A)` sector carried by two-block words `tr(AᵃBAᵇB)`. On the proper traceless `sl(n)`
tangent (tracelessness by substitution after the products — the up-front projection blows up): the
**leading-order (ε²) Hessian** non-separable content is a *single* rank-1 coupling `a·b·tr(X²)`, pinned
exactly to `e₂` (identity `e₂-Hessian=−tr(X²)/2`; verified SL(4),SL(5), two words). But across the
**full ε-series** the two-index content grows (ε³→(2,1), ε⁴→(3,1)/(2,2), …), so a single generator
does **not** close the sector — it is a *finite* multi-generator set bounded by `c=n` nilpotency at
bidegree `≤(3,3)`. NET: the long-standing two-block barrier is now a **precise, finite, bounded**
structure — the genuine content a first-principles closure must assemble. Computer-assisted structural
characterization, **not PROVEN**. The `SL(3)` GTZ A-polynomial (Track B) is the deferred
more-tractable follow-on. Proven core P1–P16 unchanged.

---

## 2026-06-05 — open-paths sweep (V43–V52) + the comprehensive Paths A–F mandate (V53–V59)

Two governed exploration runs, all banked + merged; proven core P1–P16 untouched and test-locked
(suite **179 passed, 1 skipped**); `EXPERT_OUTREACH.md` dormant.

**Open-paths sweep (V43–V52).** B71 the SL(3) figure-eight A-variety from the trace map — `Fix(T_1²)`
= exactly 3 components (matches Heusener–Muñoz–Porti / Falbel); Dehn-filling `W1=D2→M³=L`,
`W2=D3→M³L=1`; the geometric `V0` has no tidy A-variety form (Falbel 141-poly). Plus P1 Dehn-filling
exact (50-digit), P3 m=2 framing = m136, P4 SL(4) rank-independent meridian `μ=A⁻¹t`, P5 trace-ring
scoped to the pinv-limit, P6 AJ bounded-negative.

**Comprehensive Paths A–F mandate (V53–V59)** — the two prizes plus a fully-labeled speculative tail:
- **A (V54, B73) — degree=rank tower law.** On the SL(n) figure-eight bundle's principal Dehn-filling
  component `{tr A=tr A⁻¹=1}` the longitude is the meridian's `n`-th power, `Mⁿ=L`. Confirmed at SL(4)
  (`M⁴=L`, ~1e-39); SL(2) degenerate (no such component); a 2nd SL(4) component gives `M³=L`. With
  SL(3) (V47) the law holds at `n=3,4`. high-precision-numerical.
- **D (V55, B70) — the symbolic-m ε-series pinv-limit construction** is BUILT and reproduces the SL(3)
  tower from first principles (resolves the V51 stall; e₂ closure automatic via n×n matrix arithmetic).
  The SL(4) build at L=12 over ℚ is the heavy open continuation (→ the a_d proof at n=4). computer-assisted.
- **B (V53) — j=1728** re-examined: isolated + silver-mean-forced, no Coulomb family; **confirms** the
  V34 kill with explicit `j(a)`.
- **C (V56, B74) — higher-spin/W_N.** The parity grading is a LITERAL shared object (both the W_N
  charge-conjugation grading and the Dickson P-grading are `−w0` of `A_{n−1}` on a degree-`k` invariant);
  the full spectrum diverges; the dynamical reading is SPECULATIVE-ANALOGY.
- **F1 (V57, B75) — the m-axis of degree=rank.** Odd metallic bundles `m=1` and `m=3` both give `M³=L`
  at `n=3` (convention-independent test `eig[A,B]=eig(t)ⁿ`); degree=rank is a two-parameter `(m,n)`
  rank invariant. Open: even-m spectrum (cusp parity), rank-4 metallic corner. high-precision-numerical.
- **F2/F3 (V58, B76).** `2cos(π/k)=[2]_q` ⇒ the cusp `k`-set = the SU(2)_{k−2} root-of-unity level set
  (closes B69's reconciliation); no categorical family lift (V28) ⇒ anyonic-TQFT reading SPECULATIVE-
  ANALOGY. F3 (parity × CS) subsumed by V56.
- **E (V59, B68) — AJ retry** with the smarter Habiro + `|q|=1` per-q null-space route: no clean
  recursion at accessible order/degree, **confirming** the V52 bounded negative (literature theorem).

Honest headline: the mathematics is real (degree=rank, the tower factorization, the figure-eight
A-polynomial connection); every physics bridge returned negative. The two real open continuations both
need the SL(4) ambient trace ring: the symbolic-m SL(4) Jacobian (D → a_d proof) and the rank-4 / even-m
degree=rank corners (A/F1).

---

## 2026-06-05 — follow-on + unification + "Complete the Tower" runs (V60–V74)

Three governed exploration runs were banked since V59 (full per-stage detail in
`frontier/REPO_STATE.md` update blocks and `papers/VALIDATION_LEDGER.md` V60–V74; proven core P1–P16
untouched throughout; `EXPERT_OUTREACH.md` dormant/uncommitted; physics chapter CLOSED).

**Follow-on (V60–V65) and unification push (V66–V69)** — headline: **B80/V62** proved the **SL(4)
metallic tower from first principles** (CRT/F_p symbolic-m Jacobian, resolving the B70 stall); **B83/V66**
established the **`Aₙ` family `L=(−1)ⁿ⁻¹Mⁿ`** with the SL(4) A-polynomial `L=−M⁴` NEW; **B84/B85** localized
the SL(5)+ tower gap to one symbolic `e₂/Λ²` (Procesi) step (numerics + `Λ²V` shortcuts both dead). See
REPO_STATE for the per-stage breakdown.

**"Complete the Tower" run (V70–V74)** — the CC-web verification-chat handoff reconciled against `main`
(most of it predated V60–V69) and the genuine open prizes executed. Suite **220 passed, 1 skip**.

- **B87/V70 — m=3 genus (Task 3).** Spectral sequence `3,1,…`, m=2 a minimum (the `3,1,0` reading
  refuted); m=3 trace-relation curve genus 1 (`disc₃=(x²−x−1)(5x²−5x−1)`).
- **B88/V71 — SL(4) census (Task 2).** Two clean Dehn-filling components → **degrees {3,4}** at rank 4;
  the degree is the robust invariant.
- **B89/V72 — `M⁴=L` PROVED symbolic-exact (Task 1a).** Over ℚ(ω): eliminate `B` → one matrix equation;
  `A³=I` → a 10-equation exact ideal; the rank-drop locus `t11=ω·t22` → an explicit 4-parameter family
  on which `[A,B]·det(t)²=−det(t)·μ⁴` is a pure polynomial identity. (Trap: generic gauge slice is
  `det t≡0`/vacuous.) Upgrades V54.
- **B89-T/V73 — tower cohomological route CLOSED (Task T).** `H¹(F₂;ad ρ)` at the trivial-rep fixed line
  gives `char(M)^{n²−1}≠tower` (a 3rd dead shortcut after B84/B85). Advance: all-n tower = explicit
  two-sequence **Sym product** (symbolic-in-m, proved n≤4), reduced to one module-iso; `a₃(n=6)=2`.
- **B90/V74 — degree=rank uniform peripheral reduction (Task 1b).** **Lemma 1 PROVED uniform**
  (`λ=μX⁻¹μY⁻¹`, `XμX⁻¹=μA`, from the bundle relations); degree=rank reduced to one collapse-lemma,
  exponent = rank from A's degree-n Cayley–Hamilton; proved n≤4.

**Honest headline:** `M⁴=L` is now PROVED symbolic-exact at SL(4); both flagships (the tower, degree=rank)
are reduced to a single clean lemma each with the n≤4 cases proved; the cohomological route to the tower
is closed. Open: Task 6 (genus-2 generality). The mathematics is real; no physics reopened.

---

## 2026-06-06 — the V75 audit + Paper 0 (the self-reference grounding)

**The V75 audit (2026-06-05).** A CC-web verification chat audited the B87–B90 arc; three decisive checks
corrected the record. B90's L1a is a **tautology** (holds on random non-bundle `(A,t)`); B90's
"exponent = rank from Cayley–Hamilton" is **refuted** by the hinge test (both SL(4) Dehn-filling
components satisfy L1b but give exponents 4 vs 3); only **L1b** `XμX⁻¹=μA` is genuine. B89-T strengthened
with a cross-check confirming its Sym product equals B80's actual symbolic `J(m)` at n=4. degree=rank
stands PROVED at n=3,4 only; uniform-n is open. (Methodology banked: never override an expected/symbolic
result with numerics alone; don't count tautologies toward a reduction; run the decisive gate first.)

**Paper 0 (2026-06-06, V76–V78).** A new foundational thread: characterize the metallic family by a
*condition*, `m` free, rather than choosing the seed. Motivation **quarantined** in
`paths/philosophical/METALLIC_FOUNDATIONS.md` (never a premise/claim). Suite **230 passed, 1 skip**;
physics closed; P1–P16 untouched.

- **B92/V76 — Layer 1 (`proven`).** Dominant eigenvalue purely-periodic-period-1 **⟺ det=−1** (all 66
  matrices with entries ≤5) = the family `{M_m}` up to `GL(2,ℤ)` conjugacy, `m` free. Three equivalent
  forms; MyCalc-2 (CF-period a conjugacy invariant); refinement (a) (the naive premises admit det=+1);
  MyCalc-5 (systole — `m=1` minimal → the member is contingent on a metric).
- **B93/V77 — Phase C.** MyCalc-1 (`det=−1 ⟺` a negative eigenvalue ⟺ the `char(−Nᵏ)` parity sectors);
  MyCalc-4 (parity `m→−m` ≠ Galois `√→−√` — the CPT is the contragredient, not Galois; corrects Idea-4).
- **B94/V78 — G1 (the decisive gate).** Squaring the proved metallic Jacobian to a det=+1 monodromy:
  `char(J²)` factors **exactly** over the catalog `char(Nᵏ)` (universal) with **no** sign sectors and no
  `(t+1)` ⇒ **"universal catalog, det=−1 parity"** — `det=−1` is structurally distinguished. G3:
  degree=rank is det-agnostic (figure-eight is det=+1, B89) ⇒ two problems, not one.

**Honest headline:** Layer 1 is proven; `det=−1` is shown to be exactly the tower's parity condition; the
universality question is decided. OPEN: the Lawvere/renormalization fixed-point attempt (L2), literature
grounding (G2/G4), and the Paper 0 write-up.

---

## 2026-06-06 — Task M: the degree=rank mechanism (V79) + the §1–§3 cleanup pass

**Task M (B95/V79).** The V75 audit killed "exponent = Cayley–Hamilton degree"; B95 finds what the
exponent reads. The principal spectrum is **forced** by `tr A = tr A⁻¹ = 1` (eig 1 at mult n−2): `{1,i,−i}`
(n=3), `{1,1,ω,ω²}` (n=4), `{1,1,1,−1,−1}` (n=5), **impossible at n≥6**. At n=5 it has `A²=I` ⟹ `A,B`
involutions ⟹ `⟨A,B⟩` dihedral ⟹ **reducible** (no irreducible SL(5) principal rep — upgrades B78's
numerical limit to a structural reason). So **"exponent = rank" is an n∈{3,4} phenomenon**; the mechanism
reads whether the cusp's forced finite-order spectrum admits an irreducible rep — explaining the n≥5 wall
on both the tower and degree=rank. Corrects the handoff's SL(5) guess.

**Cleanup pass (CC-web audit).** §1: corrected B94's "Cayley–Hamilton" overclaim for catalog universality
to the **Sym-plethysm** (proven metallic / rigorous squares / confirmed non-square n=2 / open non-metallic
n≥3), and locked the n=2 non-square datum (`sl2_nonsquare_check.py`). §2: de-hardcoded four `/Users/dri`
absolute paths (B77/B79/B83/B88) to `Path(__file__)`-relative imports + a guard test. §3: diagnosed the
B71 sym2-shadow test's cross-environment failure as a **sort-before-rotate** fragility (the SVD/det
cube-root branch is platform-dependent); fixed the comparison to sort-after-rotate (tolerance unchanged).

---

## 2026-06-06 — geometry-invariants + literature-bridge pass (V80–V84); physics quarantined

**Mandate (CC-web handoffs).** "Compute the numbers, quarantine the interpretation." Bounded
quantum-topology invariants on the metallic mapping-torus manifolds (the SQUARE monodromy `M_m²`:
`m=1`→`4_1`, `m=2`→`m136`, `m=3`→`s464`), banked as mathematics; **every** physics reading lives only in
`paths/philosophical/PHYSICS_RESONANCES.md` (`SPECULATION`, never promoted). Physics chapter stays
**CLOSED**; proven core P1–P16 untouched; suite **249 passed, 1 skip**.

**B96/V80 — geometry invariants.** Metallic volumes strictly monotone (`2.030<3.664<4.814`; `m=1`=systole,
each cross-checked by the Bloch–Wigner dilog). The decisive Hessian computation: the complete structure is
a strict volume **maximum** (155/156 fillings of `4_1` below `V₀`, 0 above) ⟹ the Neumann–Zagier volume
Hessian is **definite `(0,2)`, NOT Lorentzian** — the most-leveraged "physics path" (CC-web Path 1) returns
negative. `|τ₃|` left open (branch-ambiguous; from-scratch 1-loop did not calibrate to `τ₁=−3,τ₂=−16`).

**B97/V81 — where the Lorentzian structure lives.** The `(2,1)` Lorentzian form is **located** as the
`so(2,1)=sl(2,ℝ)` Killing form on the **SL(2,ℝ)/Teichmüller** component (the gauge algebra of *toy* 2+1
gravity), not the SL(2,ℂ) geometric side (B96, Euclidean) — structural, present by construction, **not
emergent**; the 3+1 wall untouched. So CC-web's "Lorentzian emergence" resolves to a precise deflated
yes-and-no, quarantined in PHYSICS_RESONANCES.md (Path 1).

**B98/V82 — the trace-map Jacobian at the GEOMETRIC rep (Probe 1).** The single most important untested
computation: the tower (B89-T) is computed at the *trivial* fixed line (all traces `=n`), where Task T
degenerated; the published bridges (3d-3d; Daly arXiv:2411.04431) live at the *geometric* rep. Result
(exact SL(2)): on V0, `char(D T₁²)=(t−1)(t²−c(x)t+1)`, `c(x)=(2x²−x+1)/(x−1)`; the parabolic-puncture
fixed point `x²−3x+3=0` (the figure-eight trace field `ℚ(√−3)`) gives `c=5` and the transverse pair's
adjoint Reidemeister torsion `2−c=−3=τ₁`. So the **tower does NOT appear at the geometric rep — it is a
trivial-rep phenomenon**; the geometric rep carries the torsion/twisted-Alexander object (*consistent with*
Daly, cited, not claimed). Probe 5b: the tower ≠ the Kostant principal-`sl(2)` even-only branching.

**B99/V83 — the SL(3) geometric Jacobian (Probe 1c).** The SL(3) geometric rep (`Sym²` on V0) gives 2
eigenvalue-1's (tangent V0) + 3 transverse reciprocal pairs, sums `c∈{5, 4.5±4.664 i}`; the `c=5` pair is
the SL(2) torsion pair carried up by `Sym²`. **NOT** the trivial-point SL(3) tower (real `{−1,3,4}`) — the
geometric rep is the torsion side at SL(3) too.

**B100/V84 — literature cross-checks (Probes 2+6).** The Zickert/SnapPy **Ptolemy variety** of `4_1`
(`N=3`): 2 obstruction classes + 6 boundary-unipotent SL(3,ℂ) reps in the trivial class — the 0-dim slice
of B71's components, cross-validated from an **independent code path**. The **Baker–Petersen**
(arXiv:1211.4479) twisted Alexander **is** the B98/B99 geometric Jacobian `t²−5t+1`; the canonical
component (trace coords, genus 0) and the A-poly spectral curve (genus 3) are different curves. Two
published frameworks **agree** with the B71/B98/B99 picture (methods cited, not claimed).

**Net.** No new path to physics; the chapter stays CLOSED, now reinforced by decisive computation (B96).
The genuine value is mathematical: the volume ordering, and the located distinction between the two
trace-map fixed points (trivial→tower; geometric→adjoint torsion/twisted Alexander), which explains the
Task-T degeneration and cross-validates against Zickert/GGZ/Baker–Petersen/Daly.

---

## 2026-06-06 — the Hitchin-component reframing (V85); physics firewalled

**Handoff (CC-web).** "The Hitchin-component reframing": verify two grounding computations (verify-don't-
trust), land the **mathematics**, **firewall** the physics, and bank the "tower of spacetimes" reading as a
**dead** negative. Both appendix scripts re-derived independently before landing (the ladder: Lorentzian
only at `k=2`, split-form pattern; the V0 certificate: unique `SO(2,1)` form, signature `(2,1)`, Anosov
hallmark, elliptic control complex). Suite **256 passed, 1 skip**; proven core P1–P16 untouched; physics
chapter stays CLOSED.

**B101/V85.** The geometric component **V0** (B71 — `Sym²` of the Fuchsian `SL(2,ℝ)` rep) **is the Fuchsian
locus of the Hitchin / Fock–Goncharov positive component of the `SL(3,ℝ)` character variety** of the
once-punctured torus (the principal embedding `PSL(2,ℝ)→SL(3,ℝ)` *is* `Sym²`). Four results:
- **R1** (`STRUCTURAL`+`computer-assisted`): the Anosov hallmark (every non-peripheral word loxodromic,
  cusp `[a,b]` unipotent, elliptic control complex) + the unique `SO(2,1)` invariant form, signature
  `(2,1)` — the rigorous backbone of B97, now placed inside the Hitchin component. Cite Hitchin 1992,
  Labourie, Fock–Goncharov, Choi–Goldman, Marquis.
- **R2** (`dead`, first-class negative): the symmetric-space ladder — the principal `SL(2)` (`Symᵏ`) lands
  in **split real forms** (`Sp(k+1,ℝ)` odd, `SO(p,p±1)` even); **Lorentzian only at `k=2` (`SO(2,1)`) and
  it does not climb** (k=4→SO(3,2), k=6→SO(4,3), …). No "tower of spacetimes up the ranks"; the
  phase-space-dimension "3+1D at SL(3)" idea is structurally void (recorded `docs/atlas/FAILURE_ATLAS.md`
  with two companion dead heuristics: the Goldman metric is `(2,0)` Riemannian; the Hessian/Fisher-on-`k`
  forms are definite, not spacetime).
- **R3** (`computer-assisted`): under the principal `sl(2)`, `sl(3)=V₂⊕V₄` (weights `{±4,±2,±2,0,0}`; dims
  3,5; differential degrees 2 quadratic, 3 **cubic**); **V0 = the `{cubic=0}` slice**.
- **R4** (the genuinely-new computation; user opted in to attempt it now): (a) `H¹(F₂,sl(3)_Ad)=8` splits
  **exactly** under the principal `sl(2)` into `3` (V₂/Teichmüller, tangent V0) ⊕ `5` (V₄/cubic,
  transverse), verified at 2 Fuchsian seeds; (b) an explicit real family `ρ_t=exp(t·u)Sym²`, `u∈V₄`, at 2
  Fuchsian seeds × 2 cubic directions, **stays Anosov, leaves V0** (`|x1−x4|`>0), and **breaks the
  `SO(2,1)` form** (nulldim 0). Honest scope: an unconstrained cubic deformation also moves the puncture
  holonomy off unipotent (fixing the boundary is a codim constraint, deferred to the verification chat's
  parallel work — reconcile when it lands).

**Firewall.** Only `PHYSICS_RESONANCES.md` carries interpretation: Path 1 updated with the ladder
spacetime-tower kill; new **Path 7** cites the Hitchin→Higgs→geometric-Langlands→N=4 SYM chain
(Kapustin–Witten) **with the ceiling stated** — even total success reaches `N=4` super-Yang–Mills, one
superconformal gauge theory, *not* the Standard Model / gravity / "the universe"; never a claim, never
promoted. No §8-forbidden wording in any math artifact. (Note: the `dead` reading was never a `CLAIMS.md`
claim, so it is recorded in the failure atlas, not as an `ARCHIVE.md` D-row whose IDs match `CLAIMS.md`.)

---

## 2026-06-06 — the W1/W2 dichotomy + the R4 boundary-controlled cubic continuation (V86)

**Handoff (CC-web, from the verification chat after reading the B101/B100 report).** Two follow-ons: the
deferred R4 continuation (a cusp-controlled cubic family) and an independent resolution of the B71 W1/W2
question. **Verify-don't-trust applied to both appendix scripts before landing.** No physics (pure
character-variety / higher-Teichmüller geometry). Suite **263 passed, 1 skip**; P1–P16 untouched.

**B102/V86 — the W1/W2 dichotomy (D1–D4, SOLID; reproduces).**
- **D1:** Cayley–Hamilton on the figure-eight `T₁²` forces every irreducible `Fix(T₁²)` SL(3) character to
  satisfy `(trA−trA⁻¹)(trB−1)=0` and `(trA−trA⁻¹)(trB⁻¹−1)=0` ⇒ Case I (`trA=trA⁻¹`, self-dual) or the
  `trB=trB⁻¹=1` branch; **0 "neither"** (census; exact on B71's V0/W1/W2).
- **D2/D3:** mapping onto B71's *realized* components — **W1=(1,q,q,1,p,1,1,p) ⇒ `ρ(a)` eigenvalues
  `{1,i,−i}`** (order-4 elliptic), **W2=(p,1,1,q,1,q,p,1) ⇒ `ρ(b)` elliptic** (order-independent on the
  realized reps); the **geometric V0** point is self-dual with `tr(AB)` a root of `t²−t+7` (`Q(√−3)`; the
  whole rep is in `Q(√−3)`). **Verdict:** all SL(3) figure-eight components are excluded from the real
  `SL(3,ℝ)` Hitchin component — V0's geometric rep by **complexity**, the genuine W1/W2 by **ellipticity**
  (an elliptic generator on the unit circle is not loxodromic ⇒ fails Labourie); ellipticity is the cleaner
  obstruction. **Refinements to the handoff:** W1 carries the obstruction on `A`, W2 on `B` (the A/B
  partners); `Q(√−3)` is the geometric *point*, not all of Case I (a 2-parameter family).
- **D4:** the `{1,i,−i}` elliptic spectrum **is** Task M's forced `n=3` spectrum (B95) — the same arithmetic
  object disqualifies W1/W2 from the Hitchin component.

**B102/V86 — the R4 continuation (D5; robust mechanism, headline NOT reproduced).** Imposing `tr δC=0`,
`tr C δC=0` (`C=ρ([a,b])`) cuts the `V₄⊕V₄` (dim 10) cubic directions to a **9-dim relative family** that
keeps the cusp regular-unipotent **to first order** (`δe₁=δe₂=0`). **Honest finding:** this is first-order
only — at second order the cusp splits by cube roots into one real + a complex pair, so a generic
relative-family ray complexifies the cusp immediately (~78% complex at `t=0.05`). The handoff's clean
`(λ,1,1/λ)` geodesic boundary with `Im=0` throughout and a cusp-collision wall at **`t*≈3.775`** **does not
reproduce** (the literal `rel[:,0]` here goes complex near `t=0`, re-realifies to *negative* eigenvalues by
`t≈0.4`, and is solidly 3-real — not collided — at `t=3.775`; `t*≈3.775` is a non-reproducible SVD-basis
artifact). So the boundary control is first-order only; the strict unipotent-cusp-preserving (finite-area
FG-positive) continuation **remains `open`**. Reconciles with B101 R4(b): the unconstrained version moved the
cusp off-unipotent at first order; the relative family delays that to second order but does not eliminate it.

Cite Heusener–Muñoz–Porti, Labourie, Hitchin/Fock–Goncharov/Goldman/Marquis. (The B100 Probe-2 Ptolemy reps
would be the literal-figure-eight cross-check, route a, but reconstructing fiber matrices from Ptolemy
coordinates is reconstruction-heavy; route b — classifying B71's *realized* W1/W2/V0 — is the airtight
in-house equivalent and is what we ran.)

---

## 2026-06-07 — the SL(n) tower as a GL(2,ℤ) representation (V87); a fourth route

**Goal (user): "prove the uniform-n tower."** The central open conjecture `char(J(m))=∏_d char(Sym^d M_m)`,
proved `n≤4` (B80), reduced (B89-T) to the module-iso (M). Three routes had died (cohomological B89-T;
numerical-pinv B84; Λ² B85). This session opened a **fourth route** and merged two converging CC-web handoffs
("Task A — plethysm-universality at n=3" and "the Dehn-Twist Route to the all-n tower"). Verify-don't-trust
applied to every load-bearing fact. Suite **269 passed, 1 skip**; P1–P16 untouched; no physics.

**The idea.** Near the trivial rep `A=exp X, B=exp Y`, the metallic monodromy linearizes to
`(X,Y)↦M_m(X,Y)`; more elementarily, **`J_φ(n)` factors through the abelianization `N∈GL(2,ℤ)`** (inner autos
act trivially on traces). So `ρ_n: N↦J(n)` is a `GL(2,ℤ)`-representation and `char(J)` is a **class function
= the catalog** — universality is structural and identical for metallic and non-metallic monodromies.

**B103/V87 — what was proved.**
- **Route 1 (universality, all n):** verified at SL(3) with the exact **Lawton** trace maps of the Dehn
  twists (`U:a→a,b→ab`; `L:a→ab,b→b`; `S:a↔b`): the MCG relations `S²=I, SUS=L, SLS=U` **lift** to the 8×8
  Jacobians; `J(3)` is **constant on each abelianization class** (21 multi-word classes); the **det-sign
  parity law** (`k=2,3` always; `k=1` sector `char(±N)` by `det N`; parity `(t∓1)`) holds on metallic
  (`det−1`) **and** non-metallic (`det+1`, e.g. `N=[[3,2],[1,1]]=U²L`). Sharpens B94 (the two-sheeted
  structure is det-determined, not metallic-specific).
- **Route 2 (the explicit rep; n=3,4 EXACT over ℚ[m]):** an explicit **`m`-independent invertible `P`** with
  `P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}` (`μ_d=[2≤d≤n]+[0≤d≤n−3]`), intertwiner dim `=Σμ_d²` (Schur: 3 at n=3,
  5 at n=4). n=3 via the exact Lawton `J(m)` (word `Uᵐ S`, abelianization `M_m`, interpolated); n=4 via
  **B80's** proved exact `J(m)`. So `char(J)=∏char(Sym^d M_m)^{μ_d}` = the explicit catalog, and the
  `char(−M^k)` sign sectors are the `det(M_m)=−1` twists. This realizes the module-iso **(M)** — B89-T's lone
  open item — **constructively and exactly for n=3,4**, engine-free.

**The reframing (records the consequence).** The all-n tower question becomes **"decompose the `GL(2,ℤ)`-rep
`ρ_n` into `Sym^d` pieces."** Universality is structural (Route 1, all n); the open content is the explicit
catalog `μ_d` — proved n=3,4 (Route 2), structural n=5 (B62), open n≥5 (the Procesi wall). The Dehn-twist
composition computes `char(ρ_n)` **without** the Procesi ring (the B85 wall) — the natural continuation
(B104: the SL(4) elementary maps + non-metallic universality + the SL(5) attempt).

**Method note (this session).** The earlier eps-series F_p engine is gauge-corrupted at n≥5 (B61/B66) and
overshoots via the singular cotangent (m/m² dim 9 vs tower 8 at n=3); the **Lawton explicit trace maps** are
exact, engine-free, and give the clean `J(m)` directly — the right tool, and the basis for B104.

---

## 2026-06-07 — the Dehn-twist route: SL(4) universality + the SL(5) wall (V88)

**Handoff (CC-web): "the Dehn-Twist Route to the all-n tower"** — the natural continuation of B103, executed
in full (verify-don't-trust). Build any monodromy's trace map by composing the elementary Dehn-twist
substitutions `U,L,S` **inside the eps-series fixed-line construction** — *not* the full `(n²−1)`-coordinate
Procesi substitution `σ` (the B85 wall). Suite **274 passed, 1 skip**; P1–P16 untouched; no physics.

**B104/V88 — SL(4) (proven).** The generalized engine folds a word's twists on the dual-number pair
(`U:(P,Q)→(P,PQ)`, `L:(P,Q)→(PQ,Q)`, `S:(P,Q)→(Q,P)`) to give `J(word)` at the SL(4) trivial line.
- **GATE:** `['U','S']` (abelianization `M_1`) **reproduces B80's proved metallic SL(4) tower** mod p — the
  elementary maps are correct.
- **factor-through-N:** `char(J)` depends only on `N` (same-`N` words → identical `char(J)`).
- **non-metallic universality:** `char(J(N)) = ∏_d char(Sym^d N)^{μ_d}` (two-sequence `{0,1,2,3,4}`) with the
  **det-sign parity**, verified on metallic (`det −1`) **and genuine non-metallic** (`det +1`, e.g.
  `N=U²L=[[3,2],[1,1]]`, `N=[[5,3],[3,2]]`). So the explicit SL(4) catalog is a **computed theorem for all
  monodromies**, not a conjecture.

**B104/V88 — SL(5) (characterized wall).** The engine is consistent (returns a Jacobian) but
`char(J) ≠ catalog` (the two-sequence has `μ_2=2`, degree 24); `gcd(char(J), catalog)` has degree **21/24**
— **21 of 24 Dickson factors resolve, 3 corrupted** at the doubly-degenerate sector. This is exactly
B61/B66's gauge corruption: **the Dehn-twist composition does NOT bypass the eps-series gauge degeneracy.**
The wall is **computational** (the eps-series metric degeneracy at n≥5), characterized — **not** a failure of
the representation theory (universality is structural at all n, B103 Route 1, so `char(J_φ(5))` *is* the n=5
catalog; the eps-series simply cannot resolve 3 of its factors).

**Reframing (recorded).** The all-n tower = decompose the `GL(2,ℤ)`-rep `ρ_n`; the Dehn-twist composition
computes `char(ρ_n)` without the Procesi ring; the remaining n≥5 obstruction is now **isolated to the
eps-series doubly-degenerate sector** (a non-degenerate slice / inverse-word coordinates — B61's partial fix
— would close n=5 directly), not a structural gap. Cite B103, B80 (GATE), B61/B66 (the wall), Lawton/Procesi.

---

## 2026-06-07 — the n=5 wall characterized + the ρ_n convergence (V89)

**Handoff (CC-web): "the n=5 Resolution Attempt + Literature + Final Observations."** The single most
decisive remaining computation, plus literature positioning and the banking of the campaign's observations.
Verify-don't-trust. Suite **278 passed, 1 skip**; P1–P16 untouched; no physics (physical readings POSTULATED
+ quarantined).

**N5 — the decisive computation (B105/V89).** *Is the n≥5 tower degeneracy a coordinate artifact or a
structural change?* **VERDICT: coordinate artifact.** At SL(5) the Dehn-twist eps-series (B104) resolves
`gcd(char(J), two-seq catalog) = 21/24` Dickson factors. Three findings pin it: (1) the resolved 21 are
**universally catalog-consistent** (every monodromy, metallic + non-metallic, both det signs); (2) the
corrupted 3-dim factor is **gauge noise** — distinct across seeds while the resolved 21 are invariant (a
structural change would give a *fixed* wrong answer); (3) the eps-series ceiling is 21/24 over 20 seeds (cf.
B61's 22). Three independent structural routes (B89-T, B62, B103) agree the unresolved piece is `Sym²`.
**Conclusion (honest, strict bar):** "the formula changes at n=5" is **ruled out**; the catalog is strongly
supported; but the strict "all 3 resolved" bar is **not met** — the n=5 catalog stays formally `open`, the
obstruction pinned to the eps-series gauge-degeneracy at the cusp's repeated `−1` eigenvalue.

**H6 — the unified wall (structural).** The forced cusp spectra (B95) are `{1,i,−i}`/`{1,1,ω,ω²}`/
`{1,1,1,−1,−1}`; the **non-trivial eigenvalues are distinct at n=3,4 and collide at n=5** (`−1`, mult 2);
n≥6 has no finite-order spectrum. **One collision** is the common root cause of the tower wall, the
degree=rank wall (B95), and the eps-series rank-drop — so the **natural boundary is n=4**, proved structural.

**Convergence (the thesis).** Every positive result is a property of **one object `ρ_n`** — the `GL(2,ℤ)`-rep
on the SL(n) trace ring at the trivial point. Tower = `char(ρ_n)`; module-iso = its `Sym` decomposition;
universality = its well-definedness; Hitchin = its moduli embedding. `ρ_n` is **completely characterized for
n=3,4**, boundary at n=4 **proved**. One object, fully characterized in its natural range, boundary proved.

**Literature (cited).** L1 — Gang–Koh–Lee–Park arXiv:1305.0937 (3d theories for once-punctured-torus bundles
via 4d N=2* duality walls; **SL(2,ℂ) only** — our SL(3)/Dehn-filling/metallic data is *new within that
framework*). L4 — Bonahon–Dreyer arXiv:1209.3526 + Douglas–Sun arXiv:2011.01768 (FG coords / Hitchin
component for SL(3) on the once-punctured torus — consistent with B101 V0=FG-positive locus, B102 W1/W2
excluded). H1–H5 (computed elsewhere) + C1–C4 (corrections) tabulated by proof status in B105 FINDINGS.

---

## 2026-06-07 — B105 V90 audit: two inference downgrades (the n=5 verdict + the boundary)

**Handoff (CC verification chat): "Two corrections to B105."** The prior B105 entry (V89, above) overreached
on two *inferences* — banked here as **explicit downgrades**, not silent edits (the 21/24 computation and
the `ρ_n` thesis stand). Verify-don't-trust: Appendix A re-run + B84's own statement checked. Suite green.

**Correction A — the "gauge-noise ⟹ coordinate artifact, NOT a structural change" inference is INVALID
(withdrawn).** A rank-deficient eps-series `DX·pinv(dx)` (B84: `dx` rank-deficient at the unresolved sector;
FAILURE_ATLAS "fixed-line rank-loss makes the eps→0 pinv limit gauge-dependent") returns approach/seed-
dependent values *regardless of the true factorization*. Appendix A re-run confirms: the resolved sector
`[2,3,5,7]` is exact and seed-independent for a true value `d=11` *and* `d=99`, while the contested
eigenvalue is large seed-noise (range ~3800) whose spread is **identical** for `d=11` vs `d=99` — the true
88-unit difference is buried. So **seed-variation is uninformative about the truth** at the unresolved
sector. *Corrected:* the resolved 21 are universally catalog-consistent (real evidence); the 3 unresolved are
supported as `Sym²` by the **structural routes** (B62/B89-T/B103), *not* by the seed-variation; **a structural
deviation there is neither ruled in nor out** ⟹ the explicit **n=5 catalog is OPEN**.

**Correction B — "natural boundary at n=4, proved / complete at n=4" OVERSTATES (withdrawn).** B103's
factor-through-`N` makes `char(J(n)) =` the catalog a **class function for all `n`** — there is **no
mathematical boundary**. What walls is the explicit **computation** (eps-series pinv non-convergence, B84;
engine-free trace-ring non-closure) — a **methodological ceiling**, not a theorem. The forced-cusp collision
at n=5 (`−1` mult 2) is a genuine structural **observation** and a **candidate** common root cause, *not* a
proof that it causes the walls, and *not* a "natural boundary."

**The open frontier (restated — the live target).** Prove `char(ρ_n) =` the Dickson catalog **directly from
`ρ_n`** (B103) together with **B62's** multiplicities — *around* the σ-construction, never building it. That
would close n≥5 **by proof** and settle Correction A's open question. B105 sets up the `ρ_n` thesis but does
not attempt this proof — so it is the **open frontier**, not a closed result.

**What stays (sound).** The 21/24 universal resolution; the `ρ_n` convergence thesis (endorsed); the
forced-cusp-spectrum observation (as a structural fact / candidate root cause); the H/C ledger; the L1/L4
literature (spot-checked — GKLP 1305.0937, Bonahon–Dreyer 1209.3526, Douglas–Sun 2011.01768; IDs/authors
confirmed). **Paper 0 must use the corrected A/B statements** — "structure proven all-`n`; explicit catalog
through n=4 for all monodromies; explicit n≥5 OPEN, walled from two methods; one fully-characterized object
`ρ_n`" — *not* "complete at n=4 with a proved boundary." Banked as V90 (ledger), B105 probe `CORRECTIONS_V90`
+ FINDINGS banner + README + test reframed.

---

## 2026-06-07 — B105 V91: the three-obstacle / one-threshold correction + the sharpened ρ_n target

**Handoff (CC verification chat, Part A).** A *verified* correction to B105's convergence framing, banked as
an **explicit downgrade**. Verify-don't-trust: B95's `2cosθ=3−n` spectrum and B62's A₄ height-2 opposition
split re-derived. No physics; P1–P16 untouched; suite green.

**What B105 got right (kept).** The **tower wall and the eps-series rank-drop are genuinely one wall** — both
are B62's height-2 `char(M²)²` doubling (the multiplicity-2 eigenspace split is non-canonical, which is why
the eps-series can't resolve it). Merging those two was correct.

**The overreach (corrected).** B105 then folded the **degree=rank** wall into the same "one collision (the
repeated −1)." That conflates **three distinct obstacles** that merely share the n=5 threshold:
- **(i) degree=rank (B95):** `A`'s forced principal spectrum `2cosθ=3−n` reaches **`−1`** at n=5 (`A²=I`, a
  root of unity), degenerating the figure-eight relation `tAt⁻¹=A²B`.
- **(ii) tower / eps-series (B62):** the A₄ height-2 root space splits **(4,2)** under `θ=−w₀` (verified:
  positive-root split (2,1) → (4,2) over ±), giving **`char(M²)²`** with eigenvalue **`φ²=(3+√5)/2`**
  (golden; `char(M²)=t²−3t+1`) — pure root-system combinatorics, *no reference to `A`'s spectrum*.
- **(iii) trace-ring non-closure (engine-free):** the `n²−1` coords don't generate the SL(n) trace ring —
  purely algebraic, **onset n=4**, no eigenvalue degeneracy.
*Different eigenvalues (`−1` vs `φ²`), independent derivations (B95 vs B62), different onset (n=5 vs n=4).* So
"one collision" is a narrative over distinct mechanisms — **withdrawn**, replaced by "n=5 is a structural
threshold where several distinct `A_{n−1}` features degenerate together."

**The generative payoff — the `ρ_n` target, sharpened (A4).** The contested n=5 piece the catalog proof must
handle is **only** B62's height-2 `char(M²)²` multiplicity (which B62 already supplies structurally, via the
`θ=−w₀` `(+1,−1)` eigenspace dims on each height-`h` root space). So the live target becomes concrete: **prove
`char(ρ_n)=catalog` by showing the `ρ_n` decomposition reproduces the opposition-involution multiplicities,
directly from the `GL(2,ℤ)`-rep, without constructing σ.** The degree=rank `−1` (B95) and the trace-ring
non-closure are **separate problems the catalog proof need not touch** — a referee-defensible target.

**Scope hedge (A5).** "Explicit catalog through n=4 for all monodromies" now reads: n=3 genuine-non-metallic
both det signs verified (the 23-monodromy sweep); n=4 metallic proved (B80), non-metallic via the B104
eps-series (clean at n=4, B80-validated, not gauge-corrupted).

**Banked.** B105 probe `CORRECTIONS_V91` + `three_obstacle_distinction()` (verified) + FINDINGS banner + H6
reframe + a locking test; ledger **V91**; consolidation docs corrected. Standalone trace-map / Lie theory; no
`CLAIMS.md` promotion.

---

## 2026-06-07 — B106 hygiene (V93) + B107 physics-connection audit (V94, POSTULATED/FIREWALLED)

**B106 hygiene (V93).** A verify-don't-trust amendment to the just-merged B106 (Dehn-filling anatomy, V92).
**D1 gauge-noise gate:** the SL(4) Dehn-filling Jacobian is a `pinv` over QR-selected words at a
repeated-eigenvalue rep, so the B84 gate applies — `d1_neutral_eigenvalues_are_roots_of_unity()` recomputes
the neutral eigenvalues across ≥3 `realize` seeds and finds them *exactly* roots of unity and **seed-stable**
(principal `1,±i,−1`; secondary `1,ω,ω²`), so the fine values are real structure, not pinv artifact (the coarse
`4-4-7` count was already topological). **D4 corroboration/new split:** the SL(4) **principal** (`c=−1`, `M⁴=L`)
**corroborates** the proved B89/B83 `L=(−1)^{n−1}Mⁿ` — *not* a new advance; the **new** content is the
**secondary** (`c=i`, `M³=L`, numerical ~5e-15), the **SL(3) W2** relation, and the **per-eigenvector method**.
Banked: probe function + locking test, FINDINGS/README split, ledger **V93** (a clarification row). Merged
PR #110.

**B107 physics-connection audit (V94, POSTULATED/FIREWALLED).** Banks the CC-web physics exploration as a
first-class **dead-end log whose headline is a NEGATIVE**. *All* physical readings are **POSTULATED and
firewalled** to `paths/philosophical/PHYSICS_RESONANCES.md` (new Path 8); **nothing to `CLAIMS.md`**; the
physics chapter stays **CLOSED**; P1–P16 untouched. **A (verified anchor):** the SL(2) metallic trace map
`φ_m: a→aᵐb, b→a` **is** the Kohmoto–Kadanoff–Tang / Fibonacci-Hamiltonian trace map — via Cayley–Hamilton the
induced `(trA,trB,trAB)` map conserves `tr[A,B]=x²+y²+z²−xyz−2` (Sütő/Fricke–Vogt) for all `m` (symbolic
m=1..4), and `φ_1=(z,x,xz−y)` (= B67's `T₁`); cite Sütő (1989), Damanik–Gorodetski–Yessen (2016), Roberts
(1996). **B (verified — the decisive negative):** every SL(3) `m=1` tower eigenvalue is `±φᵏ` (the 8 values
`{1,−1,φ²,φ⁻²,φ³,−φ,φ⁻¹,−φ⁻³}`) — **one geometric scale `log φ`**; a fluctuation spectrum is a Hessian, not one
ratio, so the tower is **re-presented moduli-space monodromy, not new physics**. **C (corrected overclaim):**
tower/torsion `=` masses/dimensions are **withdrawn category errors** — only the moduli-space-level
`M_SUSY ≅ M_flat` + three-branch ↔ three-fixed-point map (the B106 classes) is citable. **D:** GKLP 1305.0937,
DGG 1108.4389/1112.5179 confirmed. **E (open fork):** the off-principal multichannel reps; **Addition 3** —
B106's root-of-unity D1 data confirms the single-scale pattern breaks there, the open `c→θ` check being the
math link to `ρ_n`. Banked: `probe.py` (`quasicrystal_anchor`, `tower_roots_are_golden`), locking test,
FINDINGS A–E + firewall banner, ledger **V94**.

---

## 2026-06-07 — intellectual-architecture reorganization (four governed rooms; docs/org only, no math)

Built the four-folder architecture for the *evolving speculative ideas*, all firewalled (nothing promotes to
`CLAIMS.md`; the physics chapter stays CLOSED; the mathematics never cites these rooms; the ρ_n catalog proof
stays the central math target).

**New rooms.** `speculations/` — `GOVERNANCE.md` (proof-status enum incl. `HELD(value-matching)` + the HELD
rule + the two uncrossable lines), `CATALOG.md` (`S001…S021`), `PHYSICS_EXERCISE.md` (the corrected tiered MASTER,
with the **κ=−2 cusp** fix vs the archived draft's κ=2 error), per-live-speculation files `S001–S013,S020`,
`TOMBSTONES.md` (the DEAD set linking to the failure atlas / CLAIMS-D / V-rows), and `archive/`. `philosophy/` —
`GOVERNANCE.md` + `P000` (what-is-not-nothing / four chosen premises) + `P001` (architecture-not-furniture) +
`P002` (necessity *given* chosen premises — a position, not a derived truth) + `P003` (dead-ends-as-boundaries),
beside the migrated `P1–P5` register and `METALLIC_FOUNDATIONS`. Root `ARCHITECTURE.md` (the one-way arrow).
`story/` + `knowledge/` follow in a second PR.

**File migration (old → new) — the mapping for the append-only/historical references above that still name the
old paths:**

| old path | new path |
|---|---|
| `paths/philosophical/PHILOSOPHICAL_PATHS.md` | `philosophy/PHILOSOPHICAL_PATHS.md` |
| `paths/philosophical/METALLIC_FOUNDATIONS.md` | `philosophy/METALLIC_FOUNDATIONS.md` |
| `paths/philosophical/PHYSICS_RESONANCES.md` | `speculations/archive/PHYSICS_RESONANCES.md` |
| `paths/philosophical/COSMOGONY_FROM_THE_VOID.md` | `speculations/archive/COSMOGONY_FROM_THE_VOID.md` (superseded by `speculations/PHYSICS_EXERCISE.md`) |

All **live** references (frontier firewall banners in B92/B96/B97/B101/B107, `frontier/README.md`,
`frontier/REPO_STATE.md`, the repo-map, `docs/atlas/FAILURE_ATLAS.md`, `CHANGELOG.md`, `paths/PATHS.md`) were
redirected to the new locations. **Append-only history above and the historical `papers/VALIDATION_LEDGER.md`
rows (V76/V80/V81/V85/V94) were left intact** — this table is the key for reading their old paths. Docs/org only;
no mathematical content, no ledger result, no test change; `CLAIMS.md` / P1–P16 / the physics-chapter status
untouched.

---

## 2026-06-07 — the Final Computation Arc (B108–B110) + the dead-ends register

Executed the CC-web "Final Computation Arc" after the architecture build, **verify-don't-trust throughout** (the
handoff's empirical facts were re-derived, and two of them were corrected).

**B108 (V95) — the prize, `θ=−w₀ → c`? NO.** The mandatory hinge (predict all four per-eigenvector degree=rank
scalars `c={1,1,−1,i}`, B106 D4) **fails**. `θ` *is* a tower symmetry (`P²=I`, `[P,J(m)]=0` symbolic; organizes the
Dickson parity, B62), and at the Dehn-filling reps it acts as the contragredient sending `c↦c⁻¹` — so it fixes
`c∈{1,−1}` (W1/W2/principal, matching `c=(−1)^{n−1}`, B83) but **not** the secondary `c=i`. Obstruction: `θ` is an
**involution (order 2)**; `c=i` is **order 4** — beyond its reach. degree=rank's `c` stays OPEN; the missing piece
is an order-4 (`ℤ/4`) ingredient (candidate: the forced cusp spectrum `{1,i,−i}`, B95). **Trajectory call:** the
negative branch — Paper 1 frames degree=rank as the central open question, with this obstruction precise.

**B109 (V96) — the void dynamics (D2) + L5 literature.** The handoff's coordinate-axis facts do NOT reproduce; the
rigorous linearization `DT₁²(2,2,2)` does, with eigenvalues `{1, φ⁴, φ⁻⁴}` (1 center = the `A↔B` asymmetry, 1
unstable, 1 stable; Lyapunov `{0, ±4 log φ}`); the void is a `(2,1)` saddle of `κ`; and the SL(3) center manifold
= the tower's root-of-unity parity sector (dim 1@SL2, 2@SL3). L5: degree=rank `Mⁿ=L` **apparently new** (HMP
1505.04451 confirms 3 components but not the power law); the `W₄` anchor at `sl(4)` is real (1111.2834) but generic
`sl(N)↔W_N`, doesn't single out n=4.

**B110 (V97) — the off-locus sector of `4₁`/SL(3) is EMPTY.** The variety has exactly three irreducible components
(HMP = B71's V0/W1/W2), all on the forced locus, so 4₁/SL(3) carries no non-principal content; the broader S011
fork (higher rank / other manifolds) stays open.

**Dead-ends register (Task 7).** ~30 kills consolidated in `docs/atlas/FAILURE_ATLAS.md` by structural pattern
(numerology / wrong-dictionary / 3+1-spacetime / coincidence / the n=5-wall REVIVABLE kills / specific-manifold
empties), each with kill mechanism + `V`/`B` + DEAD-vs-REVIVABLE; the REVIVABLE (n=5) lens foregrounded — every one
converges on the `ρ_n` proof. Probe updates: **S001** (all-`m` amphichiral PROVED — `M_m²` symmetric ⇒ the systole
not amphichirality selects `m=1`), **S006** (Bell/CHSH → TESTED-NEGATIVE — deterministic Fricke surface ⇒ CHSH≤2).
Suite 298 passed; no physics; the `ρ_n` catalog proof stays the central target; `CLAIMS.md`/P1–P16 untouched.

---

## 2026-06-07 — B111: the tower's sign structure + the degree=rank exponent (the "sign findings" handoff)

Banked the Chat 2 "Bank findings + new paths" handoff + the Opus supplement (ADDITION 1/2/3); verify-don't-trust.

**The most-leveraged computation (PATH B, done first).** The opposition-involution all-heights **closed form**
(`mult char(M^h)=⌈(n−h)/2⌉`, `char(−M^h)=⌊(n−h)/2⌋`, `h=1..n−1`; matches B62's height-2 splits) is **not** the
proved tower. Diffing vs the exact repo tower (n=3 Lawton Jacobian; n=4 B80): **`Tower(n) = [closed form, heights
1..n−1]` with exactly one `char(M¹)` promoted to `char(Mⁿ)`** (verified n=3,4). The single non-bulk ingredient is
`char(Mⁿ)` = the **degree=rank** top power (`L=c·Mⁿ`). **Decision:** the tower's **sign half IS the closed form**
(bulk θ); the only open piece is `char(Mⁿ)` (peripheral). Both halves of the `ρ_n` prize named.

**ADDITION 1 (proved negative).** On the SL(4) secondary `M⁴=ζ⁴=−1` is **scalar** ⇒ trivial commutator ⇒ `k=4`
**algebraically impossible**; `k=3` forced. On the principal `M⁴` non-scalar ⇒ `k=4` allowed (but `k=n` *not*
proven — honest scope). **ADDITION 2:** cusp orders `{n−1,n+1,2n}`; the `ord−1` formula **TESTED-NEGATIVE**.
Covering-degree A1d: `k`-to-1 at the eigenvalue level (partial-positive), full covering open. **Correction:** the
SL(3) parity is `(t−1)(t−det N)` (the handoff's `(t+det N)` was a sign slip). `s_n↔c` bridge **DEAD** (same parity
argument as B108). **Leads opened:** `S022` (the peripheral ℤ/4 — the successor to θ→c) + `TWO_SYMMETRY_FRAME`
(bulk θ + peripheral cusp; degree=rank at their interface — the promotion `char(M)→char(Mⁿ)` *is* the interface).
Suite 304 passed; no physics; the `ρ_n` catalog proof stays the target; `CLAIMS.md`/P1–P16 untouched.

---

## 2026-06-07 — the ρ_n sign half PROVED + the five follow-on paths (B112–B115)

Computed the five paths B111 opened. **B112 (V99) — the headline:** the **sign half of `ρ_n` is PROVED for all
n**, engine-free (no Procesi ring, no eps-series, no σ-construction). An elementary **root-system reversal
lemma** — `θ=−w₀` acts by `−w₀(e_i−e_j)=e_{n+1−j}−e_{n+1−i}` (height-preserving), so on the `(n−h)` positive
height-`h` roots it is the reversal `i↦(n−h+1)−i`, whose `(+1,−1)` eigenspace dims are `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)`
(verified all n≤12, two ways) — times the banked **B64** parity assignment (`+1`→`char(M^h)`, `−1`→`char(−M^h)`)
gives the closed form `mult char(M^h)=⌈(n−h)/2⌉`, `char(−M^h)=⌊(n−h)/2⌋`. The first catalog piece proved from
first principles for all n.

**B113 (V100):** the proved closed form **resolves the SL(5) sign sectors** at heights 2–4 *by proof* — matching
the SL(5) tower exactly, including `char(M²)²·char(−M²)` = B62's two gauge-corrupted modes the eps-series `pinv`
could not resolve — and **localizes degree=rank to height-1 + the top power `char(Mⁿ)`** (heights `2..n−1` are
pure bulk-θ). Honest caveat: the promotion is **n-dependent** (consumes `−M` at n=5, `+M` at n=3,4), so the
power half is the genuinely-hard open piece. **B114 (V101):** the covering-degree mechanism (S022's candidate for
the exponent) is **TESTED-NEGATIVE** — the full covering degree is `~k^{n−1}`, not `k`; `=k` holds only at the
single-eigenvalue level; the exponent lead stays the `Mᵏ`-scalar arithmetic (B111 ADD1). **B115 (V102):** the
known SL(4) Dehn-filling reps are forced-locus (like SL(3), B110), so off-locus SL(4) content is in uncomputed
components (obstruction: the missing SL(4) figure-eight character-variety classification); genus-2 degree=rank
needs a genus-2 construction not in the repo (obstruction: the genus-2 peripheral structure) — both scoped OPEN.

**State of the prize:** the **sign half of `ρ_n` is proved for all n** (B112); what remains for the full catalog
is the **power half** — the single degree=rank promotion `char(M)→char(Mⁿ)`, n-dependent, localized to the
height-1/top-power interface (B113), with the `Mᵏ`-scalar arithmetic (not covering degree) as the live lead.
Suite 312+ passed; no physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

---

## 2026-06-07 — B119: the Mᵏ-scalar (centrality) mechanism — a sharp negative on "prove k=n on the principal" (Chat-2 Path 3)

Ran Chat-2's **Path 3** (the hard path; be brave). B111 ADD1 — the one surviving exponent lead — showed the cusp
eigenvalue arithmetic *controls* the degree=rank exponent (on the SL(4) secondary `M⁴=−1` scalar ⇒ central
commutator ⇒ `k=4` impossible, `k=3=n−1` forced). The brave goal: **prove `k=n` on the principal** from
scalar-ness + bundle relations. **Result: a sharp negative.**

**Reframe (B117).** The *bulk* `char(Mⁿ)` is no longer a "promotion" — it is `Sym^n` presence (`μ_n=1`). So this is
the *peripheral* `k=n` on the Dehn-filling component, the one open shot at a positive power-half mechanism.

**The arithmetic.** The forced principal cusp spectrum (B95) is `1` at mult `n−2` plus `{a,1/a}`, `a+1/a=3−n`;
`order(a) = {4,3,2,∞}` for `n=3,4,5,≥6`. `Mᵏ` is central on the principal iff `order(a)|k`.

**Why the brave proof does not close.** Where the principal exists (`n=3,4`) the irreducible longitude `L=[A,B]` is
non-central ⇒ `k` not a multiple of `order(a)` — excluding `{order(a),2·order(a),…}` (n=4 excludes `k=3,6`) but
**not** singling out `k=n` (n=4: `k=1,2,4,5` all non-central). Centrality is **necessary, not sufficient**; `k=n`
is pinned by the **proved A-poly** `L=(−1)^{n−1}Mⁿ` (B83) — the scalar route is *subsumed* by B83, not an
independent proof. For **n≥5 there is nothing to prove**: the principal Dehn-filling rep does not exist irreducibly
(B95 — n=5 `A²=I` dihedral; n≥6 no finite-order spectrum). So **`exponent=rank` is an `n∈{3,4}` phenomenon**; the
brave `k=n` proof **cannot be completed** — the obstruction stated as sharply as B108's order-2-vs-4.

**The secondary (extends B111).** On the 2n-type (`Mᵏ` central iff `n|k`): `Mⁿ=−I` central ⇒ `k=n` gives a central
commutator ⇒ the non-central longitude is `M^{n−1}` ⇒ exponent `n−1`. **Emergent (B111 ADD2 correction):** the
cusp order on the degree=rank principal is `order(a) = {4,3,2,∞}`, **not** a clean `{n−1,n+1,2n}` law — B111 ADD2
conflated three different components (n=3 W1 = `n+1`, n=4 principal = `n−1`, n=4 secondary = `2n`). No single all-n
cusp-order law; the orders are each component's primitive cusp eigenvalue order, governing `Mᵏ` centrality. Banked
V106; suite green; no physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

## 2026-06-07 — B122 interlude extensions: the det layers split + the Sym tower is void-specific (terrain-sweeping)

Audited the Chat-2 "ran the computable terrain to its edges" handoff (verify-don't-trust, incl. the self-caught
order-6 correction) and banked two findings as **extensions of B122** (annotations, no new ledger row).

- **F1 — the two layers split by `det`.** The figure-eight monodromy is the **golden unit squared**
  (`M₁²=[[2,1],[1,1]]`, `det=+1`, eigenvalue `φ²`). The **magnitude layer** (the W-identity / `μ_d`) is a polynomial
  identity in `(x,y)`, so it is **`det`-independent** — holds `det=+1` as well as `det=−1` (verified through n=14),
  hence *more general than the metallic ray*. The **sign layer** (the inversion identity `char(M⁻¹)=char(−M)`, the
  parity factor) is **`det=−1`-specific**: `char(M⁻¹)−char(−M)=0` at `det=−1`, `=−2tτ` at `det=+1`; and the parity
  `(t−1)(t+1)` collapses to `(t−1)²` going golden → fig-8 (`=`golden², `det=+1`). So the two-layer model is exact:
  W = magnitude (`det`-independent); signs = the metallic/orientation feature (B118).
- **F2 — the `Sym` tower is void-specific.** On the SL(2) trace map `T(x,y,z)=(z,x,xz−y)`: at the **void `(2,2,2)`**
  the Jacobian eigenvalues are `{−1,φ²,ψ²}=Sym²(M)` (the n=2 tower); at the other fixed point `(0,0,0)` they are
  `{−1,e^{±iπ/3}}` = **6th roots of unity** (char poly `λ³+1`=`(λ+1)Φ₆`, `DT⁶=I` — order **6**, correcting a
  narration slip of "order 3"), elliptic and **not** `Sym`-organized. So the `Sym^d(M)` tower lives where the
  abelianization `M` acts — the void — making B106's "non-void = different spectral type" explicit at SL(2).
- **Confirmations (cross-references, no rows):** the W-identity holds through **n=14** (past the banked n≤11); the
  **S023** box-dimensions do not cleanly separate at longer chains (finite-size, drift within the m-to-m
  differences) — reconfirming the W1 demotion (the result rests on the exact arithmetic field-distinctness).

**Standing truth (in the entries).** None of this lowers the wall. The prize is unchanged: prove the tower is
**functorially** `Sym^n(W) ⊕ (Sym^{n−3}(W)⊖W)` for the external fundamental `W=V⊕1` — the one missing piece is a
**functorial `Sym(W)→trace-ring` construction** (defined without the ambient `SL(n)` trace ring), a construction to
be found, not a probe to be run. Banked as B122/K008/S023 annotations + a V111 annotation; suite green; no physics;
nothing to `CLAIMS.md`; the `ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched.

## 2026-06-07 — Firewalled triage of the cross-chat "seven hints" (tiers kept separate; the S024 collision fixed)

The companion to B122: the physics-facing hints two other chats produced on the same `μ_d` object, banked at the
**right tier** so the firewall does not leak (the governing rule: the math and the physics enter as *different
tiers*, never in one sentence).
- **A3 → `philosophy/P005` (laws and states):** the Q2 split as a **law** (spectral, all n) vs a **state**
  (geometric, n∈{3,4}) — "infinite structural depth, finite fundamental content." INTERPRETATION on B120, same tier
  as P004; no dictionary claimed.
- **A7a → B122 (math tier):** `Sym⁴(3-space)=15=sl(4)` (the unique saturating order), the offset = dim W, the
  subtraction = `⊖W` — folded into the proved B122 entry, not as a physics claim.
- **A7b/A2 → `speculations/S028` (fenced):** the `Sym⁴(3-space)=sl(4)` reading. The **algebra is proved** (B122);
  the **"3+1" geometric reading is fenced** POSTULATED — "spacetime" stripped (adjacent to the DEAD S017/S018
  spacetime-from-dimension-count), bound to B122's *open* functorial hinge (collapses with it). The spin-2/gravity
  overlay (A2) is recorded **underneath** the math, labeled "unverified analogy requiring an unestablished 3d-3d
  dictionary," never in `knowledge/`. **Crucial fix: this is `S028`, NOT `S024`** — the incoming handoff said S024,
  but S024 is already the Phase-2 monodromy/Hitchin entry (a numbering collision, corrected).
- **A4 → tombstone:** the CS-crossover `k≈4↔n=4` is m-dependent (k≈2 at m=2, k≈1 at m=3) — a volume coincidence,
  same family as the killed value-matches. TESTED-NEGATIVE, banked in `TOMBSTONES`.
- **A1 / A5 → cross-references:** the two-band reading (A1) is reconciled inside B122 (one structure, multiple
  readings); A5 (interaction-born=P004, the number-fields=S023, the dimension identity=B117) is cross-referenced,
  not double-entered.

**Watch-item fixes (the latest cross-chat review).** **S023** re-scoped: `TESTED-POSITIVE` rests on the **exact
arithmetic** (the distinct fields `ℚ(√5)/ℚ(√2)/ℚ(√13)` + `φ_m`); the spectral box-dimension is demoted to a
*supporting, finite-size* signal (computed in-house, not golden-extrapolated, but soft). **S027** sharpened: the
golden 4₁ Kashaev is the **textbook** feasibility witness; the genuinely-new content is the **m≥2** (silver/bronze)
cocycle. No math; nothing to `CLAIMS.md`; physics chapter stays CLOSED; P1–P16 untouched.

## 2026-06-07 — B122: the tower is symmetric powers of the external fundamental W=V⊕1 (unifies B121 + the Chat-2 W-identity)

Audited Chat-2's "the tower is `Sym^n(W)`" handoff (verify-don't-trust), ran the brave functorial hinge test, and
banked the result unified with B121. The two-sequence (B117) re-expressed as a virtual `GL(2)`-module:
`ρ_n = Sym^n(W) ⊕ ( Sym^{n−3}(W) ⊖ W )`, `W = V ⊕ 1`.

**What's verified.** (1) The character identity `ρ_n = Sym^n(W)+Sym^{n−3}(W)−1−V == μ_d` holds **n=2..11**
(`Sym^a(V⊕1)=⊕_{k≤a}Sym^k(V)`; `Sym⁰⊕Sym¹=W`). (2) It is a **genuine `GL(2)`-module iso** — a first pass wrongly
called it "automatic," but that's only over the cyclic `⟨M⟩`; the tower is a **`GL(2,ℤ)`-rep** (B103), and the
identity holds **symbolically in general `(x,y)`, det-independent, n≤8** (module-level proved n=3,4 via B103). So it
is functorial, not a numerical coincidence.

**The unification with B121 (the headline).** `det(W=V⊕1)=−1` → B121's **external** `det=−1` parity; `det(Fricke =
Sym²V)=+1` → the **internal** principal/Kostant parity. So Chat-2's kill of "`W` = Fricke 3-space" **is** B121's
external≠internal: Fricke carries the internal embedding (even weights), the tower the external monodromy one (mixed
parity); the tower's **odd weights** = `Sym^n(V⊕1)∋V` = the B121 parity obstruction, re-derived. **B121 and the
W-identity are one object** — the monodromy grading *is* `Sym(`external fundamental `W)`. (Banked together, not as
two ledger rows that quietly repeat — the cross-chat reconciliation Chat 1 flagged.) Corollary (A7a):
`Sym⁴(3-space)=15=sl(4)` is the *unique* saturating order — the n=4 fixed point of the dimension identity (B117);
band offset = dim W = 3 = the offset-2 in the `Sym(V)`-index (A1; one structure, reconciled readings).

**The honest verdict (the brave functorial test, run).** It is module-iso-**equivalent** to the two-sequence
(proving it all-n **==** proving `μ_d`); **no functorial `Sym(W)→trace-ring` map** exists, and the `Sym⁴(3)=15`
saturation is n=4-only (the correction term blocks a single clean `Sym^n`). So B122 **repackages** the prize and
**identifies `W` canonically**, but does **not** lower the trace-ring wall. Re-aimed prize: *prove the tower is
functorially `Sym^n(W) ⊕ (Sym^{n−3}(W)⊖W)`* — a construction that does not yet exist. This is the **magnitude**
layer; the signs `char(M^h)`/`char(−M^h)` are the orthogonal `det=−1` layer (B118). Banked V111 + K008 extended; the
3+1 / spin-2 geometric *readings* (the seven-hints addenda) are firewalled in S028 (next), never in the math. No
physics in the math; nothing to `CLAIMS.md`; the `ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched.

## 2026-06-07 — Physics-bridge sweep, Phase 3: the heavy forks mapped + the Kashaev feasibility (sweep complete)

The closing phase: the three heavy/deferred bridges, mapped as `DORMANT` speculations with concrete computations +
obstructions, plus one cheap in-house feasibility probe.
- **S025 — off-principal independent spectral content at higher rank** (the S011 continuation): EMPTY for 4₁/SL(3)
  (B110), open only at SL(4)/SL(5) or another manifold; obstruction = no SL(4) char-variety classification (B115) +
  the non-Hermitian realization (`sln_multichannel`). A real open boundary, not a queued calculation.
- **S026 — does the SL(n) tower organize the `T[4₁]` state-integral** (fixed knot, varying rank)? The moduli/A-variety
  level is in-house (B71/B83 + vol 2.0299, B82), but the quantum state-integral at higher rank needs the quantum
  dilogarithm (research-level). Vary the **rank n**, not the seed m (the family-in-m is dead, Gate 1/2).
- **S027 — the metallic Kashaev invariants as quantum modular forms** (the `GL(2,ℤ)` cocycle): **feasibility shown
  in-house** (`kashaev_feasibility.py`) — `J_N(4₁)=Σ|(q)_k|²` is a cheap finite sum and `(2π/N)log J_N → vol(4₁)`
  (monotone, from above, N≤800). The open part is the Zagier–Garoufalidis modular cocycle + the per-knot arithmetic
  in `ℚ(√(m²+4))` (tying to S023's field-distinctness).

**The physics-bridge sweep is complete (Phases 0–3).** The honest outcome, answering "what can we compute so we
don't give up on physics": the terrain is fully **mapped** (`PHYSICS_BRIDGE_MAP.md` — dead/live/heavy); the two
**live** leads are **banked** — S023 (the metallic means are arithmetically distinct real quasicrystals, despite the
m-universal algebra) and B121 (the tower is the **monodromy side of Hitchin**, separated from the Fuchsian/principal
section by the program's own `det=−1` parity); and the **heavy** forks are scoped with feasibility + obstructions.
The genuine connection-to-reality is condensed-matter quasicrystals (buildable) and the 3d-3d / complex-CS topology
of the figure-eight (real QFT/knot invariants) — **not** masses/Λ/spacetime (all dead). Banked V110 + S025/S026/S027
+ the map; the sweep added V108–V110 and S023–S027. All firewalled; nothing to `CLAIMS.md`; physics chapter stays
CLOSED; the `ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched.

## 2026-06-07 — Physics-bridge sweep, Phase 2: the monodromy sl(2) grading (an external det=−1 GL(2,ℤ)-rep)

The structural lead. The earlier maps showed "tower ≠ Kostant principal-sl(2)" is a **banked negative** (B89-T/B98);
B121 turns it into a **positive** characterization. The `(n²−1)`-dim trivial-point tower carries **two**
`SL(2)`-actions on the adjoint `sl_n`:
- **internal principal** `sl(2)⊂sl_n` (Kostant): adjoint `= ⊕_{i=1}^{n−1}Sym^{2i}`, **even** highest weights,
  `det=+1` (the defining rep `Sym^{n−1}` lands in `SL(n)`) — this **is** the Fuchsian/Hitchin section (B101);
- **external monodromy** `GL(2,ℤ)` (the mapping class group): the tower `⊕Sym^d(M_m)^{μ_d}` (B103), **mixed-parity**
  highest weights.

**Computed (B121).** The two reps share dim `n²−1` and **agree only at n=2**; for **n≥3 the tower has odd highest
weights** (Kostant is even-only) ⇒ **inequivalent**. The obstruction **is `det(M_m)=−1`**: `Sym^d(M_m)` has
eigenvalues `(−1)^j φ^{d−2j}` and `det Sym^d(M_m)=(−1)^{d(d+1)/2}` (a sign in every block; the `det=+1` partner gives
all `+1`); the odd-highest-weight blocks are exactly the `char(−M^h)` sectors (B112) — the **same `det=−1` parity**
as B118's fixed-root sign `(−1)^{h+1}` and B93/B94's catalog parity. **Kill condition not met:** same dimension but
inequivalent — **not** a coincidence.

**The bridge (firewalled, S024).** So the monodromy `sl(2)` is the **external `det=−1` `GL(2,ℤ)`-action** — the
Hitchin/Fuchsian section's **monodromy partner**, offset by the program's own `det=−1` parity. This connects the
trace-map tower to the Hitchin picture **without crossing the firewall**: the principal side is the Fuchsian/Hitchin
section (B101), the monodromy side is the MCG, the gap is `det=−1`. The Hitchin→Langlands→class-S *reading* is
firewalled (S024, POSTULATED; ceiling = N=4 SYM / class-S of the once-punctured torus, **not** the SM). Banked V109
+ B121 + S024; CATALOG/REPO_STATE/README updated. No physics in the math; nothing to `CLAIMS.md`; physics chapter
stays CLOSED; the `ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched. (Phase 3 — the heavy 3d-3d/modularity
forks — follows.)

## 2026-06-07 — Physics-bridge sweep, Phase 1: the metallic means are distinct real quasicrystals (FIREWALLED)

A brave-but-honest sweep of the bridges to physics, in response to "what can we compute so we don't give up on
physics?" The two read-only maps first established the **honest terrain**: most "obvious" bridges are already
**dead or textbook** — masses/Λ/spacetime (B107/B96/B101), holography/entanglement (V37), the Seiberg–Witten /
spectral-curve family (Gate1/2), the fusion/anyon family (only m=1 categorifies), the **SL(n≥3) Hermitian chain**
(non-Hermitian, `sln_multichannel`), and "tower ≠ Kostant" (B89-T/B98). So bravery here = computing the **few
genuinely-open forks**, each with a kill condition, all firewalled.

**Phase 0 — the terrain map.** `speculations/PHYSICS_BRIDGE_MAP.md` classifies **every** bridge (DEAD / LIVE /
HEAVY) so nothing is missed and the dead aren't revived. "Don't give up by knowing the whole terrain."

**Phase 1 — the metallic-mean quasicrystals (the live, real-materials lead; S023, `TESTED-POSITIVE`).** The SL(2)
Hermitian metallic substitution chain (`a→aᵐb, b→a`) is a **genuine, buildable quasicrystal** (golden m=1, silver
m=2, bronze m=3 — realized in photonic lattices / cold atoms); its trace map is the Kohmoto–Kadanoff–Tang map
(B107/K007). The sharp hinge, tied to **B120**: B120 proved the trace-map **algebra** (the Sym two-sequence `μ_d`)
is **m-universal**; is the *physics* too? **No** — computed (`metallic_spectra.py`): the gap-labeling module
`ℤ+ℤα_m` lives in `ℚ(√(m²+4))` with squarefree disc `{5,2,13}` → **three distinct quadratic fields**
`ℚ(√5),ℚ(√2),ℚ(√13)` (gap labels confirmed 10/10, 12/12, 12/12 on the lattice); the RG scale `φ_m` and the spectral
box-dimension `{0.628,0.636,0.650}` also differ. **The algebra is one object (m-universal); the physics is a family
of distinct, buildable materials.** The connection-to-reality is genuine and computable — the spectral theory of
real quasicrystals — *not* masses/Λ/spacetime (all dead).

**Honest scope.** 1D condensed matter, **not** fundamental physics; the m=1 gap-labeling is textbook (Bellissard
1992) — what's new is the systematic metallic-m family + the algebra-universal/physics-distinct contrast vs B120.
The SL(n≥3) extension is **blocked** (non-Hermitian). Kill condition passed (had the spectra been affinely
equivalent → TESTED-NEGATIVE; they are not). Banked V108 + S023 + the map; S007 updated (the SL(2)/m part computed,
SL(n≥3) blocked); S022 noted low-rank. Firewalled; nothing to `CLAIMS.md`; physics chapter stays CLOSED; the
`ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched. (Phases 2–3 — the monodromy/Hitchin grading and the heavy
3d-3d/modularity forks — follow.)

## 2026-06-07 — B120: the trivial-point tower is determined by (n; trace, det) — banks Chat-2 Q2/Q3 + Supplement S1–S5

Banked the Chat-2 exploration interlude (Q2/Q3) and the computed Supplement (S1–S5), **verify-don't-trust**. The
`(n²−1)`-dim trivial-point tower (the Sym two-sequence, B117/B103) is **one object** fixed by two inputs — the
unfolding depth `n` and the abelianization seed `(trace, det)` — and nothing else enters. Eight claims verified;
**three formulas corrected** (caught from scratch).

**Q3 — the determination theorem.** Distinct integer matrices with equal `(trace,det)` give **identical towers**
(`[[2,1],[1,0]]` vs `[[1,2],[1,1]]`, both `(2,−1)`; n=3,4,5, 8/15/24 roots). Forced: tower = `⊕Sym^d(M)`, and
`Sym^d` eigenvalues are degree-`d` monomials in `M`'s eigenvalues, fixed by the char poly = `(trace,det)`.
twist-count→trace (the seed `m`), swap-count mod 2→det (the parity sector).

**S2 — m-universality (the deep lead, followed).** The `n=4` tower's `char(±Mᵏ)` **multiplicities are identical for
m=1,2,3** — only the eigenvalue values `φ_m` change. The Sym content `μ_d` depends only on `(n, det)`. *Why:* the
tower is a `GL(2,ℤ)`-rep `ρ_n` (B103); the `μ_d` are its plethysm/branching multiplicities under the principal
`SL(2)`, trace-blind. **Honest scope:** this **reframes the prize as a plethysm** and is proved only n=3,4 (B103's
`ℚ[m]`-iso); it does **not** lower the trace-ring wall (all-n m-universality is the same wall) — a reduction, not a
closure.

**Q2 — the degree=rank split.** (I) SPECTRAL `char(Mⁿ)` is a tower factor ⟺ `μ_n=1`, **all n** (= `Sym^n`
presence, B117); (II) GEOMETRIC longitude=meridianⁿ at an irreducible boundary-unipotent rep, **n∈{3,4}** (forced
principal `a+1/a=3−n`, order `{4,3,2,∞}`; n=5 the `A²=I` edge — B95/B119). This **dissolves the apparent B117-vs-B119
tension** — both right, two halves of one split. Lineage rows V47/V72/V74 annotated.

**Corrections (verify-don't-trust).** **S1:** the doubling band `{2..n−3}` is forced (= the deficit
`(n−4)(n+1)/2`), but the handoff's `(n²−3n)/2` is **off by 2**. **S3+S5:** eigenvalue heights run **0..n** (the top,
`Sym^n`'s extremes, was missed); the handoff's `2·max(1,n−h−1)` guess is wrong **and** its "no closed form" claim is
wrong — a clean closed form exists: `count(n,0)=n−1`; `2(n−2)` for h∈{1,2}; `2(n−h)` for 3≤h≤n−1; `2` for h=n
(Σ=n²−1). **S4:** B116's θ-split vs Sym comparison is at the **factor** level (agrees n≤5, diverges n=6); the Chat-2
"n=3 divergence" was an eigenvalue-vs-factor units error — B116 stands.

**Governed-folder banking (firewalled).** `knowledge/K008` (the `(n; trace, det)` determination explainer, citing
B103/B117/B120); `philosophy/P004_interaction_born.md` (INTERPRETATION on a theorem — `M_m=(twist)ᵐ·(swap)`,
`SL(2,ℤ)` generated by non-expanding elements ⇒ expansion is emergent, never a primitive); and the **downgrade** of
the "Markov-blanket / boundary-open / interior↔boundary" reading to low-rank `n∈{3,4}` (in TWO_SYMMETRY_FRAME +
S022 — downgrade, not tombstone). Banked V107; suite green; no physics; no `CLAIMS.md`; the `ρ_n` / Sym-`μ_d` proof
stays the prize; P1–P16 untouched.

## 2026-06-07 — B118: the θ=−w₀ fixed-root sign = (−1)^{h+1} (NOT the anticipated uniform +1) — a refinement of B112 (Chat-2 Path 1)

Ran Chat-2's **Path 1** (the gate). B112 proved the `(+1,−1)` eigenspace **dimensions** of `θ=−w₀` on the
height-`h` roots of `A_{n−1}` by a **permutation** argument (no signs). The `⌈`-vs-`⌊` tip reduces to ONE sign: for
odd `m=n−h` there is exactly one θ-fixed root (the middle), and the 2-cycles split `(1,1)` no matter how labeled.
B112 *assumed* that sign is `+1`. **Path 1 asked whether it is `+1` for all `(n,h)`** — which would make B64 a
uniform "`+1` sector = `char(M^h)`" theorem.

**Computed it (genuine, signed).** Realizing `θ=−w₀` as the contragredient involution `τ(X)=−J Xᵀ J⁻¹` (standard
antidiagonal so/sp form, `ε_p=(−1)^{p+1}`; `τ²=id`, acts as B112's reversal), a direct index computation gives, on
the lone fixed root, the scalar **`(−1)^{h+1}`** — `FIXED-ROOT SIGN(n,h) = (−1)^{h+1}`, independent of `n`, proved
symbolically (the ε-form residual is exactly `0`) and verified numerically all `n≤12`.

**The finding (a correction).** The sign is **`(−1)^{h+1}`, NOT a uniform `+1`** — `+1` for odd `h`, `−1` for even
`h`. So the genuine *signed* θ does **not** put the fixed root in the `+1` (symmetric) sector for all `h`; B112's
unsigned-permutation reading ("the fixed root is always `+1`") is right only for odd `h`. The `(⌈,⌊)` **dimensions**
(B112) are untouched (cycle structure); only the geometric **sign** is refined. B112's `char(M^h)=⌈` **labeling**
stays tower-verified `n≤5` (B118 supplies the all-`n` sign, not an independent all-`n` labeling proof) — and B117
shows the tower is the Sym two-sequence anyway (the θ-split diverges at `n≥6`, B116). So Path 1 returns a
**closed-form sign + a correction**, not a uniform-`+1` theorem.

**Emergent (chased inline, non-circular).** For `2×2` `det=−1` monodromy `M⁻¹∼−M`, so `char(M^{−h})=char(−M^h)`
precisely for **odd `h`** (independently computed from the polynomials; fails even `h`). The fixed-root sign is
`+1` exactly for odd `h` — the same parity. So `fixed-root sign = +1 ⟺ the inversion identity holds ⟺ h odd`
(verified all `(n,h)`): the geometric eigenvalue and the polynomial identity are one fact (`−w₀` inverts the
principal torus). Banked V105; suite green; no physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16
untouched.

## 2026-06-07 — B117: the interleaving insight (the tower is the Sym two-sequence; the "promotion" is a Sym¹ absence)

The **headline reframing** of the B111–B116 run (the Opus interleaving insight, verify-don't-trust; every claim
re-derived in `probe.py` + locked in `tests/test_b117_interleaving.py`). The `(n²−1)`-dim trivial-point tower
carries **two gradings that interleave** — the HEIGHT/θ-split (B112, exact only n≤5) and the SYM decomposition
(B103/B58, the actual tower). The insight is a clean derivation of the SYM side + the dissolution of the
"promotion."

**(3a) The dimension identity DERIVES the two-sequence shape.** `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2` (roots
`{−1,4}`): the full module set `{Sym⁰..Sym^n}` (dim `(n+1)(n+2)/2`) vs the tower (dim `n²−1`) match **iff n=4**
(the unique perfect fit). n<4 → surplus (omit modules), n>4 → deficit (double modules). This *derives* B103's
`two_sequence_mult μ_d = [2≤d≤n] + [0≤d≤n−3]`: n=3 omits `Sym¹` (`{0,2,3}`, the **unique** subset of `{0,1,2,3}`
summing to 8, enumerated all 16); n=4 all of `{0..4}` mult 1 (= the B80 **proved** tower, roots verified, `3c`);
n≥5 doubles the overlap `Sym²..Sym^{n−3}` (n=5: `Sym²`; n=6: `Sym²,Sym³`). **The "n≥6 doubling is open" worry is
resolved** (= the two-sequence overlap `[2≤d≤n−3]`).

**(3b) The "promotion" is a `Sym¹` ABSENCE (B111/B113 superseded).** There is no promotion. At n=3 the height-1
`char(−M)` is **`Sym³`'s** height-1 contribution (`(−1)¹φ^{3−2} = −φ`), not a "promoted `Sym¹`"; at n=4 all
modules are present, nothing is promoted. Height-1 behaviour is a **selection** (which `Sym^d` appear), never a
promotion. The "two separable halves" (sign + power) picture and the sign-conserving-promotion question are
**dissolved** — tombstoned in `speculations/TOMBSTONES.md`.

**(6) degree=rank = `Sym^n` presence.** `μ_n = 1` for all n≥2 (the `[2≤d≤n]` arm includes d=n) ⇒ **`char(Mⁿ)` is
always a tower factor** = degree=rank at the char-poly level. *Status precision (honoring the DO-NOT — not "by
dimension"):* `Sym^n` presence is dim-**forced** only at n=3 (the unique subset); at n=2,4 it is **rep-theory**
(B33/V18, B103), not a dim necessity; at n≥5 it is the **two-sequence form** (B103). **Path 4 (n=6 cross-check,
consistency not decisive):** the two-sequence predicts `|k|=3` total `= a₃+b₃ = 2+1 = 3` (= `max(n−d,1)`, the V17
correction); B66 (26/35, gauge-corrupted) measured 2 — the known under-count (B58 Phase A).

**The reframe + re-aimed prize.** The tower = the **Sym two-sequence** (one object); the prize is to prove `μ_d`
for all n (B103's standing open problem, the realization/trace-ring wall), not "close two halves." **B112
relabeled to three tiers** (the `−w₀` multiplicity structure up to the fixed-root label — proved all n; the
fixed-root labeling = B64, pending B118; the tower realization with powers — verified n≤5, superseded). Banked
V104; suite green; no physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

## 2026-06-07 — B116: reconcile θ-split (B112) vs Sym two-sequence (B103) — and a CORRECTION to B112

Ran the B112↔B103 reconciliation (to *join* the prize's two halves). It found a **verify-don't-trust
correction** instead, banked visibly (like V90/V91). **(1)** The **Sym two-sequence (B103/B58, V27 membership
rule) = the actual tower**: `sym_counts(5)` matches the resolved SL(5) tower (B61+B62) **exactly**, including
`char(M⁵)` — which is `Sym⁵`'s top weight, so the degree=rank top power is **automatic** on the Sym side (no
separate "promotion"). **(2)** The **θ-split (B112) equals the tower only `n ≤ 5`** (there `Sym = θ-split + one
degree=rank promotion`: agree on heights `2..n−1`, differ by one at height-1, plus Sym's `char(Mⁿ)`); **at `n=6`
they DIVERGE** — exactly the banked **V26/V27** (`a₁` 2v3, `a₂` 3v2, `b₂` 1v2; they agree on `a₃(n=6)=2`).

**Correction to B112 (explicit downgrade).** B112 proves the θ-split **combinatorics** (the `⌈/⌊` eigenspace
dims of `−w₀` on the `A_{n−1}` root spaces) for all `n` — **a real theorem that stands**. But the
**identification** of the θ-split with the **tower's** multiplicities (the long-standing V25 gap) holds only
`n ≤ 5`; at `n ≥ 6` it diverges from the Sym two-sequence. So **B112's "sign half proved for all n" → "sign half
proved for `n ≤ 5`; all-n OPEN."** Annotated V99, added a correction banner to B112 FINDINGS, banked V103.

**Re-aimed prize.** The **Sym two-sequence is the better tower-candidate** (= the actual tower wherever known +
carries `char(Mⁿ)` automatically), so **proving the Sym two-sequence for all `n`** (B103's open problem) is the
live route to the catalog — *not* the θ-split — with the `Mᵏ`-scalar arithmetic (B111) for the exponent. Suite
green; no physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

---

## 2026-06-08 — B123: m=1 arithmeticity (the third selection criterion) + the quantum/knot triage (V112, SUPPORTED)

**Context.** A Chat-2 triage of a quantum-tower / knot-invariant probing session, banked verify-don't-trust: **one
genuinely new finding** (m=1 is arithmetic, m≥2 are not — a third independent `m=1` selection criterion), **five
"standard theory in our notation" kills** (tombstoned so no future run re-derives them), **one honest tooling-gated
target** (the metallic phase-structure discriminator). Tier discipline held: finding → math/knowledge tier; kills →
dead-ends register; target → DORMANT pointer. Physics quarantined.

**Done:**

- **B123 (`frontier/B123_arithmeticity_m1/`, V112, `SUPPORTED`).** Computed in-house: the figure-eight complement's
  regular ideal-triangulation shape is the **6th cyclotomic** root `z₀ = e^{iπ/3}` (`z²−z+1 = Φ₆`), invariant trace
  field `ℚ(√−3)` → **arithmetic**; and the **order-6 echo** — the `(0,0,0)` non-void trace-map Jacobian spectrum
  (`λ³+1`, 6th roots, B122) sits at `κ=−2`, the geometric/parabolic cusp (B69/B109), the same `ℚ(√−3)` (banked as an
  **observation, not a connection**). Cited: **Reid (1991)** — the figure-eight is the *unique* arithmetic knot
  complement, so the `m≥2` metallic manifolds are not arithmetic. The `m≥2` trace-field non-arithmeticity *via the
  arithmeticity criterion* is the **named confirmation step** (SnapPy/Magma — the repo has no trace-field
  classifier), so the entry is `SUPPORTED`, **not** `TESTED-POSITIVE`. Self-correction held: used the rectangular
  form `½ + (√3/2)i` for the root (sympy leaves `exp(iπ/3)` unsimplified — cosmetic, math correct). 4 tests pass.
- **`knowledge/K009`** (written, non-stub): *Why m=1 is special — three independent selection criteria*: the
  **systole** (B92/S001, a metric), the **expansion threshold** (P004/B120, the dynamics), and **arithmeticity**
  (B123, the number field). Three different imports, each picking `m=1`; none collapses the family to a member as a
  theorem (`P000` stands). Added to `knowledge/INDEX.md`; `ARCHITECTURE.md` bumped to `K001–K009`.
- **Five kills tombstoned** (`speculations/TOMBSTONES.md`, one consolidated block): quantum tower `|λ|=1` =
  **unitarity** of the CS rep; finite-`k` eigenvalues = roots of unity (**tautological**, `q=exp(2πi/(k+2))` by
  construction); Kashaev → volume = the **volume conjecture** (cross-ref S027's scope-fence); the `z₀`/k=4 phase
  match = a **k=4 arithmetic coincidence** (`k+2=6=2·3`, cross-ref the CS-crossover Value-kill); "three regimes" =
  interpretation on the standard asymptotic expansion. *Not a kill (cross-ref):* the `det=−1` middle-eigenvalue `−1`
  is the proved **B121** parity (an asset).
- **S027 §3 sharpened** (DORMANT, tooling-gated): the metallic phase-structure comparison — compute the quantum
  phases + degeneracies at each `k` for the figure-eight, compare to other knots and to the metallic family m≥2; a
  clean **yes/no** discriminator (does the metallic structure fingerprint the quantum data?). **Gate stated:** needs
  SnapPy/Magma/state-integral code — *not* attempted in numpy+sympy. The "something is hiding" instinct is
  **relocated** here, as a specific computable comparison.

Suite green; physics quarantined; nothing to `CLAIMS.md`; P1–P16 untouched; the functorial `Sym(W)→trace-ring`
construction stays the un-lowered prize.

---

## 2026-06-08 — B124: reciprocal `(λ,1/λ)` pairs + time-reversal `λ↔1/λ` — two strictly-separated tiers (V113)

**Context.** A Chat-2 handoff on the user's "what if time flows both ways and we're in the positive branch" thread:
one computable **math** fact to bank (generic-symplectic), one **interpretation** to record (labeled, fenced), one
**metallic-specific** open thread to log DORMANT. Tier discipline is the whole point — the math fact and the
time-interpretation never share a sentence. Verified §1 (and the supplement's spectral counts) from scratch.

**Done:**

- **B124 (`frontier/B124_time_reversal_reciprocity/`, V113).** *Generic (symplectic), verified:* the SL(2) **void**
  Jacobian (`T(x,y,z)=(z,x,xz−y)` at `(2,2,2)`) has eigenvalues `{φ²,−1,φ⁻²}` — a reciprocal `(λ,1/λ)` pair + the
  self-reciprocal `−1`, `det=−1`; `(DT)⁻¹` carries the same (self-reciprocal) spectrum with stable/unstable **roles
  swapped**. This is symplectic geometry, **not** a metallic feature; the only metallic-specific datum is the **rate**
  `log φ²` (same lesson as the tombstoned unitarity / roots-of-unity / volume-conjecture kills). *Metallic-specific
  (the supplement), verified:* from `ρ_n=⊕Sym^d(M)^{μ_d}` (B103), at `det=−1` the tower carries **negative**
  reciprocal-pair modes (`char(−M^h)` sectors), `det=+1` carries **none** — a `det=−1` sign/chirality imbalance
  `O(n/2)` (= amphichirality B118/B121, via `char(M⁻¹)=char(−M)`). **Decisive recompute: expanding count == contracting
  count EXACTLY, every n (2..10), both det → NO arrow** — the asymmetry is **chirality (P)**, not time-direction (T).
  **Correction B confirmed:** the raw `±1` excess `N(+1)−N(−1)` **oscillates period-4** `[−1,0,1,0,…]` — NOT monotone
  `⌊n/2⌋`; distinct natural decompositions give distinct sequences (I independently got a third, `[0,1,3,4,4,5,7,8,8]`,
  for pos-minus-neg sectors), so the **exact constant is bookkeeping-dependent / open** — the closed form was **not**
  banked. 5 tests pass.
- **Tiers banked separately.** Math: an annotation in `knowledge/K008` (the reciprocal/time-reversal structure +
  the `det=−1` chirality residue, P-not-T). Interpretation: a **labeled** entry `philosophy/P006` — the "two-headed
  time" reading (Carroll–Chen / CPT-symmetric resonance), recorded as an overlay (generic-symplectic, not metallic,
  firewalled: iteration ≠ physical time), better-motivated than the matter-overlay but not load-bearing. Dynamics
  fork: `speculations/S002` **corrected to no-arrow** (the spectrum is exactly forward/backward symmetric) + the **one
  DORMANT metallic-specific thread** — does the seed select the low-entropy reference point (entropic) or is the fixed
  point only spectrally distinguished (prior: spectral/generic)? `ARCHITECTURE`/`PHILOSOPHICAL_PATHS` bumped to
  `P000–P006`; `CATALOG` S002 row updated.

Suite green; physics quarantined; nothing to `CLAIMS.md`; P1–P16 untouched; the functorial `Sym(W)→trace-ring`
construction stays the un-lowered prize.

---

## 2026-06-08 — Documentation refresh to B124/V113 (docs only, no math, no claims)

**Context.** The research had run well ahead of the governed documentation layer; this pass brought the layer up to
the current state and adopted the project's own logic throughout. No new mathematics; nothing promoted to
`CLAIMS.md`; the firewall and the standing prize unchanged.

**Done:**

- **`knowledge/` completed (the textbook layer).** Wrote all seven stubbed explainers — `K001` trace map &
  character variety, `K002` the metallic family & continued fractions, `K003` the Dickson tower, `K004` figure-eight
  / Dehn filling / A-polynomials, `K005` the opposition involution `θ=−w₀`, `K006` the 3d-3d correspondence (with its
  firewall, the one place the project touches physics literature), `K007` the Fibonacci/quasicrystal trace map. Each
  is self-contained: standard material cited to the literature, the project's own use cited by `B`/`V`, no new
  claims, never a premise. Updated `INDEX.md` (all nine ✓, with current anchors) and `GOVERNANCE.md` (WRITTEN).
- **`story/` extended.** Added chapter `09 — the representation, crystallized` covering the B111–B124 arc (the sign
  half proved all `n`, `ρ_n = Sym^n(W)` with `W=V⊕1` the external `det=−1` fundamental, the arithmeticity and
  time-reversal asides, and the functorial `Sym(W)→trace-ring` wall as the standing prize); refreshed `08 — where it
  stands` to fold in the crystallization and hand off to 09.
- **`docs/atlas/` refreshed** (it had frozen at the PC12 / Session-3 era). Added "the representation program
  (B59–B124)" to `SUCCESS_ATLAS`, the representation-program branch + spine to `RESEARCH_TREE`, a full
  representation-program vocabulary to `GLOSSARY`, and a "Pattern G — superseded framings & standard-theory kills
  (B111–B124)" block to `FAILURE_ATLAS` (the promotion-framing supersession, `θ→c`, `s_n→c`, the CS-crossover, the
  five quantum/knot kills, the `⌊n/2⌋` constant; plus the B121 det-parity *asset*, recorded so it is not re-killed).
- **`ROADMAP` refreshed.** Extended the Phase B probe ladder through B33–B124, updated the suite count (369 passed),
  and pointed the live center at `ρ_n` / the functorial wall.
- **Stale live ranges fixed** across `ARCHITECTURE`, `README`, `philosophy/PHILOSOPHICAL_PATHS`,
  `speculations/GOVERNANCE`, `knowledge/INDEX`, `knowledge/GOVERNANCE`: `S001…S021 → S001…S028`,
  `K001–K007 (stubbed) → K001–K009 (all written)`, `P000–P003/P005 → P000–P006`, `story 00–08 → 00–09`. Historical
  `CHANGELOG`/`PROGRESS_LOG` entries left as written (append-only).

Public-surface + no-hardcoded-paths scans green; no code touched, so the math suite is unaffected (369 passed, 1
skipped at B124). Nothing to `CLAIMS.md`; P1–P16 untouched; the functorial `Sym(W)→trace-ring` construction stays
the un-lowered prize.

---

## 2026-06-08 — B125: SnapPy arithmeticity of the metallic R^m L^m bundles — overturns K009 (V114, TESTED-POSITIVE)

**Context.** A correction handoff: SnapPy is now runnable in-sandbox, so the invariant trace field of the metallic
family is computable directly. Verify-don't-trust applied to the handoff itself — reproduced §1–§3 from scratch
before banking. MATH tier only; physics untouched; the functorial `Sym(W)→trace-ring` wall not touched.

**Done (verified):**

- **The spine** (numpy, exact): `M_m² = R^m L^m`, `tr = m²+2` (→ 3,6,11,18,27,38). The orientable metallic members
  ARE the once-punctured-torus bundles `R^m L^m`; `m=1` = the figure-eight (`m004`, vol 2.029883, build-checked).
- **The result** (SnapPy 3.3.2 + cypari, reproduced two independent ways — the shape field [Neumann–Reid] and the
  lift-independent traces-of-squares): **arithmeticity does NOT uniquely select `m=1`.** It is a **two-element
  selector `{m=1 golden `ℚ(√−3)`, m=2 silver `ℚ(i)`}`**; `m≥3` are non-arithmetic (`kM` not imaginary quadratic).
  The two arithmetic fields are distinct → different Bianchi families → not commensurable → two genuinely distinct
  arithmetic metallic manifolds (= the "exactly two arithmetic punctured-torus bundles" K009 already cited).
- **Honest scope** (verify-don't-trust on the handoff): the two arithmetic verdicts + the `m≥3` non-arithmetic
  verdict reproduce robustly; the *exact* `m≥3` field degree is primitive-element/precision-sensitive (I observed 4
  or 8; the canonical value is 6) — it does not move any verdict (>2 kills imaginary-quadratic), so it is not
  over-claimed.
- **The correction.** Overturns the B123/K009 "third *independent* / *unique* `m=1` arithmetic criterion," which
  mis-applied **Reid 1991** (a *knot* theorem) to *bundles*. Corrected `knowledge/K009` (systole + expansion still
  uniquely select `m=1`; arithmeticity is the two-element selector), `K002`, `K004`, `INDEX`; annotated the V112
  ledger row. **Preserved:** Reid 1991 stands (knots ≠ bundles; `m=2` being arithmetic confirms its scope — `m=2` is
  necessarily not a knot); the order-6 echo stays an observation.
- **Tooling note** (`REPRODUCIBILITY`): SnapPy 3.3.2 + cypari 2.5.6 installable/usable in-sandbox (the SnapPy gate is
  lifted; the documented gotchas recorded); MAGMA is NOT installable (license-gated) — genuinely MAGMA-only work
  stays parked for *no tool*. The B125 test skips its live recompute when SnapPy is absent (`importorskip`) so the
  suite stays green without it.

Nothing to `CLAIMS.md`; P1–P16 untouched; the functorial `Sym(W)→trace-ring` construction stays the un-lowered prize.

---

## 2026-06-08 — B126: the ladder to physics — how far does the metallic rigidity propagate? (V115)

**Context.** The user's foundational question ("what do we lack for a bridge to fundamental physics; what question
are we posing wrong?"), run in "hardworking mode" with a five-agent literature fleet + direct computation, and
synthesizing two exploration threads (compute-first; the four-floor ladder). Precondition agreed: a clean negative is
a real result. MATH/number-theory tier; physics readings firewalled.

**The answer (literature-grounded + computed).** The metallic object's *classical* rigidity propagates **exactly two
floors** up the ladder (quantize → 3d `T[M]` → 4d → particle content), provably, then hits a **nameable** wall:
- **Floor 1 — arithmetic → quantization:** the invariant trace field determines the *field* of the perturbative
  quantum series — a THEOREM (Dimofte–Garoufalidis arXiv:1202.6268/1511.05628), **proven for our exact family**
  (once-punctured-torus bundles, Yoon arXiv:2110.11003: 1-loop = adjoint torsion). Caveat: the trace-field-valuedness
  is *universal*, so imaginary-quadratic / Bianchi fields are NOT "quantum-special" — the one untested door is the
  `K₃`/Bloch grading on `ℚ(√−3)`/`ℚ(i)`.
- **Floor 2 — Mostow → `T[M]` rigidity:** no marginal couplings; `M` selects the SUSY phase (`4₁` has irreducible
  flat connections → unbroken SUSY, gapped vacua, Cho–Gang–Kim arXiv:2007.01532); `H₁` torsion → one-form/center
  symmetry / line-operator spectrum (DGG; Aharony–Seiberg–Tachikawa; arXiv:2511.13696). `T[M]` is a concrete rank-1
  **abelian** 3d N=2 SCFT.
- **The wall:** 3d→4d (the 4d theory is data of the 2d *boundary* `∂M`, not `M`; ceiling N=4 SYM / N=2\*,
  Kapustin–Witten) + the SUSY-breaking *scale* (orthogonal input — no manifold mechanism). **So we lack no concept; we
  lack what no 3-manifold can carry.**

**Computed in-house (verify-don't-trust):**
- **(A)** `H₁(M_m) = ℤ ⊕ (ℤ/m)²` — PROVED by the Smith normal form of `M_m²−I = m·M_m` (invariant factors `(m,m)`),
  confirmed by SnapPy `m=1..7`. The metallic `m` *is* the order of the homology torsion. (Verifies a cross-chat
  observation; the SU(m)/Standard-Model reading is the firewalled `S029`.)
- **(B)** arithmetic(`m=1,2`) ⟺ `κ` rational in z on the geometric component (κ-degree over `ℚ(z)` = `[1,1,3,3,7,6]`,
  m=1..6; m≤4 computed exactly, the jump is at the arithmetic boundary m=2/3). **Family-specific, not a law** — the
  literature has no "arithmetic ⟺ simple A-poly" theorem.

**Banked:** B126 (probe + FINDINGS + README + test); `speculations/S029` (the center-symmetry reading, POSTULATED,
five kill conditions); `philosophy/P007` (the maximal-probe reframe; the right question is "how far does rigidity
propagate", answered); `speculations/LADDER_LITERATURE.md` (the five-agent citation map); the `PHYSICS_BRIDGE_MAP`
ladder section; CATALOG S029. **Correction:** the inherited "exactly two arithmetic punctured-torus bundles" framing
is an off-by-one (BMR 1995 = three commensurability classes; the figure-eight + sister m003 are two bundles in one
ℚ(√−3) class) — corrected across K009/K002/B125. `ARCHITECTURE`/`PHILOSOPHICAL_PATHS` bumped to `P000–P007`; CATALOG
to `S001…S029`.

Nothing to `CLAIMS.md`; P1–P16 untouched; the functorial `Sym(W)→trace-ring` construction stays the un-lowered prize.

---

## 2026-06-08 — B127: chirality, Fibonacci, arithmetic, and the object's proper name (V116)

**Context.** A CC handoff resolving the "threads 3 & 4 + Fibonacci" investigation, audited letter-by-letter
(verify-don't-trust on the handoff itself — every computational claim re-derived in-sandbox; two citation errors in
the merged B126 caught and fixed). The user's brief: co-researcher not just banker; brave but standards-strict. Net:
the physics-bridge claim is a **clean, multiply-confirmed negative**, and the strongest survivor is the object's
**proper name**.

**Audit result — all computational claims verified.** CS≡0 for the metallic bundles `M_m²=R^m L^m` (machine zero,
m=1..6) against a discriminating census mix (m003=4.93, m004=0, m006=−2.25); the Fibonacci fusion matrix = the golden
substitution matrix; k=3 from 2cos(π/5)=φ; Yang–Lee `c=−22/5` vs Fibonacci `c=+14/5`; the arithmetic separation
`ℚ(ζ3)∩ℚ(ζ5)=ℚ`; the cusp cutoff `a+1/a=3−n` reproducing n∈{3,4} (n=5→a=−1, the B95 degeneration); the null scale
test; and the **three BMR arithmetic classes named** `RL→ℚ(√−3)`, `RRLL→ℚ(i)`, `RRL→ℚ(√−7)` (√−7 non-metallic).
Chat-2's kills are **rigorous, not paranoid**.

**Banked:**
- **B127** (probe/test/FINDINGS/README): M-1 fusion-algebra; M-2 the **CS=0 achiral locus**; M-3 expansion ⊥
  unitary-topological-order (+ the new `λ_m<2`-only-m=1 anyon obstruction); M-4 the arithmetic trichotomy; the
  Fricke–Vogt dictionary; central charges; the null scale test; BMR three classes.
- **The proper name** (the headline positive, full knowledge + philosophy entry per the user's choice):
  `knowledge/K010` — the metallic-mean Schrödinger cocycle / KKT trace map / Fricke–Vogt invariant; the
  `κ=2` (periodic AC) / `κ>2` (Cantor, Damanik–Gorodetski horseshoe) dictionary; "non-cancellation = Fricke–Vogt
  positivity = Cantor spectrum." `philosophy/P008` — the principle named; emergent aperiodic-order physics,
  firewalled from fundamental.
- **Four kills tombstoned** (K-A/K-B/K-C/K-D/K-E) with their killing computations; `S030` the Fibonacci/Yang–Lee
  two-categorification fork (DORMANT, fusion-rule-only). `S029`/`P007` sharpened (even the topological-matter landing
  is non-unitary/achiral; the anyon link is fusion-algebra-only). A subtlety handled: B124's *algebraic* tower
  P-parity vs B127's *topological* CS chirality are orthogonal and both stand.
- **Citation fixes** to the merged B126: re-attach Floor-2 SUSY from the mis-attached Cho–Gang–Kim arXiv:2007.01532
  (which is non-hyperbolic→unitary, actually supporting K-D) to Gang–Yonekura arXiv:1803.04009 (tag downgraded);
  split "Generalized Global Symmetries of T[M]" into Part I (2010.15890=JHEP04(2021)232) / Part II
  (2511.13696=JHEP05(2026)087) across S029/LADDER_LITERATURE/PHYSICS_BRIDGE_MAP/B126. `K001–K010`, `S001…S030`,
  `P000–P008`.

MATH + emergent-physics tier; physics POSTULATED/quarantined; nothing to `CLAIMS.md`; P1–P16 and the functorial
`Sym(W)→trace-ring` wall untouched.

---

## 2026-06-08 — B128: the symmetry-breaking landscape — chirality recursion, the order parameter, the torsion firewall (V117)

The arc *after* B127/K010, internalized from a cross-session handoff and **re-derived in-sandbox** (verify-don't-trust)
on validated controls with the **correct** chirality test. **Result:** the metallic structure **permits symmetry
breaking but never forces it** — composition into a generic *order* can break parity (CS≠0), but every
structure-preserving operation keeps the object achiral and *which* arrangement breaks is a free ordering choice.

- **Method bug (propagated as a `REPRODUCIBILITY.md` SCAN):** naive `is_isometric_to(mirror)` is orientation-blind →
  **false positives** on known-chiral m015/m016/m009; raw CS sign unsafe. Correct test:
  `symmetry_group().is_amphicheiral()` gated on `is_full_group()`. Re-verified controls in-sandbox.
- **B128** (probe/test/FINDINGS/README): **M-A** the **chirality recursion theorem** — `W=R^{m₁}L^{m₁}…R^{m_k}L^{m_k}`
  achiral ⟺ the block-sequence `(m₁…m_k)` reversal is a cyclic rotation (15/15 SnapPy across k≤4 + structural reason);
  **M-B** the order parameter is the **ordering**, not the count (balanced #R=#L=6 triples that are chiral); **M-C** the
  exact `Z₂` (block-reversal negates CS to machine zero). Banked as `knowledge/K011` (sharpens B127/M-2: pure metallic
  words = the k=1 corner).
- **Tombstone K-F:** "single torsion `ℤ/n` → `SU(n)` center → gauge bridge" — DEAD, (1) torsion tracks
  periodicity/symmetry-order not chirality (single torsion in both achiral `RRLLRRRLLL` and chiral `(1,2,3)`; doubling
  is the periodic case), (2) center≠gauge (S029/S030). `speculations/TOMBSTONES.md` + S029 cross-ref.
- **Firewall — fifth direction:** `P007`/`P008` sharpened — the symmetric object **cannot force its own breaking**;
  existence inevitable, specific physics a contingent SSB selection. `K001–K011`, `S001…S030`, `P000–P008`.

MATH + a firewalled SSB-sharpening tier; physics POSTULATED/quarantined; nothing to `CLAIMS.md`; P1–P16, the functorial
`Sym(W)→trace-ring` wall (B85), and the merged B127/K010/P008/S030 untouched.

---

## 2026-06-08 — B129: the SL(3) tower is sealed in ℚ(√−3) — the firewall from inside the tower (V118)

The arc *after* B128, internalized from a cross-session handoff and **re-derived in-sandbox** (verify-don't-trust).
**Does climbing the SL(n) tower produce new content, or is it the single SL(2) Fibonacci datum in larger irreps?** The
latter — the **sixth** firewall direction, the first from *inside* the tower.

- **S1a (EXACT, the load-bearing leg):** the principal `Sym²` metallic SL(3) rep is **irreducible** (algebra = `M₃`)
  yet **every trace lies in ℚ(√−3)** (`trA=trB=3`, `trAB=½−(3√3/2)i`, `trA⁻¹B=9/2+(5√3/2)i`, `tr[A,B]=½+(3√3/2)i`).
  SL(2) arithmetic in SL(3) clothing — no new field/generator/modulus.
- **S1b (computer-assisted, a distribution):** off-sublocus root-find `tcoords(A,B)=tcoords(AB,A)` over the 4-dim
  bulk; a 15-seed scan gives 427 converged fixed points, **max distance-to-ℚ(√−3) = 1.2e-6**, 0 beyond 1e-5 → **0
  escapes**. Genuine content = the `Sym²` image (S1a).
- **Covers correction (strengthens S029):** the firewall is **abelian × discrete, not "rank always 1"** — a
  chat-only over-claim. Single bundles are 1-cusped rank-1, but covers reach rank 2 (silver `b++RRLL` degree-2 →
  `(2,2)`); rank grows by **replication** only.
- **Two method bugs banked (REPRODUCIBILITY SCAN):** B1 the `inQ3` detector (accept rationals; small `maxden` — a
  large one approximates any real); B2 saddle fixed points (root-find, not iterate; the rep is unipotent so `|eig|=1`
  can't separate genuine from trivial; robust **polished-distance** escape test).
- **Verify-don't-trust correction:** the handoff's clean 22/56/0 reducible/finite/genuine split did **not** reproduce
  (the search rarely converges to the genuine saddle); the robust S1b evidence is the **distance distribution** + the
  **exact** S1a. Conclusion (0 escapes; sealed in ℚ(√−3)) is the same. Banked `knowledge/K012`; capstone
  `speculations/S031` (open MATH, **not** a bridge); `P007` sixth direction. `K001–K012`, `S001…S031`, `P000–P008`.

MATH tier; physics POSTULATED/quarantined; nothing to `CLAIMS.md`; P1–P16, the functorial `Sym(W)→trace-ring` wall
(B85), and the merged B124–B128 (K010/K011/P007/P008/S029/S030) untouched.

---

## 2026-06-08 — B130: no forced choice in the invariant ring — the seventh firewall form + the located which-seed fork (V119)

The arc *after* B129, internalized from a cross-session handoff and **re-derived in-sandbox** (verify-don't-trust;
the handoff itself carried a killed false-positive, K-G). The firewall question driven to its deepest **forced-answer**
form: **does the structure carry an invariant that is *both* discretely multivalued *and* unsymmetrizable** — the exact
object a forced choice requires? In the trace-ring invariants, **no** — the **seventh** firewall direction, the
sharpest (not "does it reach physics" but "can it ever be made to choose").

- **No forced choice (κ free on the fixed locus):** adjoin `k=κ`, eliminate `(x,y,z)` from `φ_m(x,y,z)=(x,y,z)`; the
  `k`-only elimination ideal is **empty** (m=2,3,4 symbolic; m=5 a 259-value numerical continuum) → κ varies
  continuously, no discrete value to select. Chirality is multivalued but the `Z₂` mirror relates its values (B128).
- **The located fork:** within a fixed m the substitution `a→aᵐb,b→a` is the **unique deterministic** word; across m,
  `trace=m` distinct → **not GL(2,ℤ)-conjugate** (Perron fields ℚ(√(m²+4))) — a genuine discrete fork, but it is the
  **external seed label** (which structure exists), not a choice a unit makes from inside.
- **Reading:** the structure is a **moduli space** (continuous κ × discrete seed-label) — *parametrizes, does not
  choose*; the root of "permits but never forces" (B128). Banked `knowledge/K013`; `P007` seventh direction; `P008`
  the root.
- **Tombstone K-G:** "forced choice from isolated fixed points at m≥2" — DEAD (the *revival* failure mode): `sp.solve`
  mislabeled **curve degeneracies** as isolated points (empty κ-elimination → κ free), and the symmetry argument was
  circular. Method note → REPRODUCIBILITY (use the κ-elimination ideal + Jacobian rank, not `sp.solve` branch-counting).
- **Foundation cross-check (honored, not re-banked):** the arithmetic-complexity-vs-m law is B126's κ-degree
  `[1,1,3,3,7,6]`; a separate "field-degree vs m" algdep attempt was a noisier proxy (precision artifact) — B126 owns
  it.
- **Forward program `speculations/S032` (open MATH, not a bridge):** (A) the theorem-version (no invariant *whatsoever*
  is forced); (B) the two-seed question — does gluing `M_{m₁},M_{m₂}` along their cusp tori create an *internal* fork
  (is the minimal multiplicity for an internal forced choice **two**?), detector = the 0-dim part of the gluing
  character variety via κ-elimination + Jacobian rank. Co-researcher emergent insight (the moduli-space framing; the
  S031+B130 vertical/internal rigidity synthesis) banked in FINDINGS/S032. `K001–K013`, `S001…S032`, `P000–P008`.

MATH tier; physics POSTULATED/quarantined; nothing to `CLAIMS.md`; P1–P16, the functorial `Sym(W)→trace-ring` wall
(B85), and the merged B124–B129 (K010/K011/K012/P007/P008/S029/S030/S031) untouched.

---

## 2026-06-09 — B131: two-seed gluing creates an internal discrete fork — heterogeneity makes a choice (answers S032-B) (V120)

The autonomous continuation after B130 (the user chose "push into the amalgam"). B130 located the question: a single
metallic seed is **internally fork-free** (κ free; only fork = the external seed `m`). **S032-B** (the precise form of
the standing "minimal multiplicity to become more" intuition): does combining two distinct seeds create an *internal*
fork? **Answer: YES — and it is heterogeneity, not multiplicity.** Re-derived in-sandbox (verify-don't-trust).

- **Mechanism (proven):** each seed's fixed locus is a 1-dim curve whose boundary data `(κ, trT)` traces an
  **A-polynomial curve** in the 2-dim boundary-torus character space; gluing matches the curves. **Same seed → same
  curve → continuum** (no fork); **distinct seeds → distinct curves → 0-dim intersection → discrete fork.**
- **A-poly curves validated** two independent ways: m=1 `κ=trT⁴−5trT²+2` (**B67**), m=2 `κ=trT²−6` (**B69/V33**),
  re-derived here from explicit SL(2,ℂ) matrices (residual ~1e-14); m=3 irrational (B69 double cover).
- **Forks:** (1,2) **exact** `{−4,−2}` (both irreducible, κ≠2); (1,3) 6 values, (2,3) 4 values (numerical). `κ=−2` =
  shared complete-cusp config; the others genuine. By B130's definition a forced choice exists.
- **K-G discipline applied:** the discreteness is a genuine transversal 0-dim intersection (not a curve degeneracy);
  all fork points κ≠2 hence irreducible.
- Banked `knowledge/K014` (choice from heterogeneity, companion to K013); resolved `speculations/S032` Target B (YES;
  Target A still open); `P008` Coda 3 (choice is born from the interaction of *different* units). `K001–K014`,
  `S001…S032`, `P000–P008`.

The reading: a single seed is a **moduli space** (parametrizes, does not choose, B130); two **distinct** seeds glued
create **discreteness** — choice is emergent/relational, born from heterogeneity. Emergent aperiodic-order / 3-manifold
mathematics — **not** a physics bridge. MATH tier; physics POSTULATED/quarantined; nothing to `CLAIMS.md`; P1–P16, the
functorial `Sym(W)→trace-ring` wall (B85), and the merged B124–B130 untouched.

---

## 2026-06-09 — B132: the quantum layer — eigenvalue field-fusion, chirality-arithmetic, quantum selection criteria (V121)

Internalizes a cross-session "Chat-1" handoff (10 results) built on a **stale snapshot** (pre-B130/B131), **re-derived
in-sandbox** (verify-don't-trust). **Reconciliation:** B130/B131 already merged; the handoff's "KEY" Step 17 (two-seed
internal fork) **is** B131 (already done) — this quantum batch is its **companion** at the quantum level. Renumbered to
B132 / K015,K016 / P009 / V121.

The new content is a **quantum layer**: the SU(2)_k WRT data `Z_k` of the metallic bundles (validated convention: `R=T`,
`L=STS⁻¹`, framing-free `T`; eigenvalue-order method, exact). **Headline — chirality shifts the eigenvalue arithmetic:**
at k=4, achiral/same-seed compositions → **ℚ(√−3)**; chiral/cross-seed → **ℚ(ζ₁₂) fused and the partition function
vanishes** (`|Z|=0`). The quantum companion of B128 (chirality recursion) + B131 (classical fork).

- **Verified:** S1c field-fusion m=1..7 (m≡2 mod 4 → ℚ(i)); S7 the chirality-arithmetic table; S1a `Z_{k=4}(M_1)=ω`;
  S3a pure-phase `|Z|=1` m=1-unique; S2 vanishing period `=|O_K^×|/2` (m=1→3, m=2→2, m=3/4 aperiodic); S4 two scales by
  m mod 4; S5 chiral fragility (non-cancellation selects the symmetric vacuum); S6 silver↔L5a1 commensurability; S8 the
  Lee–Yang σ₃ realization (`d_τ=−1/φ`).
- **Quarantined (verify-don't-trust):** S9 (RRL κ-degree=3 refutes the criterion) did **not** reproduce — got degree
  1/2 (convention-dependent), never 3; not banked.
- Banked `knowledge/K015` (chirality-arithmetic field-fusion) + `K016` (m=1 criteria, +2 quantum); `philosophy/P009`
  (Monadic Closure as a firewalled synthesis — the seven closures reduce to ~3 root causes, **not** a theorem);
  upgraded `speculations/S030` DORMANT→**TESTED-POSITIVE** (Lee–Yang computed) + `K010` reference. `K001–K016`,
  `S001…S032`, `P000–P009`.

The native physics is the **Lee–Yang edge** (emergent non-equilibrium criticality), not the Standard Model. MATH /
quantum-topology tier; physics POSTULATED/quarantined; nothing to `CLAIMS.md`; P1–P16, the functorial
`Sym(W)→trace-ring` wall (B85), S031, and the merged B124–B131 untouched.

---

## 2026-06-09 — B133: scope-correction to merged B132/K015 — "chirality shifts the arithmetic" is a quantum-group artifact (V122)

**Verify-don't-trust applied to the project's own merged work** (the same correction discipline applied to incoming
handoffs, now flowing toward the repo). A correction handoff flagged that B132/K015's headline — *"chirality shifts the
eigenvalue arithmetic (achiral→ℚ(√−3), chiral→ℚ(ζ₁₂))"* — is false. **Verified in-sandbox and confirmed (and extended).**

- **The decisive control** (k=4, `is_amphicheiral`-verified): **achiral words alone span all three fields** —
  `RRLL`→ℚ(ζ₁₂), `RRRLLL`→ℚ(√−3), `RLRLRL`→ℚ. So the field tracks the **word's spin-content mod 4** (the SU(2)_k
  T-twist), **not** chirality, **not** the manifold. The eigenvalue *orders* are correct; the *attribution* was the
  artifact (chirality was confounded with composition).
- **Extended beyond the handoff:** the k=4 **vanishing** is also not chirality-linked (achiral `RRLRLL`,`RLRRLL`
  vanish) — so **S5 chiral-fragility is also withdrawn**, not just restated.
- **Banked:** rewrote `K015` (quantum-group field content, not chirality; kept the eigenvalue-order method + m-mod-4
  mechanism + the control); withdrew S7/S5 in the B132 probe/FINDINGS/README + tests; **tombstone K-H** (third
  recurrence of this field-fusion artifact; sibling of K-G); **REPRODUCIBILITY MB6** — *reproduction is not
  interpretation; run the control*. Annotated V121. (Also fixed a latent `_field` bug: order-2-only → ℚ rational.)
- **Confirmed solid, untouched:** P009 (Monadic Closure scrutiny), the S9 quarantine, S1a/S2/S3a (single-seed m=1),
  S6, S8/Lee–Yang/S030. Classical trace fields stay disjoint (ℚ(√−3)∩ℚ(i)=ℚ; B125/B129).

Within-MATH-tier correctness fix; nothing to `CLAIMS.md`; P1–P16, B85, S031, and the merged B124–B131 untouched.
This is Phase A of the approved program (correction + paths 1/2/4: novelty audit, one proof, Lee–Yang; paper deferred).

---

## 2026-06-09 — B134: the chirality recursion PROVED (corollary of GHH 2008) + the novelty audit (V123)

Phase B (novelty/literature audit) + Phase C (one proof) of the approved program. A deep adversarial literature pass
(deep-research workflow: 102 agents, fan-out → fetch → 3-vote verify → cited synthesis) placed the project's three
candidate-novel results against prior art; banked the audit and **proved** the one novel kernel.

- **Novelty verdicts** (`docs/NOVELTY_AUDIT.md`): **R1** chirality recursion — PARTIALLY-KNOWN (mechanism = Goodman–
  Heard–Hodgson 2008's anti-palindromic-word criterion; the integer-block-length lift is the novel kernel); **R2**
  two-seed fork — KNOWN (Kitano–Nozaki 2020), with a framing qualification (discreteness is gluing-map-driven, not
  distinctness; "heterogeneity" is identity-gluing-specific); **R3** SU(2)_k field content — KNOWN/standard (Jeffrey
  1992; Dong–Lin–Ng 2015; Lawrence–Zagier 1999) — confirming the B133 correction.
- **The theorem (proved):** metallic-block bundle `R^{m₁}L^{m₁}…R^{m_k}L^{m_k}` is **amphichiral ⟺ the block-length
  sequence is a cyclic palindrome.** Proof: GHH give amphichiral ⟺ word anti-palindromic; `reverse(W)` and `swap(W)`
  are both `LᵃRᵃ`-block words, matching cyclically iff the block-length sequences agree up to rotation. **∎** Verified:
  the lemma holds exhaustively (5460 sequences) + SnapPy three-way agreement (16/16). **B128/K011 upgraded from
  computer-assisted (15/15) to PROVED.**
- **Reconciliations:** K011 → PROVED (cite GHH); K014/B131 annotated (Kitano–Nozaki + the gluing-map qualification,
  verified: swap-glue same-seed → degree-16 discrete); K015/K010 → R3 standard citations. `K001–K016`, `S001…S032`,
  `P000–P009`.

The honest net: of the three, two are known and one has a now-proved novel kernel — exactly what an audit should
surface. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, S031, and the merged B124–B133 untouched.

---

## 2026-06-09 — B135 + B136: the Lee–Yang bridge is m=1-specific; amphichirality for all LR words (V124, V125)

The last two approved paths (Phase D, then the generalization of the proved chirality theorem), banked together.

- **B135 (Phase D — Lee–Yang, V124).** The Lee–Yang bridge is **m=1-specific**: only `λ₁=φ<2` is a quantum dimension
  (`2cos(π/(k+2))<2` ⟹ m=1); m≥2 (`λ_m>2`) cannot be → **no metallic family of Lee–Yang CFTs**. The metallic *family*
  is the spectral/quasicrystal one (`K010`, ℚ(√(m²+4))). The single golden bridge (m=1 → M(2,5)) holds at
  **modular-data level** (σ₃ Galois conjugate Fibonacci→Yang–Lee: `d_τ=−1/φ`, S-matrix, `c=−22/5`, `c_eff=2/5`) —
  stronger than fusion-rule-only, but not a full RCFT identification. `S030` sharpened (m=1-specific, modular-data,
  emergent, firewalled). Standard modular data: Jeffrey 1992 / Dong–Lin–Ng 2015 / Lawrence–Zagier 1999.
- **B136 (generalization of the proved theorem, V125).** Extends B134's metallic recursion to **any** LR word:
  `R^{a₁}L^{b₁}…R^{a_k}L^{b_k}` is **amphichiral ⟺ the block-pair sequence `((a_i,b_i))` is fixed up to cyclic rotation
  by (reverse order + swap each `(a,b)→(b,a)`)**. Proved as a GHH-2008 corollary in block-pair form; reduces to B134's
  cyclic palindrome on the metallic locus `a_i=b_i`. Verified: lemma exhaustive (7380 sequences) + SnapPy on metallic
  and **non-metallic** words. `K011` generalized. Honest novelty: a clean restatement/generalization of GHH's
  criterion, not a new 3-manifold theorem.

This completes the approved program (Phases A–D + the generalization; paper deferred). `K001–K016`, `S001…S032`,
`P000–P009`. MATH (+ emergent-physics, firewalled) tiers; nothing to `CLAIMS.md`; P1–P16, B85, S031, the merged
B124–B134 untouched.

---

## 2026-06-09 — B137: S031 sealing extended to m=2 (silver, SL(3), ℚ(i)) + the reducible-filter (MB7) (V126)

A "push further" increment on the **S031** capstone (the SL(n) sealing). B129 verified m=1 at SL(3) (ℚ(√−3)) and left
m≥2 undone; this closes m=2 (silver, ℚ(i)).

- **Result:** the SL(3) tower is sealed in `K_m` for **both arithmetic metallic members** — m=1 in ℚ(√−3) (reproduces
  B129) and **m=2 in ℚ(i)** (new): among **irreducible** off-sublocus fixed points, **0 escapes** from the SL(2) trace
  field (2 seeds each). Strengthens S031 from {m=1} to {m=1, m=2}; theorem-version (all m,n) stays open.
- **Verify-don't-trust catch (MB7):** a naive search nearly read as "S031 false for m=2" (16 escapes, dist 0.004) —
  but the escapes were all **reducible** degenerate points (algdim 7, `trA=−1`, `|eig|=1`, well-converged), whose `κ`
  isn't constrained to `K_m`. B129's m=1 missed this only because its reducibles are rational (∈ ℚ(√−3)). Guard:
  count escapes only among **irreducible** (algdim=9) points; then m=2 seals. → `REPRODUCIBILITY.md` MB7 (sibling of
  MB2/K-G/K-H).
- Banked B137 (probe/FINDINGS/README/test); S031 evidence extended; m≥3 (non-quadratic `K_m`) and SL(n≥4) flagged open.

MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B136 untouched.

---

## 2026-06-09 — B138: S031 push — principal-image direction PROVED (all n); SL(4) bulk obstruction; object-clarification (V127)

Pushing S031 further: into SL(4), then toward the proof. The honest outcome:

- **Principal-image direction PROVED (all n)** — the *easy half* of S031: the principal `Sym^{n−1}` image of an SL(2)
  rep over `K` is a `K`-sealed fixed point for every n, because `Sym^d` is **ℤ-defined** (its matrix entries are
  integer polynomials in `g`'s entries), so `g∈SL(2,K) ⟹ Sym^{n−1}(g)∈SL(n,K)` and all word-traces ∈ K. Verified
  symbolically n=2..5 for m=1 (ℚ(√−3)) and m=2 (ℚ(i)). The open **converse** (nothing *else* escapes) is the hard half.
- **SL(4) bulk: intractable in-session (honest negative).** The B137-style off-sublocus root-find at SL(4) times out
  with a faithful 340-word residual and under-pins the character with a lighter one — SL(4) sealing evidence not
  obtained (needs a complete SL(4) trace-coordinate set; NEEDS-EXPERTISE).
- **Object-clarification (a verify-don't-trust note on my own reasoning):** S031 is about the **discrete** trace-map
  fixed points `(A^mB,A)` (B129/B137), *not* B71's positive-dim **geometric** components (V0/W1/W2). A generic
  geometric-component point has continuous traces (no number field) → `realize_bundle_rep` returned "OTHER" and does
  not test sealing. (I briefly conflated these; caught and banked.)

**S031 status:** principal direction PROVED; SL(3) full sealing verified m=1 (B129), m=2 (B137); SL(n≥4) + the all-n
converse OPEN. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B137 untouched.

---

## 2026-06-09 — CHAT-1 LEADS REGISTER: selective registration (open-lead catalog, MB8, S033)

Cross-checked the **CHAT-1 LEADS REGISTER** (a ~23-thread quantum-layer triage) against the repo and registered
only the **non-duplicate, non-stale** leads — *not* the whole doc (much was already banked or refuted):

- **`docs/OPEN_LEADS.md`** (new) — the live open-lead catalog. Carries §B/§D open leads as rows: **L6**
  non-metallic sealing (★★★, the genuine S031 generalization), **L5** its SL(3) scout, **L7** one-theorem capstone
  (★★★), **L8** chiral compositions, **L10** classical field-fusion (likely negative), **L11** rank-2 covers.
  Records dispositions so nothing is re-run: **L1–L3** BANKED (K016), **L9** BANKED (B132 S6), **L12** WITHDRAWN
  (K-H), and **L4** ("chiral fragility") **WITHDRAWN (B133)** — the k=4 vanishing is composition-driven, not
  chirality (control: achiral `RRLRLL`,`RLRRLL` also vanish).
- **`REPRODUCIBILITY.md` — MB8** — "a generic/necessary feature is not a discriminating/sufficient one — check the
  null case." The CHAT-1 §E guard; banked as **MB8** (its doc-label "MB7" collided with the existing reducible-locus
  MB7). Sibling of MB6 (missing control ↔ missing null case).
- **`speculations/S033`** (new, FIREWALLED) — "Gate-1": the Whitehead-link cusp-swap-as-Weyl-reflection probe.
  Prior LOW (abelian wall, sibling of S029/S028), tool-gated (Sage/GKLP), unrun; even a "yes" is emergent and
  carries no chirality. CATALOG updated (`S001…S033`).

No frontier probe (bookkeeping/registration, not a computation); no `CLAIMS.md` change; P1–P16, B85 untouched.

---

## 2026-06-09 — B139: "SM through multiplicity" — firewall cartography (NOT a crossing) (V128)

Banked three Chat-2 informatory calculations decomposing *"can multiplicity produce the Standard Model?"* as
**cartography of the firewall** — a sharper statement + one guard + one open probe. **Firewall-CONFIRMING, not a
result, not a physics crossing.** The CHAT-1 leads registration (above) is folded into this PR.

- **The sharper firewall statement (S029 framing note).** Multiplicity permits MORE structure (more abelian
  couplings = cusp count, a discrete trace-fork B131, chiral objects = CS-sign) but cannot permit the TWO
  SM-distinguishing structures: a **simple non-abelian factor** (contingently blocked; Gate-1/`S033`) and
  **irreducible chirality** (structurally blocked).
- **Item 1 — chirality articulation (VERIFIED), `philosophy/P009`.** The SM-side face of `det=−1→CS=0`: the mirror
  (`swap_{R↔L}∘reverse`) sends the monodromy `M→Mᵀ` (since `L=Rᵀ`), preserving trace/charpoly/Perron-field/volume
  and only flipping the CS sign — **chirality is a CS-sign, not an inequivalence.** Verified for 6 chiral words
  (universal for achiral too); SnapPy: vol invariant, CS flips, `H₁` invariant. **Load-bearing caveat banked:**
  "structurally blocked" = blocked at all *standard* invariants, **not** a proof no invariant distinguishes. (Also
  fixed a B133 leftover in P009 — the withdrawn "chirality fuses the eigenvalue field" line.)
- **Item 2 — MB9** (`REPRODUCIBILITY.md`): a non-abelian symmetry **group** ≠ non-abelian **gauge** content (the
  firewall is on the abelian × discrete trace-ring/`T[M]`, not the monodromy group). Cluster MB6/MB8/MB9 = "right
  object, wrong level."
- **Item 3 — open lead B139-G** (`docs/OPEN_LEADS.md`): does the chirality block survive the **genus ladder**?
  (genus-1 special; the falsifier for Item 1; trace-level, unrun; a break gives only *emergent* chirality).

MATH tier (cartography); nothing to `CLAIMS.md`; P1–P16, B85, S031, the merged B124–B138 untouched. Ledger
**V128**. `frontier/B139_firewall_cartography/` + `tests/test_b139_firewall_cartography.py` (4 tests, green).

---

## 2026-06-09 — B140: compute-session reconciliation (close B139-G, reframe S031, sharpen B138, record RᵐLᵐ + fields) (V129)

A Chat-2 compute session reconciled against the repo. **Subtractive/clarifying** — close one open lead, retract one
(never-banked) over-claim, tighten two framings, record two facts. **No new frontier claim.** All load-bearing items
re-derived in-sandbox (sympy-exact).

- **Item 1 — B139-G CLOSED (genus-general).** The chirality firewall has no genus gap: the mirror = the standard
  **orientation-reversal theorem** (same volume, opposite CS, conjugate-isomorphic trace field) — **genus-independent**.
  The genus-1 `M→Mᵀ` is a genus-1 *mechanism*; the conclusion is general. Confirmed genus-1 bundles + chiral knots
  (vol same / CS opposite); the genus-2 numeric is theorem-backed (twister/Sage absent). `OPEN_LEADS` → ANSWERED;
  `P009` + `S029` caveats updated (residual caveat = the general "no *cleverer* invariant" one).
- **Items 2–3 — reframe S031 + sharpen B138 (φ vs φ²).** `N=[[m,1],[1,0]]` has `det=−1` and `N²=RᵐLᵐ`, so `φ_m` (det −1)
  has **discrete** fixed points (S031's object) while `φ_m²` (the bundle) has a **positive-dim** fixed locus (B71). The
  unique irreducible φ-fixed point is the **rational** `Sym²(0,0,0)` (SL(3): `(−1,−1,−1)`, commutator 3) — so "sealed
  in `K_m`" is loose (`K_m` is the `φ²`-bundle field; φ-fixed content is **ℚ**). **B129's 0-escape conclusion STANDS**
  (ℚ ⊂ ℚ(√−3); a calibration, not a refutation). S031 reframed as **rigidity/uniqueness**; the non-principal/HMP
  over-claim **retracted** (no non-principal irreducible φ-fixed points). B138 FINDINGS sharpened with the `det=−1`
  mechanism.
- **Item 4 — record:** `[[m,1],[1,0]]² = RᵐLᵐ`; `(m,m)` cyclic palindrome ⟹ every metallic bundle amphichiral (K011).
- **Item 5 — record (≠ S031):** the `φ²`-geometric bundle trace fields m=1→ℚ(√−3), m=2→ℚ(i), m≥3→higher-degree
  (structural; B125/B129) — distinct from S031's φ-fixed points (K010).

MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B139 untouched; B129's conclusion stands. Ledger
**V129**. `frontier/B140_compute_reconciliation/` + `tests/test_b140_compute_reconciliation.py` (6 tests, green).

---

## 2026-06-09 — B141: split S031 — φ-fixed tower REDUCIBLE (Q₈), φ²-geometric tower IRREDUCIBLE (dense fig-8) (V130)

Third reconciliation pass on S031, one layer past B140 — a substantive correction to B140's reframe. The root of the
φ-vs-φ² distinction is **finiteness vs density of the SL(2) image.** All re-derived in-sandbox. **B129 preserved.**

- **Item 1 (RIGOROUS, all n).** The unique irreducible SL(2) φ-fixed point `(0,0,0)` (κ=−2) is the **quaternion group
  Q₈** (`A²=B²=−I`, `AB=−BA`, order 8), finite with max irrep dim 2. So the principal `Sym^{n−1}` image (dim n) is
  **reducible for all n≥3** (alg-dim `{2:4,3:3,4:4,5:4,6:4,7:4}`; `χ_{Sym²}=(3,3,−1,−1,−1)=χ_a⊕χ_b⊕χ_c`). **No
  irreducible principal φ-fixed point at n≥3** — corrects B140's "rigidity of the principal *irreducible* fixed point."
- **Item 2 (RIGOROUS, all n).** The φ²-geometric fig-8 holonomy (B129's S1a, Zariski-dense) has `Sym^{n−1}`
  **irreducible ∀n** (alg dim n², n=2..5), traces in ℚ(√−3).
- **Item 3 (SOLID).** Finite image (Q₈) → reducible tower; dense image (fig-8) → irreducible tower — S031 conflated
  the two (irreducibility+ℚ(√−3) from φ², "fixed point" from φ; no single object has both).
- **Item 4 (CONJECTURE, open n≥4).** The SL(3) φ-fixed locus appears entirely reducible (intertwiner search: 60/60
  converged, 0 irreducible). Rigorous path = symbolic elimination (the SL(4) route).

**Split:** S031a (φ-fixed) = **reducible × discrete**; S031b (φ²-geometric) = **irreducible ∀n in ℚ(√−3)** (B129 S1a).
B129's 0-escape conclusion **stands** (φ-fixed traces rational ⊂ ℚ(√−3); object-identity calibration). S031, CATALOG,
K012, and B140 FINDINGS updated. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B140 untouched.
Ledger **V130**. `frontier/B141_s031_split/` + `tests/test_b141_s031_split.py` (6 tests, green).

---

## 2026-06-09 — B142: (A) S031a principal RIGOROUS (Klein-4); (B) magic-manifold cartography + MB10; (C) inventory (V131)

Three independent subtractive items. **Sage 10.9 + SnapPy-in-Sage + Ptolemy + Singular installed** (`~/.local/bin/sage-python`),
so the Sage-gated computations now run; the relevant parts were exercised here.

- **Item A — RIGOROUS (upgrades B141 Item-4 principal from conjecture).** The principal φ-fixed stratum is reducible
  by a one-line proof: principal eigenvalues `{1,−1,−1}` ⟹ `A²=I`; the φ-fixed necessary condition `A~B~AB` makes
  `B`,`AB` involutions; two involutions whose product is an involution **commute** (`(AB)²=I ⟹ BAB=A ⟹ BA=AB`) ⟹
  Klein-4 (abelian) ⟹ **reducible**. No search; reconfirmed 78/78. Full SL(3) locus (all strata, n≥4) stays CONJECTURE.
- **Item B — CARTOGRAPHY (firewall-confirming, NOT a result/crossing).** The "Borromean/SU(3) gauge enhancement" claim
  dies three ways: (B.1) **misidentified** — `s776` = the magic manifold (`6³₁`, ℚ(√−7), 3-chain link, **not**
  Brunnian); the real Borromean rings = `L6a4` (ℚ(i)); `is_isometric_to`=False; (B.2) **structure ≠ gauge (MB10)** —
  Thurston SL(2,ℂ) char-variety dim = #cusps = **3** not 2 (generic; MB8 null control across sym 8/12/48), and SL(2,ℂ)
  dim ≠ rank(SU(3)) — SU(3) is **SL(3,ℂ)** CS (s776 SL(3,ℂ) Ptolemy: 14 obstruction classes, dim 6); (B.3) **outside
  the forced chain** — trace field not ℚ(√−3). Banked as tombstone **K-I** + guard **MB10**. Trace fields confirmed via
  the new Sage `find_field` (s776 `x²−x+2`, L6a4 `x²+1`, 4₁ `x²−x+1`).
- **Item C — inventory** in `docs/OPEN_LEADS.md` ("Standing open threads"): S031a full-locus (symbolic elimination, the
  rigorous prize, = SL(4) machinery), B85, S032-A, S033 (now tied to MB10), K011 GHH-iff, genus-2 CS.

MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B141 untouched; B129/B141 preserved. Ledger **V131**.
`frontier/B142_klein4_and_magic_cartography/` + `tests/test_b142_klein4_and_magic_cartography.py` (5 passed + 1 sage-skip
under pyenv; 6 under Sage).

---

## 2026-06-09 — B143: strategic synthesis banked (3-voice) + Campaign-1 feasibility scope — the venue verdict (V132)

A joint reflection by three independent runs (CC + Chat-1 Opus 4.6 + Chat-2 Opus 4.8) on *how the SM could emerge from
not-nothing / interaction of not-nothings*, banked as **`docs/STRATEGIC_SYNTHESIS.md`** (two-tier: math program /
labeled POSTULATED aspiration). Plus the gating feasibility scope for the chosen Campaign 1.

- **The map:** monad + subtractive shell; the three-layer "why" (forced≠contingent / finiteness-density [B141] /
  right-object-wrong-level); the **corrected scorecard** — chirality is the *only proven* obstruction; the other three
  SM features are unchecked because the 3d-3d cusp→gauge dictionary is **borrowed/POSTULATED** (verified K006); the
  chirality (i) generic vs (ii) the real wall distinction; the open-paths map; the Campaign 1/2/3 roadmap.
- **MB11** banked: *state every result twice — bare math theorem + labeled POSTULATED physics reading; never let the
  second contaminate the first* (distilled from a drift caught in CC's own reflection).
- **Campaign-1 venue verdict (the gating result):** the **algebraic (trace) venue is mirror-blind to chirality-(ii)** —
  RIGOROUS: B131's interaction lives in `(κ,trT)`, both trace invariants, and the mirror preserves all traces
  (B139/B140), so the fork is automatically mirror-invariant. The algebraic venue carries the κ-**landscape**, not
  chirality. Chirality-(ii) needs an orientation-sensitive invariant → the **topological venue** (closed JSJ composite;
  needs **Regina**, not installed) or a **2-cusped hyperbolic-link realization** (construction open). ⟹ **B144.**
- Verified: B131 reuse reproduces `fork(1,2)={−4,−2}`; Chat-1's "588 reps / Massey" claim corrected (Massey dead for
  s776, the 3-chain link; K-I).

MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B142 untouched. Ledger **V132**.
`docs/STRATEGIC_SYNTHESIS.md` + `frontier/B143_interaction_feasibility/` + `tests/test_b143_interaction_feasibility.py`
(4 passed).

---

## 2026-06-09 — B144: Campaign 1 (chirality of cusp-glued interactions) — firewall extends structurally (MB12) + redirect (V133)

Campaign 1 at the bottleneck, run with the **MB12** discipline (check a target for vacuity *before* computing). MB12
collapsed the naive "find a chirality crack" campaign and gave the real, structural result.

- **MB12 vacuity chain:** "orientation-independent invariant distinguishing M from M̄" (vacuous: equal by definition);
  "orientation-sensitive invariant doing more than flip sign" (vacuous: CS/WRT/η conjugate for *every* 3-manifold);
  chiral = no orientation-reversing self-homeo (generic, B128 — not the wall); "preferred vs convention handedness"
  (vacuous for seed-gluing — mirror-closure).
- **Structural result:** for amphichiral pieces, `M̄(m1,m2,φ) ≅⁺ M(m1,m2, h₂φh₁⁻¹)` with `h_i∈GL(2,ℤ)` (det −1), and
  `h₂φh₁⁻¹∈GL(2,ℤ)` always ⟹ **the family is mirror-closed ⟹ no preferred handedness.** The firewall **extends to
  cusp-glued interactions structurally** (the `R↔L` mirror is a symmetry at every level). Seed-heterogeneity injects
  *contingency* (B131's κ-fork) but **not** chirality-breaking — different axes. Premise verified (both pieces
  amphichiral); chiral-(i) composites generic (exist) but mirror-closed (no preferred side).
- **Chat-2's one-instance Regina gate:** pieces truncate to a boundary torus (constructible) but the closed glue isn't
  a single Regina call (closed non-hyperbolic) → explicit certification **not in-session-tractable**; the structural
  argument carries it (a tooling limit, not a mirror-closure failure).
- **Redirect (POSTULATED):** preferred handedness — what the SM needs — requires **breaking the `R↔L` mirror symmetry**:
  a **chirally-asymmetric input** (a substitution not fixed by swap+reverse), **not** more seeds. New highest lead
  (Campaign 1′, `docs/OPEN_LEADS.md`).

**MB12** banked; `docs/STRATEGIC_SYNTHESIS.md` (i)/(ii) section fixed (vacuous formulations withdrawn); S032 +
OPEN_LEADS updated. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B143 untouched. Ledger **V133**.
`frontier/B144_interaction_chirality/` + `tests/test_b144_interaction_chirality.py` (3 passed + 1 regina-skip pyenv).

---

## 2026-06-09 — B145: Campaign 1′ — chirality cannot be forced (canonicity ⟺ self-mirror); parity is contingent (V134)

B144's redirect asked whether a chirally-asymmetric input can be **forced**. Answer: **no** — and this closes the
chirality axis. **Framing (GHH/B128):** `b++W` amphichiral ⟺ `W` anti-palindromic (= palindromic continued-fraction
period); the metallic `RᵐLᵐ` (canonical/arithmetic) family is **exactly** the self-mirror family.

- **Catalog (n=39 o-p-t bundles, len ≤ 7):** GHH ⟺ SnapPy `is_amphicheiral` on **all 39**; minimal-volume bundle =
  figure-eight `RL` (amphichiral), minimal chiral `RRL` strictly larger; trace-field degrees amphichiral ∈ {2,8},
  chiral ∈ {4,6,8,12} — **every quadratic (arithmetic) trace field is amphichiral; no arithmetic chiral o-p-t bundle**;
  simplest substitution (Fibonacci → `RL`) self-mirror.
- **Verdict (MATH):** canonicity (minimal volume / arithmeticity / simplest substitution / palindromic period)
  **coincides with the self-mirror (amphichiral) condition**; chirality requires leaving the canonical locus.
- **Aspiration (POSTULATED):** **preferred handedness (parity) is irreducibly contingent** — *forced ⟹ self-mirror ⟹
  no parity*. The deepest firewall statement; parity lives strictly on the contingent side. **Not a K-A revival**
  (opposite conclusion — chirality is non-canonical).

New knowledge **K017**; `STRATEGIC_SYNTHESIS`, S032, OPEN_LEADS updated (Campaign 1′ resolved; 1″ residue). MATH tier;
nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B144 untouched; K-A not revived. Ledger **V134**.
`frontier/B145_forced_chirality/` + `tests/test_b145_forced_chirality.py` (4 passed).

---

## 2026-06-09 — B146: B145 scrutiny calibration — tighten the conclusion, the dichotomy, the refuted arithmetic arm (V135)

A scrutiny pass (independently reproduced) found B145 **sound but over-scoped**; this calibrates it. MATH tier; K-A
stays dead.

- **Part A (verified):** the four axioms **permit** chirality (`RRL/RLL` det-1 Pisot **chiral**) — amphichirality is
  forced by the metallic minimality criterion (`b→a`), so bare-math = "metallic ⟹ self-mirror," not "forced ⟹
  self-mirror" (A1); "no single **canonical** object is chiral," not "chirality can't be forced" (A2); the
  **two-mechanism** statement replaces the slogan (A3); symmetric ⟹ amphichiral is **sufficient, not necessary**
  (`RRLLRL`, A4).
- **A5 (the catch):** B145's arithmeticity arm is **refuted as stated** — it used the *non-invariant* trace field;
  with the **invariant** trace field the imaginary-quadratic o-p-t bundles are `RL=ℚ(√−3), RRLL=ℚ(i)` (amphichiral) **and
  `RRL/RLL=ℚ(√−7)` (CHIRAL)**. So the surviving canonical⟹self-mirror rests on the near-tautological volume/palindromic
  arms, not arithmeticity.
- **B1 (the dichotomy):** `M` and `M̄` agree on every orientation-*independent* invariant (verified RRL/RLL/RRRL: equal
  vol/`H₁`/trace-field, CS flips) ⟹ **no canonical selection can prefer a handedness**; this **derives** the κ/chirality
  asymmetry (κ-fork genuine — κ orientation-independent; chirality-fork convention — handedness orientation-sensitive).
  Not a K-A revival.
- **B2 (open → B147):** is the chiral pair `RRL/RLL` (ℚ(√−7)) **fully arithmetic** (integral traces, Maclachlan–Reid;
  BMR finiteness = route to a theorem)? If yes, "no arithmetic chiral o-p-t bundle" is outright false.
- **Housekeeping:** stripped per-chat AI labels from the living/governing docs (generic "AI-assisted" is fine) +
  extended `test_public_surface_scan.py` (`test_no_ai_labels_in_living_docs`); append-only history flagged as a
  scheduled scrub.

`K017` rewritten; `STRATEGIC_SYNTHESIS`/`OPEN_LEADS` synced. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged
B124–B145 untouched; K-A not revived. Ledger **V135**. `frontier/B146_b145_calibration/` +
`tests/test_b146_b145_calibration.py` (2 passed + 1 sage-skip; guard green).

## 2026-06-10 — B147: the chiral pair RRL/RLL is FULLY ARITHMETIC — the arithmetic arm collapses (V136)

B146 left one residue: imaginary-quadratic **invariant** trace field (ℚ(√−7)) is *necessary* for arithmeticity, not
sufficient. B147 applies the **full** Maclachlan–Reid criterion. MATH tier; K-A stays dead.

- **Result:** `RRL/RLL` have **integral traces** (every holonomy-trace minimal polynomial is monic) on top of the
  imaginary-quadratic invariant trace field ℚ(√−7) ⟹ **they are arithmetic CHIRAL once-punctured-torus bundles.**
  Independently confirmed by **Humbert** (vol = 3 × Bianchi covolume of ℚ(√−7); the figure-eight control reproduces the
  known **12**). The scan (len ≤ 7) finds exactly **four** arithmetic o-p-t bundles: `RL` (ℚ(√−3), amphichiral),
  `RRLL` (ℚ(i), amphichiral), and the chiral mirror pair `RRL/RLL` (ℚ(√−7)).
- **B145's arithmeticity arm is REFUTED OUTRIGHT** — arithmetic chiral o-p-t bundles **exist**, so "arithmetic ⟹
  amphichiral" is false; the surviving "no single canonical object is chiral" rests on the volume/palindromic arms only.
- **"Exactly two o-p-t bundles" corrected** — that count is the **metallic** m=1,2 family (B125, which **stands**); ≥4
  arithmetic o-p-t bundles exist overall.
- **The firewall survives — a sub-claim correction, not a crossing.** `RRL/RLL` are a mirror pair, both arithmetic;
  arithmeticity is orientation-independent, so by the B146 dichotomy it cannot prefer a handedness. Not a K-A revival.
- **Guard:** the eager-yes (RRL "arithmetic" vs the cited "exactly two") was held until the integrality test was
  validated to *discriminate* (caught a real `polcoef` bug: read the leading coefficient at the **actual** degree) and
  an **independent** method (Humbert) confirmed it. Two methods agree.

`K017` updated (arithmetic arm refuted outright; firewall survives via the dichotomy); `STRATEGIC_SYNTHESIS`/`OPEN_LEADS`
synced (Campaign 1″ resolved); B125 docstring carries the "exactly two" → metallic-m=1,2 calibration note. MATH tier;
nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B146 untouched; K-A not revived. Ledger **V136**.
`frontier/B147_arithmetic_chiral_bundle/` + `tests/test_b147_arithmetic_chiral_bundle.py` (4 passed; pyenv, SnapPy +
cypari).

## 2026-06-10 — B148: κ/Fricke–Vogt pinned, the metallic monodromy = SL(2,ℤ) MCG action, the class-S open question (V137)

A physics-boundary scrutiny pass reframed the project's core question as the cosmological-constant problem ("why does
exact cancellation fail by a tiny *forced* amount," κ = tr[A,B] the candidate residue-skeleton). The computations it
surfaced were **independently re-derived here** (verify-don't-trust on a cross-session handoff — every claim re-proved
symbolically, not inherited). MATH tier; **firewalled** throughout.

- **§0 firewall (gating):** κ is scale-free (pure number / ℂ/π²ℤ) — no β-function, no RG, no anomaly — and **cannot**
  become a dimensionful energy density without an externally supplied scale. Every precedent (θ-vacuum, CS level,
  quantized Hall, anomaly coefficients) fixes a dimensionless *ratio*; the *scale* is supplied independently. Mainstream
  physics does **not** force a commutator-type obstruction. Everything below is math about the tower's symmetry, not a
  bridge to physics; nothing to `CLAIMS.md`.
- **§1 (re-derived):** `tr(ABA⁻¹B⁻¹)=x²+y²+z²−xyz−2=:κ`; `κ=4·I_FV+2` exactly under the half-trace convention (`x=2X`);
  both trace maps preserve their own invariant.
- **§2 (re-derived):** `tr(RᵐLᵐ)=m²+2`; the Dehn twists `τ_a,τ_b` preserve κ ⟹ the metallic monodromies **are** the
  SL(2,ℤ) MCG action; κ=−2 = the Markov surface; the Markov root `(3,3,3)` and the Q₈ point `(0,0,0)` are two distinct
  orbits on that surface (not a point).
- **§3 (re-derived):** `RᵐLᵐ` hyperbolic; eigenvalue = (metallic mean)²; fixed slopes = roots of `t²+mt−1=0`; trace
  field ℚ(√(m²+4)) reduced (m=1, m=4 share ℚ(√5)).
- **Open (reading/proof, not sandbox):** L14 class-S coincidence (the one mathematically-tractable direction — still
  math, not a crossing) and L15 firewall confirmation (the decisive boundary check, GTZ / Dimofte / Córdova–Jafferis).

`STRATEGIC_SYNTHESIS` §8 + `OPEN_LEADS` (L14/L15, Campaign 4) added; living-docs guard widened to B147/B148. MATH tier;
nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B147 untouched; firewall intact. Ledger **V137**.
`frontier/B148_kappa_fricke_metallic/` + `tests/test_b148_kappa_fricke_metallic.py` (5 passed; pyenv, pure sympy).

## 2026-06-10 — B149: B89's family is the COMPLETE irreducible component; M⁴=L unconditional on the irreducible locus (V138)

H1 (refocused). B89 is **already** an exact symbolic proof over ℚ(ω) (re-read + re-ran: `[A,B]det²=−det·μ⁴` holds
entry-by-entry `==0`; the handoff's "numerically-coaxed" premise doesn't apply; `exp011` is a separate downstream
numeric check). The real residual gap was **completeness**: B89 *posits* a 4-param family and proves M⁴=L on it — does
it exhaust the defining ideal's variety? MATH tier; no physics; B89's proof untouched (scope refined).

- **Method:** gauge-stratify the defining ideal `I` (10 quadratics `S=tAt` off-pattern, A=diag(1,1,ω,ω²)) by rank of the
  coupling block `Q=t[0:2,2:4]` (rank gauge-invariant; the full 16-var primdec is gauge-intractable). The Q normal forms
  (rank 2→I₂; rank 1→three forms; rank 0→0) **exhaust all reps up to gauge**.
- **Exhibited (symbolic, Sage/Singular `minimal_associated_primes` over ℚ(ω)):** rank-Q2 (B89's, dense) = **exactly 2
  components, both M⁴=L** (by exact ideal membership) — B89's family (`det≠0`) + a vacuous (`det≡0`) branch; rank-Q1
  forms vacuous/reducible; **rank-Q0 reducible — exhibited** (`Q=0`⇒`span(e₂,e₃)` invariant under A,t,B).
- **Decisive classification (exact over F_p, p≡1 mod 3, two primes; Burnside algebra-dim=16 ⟺ absolutely irreducible):**
  the **only** stratum carrying irreducible reps is rank-Q2 = B89's family; **decisive cell (irreducible ∧ M⁴=L fails) =
  0**. → **OUTCOME (a):** B89's family is the complete component of irreducible bundle reps; M⁴=L is **unconditional on
  the irreducible locus**; every M⁴=L violation in `V(I)` is reducible (MB7) or vacuous (det=0). Scope upgraded from "on
  the principal component" to "the principal component **is** the irreducible locus."
- **Methodology (verify-don't-trust caught 3 wrong turns):** a symbol-name collision (caught by the consistency gate);
  the **Schur commutant test is invalid for irreducibility** (a reducible non-semisimple rep can have commutant=scalars
  — it falsely flagged the provably-reducible Q=0 stratum; the correct **Burnside** test was validated against the Q=0
  exhibit and B89's known irreducibility); a BFS algebra-dim blowup (→ span-closure). No float claim is load-bearing.
- **Next (H2, by hand, external):** read HMP (arXiv:1505.04451, `φ(m³ℓ)=1`) and Tillmann (math/0508295, trace
  dictionary) — only a human/external source closes the literature/novelty question. Do **not** branch to L14 until H2.

`OPEN_LEADS` H1 resolved / H2 logged; B89 FINDINGS forward note (scope upgraded); living-docs guard widened to B149.
MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, B89, the merged B124–B148 untouched. Ledger **V138**.
`frontier/B149_sl4_ideal_completeness/` (probe/decompose/classify_fp + `decomposition.json`, `irreducibility_fp.json`) +
`tests/test_b149_sl4_ideal_completeness.py` (6 passed; pyenv).

## 2026-06-10 — B150: class-S coincidence (L14) — the trace-map action IS the N=2\* S-duality MCG action; τ-modularity & physical magnitude are RHYME (V139)

L14 scoping/characterization pass (focused literature read; **not** a verdict-of-match, no sandbox "match" fabricated):
does the SL(2,ℤ) trace-map action on the once-punctured-torus character variety (B148's object) coincide with the
class-S S-duality / MCG action? MATH tier (physics-adjacent, **firewalled**); nothing to `CLAIMS.md`.

- **Binding distinction (two spaces):** SL(2,ℤ) on the UV coupling τ = the well-known modularity = HOMONYM → RHYME;
  FORCED requires the action **on the character variety** to reproduce the B148 anchors (hyperbolic classes, λ_m²,
  ℚ(√(m²+4)) fixed slopes, the κ cubic, κ=−2 Markov).
- **Sources read:** Allegretti–Shan (2411.17378) — `M_flat(S_{1,1},SL₂ℂ)` = the Fricke cubic, MCG `SL₂(ℤ)=Mod(S_{1,1})`
  by Dehn twists, three subalgebras = quantized K-theoretic Coulomb branches of the **N=2\*** theories MCG-permuted,
  S-duality acting "on the character variety itself through MCG, not merely on τ"; Cantat–Loray (AIF 2009 / 0711.1579) —
  dynamical degree = homology spectral radius (= λ_m² for `RᵐLᵐ`); GMN (0907.3987) — Coulomb branch = Hitchin moduli.
  Convention verified: B148 `κ = λ+λ⁻¹` exactly; same cubic; κ=−2 ⟺ λ=−1.
- **Verdict — MIXED.** **FORCED at the character-variety / MCG level** — the SL(2,ℤ) trace-map action on the Fricke
  character variety **is** the N=2\* S-duality mapping-class action (same cubic/MCG/Dehn-twist generators; λ_m² = the
  Cantat–Loray dynamical degree; κ=−2 = the Markov fiber; Coulomb branches MCG-permuted). **RHYME at the τ-modularity
  level** (homonym) **and at the physical-magnitude / gauge level** (gauge group free input, no scale fixed, N=2\*
  non-chiral — the firewall, **L15's** separate question). **Even the FORCED part is mathematics** (symmetry = a known
  duality action); it does **not** cross to physical magnitude. The widest reach of the one-object picture yet,
  literature-confirmed. (Refines, not contradicts, the earlier "RHYME/PARTIAL" scoping, which answered the different
  "is SL(2,ℤ) a Weyl group / does it select the SM" question.)

`OPEN_LEADS` L14 status → CHARACTERIZED (MIXED); L15 (firewall confirmation) and H2 (HMP/Tillmann by hand) remain
open/separate; living-docs guard widened to B150. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B149
untouched; firewall intact. Ledger **V139**. `frontier/B150_class_s_coincidence/` +
`tests/test_b150_class_s_coincidence.py` (5 passed; pyenv).

## 2026-06-10 — B151: firewall confirmation (L15) — the firewall HOLDS; the unification is a symmetry identity that terminates at the wall (V140)

The decisive boundary check, a **reading** task (how the primary sources assign units). L14 made the bridge real (the
unit's SL(2,ℤ) symmetry IS the N=2\* duality action), so the firewall is tested hardest here. MATH tier (physics-boundary),
**firewalled**; nothing to `CLAIMS.md`.

- **The question:** in 3d–3d applied to the figure-eight, does the complex volume / CS invariant enter the partition
  function **only** as a dimensionless exponent, with all dimensionful content in `ℏ↔k` + the squashing radius and **none**
  in the invariant?
- **Anchor (computed, SnapPy):** figure-eight Vol = 2.0298832128 (= 2·V_tet), **CS = 0** (amphichiral); `Vol+iCS ∈ ℂ/4π²ℤ`
  — a dimensionless number mod a lattice. **Pre-strengthening:** CS (the candidate scale-carrier) vanishes for the unit,
  so its complex volume is purely the real hyperbolic volume — the unit is the *least* likely object to carry a scale.
- **The reading (3 sources, all FIREWALL_HOLDS):** GTZ (1111.2828) — `ĉ(ρ) ∈ ℂ/4π²ℤ` (Neumann extended Bloch group),
  dimensionless; Dimofte (1409.0857) — complex CS *at level k*, state-integral on `L(k,1)`, units in `k↔ℏ` + lens
  geometry, `Vol_C` the exponent saddle; Córdova–Jafferis (1305.2891) — "a squashing parameter controls the imaginary
  part of the complex CS level." In every case the units sit in `ℏ/k` + the squashing radius, never in the invariant.
- **Verdict — FIREWALL HOLDS, decisively.** No κ-type or volume-type invariant of the unit can source a physical scale.
  The unification is a **symmetry identity (L14)** and **terminates at the firewall (L15)** — a real bridge + a confirmed
  wall = the honest boundary of the one-object picture; the cosmological-constant question lies on the far side. Banked as
  the firewall holding (a real result, **not** a crossing; the real L14 bridge is **not** over-read — a symmetry is not a
  scale).

`OPEN_LEADS` L15 → CONFIRMED; `STRATEGIC_SYNTHESIS` §8 updated (L14/L15 both resolved); living-docs guard widened to B151.
H2 (HMP/Tillmann by hand) and H4/H5 (deeper-understanding frontier) remain separate/open. MATH tier; nothing to
`CLAIMS.md`; P1–P16, B85, the merged B124–B150 untouched; firewall intact. Ledger **V140**.
`frontier/B151_firewall_confirmation/` + `tests/test_b151_firewall_confirmation.py` (5 passed; pyenv).

---

## 2026-06-11 — B152: Chern–Simons as a one-sided parity order parameter (census test) (V141)

**Context (catch-up entry).** Cross-session brief item F4, reproduced independently in-sandbox before banking.

**Done.** Scanned SnapPy `OrientableCuspedCensus[:240]` testing the law *amphichiral ⇒ CS is 2-torsion*
(`CS mod ½ ∈ {0,¼}`). Method guards: amphichirality via `symmetry_group().is_amphicheiral()` **gated on**
`is_full_group()` (naive `is_isometric_to` is orientation-blind, B128); CS 2-torsion by **circular** proximity
to `{0,¼}` mod ½ (a tiny negative CS wraps to ~0.4999 under `%0.5` — a modulo-sign bug caught and fixed in my
own probe in-session). **Result:** 7 amphichiral (m003, m004, m135, m136, m203, m206, m207), **0 necessity
violations**, and **exactly one converse counterexample** m208 (chiral, full group, yet CS=0) — so CS-2-torsion
is **necessary but not sufficient**, the correct one-sided behaviour of an order parameter. No physics; a fact
about the census. `frontier/B152_cs_amphichirality_census/` + test (3 passed). Ledger **V141**.

---

## 2026-06-15 — B153 + the self-scrutiny campaign: the rank-stratified degeneration, two corrections, and a repo-wide audit

**Context.** After three adversarial review rounds deflated the PC13 "SL(4) figure-eight A-polynomial
component" to a *slice*, this session (a) banked the honest, stronger replacement — the **rank-stratified
degeneration of degree=rank** — then (b) on the owner's request ran a **repo-wide self-scrutiny campaign**
(multi-agent workflow) that **found real bugs in merged work**, which were verified and corrected. Discipline
throughout: verify-don't-trust (re-derive, don't re-run); two-mirrors (the audit *de-risks*, it does not
*certify* — novelty still needs the external specialist); nothing to `CLAIMS.md` (except an owner-approved
*down-tiering* of P10); PR-merged as `originaxiom`.

**Done.**

- **B153 — the rank-stratified degeneration (V142; PR #176, merged).** The figure-eight degree=rank relation
  `L=(−1)^{n-1}Mⁿ` is **rank-stratified**: a genuine SL(n,ℂ) character-variety **component at n=3** (`L=+M³`,
  Falbel), a measure-zero **slice at n=4** (`L=−M⁴`, exact over ℚ(ω): A-free tangent 29/kernel 19), and **not
  realized on an irreducible rep at n=5**. Built a validated reusable toolkit (`sln_toolkit.py`) that seals the
  recurring bug classes (finite-difference, sqrt-branch, near-singular `t⁻¹`). Supersedes PC13's "component".

- **B153 n=5 CORRECTION (V143; PR #177, merged) — a real bug the self-audit found.** The banked "n=5 non-ss:
  0/120, no irreducible reps" was a `det t=0`-drift artifact (the *same* vacuous-stratum bug fixed at n=3 but
  never back-applied to n=5). With `det t=1` pinned, **irreducible SL(5) reps with spectrum {1,1,1,−1,−1} DO
  exist** (non-semisimple, the two `[3]`-block Jordan types), certified by **two independent tests that agree**
  (Burnside span-rank 25 **and** Schur commutant dim 1; ~15-orders SVD gaps; cond(t)~20). But degree=rank
  **fails** on them. Headline survives; reason corrected. `n5_nonss_irreducible.py` + regression test.

- **B153 n=3 EXACT (V144; PR #178, merged).** Re-derived the n=3 endpoint **exactly over F_p** (3 primes; the
  A-free-tangent function first **validated by reproducing the known n=4 = 19**): the **dim-5 component** is the
  geometric one — tangent **11**, `tr A` rigid, irreducible (Burnside 9), carries **`L=+M³`** (matrix identity);
  the **dim-3 component** is a **reducible slice** — tangent **10**, not the earlier numerical "**14**" (a second
  numerical error caught). Upgrades the lower endpoint to match n=4's exactness. `n3_exact_endpoint.sage`.

- **Self-scrutiny campaign (multi-agent workflow).** The full-panel run died twice on a 427-agent fan-out (it
  paneled every load-bearing claim) competing with heavy Sage; **32 verdicts survived: 28 CONFIRMED, 4
  OVER_TIERED**. A **leaner re-run** (panels only flagged claims) covers all ~90 claims for the synthesis.

- **Consolidated corrections (V145; pending PR `frontier/self-audit-corrections`).** Each flag independently
  re-verified, then corrected in place: **B95/V79** — "principal spectrum *forced*" → forced *given* the
  mult-(n−2)/finite-order ansatz (counterexample {1,ω,ω²,e^{±iπ/3}}); and the key **finite-order insight** —
  a principal/Dehn-filling rep has `A` finite-order ⟹ semisimple ⟹ `A²=I` ⟹ dihedral ⟹ reducible, so **no
  irreducible principal rep at n=5 is PROVEN** (which *upgrades* the B153 n=5 endpoint from numerical to proven
  for the principal family, and reconciles B95 ↔ B153). **P10** (CLAIMS.md, owner-approved down-tiering) —
  "five filters all select 4₁" → trace-3 sieve **PROVED**; the other four documented/suggestive
  (NEEDS-SPECIALIST). **B92/V76-V78** — "all det=−1 trace-m matrices conjugate to the companion" is **false at
  m≥4** (Sage class numbers: h(m²+4)=2 at m=4, disc 20); the companion is one GL(2,ℤ) class among `h`. **V99/B112**
  — "sign half for all n" already self-relabeled by B116/B117/B118; ledger back-pointer added.

**Verdict.** The verification principle paid off: the audit's B95 flag and my own n=5 re-derivation
*independently converged* on the same gap — and fixing it made the result **stronger** (the n=5 absence is
provable for the principal family, not merely numerical). MATH tier; P1–P9, P11–P16, B85 untouched.

**Open / next.** Fold any NEW flags from the lean synthesis into the corrections PR; run the full-suite gate;
then continue the math (Phase C): the **silver bundle (m=2) generality** of the degeneration (φ_silver =
`A↦A³BA²B, B↦A²B`, derived) and a from-first-principles proof on the non-ss locus. Specialist novelty email
drafted (owner sends). Ledgers **V142–V145**.

---

## 2026-06-16 — B154: the metallic meridian and the order-based degree=rank exponent (silver bundle)

**Context.** Phase C of the B153 campaign: does the rank-stratified degeneration of degree=rank generalize
from the figure-eight (m=1, RL) to the silver bundle (m=2, R²L²)? Banked incrementally (PRs #180–189) as a
single arc, each step verified, several **self-corrections** caught by the verify-don't-trust discipline.

**Done (B154; V146, V147).**

- **The metallic meridian `µ = A⁻ᵐt`** — derived from the exact free-group identity `φ_m([A,B]) = Aᵐ[A,B]A⁻ᵐ`
  (the monodromy fixes the fiber boundary only up to conjugacy; verified m=1,2 by word reduction). The
  figure-eight's `A⁻¹t` is the m=1 case; it is the cusp meridian (`µ` commutes with `[A,B]`).

- **Degree=rank GENERALIZES to the metallic family.** With `µ=A⁻ᵐt`, the matrix identity `[A,B]=±µᵏ` holds for
  the silver bundle (SL(3): `{1,ω,ω²}`→`+µ⁴`, `{1,i,−i}`→`+µ²`; SL(4) `{1,1,ω,ω²}`→`−µ⁴`). So it is **not**
  figure-eight-special.

- **The exponent is ORDER-based, not rank-based** — "degree=rank" is a *coincidence of the principal spectra*
  (B95 ties their order to the rank). Decisive test: figure-eight `{1,ω,ω²}` (order 3) gives `k=4` at *both*
  n=3 and n=4 (not `k=n`). Closed-form fit **`k = 4 − m(o−3)`** (o = boundary-spectrum order) on all six
  accessible (m,o,n) points; the o=4/SL(4) corner admits no irreducibles. `k` is the **A-polynomial slope**
  (holds along a curve at generic M; finite-order points are the Dehn fillings).

- **Geometry.** The silver `{1,ω,ω²}`@SL3 degree=rank locus is a **component** of the fixed-spectrum variety
  (codim 0, deformation theory) that is an **A-free slice** (tr A moves, tangent 11) — exactly the
  **figure-eight n=4 pattern**, not the rigid n=3. Tentative: rigidity may also be order-based.

- **Foundation + machinery.** The silver SL(2) character variety (`κ=½z²+8/z²−2`, distinct from figure-eight)
  via the trace-map fixed locus; the silver bundle relations eliminate to `F1: tB²=A⁻¹tA, F2: tBt⁻¹=A²B`; the
  convention-free monodromy-t solver. Validated throughout against the figure-eight control (reproduces B67).

- **Self-corrections (verify-don't-trust, this arc):** the best-rep scan over-read → the wrong-meridian
  over-negative (PR #181, "silver doesn't carry it") → the derived true positive (`µ=A⁻ᵐt`); and the "slice
  ~25%" wording → the precise component(fixed-spectrum)+slice(A-free) deformation theory. A genuine
  *derivation* of `k=4−m(o−3)` is OPEN (reduces to the metallic A-polynomial — the B67→B89 program
  generalized).

**Also (2026-06-16): the lean self-audit workflow COMPLETED** (V147) — 62 claims, 48 CONFIRMED, only P10/P12
flagged (both already handled); it independently reversed its own P12 BUGGED verdict and confirmed P10's fix.
Acted on its two minor recommendations (P12 shape-coordinate caveat + a CI identification test; P10 min-volume
m003-tie annotation). The two-mirrors discipline is working. MATH tier throughout; nothing to `CLAIMS.md`
(the P10/P12 edits are honesty caveats); P1–P16 cores untouched. Ledgers **V146, V147**.

---

## 2026-06-16 — B155: the "golden × phase" spectral bridge at n=4 (processing the external handoff, step 1/3)

Processing three external files (an external-review note's two results + the cross-session "Ω" synthesis brief +
the Chat history) **one-by-one through governance, straight to the repo**, each **independently re-derived**
before banking (verify-don't-trust: a cross-session claim is corroboration, not validation). **Step 1 = Result C.**

**B155 — the canonical n=4 object.** A single integer matrix `M_g = [[1,1,0,0],[0,1,1,0],[1,1,1,1],[1,1,0,1]] ∈
SL(4,ℤ)` realizes **"figure-eight monodromy × order-6 phase"** as a *rational block structure* (re-derived
exactly, pure sympy, all checks PASS):

- **Spectrum.** `charpoly(M_g) = (x²−3x+1)(x²−x+1) = x⁴−4x³+5x²−4x+1` — the **golden** factor (figure-eight
  monodromy trace poly, disc 5, root φ², real ⇒ Anosov) × the **phase** factor (`Φ₆`, disc −3, |root|=1, finite
  order 6).
- **Rational form.** `M_g ∼_ℚ [[2,1],[1,1]] ⊕ [[0,1],[−1,1]]` (same invariant factors) and **nonderogatory**
  (min poly = char poly) ⇒ any matrix with this charpoly is ℚ-conjugate to it.
- **Glue.** The two invariant 2-planes glue inside ℤ⁴ with cokernel **(ℤ/2)²** (sublattice index 4, SNF
  `diag(1,1,2,2)`), and this is **representative-specific** — the block-diagonal form with the same χ has
  *trivial* glue (a GL(4,ℤ)-class invariant, not forced by the spectral type).
- **Inertia.** An invariant symmetric form of **signature (1,3)** with discriminant **−15 = disc ℚ(√5)·disc ℚ(√−3)**.

**B206 ≅ Ω₄, honestly scoped.** The Ω positive-shear family `R_{a,m}` (reciprocal charpoly
`x⁴−ax³+(2a−2m−4)x²−ax+1`, signature (1,3) on its live cone) reaches `M_g`'s charpoly only at the *half-integer*
point **`a=4, m=−1/2`**. So the bridge is the **shared canonical object** (same charpoly + signature + ℚ-conjugacy
class), **not** a common integer lattice point; the shorthand "same matrix two ways" overstates it — this is the
honest statement banked.

**Firewall.** Signature (1,3) = **algebraic inertia** of a bilinear form, NOT spacetime/metric/time. No physics
claim; the Ω "non-cancellation" motivation stays firewalled. MATH tier; nothing to `CLAIMS.md`; P1–P16 untouched.
Reproducer `frontier/B155_golden_phase_bridge/golden_phase_bridge.py`; test `tests/test_b155_golden_phase_bridge.py`
(6 passed). Ledger **V148**. Steps 2 (two-results note → `papers/`) and 3 (unified brief → `docs/`) follow.

---

## 2026-06-16 — B156: full Ω-branch integration, Phase 1 (the strict-full cone)

Owner chose, after the 3-file handoff (B155/PC17/brief), to do the **full Ω-branch integration then the
derive-k research push**, "both, sequenced," with "all relevant agents." This is **Phase 1**: re-derive the
Ω theorems under our governance and bank the Ω-specific content as `frontier/B156_omega_strict_full_cone/`.

**Method (verify-don't-trust, multi-agent).** A Workflow ran **4 independent verifiers + adversarial
skeptics** (one per claim). All re-derived from scratch (not the handoff's code), all re-run by the main loop:

- **Core R/G algebra** [proved]: `R_{a,m} ∈ SL(4,ℤ)`, `det R=1`, palindromic `χ`, `RᵀGR=G`, `det G=−δ/(m+1)`,
  shears `A:δ→δ+2`/`C:δ→δ−1`, signature **(1,3)** on the live cone / (1,2,1) wall / (2,2) below — constancy
  *rigorous* (det `G<0` on the convex cone + Sylvester pivot certificate). 16/16 PASS.
- **TC-2** [proved]: strict-full ⟹ `M~M⁻¹` ⟹ reciprocal char poly; 8/8 strict-full examples palindromic + 2
  non-reciprocal controls with no nondegenerate form.
- **Fibonacci block-count** [exact]: `F_{n+1}` (compositions into {1,2}), growth `φ`, four methods agree.
- **Wall-avoiding history entropy = log 2** [proved], by an **exact** mechanism (not numerics):
  `log W_n − n·log2 → log(1−φ^{−δ})`, so `W_n(δ) ~ (1−φ^{−δ})·2ⁿ`.

**Counts.** Strict-full **survivor** = a history from the Ω₄ seed (golden×phase char poly, strict-full at L4)
staying strict-full at every level. L4–L7 = **96/672/3840/20928** independently re-confirmed by *two*
from-scratch enumerators (exact `det`-of-generic-form test, with and without the reciprocity shortcut).
L8–L10 = 105312/521904/2488080 from the exact-state artifacts; the independent re-run is the **heavy
background counter** (state-propagation to L10), to be appended when it lands.

**Two verify-don't-trust payoffs.** (1) The handoff's own brute-force script attributes strict-full status
*per char-poly class representative* and **over-counts** (L5: 3120 vs the true 672; L6: 57792 vs 3840) — the
correct count is *per-matrix*. Blindly launching it for a 40 hr run would have computed the wrong quantity;
the correct definition was pinned **before** any heavy job. (2) Caught a circular intermediate identity in the
handoff's TC-2 exposition (fixed; the result stands).

**Firewall.** The Ω claim-boundary table is copied **verbatim** into the FINDINGS: signature (1,3) =
algebraic inertia (NOT spacetime), history entropy = word-growth (NOT thermodynamic), endpoint/class entropy
OPEN, U/V free-semigroup REFUTED, gravity/QM/cosmology FORBIDDEN. The Ω₄ seed = the `frontier/B155`
golden×phase object (the two programs converge there). Expert one-page note → `papers/omega_strict_full_note/`
(**PC18**); novelty NEEDS-SPECIALIST. MATH tier; nothing to `CLAIMS.md`; P1–P16 untouched. Ledger **V149**.
Reproducers in `frontier/B156_omega_strict_full_cone/`; test `tests/test_b156_omega_strict_full_cone.py`
(6 passed). Next: append the L8–L10 re-run counts, then **Phase 2** (derive `k=4−m(o−3)`).

---

## 2026-06-16 — B156 completion: source-chat cross-check, TC-1/TC-4, the commuting-shears scope

Owner supplied the **source reasoning** for the Ω work: the ChatGPT/Ω chat (1435 messages) that produced it,
which itself ingested the ~1085pp Claude trace — *the two chats cross-examined each other*. Digested as a
cross-check (gitignored `audit/handoff_2026-06-15/chatgpt_omega_transcripts/`); an agent cross-checked it
against the banked B156, and everything new was **re-derived here** (verify-don't-trust), not transcribed.

- **B156 confirmed faithful.** All four theorems + firewall + counts correctly transferred; our independent
  re-derivations (the (1,3) Sylvester-pivot rigor, the exact log-2 survival mechanism) *strengthen* the source.
  History entropy **log 2** is the final value — it supersedes the earlier lower bounds `log φ` and `(1/3)log 7`
  (both `< log 2`); B156/PC18 already used log 2.
- **Two missed theorems banked (re-derived):** **TC-1** [exact] — Ω₄ is the *unique minimal* strict-full seed
  (minimal SC level L=4; every strict-full L4 history has charpoly (4,5,4) = golden×phase = the `frontier/B155`
  object); **TC-4** [proved] — orientation no-go (relabel-closed ensembles have zero net Pfaffian residual; the
  Pfaffian sign law `Ω(πw)=sign(π)Ω(w)` + ensemble closure → boundary-induced orientation). `tc1_tc4_verify.py`.
- **Decisive scope (the collaboration's concluding verdict):** **Ω is the abelianized shadow of the trace-map
  tower, not its mechanism.** The strict-full shears `A=S₀₃, C=S₂₃` **commute** (`E₀₃E₂₃=E₂₃E₀₃=0`), so
  `R↦A, L↦C` cannot represent the noncommutative trace-map monodromy (and the R-cone endpoint entropy is 0,
  order-independent). The **Ω↔tower bridge audit** (κ↦δ/det G? χ_Ω↦Dickson/Lucas? do R,L relations realize?) was
  proposed but **never run** — recorded as the open frontier (`docs/OPEN_LEADS.md` L18, `docs/UNIFIED_STATE.md`).
- **Counts:** the independent heavy re-run (state-propagation, fresh code) re-confirmed the **full strict-full
  tower L4–L10 = 96/672/3840/20928/105312/521904/2488080** (endpoint matrices 36→65472; L10 took ~3.5 h,
  112200 distinct metric-solves), matching the handoff artifacts at **every** level — **Phase 1 closed**.
  Updated B156 FINDINGS + `docs/UNIFIED_STATE.md` + PC18 + ledger **V150**; test lock 8 checks. **Phase 2**
  (derive `k=4−m(o−3)`) launched concurrently.

---

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->
