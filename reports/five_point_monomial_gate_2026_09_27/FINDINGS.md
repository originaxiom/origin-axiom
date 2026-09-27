# A better common-parent seed: irreducible, non-self-dual, correct capacity; no interior modes at t=2

2026-09-27. Local research, branch `audit/fork-2026-09-20`.
Seal `147c07c90390fba0214a4af31d144a9625673026` preceded every scientific
execution. Both literal inputs and every selected quotient direction were
tested. No physical chirality, completed TOE or shared-bank completion claim.

## What changed, and what was retained

The [previous two global seeds](../finite_irreducible_sl5_2026_09_27/FINDINGS.md)
used the rank-five AUGMENTATION module of six-point permutation groups.
Their M6 longitude fixed only one direction. Their small-neighborhood
index bound remains valid.

Both groups have fifteen involutions and precisely five Klein-four
subgroups. Conjugation on those five subgroups gives a verified faithful
even-permutation image of order sixty: A5, now identified by its actual
action, not guessed from its order. Its rank-five PERMUTATION module is a
different representation, reducible 1+4 at the finite point. This is a
declared new starting representation.

B1295 already surveyed covers through degree ten. The associated five-sheet
cover of M2 has three cusps (peripheral sheet orbits of sizes 3,1,1) and
degree ten over m004. Its existence is not claimed as a new cover discovery;
this calculation concerns deformations of a common rank-five coefficient.

## Two exact one-parameter families

Write G=D(t^v)P with P acting on column basis vectors and v indexed by
output row. In both cases T is the pure permutation (0 1 2), fixing 3 and 4.
The following permutations are image lists, not cycle notation.

| Seed | B permutation | C permutation | B exponents | C exponents | Longitude |
|---|---|---|---|---|---|
| 0 | [2,4,3,1,0] | [4,1,3,2,0] | [0,0,2,-1,-1] | [1,-2,1,0,0] | T |
| 1 | [2,1,3,0,4] | [4,1,0,3,2] | [3,-1,-1,0,-1] | [1,1,-3,1,0] | T inverse |

Relators, determinant-one conditions and the PURE preferred longitude give
an integer linear system of rank seven in ten exponent variables.
Its solution dimension is three. Two dimensions are diagonal conjugation
commuting with T, leaving one genuine rational quotient direction for
each seed. The table records primitive integer representatives of those
directions, not a claimed saturated integral lattice basis.

Exact word-exponent addition proves the relators and fixed peripheral
pair for ALL nonzero t. This is not an interpolation from a finite grid.
At t=1 both controls have matrix-algebra dimension 17 and bilinear-form
space dimension 2, as expected for the reducible permutation module.
At the preregistered t=2, BOTH families instead have:

- full generated matrix-algebra dimension **25**, certifying complex
  irreducibility, not merely a scalar-commutant test;
- invariant bilinear-form dimension **0**, certifying non-self-duality;
- the actual M6 meridian equal to I and longitude equal to T or T inverse,
  hence boundary fixed dimension **3** in E.

This removes two obstructions to using these points as starting candidates:
reducibility and the previous longitude's capacity-one bound. It does NOT
derive an index of three. The parameter t=2 is an exact test input, not a
selected vacuum, a derived scale or an observed physical constant.

## Both actual coefficients were computed: no interior cohomology at t=2

The [parent dictionary](../m6_parent_admission_2026_09_27/FINDINGS.md)
requires E and its ACTUAL exterior square, not independent fitted modules.
Tuples below mean (a0,a1,t0,t1,r1), including global invariant corrections.
Both seeds give the same tuples; V and its actual dual agree.

| Coefficient | M2 tuple | M6 tuple | M6 interior n | M6 dual n | Interior index |
|---|---|---|---:|---:|---:|
| E | (0,3,3,6,3) | (0,3,3,6,3) | 0 | 0 | 0 |
| exterior-square E | (0,4,4,8,4) | (0,4,4,8,4) | 0 | 0 | 0 |

All H1 at these points restricts nontrivially to the boundary. There is no
hidden algebraic chiral count in these particular coefficients at t=2.
Unlike the finite controls, this zero is not explained by an invariant
bilinear form: no such form exists in E. This does NOT prove a universal
zero for all non-self-dual representations or even every parameter here.

## The first-order escape test

The twenty off-diagonal matrix units give the exact adjoint module
transverse to monomial variations. At both t=2 points:

- H1 dimension = 8;
- full-torus, meridian-circle and longitude-circle restriction ranks = 8;
- all three relative kernels = **0**.

Thus no non-gauge FIRST-ORDER direction leaves the monomial ansatz while
fixing the meridian at those points. We have not proved that every
higher-order/nonreduced deformation is absent, that all parameters have
the same rank, or that a distant component is empty. This is not a
repetition of the previous 3+1+1 implicit-function theorem.

## Verification and the next discriminating step

Native producer and new focused suite both exit 0; six tests pass.
Combined current parent/boundary/deck/global/local/finite/monomial suite:
**76 passed**, exit 0. Optional tkinter GUI warning only. All five source
hashes and four reused dependency hashes remained unchanged. Tests also
check the family equations at the unfitted values -1,3,5; the all-t proof
comes from integer word exponents, not these finite checks.

The first hash command failed before sealing because of the host's invalid
C.UTF-8 locale; the successful C-locale retry and that failure are retained.
There were no scientific-run failures in this gate. Raw stdout, structured
results and terminal receipts are preserved; no independent external
mathematical review is claimed.

The next worthwhile algebraic test is a DETERMINANTAL EXCEPTIONAL-PARAMETER
calculation: determine where interior cohomology or relative off-monomial
rank can jump, then certify those values individually. A new random scan
would not answer that question. If the exceptional points do not help,
retain the useful family and change the specified mechanism explicitly.

A finite-energy harmonic metric for these reductive monomial backgrounds
is a separate analytic lead, not proved here. Even proving it would not
make these zero interior counts into physical generations. The physical
parent action, chosen metric, norm/domain, full spectrum, interactions,
anomalies and discriminating observations remain essential obligations.
