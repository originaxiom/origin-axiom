# PC12 Draft Note Skeleton

Status: internal computational-note skeleton (rescaled 2026-06-01 from
theorem-note per the B53 literature screen). Not a public preprint. Per
`LITERATURE_POSITIONING.md`, Thm 1-3, the exchange decomposition, and the
symbolic-`m` factorization are `STANDARD_REPACKAGE` (Lawton `SL(3,C)`
coordinates; Baake-Grimm-Roberts substitution trace maps; Bellon-Viallet
algebraic entropy); only Thm 4 (fixed-line splitting) is `APPARENTLY_NEW`, and it
is elementary. The note states the standard blocks with citations and presents
Thm 4 as the lone new arithmetic observation -- no heavy theorem-prose for the
standard blocks is warranted.

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
symbolic support: B51 derives the c=3 fixed-line derivative rows from the
  triple-root recurrence with m formal
general-c support: B54 proves [J(m,c),P]=0 for symbolic c, so the exchange
  block-diagonalization holds on the whole fixed line (not just c=3); the c=1
  specialization gives the Eisenstein/golden twin polynomials (disc -3, 5)
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
symbolic proof module: B51 proves the c=3 Jacobian block factorization for
  formal m, replacing the earlier m<=50 confidence check for that component
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

0. For the diagonal fixed line `c=3`, use the symbolic derivative module:

```text
tau_k recurrence at c=3 has characteristic equation (r-1)^3=0
d tau_k / d x1 = k(k^2-1)/2
d tau_k / d x2 = 1-k^2
d tau_k / d x3 = k(k+1)/2
d tau_k / d x4 = -k(k^2-1)/2
d tau_k / d x6 = k(k-1)/2
```

The exchange `x1<->x4, x2<->x5, x3<->x8, x6<->x7` gives the `sigma`
derivatives. The symbolic `8x8` Jacobian commutes with exchange and has
sector characteristic polynomials:

```text
symmetric:     (t-1)(t+1)(t^2-(m^2+2)t+1)
antisymmetric: (t^2+mt-1)(t^2-(m^3+3m)t-1)
```

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
The naive three-channel Fibonacci tight-binding bridge fails: standard
multichannel transfer matrices are doubled 6x6 symplectic matrices, not the
PC12 3x3 SL(3) character-variety recursion.
```

## Reproducibility Appendix

Required commands:

```bash
python frontier/B48_sl3_metallic_trace_maps/probe.py
python frontier/B48_sl3_metallic_trace_maps/probe.py --deep
python frontier/B49_sl3_certificate_proof_hardening/probe.py
python frontier/B51_sl3_symbolic_m_factorization/probe.py
python frontier/B52_multichannel_fibonacci_bridge_control/probe.py
python -m pytest tests/test_sl3_metallic_trace_maps.py tests/test_sl3_certificate_proof_hardening.py tests/test_sl3_symbolic_m_factorization.py tests/test_multichannel_fibonacci_bridge_control.py -q
```

## Draftability Gate

PC12 can move from `NEEDS_VALIDATION` toward `DRAFTABLE` only after:

```text
literature positioning -- DONE (LITERATURE_POSITIONING.md): rescaled to a
  computational note; Thm 1-3 are STANDARD_REPACKAGE, Thm 4 the lone new bit
entropy (Thm 3) stated with a Bellon-Viallet degree-growth citation, not as a
  fresh theorem
global c>=15 and c<=-12 exclusions (Thm 4, the one genuinely new block) written
  as readable prose -- still worth doing
compact SU(3) language verified as non-physics
physics-bridge language keeps the B52 negative control explicit; the
  self-evidencing / free-energy framing stays quarantined in paths/E21, not PC12
independent specialist read of Thm 4 + framing -- deferred this cycle
```
