# R5: the complete one-loop spectrum stabilizes the SM angular directions

**Positive result.** In the explicitly chosen R4 compact-E6 theory, the full
one-loop calculation lifts its eleven extra tree-level scalar zero modes
with **positive** leading mass-squared corrections. Both scalar and vector
loops favor local stability of the SM orientation; fermion masses are
orientation-independent on this family. This is a concrete quantum-dynamical
advance beyond the classical subgroup/vacuum construction.

It is **not** a derived action, a completed TOE, a full pole-mass calculation,
or a certified globally selected vacuum. The precise scope matters just as
much for this positive result as for any negative.

## 1. The physical model and what was actually summed

The [R4 action](VACUUM_MODEL.md) contains two complex scalar 27s, one real
adjoint, compact E6 gauge fields and Weyl-27 fermions with the invariant cubic
Yukawa coupling. Here all displayed scalar-potential coefficients equal a
common positive lambda; they are **not** all the independent allowed couplings.

The tree vacuum family is `phi1=S, phi2=N, A in su5, Tr27 A^2=5`. Scales are
in R4's arbitrary VEV units, not GeV or measured Planck units. Use
`Tr27(t_a t_b)=3 delta_ab` to define the free gauge coupling g; the actual
representation verifies this normalization on the simple SU2 generators.

The full fluctuation calculation includes **186 real scalar modes, 78 vector
modes and 27 Weyl modes** for the illustrative one-family Yukawa choice
y1=y2=1/4. At the SM point, 109 scalar eigenvalues are positive, 66 vectors
are massive, and ten Weyl masses are nonzero. The 77 scalar zeros include
66 gauge Goldstones and the eleven physical octet/triplet directions. None
was silently discarded. The fermion contribution was included, then found
to cancel in angular differences: its mass matrix contains S,N, not A.
This cancellation holds for any fixed family/Yukawa matrices in this action;
it does not derive the number of families.

Scalar masses solve the generalized kinetic-metric problem, not the raw
coordinate Hessian. For R4's Hermitian generators T, the metrics are
`K_s=diag(2 I108, Tr27(T_a T_b))`, `K_g=Tr27(T_a T_b)/3`.
Both an independent generalized eigenvalue solve and a direct kinetic-term
vector-mass calculation agree with the canonical normalization. Radial
controls give mass squared 4 lambda and 40 lambda as expected. The full
constraint Jacobian also agrees with a non-Y directional derivative to
1.70e-12. Non-positive kinetic and significantly negative mass controls fail.

The one-loop potential is MS-bar, Landau gauge, with scalar/Weyl/vector
weights 1,-2,3 and logarithmic constants 3/2,3/2,5/6, respectively. The
standard theoretical formula and conventions were checked against
[Martin, hep-ph/0111209v2, equations 1.1 and 3.2–3.5](https://arxiv.org/pdf/hep-ph/0111209).
No measured number was supplied to the calculation.

## 2. The eleven modes are lifted, not a reason to kill the vacuum

For a canonically normalized tangent X, `Tr X^2=1`, use the exact
norm-preserving path `(Y+epsilon X)/sqrt(1+epsilon^2/5)`. The leading
effective-potential curvatures are

```text
m_octet^2  = 0.00252156240250 lambda^2 + 0.11870218374944 g^4
m_triplet^2 = 0.01152111059417 lambda^2 + 0.11047574321489 g^4.
```

All coefficients are positive. Thus the result is not confined to a tuned
coupling-grid point: the common-quartic ray has positive leading angular
curvatures wherever this perturbative expansion is applicable. It is not a
claim about the entire independent-coupling space or all loop orders.

At the **preselected**, illustrative lambda=.2,g=.5 point, the values are
0.00751974898044 and 0.00736557837470 in squared VEV units. SM symmetry makes
them common within the eight- and three-dimensional irreducible multiplets;
off-diagonal color/weak directions independently reproduce the diagonal
calculations. A positive tree-level normal Hessian and positive leading
angular lifting support the corresponding perturbative local branch.
The full shifted vacuum and momentum-dependent pole masses have not been solved.

The initial finite differences used four successively halved steps. A separately
pre-sealed extension then differentiated J and the gauge orbit analytically and
used the spectral Hessian of `Tr f(M^2)`, including degeneracies and the
massless kernel. It agrees with the smallest-step estimate to 2.16e-6 in the
unit-coupling vector coefficient and 2.23e-8 in the scalar coefficient.
Nontrivial scalar, rotating-matrix, degenerate and emerging-zero-mass toy
controls independently test that derivative formula. This agreement did not
come from asserting a desired sign in the tests.

## 3. Scale independence is now an exact identity, not a lucky scan

The first run found sector-by-sector fourth-mass traces constant on the 99
named/random backgrounds (maximum variations 8.65e-12 and 5.12e-13).
The extension proves the corresponding **rational polynomial identities in
all four Cartan coordinates**, by exact coefficient subtraction.

For N=Tr27 A^2, the formal generalized operators built from J and G give

```text
Tr[(M_s^2/lambda)^2] = 73132/81 + (128/9) N + (193/3) N^2
Tr[(M_v^2/g^2)^2]    = 232/9 + 8 N + (9/2) N^2.
```

Both polynomial remainders are exactly zero. On the physical tree-vacuum
surface N=5 these equal **209167/81** and **3209/18**. Away from that surface,
2 J^T J is only a formal operator, not the complete off-vacuum scalar Hessian.
Compact SU5 diagonalization extends the fixed-norm identities from Cartan
representatives to this whole SU5-adjoint family.

Consequently its one-loop **angular differences** are independent of mu,
and their scalar/vector parts scale as lambda^2/g^4. Direct comparisons at
mu=1/2,1,2 agree. This proves neither that the full potential is scale
independent nor that all omitted operators are protected against generation.

## 4. Vacuum comparison: encouraging, but not a global certificate

At lambda=.2,g=.5 the SM orientation lies below the named SU4xU1 and old
generic competitors by **0.00065673281014** and **0.00280092372015** in VEV^4
units. Their unbroken dimensions are 16 and 4, versus 12 for SM.

All 96 random Cartan-sphere points and every complete scalar/vector spectrum
are preserved. Of eight pre-registered local-search starts, six random starts
converged to SM-like dimension-12 configurations within 1.86e-13 of the SM
energy. Starting at SM stayed there. Starting at SU4 also stopped immediately:
**optimizer success at a symmetric stationary point does not certify a minimum**.
No lower point was found by this bounded search; global optimality and
uniqueness were **not** proved. Sign-related and gauge-related orientations
must not be counted as independent matter generations or ignored in uniqueness.

## 5. What remains live

- Extend the stationary-vacuum calculation to its normal quantum shifts and
  a controlled perturbative range; determine other allowed couplings and
  any other tree-vacuum branches before a global selection claim.
- Construct and price the light electroweak doublet, then match the actual
  scalar/vector/fermion spectrum. R4 has no tree-level massless physical Higgs
  doublet; lifting an octet and triplet does not supply one. R2's older fitted
  spectrum and R3's restricted mass bound cannot be transplanted unchanged.
- Restrict or derive the spacetime, real form, field content, action, scales
  and Yukawa inputs from the programme, and compute independent observable
  consequences. Four-dimensional gravity is not supplied by this cell.

These are outstanding tasks, not reasons to erase the verified dynamical result.

## Evidence and reproduction

R5 design/code first sealed **0ac9352a**, first output preserved **b8833482**.
The derivative extension was sealed in b8833482 before its execution. Both
first scientific runs succeeded; the original R4 and upstream producers and
first results remain unchanged.

- [R5 design](EXTENSION_3.md), [full first result](quantum_first_run.json).
- [Independent derivative design](EXTENSION_3_DERIVATIVE.md),
  [exact identities and derivative result](quantum_derivative_first_run.json).
- [Code](quantum_vacuum.py), [derivative instrument](quantum_derivative.py).

```sh
OPENBLAS_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.quantum_vacuum --output /tmp/oa-quantum-new-run.json
OPENBLAS_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.quantum_derivative --output /tmp/oa-quantum-derivative-new-run.json
```

The runners refuse to overwrite outputs. Test and staged-gate evidence is
recorded separately in `QUANTUM_FINAL_CHECKS.txt`; this is not a full-repository
green certificate. Historical missing-evidence and seal-format failures
remain visible in [FAILURES.md](FAILURES.md).
