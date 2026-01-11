# Origin Axiom — Phase 3 (Mechanism Phase)

> **Status:** Draft contract for Phase 3 mechanism; supersedes the exploratory
> flavor-calibration add-on as the canonical Phase 3 in the Phase 0 corridor.

## 1. Role in the Phase 0 program

Phase 3 (Mechanism) is the first phase whose *object* is an explicitly
mathematical implementation of the Origin Axiom:

- We pick a concrete global amplitude \(A\) and floor \(\varepsilon\).
- We define a **minimal-intervention** enforcement rule that guarantees
  \(|A| \ge \varepsilon\) at all times.
- We embed this rule into a simple but dynamical toy vacuum (e.g. a driven
  cavity / scalar field mode) and study binding vs non-binding regimes.

The goal is **not** to match empirical data yet, but to show that a single,
well-defined mechanism can:

1. Enforce the non-cancellation floor without blowing up the dynamics.
2. Produce a well-defined residual energy density that could be mapped to
   vacuum energy in later phases.
3. Support a Phase-0-compatible corridor over \(\theta\) via an explicit
   test suite and a `theta_filter` artifact.

## 2. Required artifacts and interface to Phase 0

Phase 3 (Mechanism) must emit:

- **Canonical PDF**
  - Path: `phase3/artifacts/origin-axiom-phase3.pdf`.
  - Built from `phase3/paper/main.tex` via the Phase 3 Snakemake workflow.

- **Theta-filter artifact (ledger interface)**
  - Path: `phase3/outputs/theta_filter/phase_03_theta_filter.json`.
  - Schema: Phase 0 Appendix B (`schema_version: "1.0"`).
  - Required fields:
    - `theta_domain`: `[0.0, 6.283185307179586]`.
    - `theta_prior`: prior / corridor on \([0, 2\pi)\), represented as
      intervals or discrete points.
    - `theta_grid`: list of evaluated \(\theta\) values.
    - `tests`: array of test names.
    - `pass`: Boolean mask, same length as `theta_grid`.
    - `fail_reasons`: per-\(\theta\) list of strings explaining failures.
    - `provenance`:
      - `git_commit`, `config_hash`, `environment`.
      - `run_ids`: mapping of labels like `"theta=2.18"` to run directories.
  - Optional fields (recommended):
    - Scores and diagnostics (e.g. `stability_margin`, `binding_fraction`).

The Phase 0 ledger must be able to ingest this file without code changes and
update `phase0/phase_outputs/theta_corridor_history.jsonl` accordingly.

## 3. Test suite for Phase 3 (Mechanism)

For each \(\theta\) on `theta_grid`, Phase 3 runs a pair of simulations:

- **Constraint ON**: Origin Axiom enforced (minimal intervention).
- **Constraint OFF**: identical configuration and seed, enforcement disabled.

The *baseline test suite* is:

1. `binds`: true if the OFF run violates the floor at least once while ON
   remains above the floor.
2. `stable`: true if the ON run remains numerically and physically stable
   (no blow-ups, no runaway oscillations).
3. `minimal_intervention`: true if the intervention norm stays within a
   declared budget (consistent with the minimal-intervention hypothesis).
4. `vacuum_consistency`: true if the long-time residual energy density in
   the ON run converges to a well-behaved limit that depends smoothly on
   \(\theta\).

A \(\theta\) value is **admissible** for Phase 3 iff all tests above pass.
The Phase 3 corridor is the subset of `theta_grid` passing the test suite.

## 4. Run IDs and outputs layout

Each evaluated \(\theta\) is associated with a reproducible run directory:

- Root: `phase3/outputs/runs/`.
- Per-theta runs:
  - `phase3/outputs/runs/mech_theta_<theta_slug>/run_<uuid>/`.

Each run directory must contain at minimum:

- A machine-readable config snapshot (YAML or JSON).
- Logs of the ON/OFF simulations (including random seeds).
- Key summary metrics (binding counts, stability metrics, residual energy).
- Any additional diagnostics required by the paper.

The `theta_filter.provenance.run_ids` field maps human-readable θ labels to
the *leaf* run directories above.

## 5. Reproducibility levels and gate

Phase 3 (Mechanism) follows the Phase 1/2 style gate:

- **Level A (snapshot)**:
  - Verify that the committed artifacts and bundle manifest are internally
    consistent.
  - Entry point: `bash scripts/phase3_gate.sh --level A`.

- **Level B (regenerate)**:
  - Rebuild all tables, figures, the paper, and the paper bundle from
    source using Snakemake, then verify the bundle.
  - Entry point (suggested):
    - `snakemake -s phase3/workflow/Snakefile -c 1 all`
    - followed by `bash scripts/phase3_gate.sh --level B`.

- **Level C (heavy runs, optional)**:
  - Developer-only mode for extended scans or higher-resolution sweeps.
  - Populates additional git-ignored run directories under
    `phase3/outputs/runs/`.

The canonical PDF and theta_filter must be reproducible at Level B.

## 6. Claims and non-claims (Phase 3 mechanism)

**Claims (mechanism-level, not yet empirical):**

1. There exists at least one implementation of the Origin Axiom (non-zero
   floor + minimal intervention) that:
   - produces stable dynamics in the chosen toy vacuum, and
   - yields a finite, well-defined residual energy density for admissible
     \(\theta\) values.

2. For each admissible \(\theta\), the ON vs OFF ablation demonstrates that
   the floor changes the dynamics in a diagnostically relevant way
   (binding regime with a valid binding certificate).

3. The set of admissible \(\theta\) values, together with the test suite and
   run IDs, is faithfully encoded in `phase_03_theta_filter.json` and can
   be ingested by the Phase 0 ledger.

**Non-claims (explicit):**

- No claim that Phase 3’s toy vacuum is the real universe.
- No claim of a unique, canonically derived \(\theta_\star\).
- No claim of matching observed vacuum energy or other data.
- No claim that this is the *only* valid implementation of the Origin Axiom.

This contract is considered **locked** once the Phase 3 mechanism paper,
code, and theta_filter artifact satisfy the conditions above and pass the
Level B gate in a clean repository state.

---

## Companion docs: role, Stage 2 diagnostics, and archived flavor

For context on how this canonical Phase 3 mechanism module fits into the wider
program, the following documents are relevant:

- `ROLE_IN_PROGRAM.md` explains how Phase 3 sits between the Phase 2 bounded
  vacuum-floor implementation and the Phase 4 FRW toy diagnostics, and which
  questions the mechanism module is allowed to ask (and not ask).

- `stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md` and
  `stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md` summarise the Stage 2
  mech/measure and joint mech–FRW belts. These belts treat Phase 3 outputs as
  fixed inputs and provide **diagnostic-only** tables and correlations; they do
  not alter the Phase 3 mechanism contract or introduce new Phase 3 claims.

- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` places these Stage 2 belts in the
  wider diagnostic context (FRW corridor, FRW data probes, θ★ diagnostics, and
  doc/repo audit). It should be read as a downstream companion to this
  mechanism contract, not as an extension of Phase 3 scope.

- `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md` records the status of the
  archived Phase 3 flavor-sector experiment. That tree is explicitly
  non-canonical; no flavor-sector claims live in this Phase 3 mechanism module.

---

Doc status: Canonical Phase 3 mechanism contract; defines the non-cancellation mechanism, vacuum floor, amplitudes, and binding certificate that underpin the Phase 3 paper and Stage 2 mechanism/joint diagnostics; interpreted under `phase3/PHASE3_ALIGNMENT_v1.md`.
