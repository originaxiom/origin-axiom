# Phases

This repository is organized as a phased program. Each phase is allowed to make only a bounded set of claims, and must provide reproducible artifacts as evidence.

## Phase 0 — Governance and Corridor Method (meta-phase)
**Purpose:** define the discipline that prevents drift:
- claim taxonomy (what we are / are not claiming),
- artifact schema standards,
- the "theta corridor" narrowing concept (filters + ledger),
- reproducibility contracts (what is tracked vs regenerated),
- failure modes and falsifiability rules.

**Outputs:** schemas, filters, and a paper skeleton describing the method — not physics results.

**Done when:**
- corridor schema + filter schema stable,
- ledger scripts stable,
- Phase 1 and Phase 2 can reference Phase 0 as their governance contract.

## Phase 1 — Toy models (existence + scaling in controlled settings)
**Purpose:** demonstrate non-cancellation residue exists and behaves systematically in toy settings.

**Allowed claim types:** existence / robustness / scaling (toy-domain only).

**Canonical artifacts:** Phase 1 paper + canonical figures in `phase1/outputs/figures/`.

## Phase 2 — Mode-sum model + FRW comparison (bounded viability checks)
**Purpose:** show the residue mechanism survives a stricter model and can be compared against FRW-style observables without overclaiming.

**Allowed claim types:** existence / robustness / bounded viability (explicitly non-cosmology claims unless stated).

**Canonical artifacts:** Phase 2 paper + canonical figures in `phase2/outputs/figures/`.


## Phase 3 — Mechanism module
**Purpose:** lock a baseline non-cancellation floor on a global amplitude and
provide binding-style diagnostics at the mechanism level.

**Allowed claim types:** mechanism-level existence/robustness/diagnostic
statements (no corridor narrowing, no flavor calibration).

**Canonical artifacts:** Phase 3 paper (`phase3/artifacts/origin-axiom-phase3.pdf`)
and tables in `phase3/outputs/tables/`.

**Archived flavor add-on:** flavor-sector calibration is archived under
`experiments/phase3_flavor_v1/` and is non-canonical.

## Next phases (placeholders)
Future phases must:
1) declare scope + non-claims,
2) define canonical artifacts,
3) add claim IDs to the global index,
4) obey Phase 0 governance rules.

## Stage 2 — Diagnostic belts (non-canonical, in progress)
Stage 2 lives under `stage2/` and remains strictly downstream of Phase 3/4
artifacts. Active belts include:
- `stage2/frw_corridor_analysis`
- `stage2/mech_measure_analysis`
- `stage2/joint_mech_frw_analysis`
- `stage2/frw_data_probe_analysis`
