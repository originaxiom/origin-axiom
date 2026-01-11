# Phase 3 Scope (Flavor Integration Add-on)

## Goal
Phase 3 integrates the **flavor anchor** (a single phase θ extracted from CKM+PMNS fits) into the **already-established Phase 2 vacuum mechanism**, and documents the resulting **correlation** under strict under-claiming.

## In scope
1. Reproducible θ-fit pipeline (CKM + PMNS) with uncertainty reporting and fit diagnostics.
2. Inject θ into the Phase 2 vacuum-residue mechanism (as a parameterization layer), producing Δρ_vac(θ) / residue metrics.
3. Document **what would falsify** the flavor↔vacuum linkage hypothesis (e.g., future global-fit tightening).
4. Phase 3 paper + provenance bundle + gates, satisfying Phase 0 discipline.

## Out of scope (explicit)
- Claiming a full solution to the cosmological constant problem.
- Claiming θ is uniquely derived from first principles.
- Expanding Phase 3 into baryogenesis / dark matter as core results.
- Re-opening Phase 2 or changing Phase 2 claims.

## Notes
If new facts emerge that are necessary to fulfill this scope, they must be introduced via a **Scope Addendum** file and recorded in CLAIMS_TABLE.

---

## Archive status and canonical Phase 3

_Status note (2026-01-11)._ This `experiments/phase3_flavor_v1/` tree is an
archived Phase 3 flavor-sector experiment. It is **not** part of the canonical
Phase 3 mechanism module.

- See `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md` for the explicit
  archive banner and the rationale for retiring this experiment from the main
  claims ladder.

- Canonical Phase 3 lives under `phase3/` and is documented by
  `phase3/MECHANISM_CONTRACT.md`, `phase3/ROLE_IN_PROGRAM.md`, and the Phase 3
  paper `artifacts/origin-axiom-phase3.pdf`. All live Phase 3 claims and
  diagnostics should be interpreted with respect to those canonical artifacts,
  not this archived flavor tree.
