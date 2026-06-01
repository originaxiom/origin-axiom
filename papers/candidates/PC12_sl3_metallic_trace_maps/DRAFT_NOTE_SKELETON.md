# PC12 Draft Note Skeleton

Status: internal proof-draft skeleton. This is not a public preprint.

## Working Title

Metallic `SL(3)` Trace Maps: Commutator Invariants, Entropy, and Fixed-Line
Arithmetic

## Abstract Skeleton

We study the polynomial trace maps induced on the rank-two `SL(3,C)` character
algebra by the metallic free-group automorphisms

```text
phi_m(a)=a^m b
phi_m(b)=a
```

for `m>=1`. In standard trace generators, Cayley-Hamilton recurrences give an
explicit eight-coordinate formula. The maps preserve the unordered commutator
trace pair `{tr([A,B]), tr([A,B]^-1)}` and have algebraic entropy
`log((m+sqrt(m^2+4))/2)`. Along the diagonal fixed line, the antisymmetric
Jacobian quartic has a short integer splitting classification. The compact
diagonal `SU(3)` slice retains only `c=-1,0,1,3`.

## Claim Boundary

```text
standalone trace-map / character-variety mathematics
not an Origin-core claim
not a physics model
not a proof of PC11's T1/S1 selector
```

## Theorem Package

### Theorem 1 -- Metallic `SL(3)` Trace Map

For `m>=1`, the automorphism `phi_m(a)=a^m b`, `phi_m(b)=a` induces the
eight-coordinate trace map

```text
T_m=(tau_m, x1, tau_{m+1}, sigma_m, x4, sigma_{m-1}, tau_{m-1}, sigma_{m+1})
```

where

```text
tau_k   = x1 tau_{k-1} - x4 tau_{k-2} + tau_{k-3}
sigma_k = x4 sigma_{k-1} - x1 sigma_{k-2} + sigma_{k-3}
```

with the initial values from `CERTIFICATE_APPENDIX.md`.

Proof status:

```text
prose proof: straightforward Cayley-Hamilton derivation needed
machine check: B48 trace-map formula and direct SL(3,Z) sanity checks
```

### Theorem 2 -- Commutator Trace-Pair Invariant

The unordered pair

```text
{tr([A,B]), tr([A,B]^-1)}
```

is invariant under `T_m`.

Proof status:

```text
prose proof: group identity [a^m b,a] is conjugate to [a,b]^-1
machine check: covered structurally by B48/B27 commutator controls
```

### Theorem 3 -- Algebraic Entropy

The algebraic entropy is

```text
h_alg(T_m)=log((m+sqrt(m^2+4))/2).
```

Proof status:

```text
prose proof: degree induction from metallic sequence A_{n+1}=mA_n+A_{n-1}
machine check: B48 entropy degree recurrence and dominance checks
remaining polish: write no-cancellation dominance lemma cleanly
```

### Theorem 4 -- Fixed-Line Splitting Classification

The antisymmetric fixed-line quartic splits over `Z` exactly for:

```text
c = 1, 3
c = 0  with 3 | m
c = 2  with 6 | m
c = -1 with 2 | m
c = -3 with m = 2, 3
c = -9, -11 with m = 1
```

Proof status:

```text
prose proof: partially assembled by B49
machine check: B48 broad rectangle plus B49 proof-module checks
remaining polish: global c>=15 and c<=-12 coefficient-positivity exclusions
```

### Theorem 5 -- Compact Diagonal `SU(3)` Slice

Among integer splitting values, the compact diagonal `SU(3)` slice realizes
precisely:

```text
c = -1, 0, 1, 3
```

Proof status:

```text
prose proof: explicit representatives plus centrality exclusion for c=2
machine check: B48 compact SU(3) representative check
remaining polish: state as compact-unitary math only, not physics
```

## Proof Architecture For Theorem 4

The fixed-line splitting proof should be written in this order:

1. Put the antisymmetric quartic in the form:

```text
chi(t)=t^4-A t^3+C t^2+A t+1
```

2. Prove the universal criterion:

```text
chi(t)=(t^2-alpha t-1)(t^2-beta t-1), alpha,beta in Z
iff D=A^2-4(C+2) is a square and A+sqrt(D) is even.
```

3. List direct split families:

```text
c=1, c=3, c=0 with 3|m, c=2 with 6|m, c=-1 with 2|m
```

4. Prove the isolated negative split cases:

```text
(c,m)=(-9,1), (-11,1), (-3,2), (-3,3)
```

5. State the square-gap propagation lemma once:

```text
R^2 < D < (R+1)^2
```

and use third-difference recurrence propagation to keep both gaps positive.

6. Apply finite positive-strip tables for:

```text
4 <= c <= 14
```

7. Apply negative strip and boundary tables for:

```text
-11 <= c <= -2
```

8. Add global exclusions:

```text
c >= 15
c <= -12
```

These are the only parts still needing the most prose polish.

## Non-Claims Section

The note must explicitly say:

```text
No physical interpretation is claimed.
Compact SU(3) is used as a compact-unitary slice, not a gauge theory.
The direct/inverse trace distinction is not particle/antiparticle physics.
This does not solve the PC11 T1/S1 selector.
```

## Reproducibility Appendix

Required commands:

```bash
python frontier/B48_sl3_metallic_trace_maps/probe.py
python frontier/B48_sl3_metallic_trace_maps/probe.py --deep
python frontier/B49_sl3_certificate_proof_hardening/probe.py
python -m pytest tests/test_sl3_metallic_trace_maps.py tests/test_sl3_certificate_proof_hardening.py -q
```

## Draftability Gate

PC12 can move from `NEEDS_VALIDATION` toward `DRAFTABLE` only after:

```text
the global c>=15 and c<=-12 exclusions are written as readable prose
the entropy no-cancellation proof is written cleanly
the Lawton/Procesi/trace-map literature positioning is checked
the compact SU(3) language is verified as non-physics
```
