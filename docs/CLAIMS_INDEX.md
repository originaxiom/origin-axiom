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

## Phase 3 — Flavor-sector calibration add-on (CKM/PMNS θ-filter)

**Source of truth:** `phase3/CLAIMS.md`  

Scope (summary):
- Ledger-compatible add-on that fits a fixed, explicitly stated ansatz to frozen CKM/PMNS CP-phase targets.
- Allowed claim types: corridor-compatible fit, injection, and procedural falsifiability statements under the declared ansatz
  (no Origin Axiom proof, no Standard Model parameter reduction).
- Canonical artifacts: Phase 3 paper `phase3/artifacts/origin-axiom-phase3.pdf`, fit tables in `phase3/outputs/tables/`,
  and the ledger-facing θ-filter `phase3/outputs/theta_filter/phase_03_theta_filter.json`.

Registered Phase 3 claims (see `phase3/CLAIMS.md` for full statements and evidence):

- **C3.1 — Fit claim (within ansatz)**  
  CKM+PMNS-anchored best-fit θ and uncertainty interval within the declared Phase 3 ansatz class, with diagnostics in
  `theta_fit_summary.csv` and `theta_fit_diagnostics.json`.

- **C3.2 — Injection claim (conditional)**  
  Given a θ value (fit-derived), injecting θ into the Phase 2 vacuum mechanism produces a reproducible Δρ_vac(θ) /
  residue metric curve under the declared injection hook (`fig2_delta_rho_vac_vs_theta.pdf` and meta).

- **C3.3 — Falsifiability claim (procedural)**  
  Explicit conditions under which the flavor↔vacuum linkage hypothesis and the locked Phase 3 ansatz/target combination
  are weakened or falsified, including the case where the Phase 0 corridor ledger reports an empty combined corridor
  once the Phase 3 θ-filter is applied.

---

## Future phases (placeholders)

Future phases must:

1. Declare scope and explicit non-claims.
2. Define canonical artifacts (paper, figures, configs).
3. Add claim IDs to their own `PHASEx/CLAIMS.md`.
4. Register those claim IDs here.
5. Obey Phase 0 governance rules (especially P0-C01–P0-C07).