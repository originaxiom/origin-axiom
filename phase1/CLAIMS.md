# Phase 1 Claims Register

Each claim must map to a paper section + an artifact (figure/table/run log) OR be explicitly
labeled as an axiom/assumption.

C1 (Axiom): A strict non-cancellation bound exists: |A| > ε > 0.
- Status: Postulate (not derived)
- Paper: Sec. 2
- Evidence: N/A (axiom)

C2 (Toy lemma): For finite sums of complex contributions, forbidding perfect cancellation
implies a non-zero residual amplitude floor for any non-π relative phase (“twist”).
- Status: Demonstrated (analytic + numeric)
- Paper: Sec. 3
- Artifacts: Fig A (phasor toy)

C3 (Numerical existence proof): In a lattice toy model where A is the global mean field,
enforcing |A| ≥ ε prevents deep cancellation while keeping dynamics stable.
- Status: Demonstrated (numeric)
- Paper: Sec. 4–5
- Artifacts: Fig B (|A(t)| constrained vs unconstrained), run metadata

C4 (Scaling): Unconstrained residual scales toward zero with increasing system size
(≈ N^{-1/2} or equivalent), while constrained residual saturates at ε (intensive).
- Status: Demonstrated (numeric sweep)
- Paper: Sec. 5
- Artifacts: Fig C (scaling curve), sweep table

C5 (Energy discipline): Constraint enforcement does not introduce order-one energy artifacts
in the toy model (within numerical tolerance).
- Status: Demonstrated (numeric check)
- Paper: Sec. 5 + Sec. 6 (limitations)
- Artifacts: Table / log ΔE/E, optional inset