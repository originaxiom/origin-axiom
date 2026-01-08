
## Phase 3A — Flavor-sector θ-filter (experimental add-on, archived negative result)

This module was originally implemented under `phase3/` as a flavor-sector
calibration add-on. It exports a θ-filter derived from CKM/PMNS snapshots and
feeds into the Phase 0 corridor ledger. In its locked configuration, the
Phase 0 ledger reports an empty combined corridor once this filter is applied,
so it is treated as a negative result for that ansatz/target combination.

The full implementation and its paper are now archived under:
`experiments/phase3_flavor_v1/`.

This experiment is **not** the "Phase III: principled mechanism" described in
the Phase 0 contracts; `phase3/` is reserved for that mechanism.




## C3.1 — Fit claim (within ansatz)
We can reproduce a best-fit θ and uncertainty interval from the stated CKM+PMNS targets within the Phase 3 ansatz class, with documented goodness-of-fit and diagnostics.

## C3.2 — Injection claim (conditional)
Given a θ value (fit-derived), injecting θ into the Phase 2 vacuum mechanism produces a reproducible Δρ_vac(θ) / residue metric curve under the declared injection hook.

## C3.3 — Falsifiability claim (procedural)
We provide explicit conditions under which the flavor↔vacuum linkage hypothesis would be weakened or falsified. For example:
- if future data exclude the fitted θ region under the chosen ansatz; or
- if the Phase 0 corridor ledger, when updated with the Phase 3 θ-filter, yields an empty
  intersection with the Phase 0–2 corridor, indicating that no θ survives all filters for
  that specific Phase 3 ansatz/target combination.
In both cases, the failure is attributed to the locked ansatz/target choice and test suite,
not treated as a proof that the Origin Axiom itself is false.
