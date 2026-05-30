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

## 2026-05-29 — PC02 external-review brief

**Review-ready handoff, not public draft.**

Completed the final PC02 wording pass on branch
`paper/pc02-conditional-uniqueness`.

- Added `papers/candidates/PC02_conditional_uniqueness/EXTERNAL_REVIEW_BRIEF.md`.
- Tightened the PC02 paper card and review packet so the current state is
  "ready for external mathematical review," not publication-ready.
- Advanced PC02 readiness from `EVIDENCE_EXISTS` to `NEEDS_VALIDATION` in both
  `papers/CANDIDATES.md` and the paper card, reflecting that the evidence and
  proof packet exist but still need outside mathematical review before becoming
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
  from A1-A7 plus exchange. External review should ask whether T1 is a theorem,
  a standard naturality/filter-inheritance principle, or an extra axiom.
- **Documentation synchronized:** `README.md`, `docs/atlas/README.md`,
  `docs/atlas/REVIEWER_GUIDE.md`, and PC11 now point to the C5 package and keep
  the spectrum bridge conditional, not predictive.

Ledger update: 15 proven, **5 conditional**, 9 open, 10 dead. Proven test suite
unchanged.

---

## 2026-05-30 — PC11 external-review packet and freeze preparation

**Prepared the trace-selector branch for external review and freeze.**

Added a Markdown-only review layer for the now-narrowed mathematical question:

```text
Is T1 natural, standard, derivable, or inserted?
```

- `papers/EXTERNAL_REVIEW_INDEX.md` routes reviewers to the two ready packets:
  PC02 (conditional uniqueness) and PC11 (half-step trace lift / C5 selector).
- `papers/candidates/PC11_trace_map_spectrum_bridge/EXTERNAL_REVIEW_BRIEF.md`
  gives a compact review handoff focused on the trace lift, projective quotient,
  tangent return quadratic, and T1.
- `papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md` gives the
  full audit path, reproduction commands, controls, non-claims, and outcome
  labels.
- PC11 readiness advanced from `EVIDENCE_EXISTS` to `NEEDS_VALIDATION`; it is
  blocked from stronger status until external review of T1.
- `REPRODUCIBILITY.md` now records the planned freeze tag
  `trace-selector-c5-freeze`.

No claims changed. Ledger remains 15 proven, 5 conditional, 9 open, 10 dead.

---

## 2026-05-30 — External-review workflow scaffold

**Added the review intake and triage process; no claims changed.**

Added:

- `papers/REVIEW_WORKFLOW.md` — process for selecting a packet, sending minimal
  files, recording feedback, assigning outcome labels, and deciding repository
  actions.
- `papers/REVIEW_RESPONSE_LEDGER.md` — public-safe ledger template for external
  responses, with allowed decisions (`ACCEPT_FIX`, `ACCEPT_CLARIFY`,
  `NEEDS_REPRO`, `DISPUTE_WITH_REASON`, `OUT_OF_SCOPE`, `KILL_OR_RESCOPE`).
- Navigation updates in `papers/README.md`, `papers/EXTERNAL_REVIEW_INDEX.md`,
  and `docs/atlas/REVIEWER_GUIDE.md`.

The workflow explicitly forbids raw private correspondence, private contact
details, and claim-status changes before a response is logged, triaged, and
linked to a commit or PR.

Ledger unchanged: 15 proven, 5 conditional, 9 open, 10 dead.

---

## 2026-05-30 — PC02 outreach kit

**Prepared the first external-review outreach template; no claims changed.**

Added `papers/candidates/PC02_conditional_uniqueness/OUTREACH_KIT.md` with:

- reviewer fit criteria for topology / mapping-torus / `SL(2,Z)` expertise;
- short first-contact and full-review request templates;
- the minimal file packet to send;
- response logging instructions for `papers/REVIEW_RESPONSE_LEDGER.md`;
- explicit non-claims preserving the conditional theorem framing.

Updated `papers/EXTERNAL_REVIEW_INDEX.md` and `papers/REVIEW_WORKFLOW.md` so PC02
outreach starts from the kit. No reviewer names, emails, private correspondence,
or raw transcripts were added.

Ledger unchanged: 15 proven, 5 conditional, 9 open, 10 dead.

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

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->
