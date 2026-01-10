# Claims Index (Global)

This file is the top-level map of claims across phases.

Rule: every claim must have:
- a stable claim ID,
- a phase owner,
- evidence pointers (canonical figures and/or pinned run IDs),
- an explicit "non-claim" boundary,
- a phase-local source-of-truth file (`PHASEx/CLAIMS.md`).

This index is *navigational*: it lists claim IDs and short labels and points to the phase-local ledgers, which contain full statements and evidence.

---

## Phase 0 — Method / Governance / Reproducibility

**Source of truth:** `phase0/CLAIMS.md`  

Phase 0 makes **no physics claims**. It defines contracts for:
- claim taxonomy and scope separation,
- corridor/filter schemas and bookkeeping,
- reproducibility, artifact hierarchy, and provenance logging,
- archive/deprecation policy.

Registered Phase 0 claims:

- **P0-C01 — Theta filter and corridor schemas are first-class, versioned objects**  
  See `phase0/CLAIMS.md` for statement and evidence.

- **P0-C02 — Global \(\theta\)-corridor bookkeeping is explicit and auditable**  
  See `phase0/CLAIMS.md`.

- **P0-C03 — Claim taxonomy and scope separation are enforced across phases**  
  See `phase0/CLAIMS.md`.

- **P0-C04 — Reproducibility contract for phases and artifacts**  
  See `phase0/CLAIMS.md`.

- **P0-C05 — Provenance logs (PROGRESS_LOG) are part of the formal record**  
  See `phase0/CLAIMS.md`.

- **P0-C06 — Archive and deprecation policy keeps the main repo defensible**  
  See `phase0/CLAIMS.md`.

- **P0-C07 — Phase 0 paper is the canonical narrative for governance and corridor method**  
  See `phase0/CLAIMS.md`.

---

## Phase 1 — Lattice toy model and residue mechanism (toy domain)

**Source of truth:** `phase1/CLAIMS.md`  

Scope (summary):
- Toy-domain lattice model demonstrating a residue mechanism under controlled assumptions.
- Allowed claim types: existence / robustness / scaling (toy-domain only).
- Canonical artifacts: Phase 1 paper + canonical figures in `phase1/outputs/figures/`.

For full list of Phase 1 claim IDs and evidence, see `phase1/CLAIMS.md`.

---

## Phase 2 — Mode-sum model + FRW comparison (bounded viability checks)

**Source of truth:** `phase2/CLAIMS.md`  

Scope (summary):
- Mode-sum model implementing the residue mechanism in a stricter setting.
- Comparison against FRW-style observables under clearly stated approximations.
- Allowed claim types: existence / robustness / bounded viability (explicitly non-cosmology claims unless stated).
- Canonical artifacts: Phase 2 paper + canonical figures in `phase2/outputs/figures/`.

For full list of Phase 2 claim IDs and evidence, see `phase2/CLAIMS.md`.

---

## Phase 3 — Mechanism module (toy vacuum floor + diagnostics)

**Source of truth:** Phase 3 paper appendix
(`phase3/paper/appendix/A_claims_table.tex`) and `phase3/ROLE_IN_PROGRAM.md`.
There is no standalone `phase3/CLAIMS.md` at this rung.

Scope (summary):
- Baseline non-cancellation floor on a global amplitude observable.
- Binding-style diagnostics and mechanism-level tables (no corridor narrowing).
- No flavor-sector calibration in canonical Phase 3.

Canonical artifacts: Phase 3 paper `phase3/artifacts/origin-axiom-phase3.pdf`
and tables in `phase3/outputs/tables/`.

Archived flavor-sector calibration lives under
`experiments/phase3_flavor_v1/` and is non-canonical.

---

## Future phases (placeholders)

Future phases must:

1. Declare scope and explicit non-claims.
2. Define canonical artifacts (paper, figures, configs).
3. Add claim IDs to their own `PHASEx/CLAIMS.md`.
4. Register those claim IDs here.
5. Obey Phase 0 governance rules (especially P0-C01–P0-C07).

---

For the status of each phase, and which layers are allowed to carry canonical claims, see also `docs/GATES_AND_STATUS.md`.
