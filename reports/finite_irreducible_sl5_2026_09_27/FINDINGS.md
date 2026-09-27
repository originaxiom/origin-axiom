# Irreducible global seeds exist; these two have the wrong cusp capacity

2026-09-27. Local fork `audit/fork-2026-09-20`. Preregistered inputs,
proof, producer and tests were committed at
`8aea811f8f89121cfc3aea7600c0b793dcfa4dd5` before execution. This is a
local research result, not shared-bank completion or a physical chirality claim.

## What was exhaustively searched

For each of the two fixed meridians in INPUTS.json, EVERY ordered pair
(B,C) in A6 x A6 was tested against the diagram-certified M2 relators:
129600 pairs per meridian. No adaptive stopping. The rank-five module is
the augmentation subspace of the six-point permutation representation.
Double transitivity certifies its complex irreducibility. Equivalence here
is conjugacy by the S6 centralizer of the fixed meridian, not classification
under all complex basis changes.

| Six-point meridian | Relator solutions | Transitive | Irreducible augmentation | Representatives |
|---|---:|---:|---:|---:|
| (3,1,1,1) | 46 | 0 | 0 | 0 |
| (3,3) | 46 | 45 | 36 | 2 |

Both representatives were diagnosed; the declared twelve-representative
cap omitted none. The full representative-list hashes and literal generator
permutations are in RESULTS.json. Both image groups have order 60;
their group isomorphism type is not asserted on order alone.

## The positive

These are exact GLOBAL irreducible SL5 representations of M2, with an
explicit positive invariant Gram matrix Q=I+ones. They are different starting
points from the previous nonsplit seed's locally forced 3+1+1 splitting.
The semisimple order-three meridian is a declared change of peripheral
class, not a deformation within the earlier nontrivial-Jordan class.

In the trace-free Q-self-adjoint rank-fourteen module, transverse to SO(Q)
inside SL5, both seeds have H1 dimension 5. Restriction to the full cusp
torus, meridian circle and longitude circle each has rank 4 and kernel 1.
Thus there is a genuine first-order nonorthogonal relative direction.
Its nonlinear integrability is NOT established.

## The limiting fact is the actual longitude

The preferred longitude is T for representative 0 and T inverse for 1.
On M6 the meridian cubes to identity, but that longitude still fixes only
ONE direction in E, not three. The computed tuples below are
(a0,a1,t0,t1,r1); V and its actual dual agree.

| Coefficient | M2 tuple | M6 tuple | M6 interior dimension | Index |
|---|---|---|---:|---:|
| E | (0,1,1,2,1) | (0,3,1,2,1) | 2 | 0 |
| exterior-square E | (0,5,4,8,4) | (0,5,4,8,4) | 1 | 0 |

The interior dimensions are NOT boundary capacity or chiral index. Self-duality
forces both indices zero and was declared before execution: these are controls,
not non-vacuous failures of chirality.

At either seed, global invariant dimensions for E and its dual on M6 are
zero and boundary invariant dimensions are one. Nonzero minors persist
nearby, so the former remain zero and the latter cannot exceed one in a
sufficiently small neighborhood. The exact boundary index identity then
gives |I(E)| <= 1 there. This prevents a NEARBY ordinary interior-index-three
route even if the first-order nonorthogonal direction integrates. It is
not a no-go for distant components, different peripheral data, physical
sources, or different physical operators.

## Verification and next decision

Native producer: exit 0. New focused tests: 6 passed. Combined current
parent/boundary/deck/global/local/finite regression: 70 passed, exit 0.
The sole warning concerns optional tkinter GUI support, not these calculations.
All five source hashes and three dependency hashes were unchanged after runs.
Raw stdout and terminal receipts are retained alongside this report.

Do not spend a nonlinear continuation solely to chase three in these seeds'
small neighborhood. A new seed must first clear the ACTUAL paired meridian
and longitude capacity screen. A possible different five-point action of the
order-sixty image is only an untested lead; identifying it and testing any
monomial lifts would change the representation, not overturn this result.
No mathematical index has been identified with a normalizable physical fermion,
and no action, anomaly-free spectrum or empirical prediction is derived here.
