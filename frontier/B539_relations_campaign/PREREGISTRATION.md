# B539 — The Relations Campaign (pre-registration)

*Committed before compute, 2026-07-12. The reframe's final door: the object
forces RELATIONS between dimensionless observables (never values). Does any
pair of SM dimensionless parameters satisfy the object's forced relations?
Value-matching stays closed (B533 Gate 3); this campaign tests two-variable
relation structure, with a positive control and a null model.*

## R0 — The relation catalog (object side, exact)

From B535's read-out dictionary: classify all pairwise ratios of the 17
components in ℚ(τ). Extract the PREREGISTERED generating relation set:
two-variable polynomial relations P(x,y) = 0 with integer coefficients of
height ≤ 8 and degree ≤ 4 that the object forces between read-out ratios.
Known members (must be recovered): y = x² (τ² = φ, the cross/within-species
law); x²y − ... the Perron identities (β·|λ₂| = φ as a ratio relation);
f_A − f_a = f_a². The catalog is FROZEN at the end of R0, before R2.

## R1 — Observer-invariance (which relations are structural?)

For each of the 6 coupling types: does the type's read-out set expose the
catalog relations? A relation is STRUCTURAL if every coupling type carries a
ratio pair satisfying it. Prediction: y = x² (τ,φ) is exposed by all types;
type-specific relations get marked observation-side and EXCLUDED from R2.

## R2 — The test (SM bin + positive control + null)

**Positive control (forced bin):** the measured E8 ladder ratios (B538) must
satisfy the golden self-similarity relations within experimental tolerance —
if the control fails, the method is broken and R2 is void.

**Test bin:** the same 21 SM dimensionless parameters as B533 Gate 3 (frozen
list, PDG values at conventional scales — scale-dependence noted as caveat).
For every ordered pair (x,y) of SM values and every catalog relation P:
hit ⟺ |P(x,y)| / scale(P,x,y) < tol, at tol ∈ {1e-2, 1e-3, 1e-4}.

**Null model:** 500 synthetic 21-sets, each value magnitude-matched
(log-uniform within [v/2, 2v] of the true value), same hit-counting.
Verdict criteria (frozen): a relation-pair hit is REAL only if its
family-wise p (vs the null distribution of total hit counts) is < 0.001 at
tol ≤ 1e-3 AND survives tightening to the value's experimental precision.
Otherwise: NO-MATCH, banked as the honest closure of the relations door.

**Stated expectation (before compute):** positive control PASSES;
SM bin: NO-MATCH (hit counts within the null distribution). If that holds,
the reframe's ledger is complete and symmetric: the object's relations
hold in forced/critical data and are absent from the SM parameter set —
the structural theorem in its final, fully-tested form.

## Method
Exact algebra in ℚ(τ) (sympy) for R0/R1; float64 with per-value tolerances
for R2 (values carry ≤ 1e-6 relative precision). Locks: tests/test_b539.py.
