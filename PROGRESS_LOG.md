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

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->
