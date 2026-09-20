# R40: the nonsplit positive has a faithful parent map, not yet a physical vacuum

2026-09-20. Own branch audit/physical-bridge-2026-09-05.
Scientific snapshot 9e2d43ec8a6710ece4906b0b8468b58fdb84c0a5 was pushed
and server-confirmed before first execution. All six scientific files
remain unchanged. The intended pre-execution seal-LEDGER entry failed;
its explicit post-execution correction is described in section 7 below.
No shared B, independent main acceptance or TOE completion.

## The result that changes the next task

The actual R27 nonsplit coefficient embeds faithfully into the supplied
E8 candidate through a determinant-one rank-five enlargement. Its +1
interior index survives unchanged; the complete accompanying exterior-
square coefficient also has +1. Thus the formal SU5 matter difference
is 10+bar5, with an additional vector-like 5/bar5 pair in the interior
counts. Its SU5 cubic anomaly cancels under that formal interpretation.

This is a positive coefficient/group-theory join, not a derived physical
generation. The extra block-preserving U1 gives nonzero formal anomaly
coefficients (5,15,-75). More fundamentally, an actual positive global
background and its normalizable fermion modes are not established by
these algebraic cohomology groups. Both qualifications are part of the
result, not separate reasons to erase it.

Sources and exact controls: [design](COEFFICIENT_PARENT_DESIGN.md),
[authored argument](COEFFICIENT_PARENT_PROOF.md),
[producer](coefficient_parent.py), [prior/reuse](COEFFICIENT_PARENT_PRIOR.md),
[native output](COEFFICIENT_PARENT_NATIVE_FIRST.jsonl),
[receipts](COEFFICIENT_PARENT_RECEIPTS.json).

## 1. Why the previous four cannot simply be reused

For the original marked m010 witness, V=chi Sym3(rho) has
det(V)=chi^4, nontrivial of order three. It is not the defining-four
SL4 coefficient of the geometric R39 background. Matching ranks would
lose the actual determinant character. All eight scalar repairs with
determinant one were exhausted exactly; they have zero interior index.
This only excludes that scalar-replacement repair, not every embedding.

Instead retain V literally and add L=(det V)^-1=chi^2:

    W=V+L,                 X -> diag(X,det(X)^-1).

The map is injective because its upper block recovers X. All relations,
marked peripheral maps, determinants and the nonsplit subspace are
checked. The wrong determinant line fails. Rank five is minimal only
under this unchanged-direct-summand requirement; it is not a physical
dimension, a selected parent or a uniqueness theorem for the programme.

## 2. Every parent sector, not a selected branch

The complete root/weight computation gives, gauge factor first,

    E8 -> (SU5 x SU5)/Z5,
    248=(24,1)+(1,24)+(10,5)+(bar10,bar5)
                          +(5,bar10)+(bar5,10).

The product root-lattice index is five; the actual center kernel is
(zeta,zeta^-2). Each separate factor embeds faithfully. Incorrect
conjugation bars preserve dimension 248 but fail the full weight test.
This known subgroup is credited to the primary literature in the prior;
the new use here is the explicit actual-coefficient map and all sectors.
Complex flat monodromy is not claimed unitary. E8 and the physical
spacetime remain supplied model choices.

## 3. Exact cohomology roster

Let n(E)=dim ker[H1(M,E)->H1(T,E)] and I(E)=n(E)-n(E dual).
These are algebraic interior restriction groups, NOT asserted L2 kernels.
The table retains global flat invariants to expose omitted-sector risks.
All H1/H2 and torus/restriction data are in the native output.

| coefficient | rank | H0(E), H0(E dual) | n(E), n(E dual) | I(E) |
|---|---:|---|---|---:|
| trivial | 1 | 1,1 | 0,0 | 0 |
| V | 4 | 0,0 | 1,0 | 1 |
| L | 1 | 0,0 | 0,0 | 0 |
| W | 5 | 0,0 | 1,0 | 1 |
| exterior-square V | 6 | 1,0 | 1,0 | 1 |
| V L | 4 | 1,1 | 1,1 | 0 |
| exterior-square W | 10 | 2,1 | 2,1 | 1 |
| V L^-1 | 4 | 0,0 | 0,1 | -1 |
| End0(V) | 15 | 1,1 | 2,2 | 0 |
| End0(W) | 24 | 2,2 | 3,3 | 0 |
| chi^2 Sym4(rho) | 5 | 1,0 | 1,0 | 1 |

Every row includes the dual complex, relator, differential, peripheral
and restriction-chain checks, two restriction-rank constructions and
duality/Euler identities from the reused R27 engine. Direct-sum
identities hold for EVERY reported cohomology dimension, not just I.
An explicit invertible Clebsch--Gordan matrix intertwines the actual
two generators for exterior-square Sym3=Sym4+1. No semisimplification
was substituted for V; R27's semisimple zero remains a separate control.

## 4. The positive SU5 result and the U1 warning coexist

For the block-preserving T=diag(1,1,1,1,-4), the signed formal roster is

    10_1 + bar5_2 - 1_5,

plus the zero-index pairs/real sectors explicitly retained above. The
minus sign means the conjugate singlet 1_-5 in this formal dictionary.
It is not the usual anomaly-free SO10-family U1 assignment.
Using A(5)=A(10)=1 and T(5)=1,T(10)=3, verified symbolically,

| conditional local anomaly | coefficient |
|---|---:|
| SU5 cubed | 0 |
| SU5 squared times U1 | 5 |
| gravity squared times U1 | 15 |
| U1 cubed | -75 |

This is a diagnostic conditional on identifying these indices with the
left-Weyl differences. It is NOT an actual quantum-anomaly calculation
of a derived compactification. In particular, all form degrees, source
and end states, normalizability and matching contributions must come
from one actual action. Ordinary H0 does not by itself count physical
vectors. Nor is SU5 x U1 asserted to be the full physical commutant.

The nonzero entries require a real resolution if that U1 and dictionary
survive: complete anomaly matching/inflow or a different consistently
derived sector/background. Giving an anomalous gauge boson a Higgs mass
alone is not anomaly cancellation. Do not add unmotivated rescue fields
or call the bundle impossible. Likewise SU5^3=0 alone is not a vacuum.

## 5. The metric/current map sharpens, but does not pay, the physical debt

The positive-metric enlargement is H5=diag(H4,(det H4)^-1). Within this
block ansatz, harmonicity of H5 is equivalent to harmonicity of H4:
it does not manufacture a solution. The connection and full residual
map is X -> diag(X,-tr X). The current therefore must be mapped in
all components; an arbitrary prescribed current is not a source action.
The whole-Cartan trace computation gives tr248=60 tr5 and
tr5 j_*(X)^2=tr4 X^2+(tr4 X)^2 on Hermitian tangent fields.

The incoming finite-energy and controlled-growth restrictions remain
scoped. A smooth, complete, source-free finite-energy nonsplit bundle
still meets F01's obstruction; adding the determinant line does not
remove it. F04's rank-four bound transfers through this block metric
ansatz, not by assertion to every rank-five metric. F02 supplies the
ordinary-L2 graph-domain theorem only for an actual specified positive
background. F05's geometric positive gap is not automatically a gap
for this nongeometric coefficient. [Reception](FORK_F02_F05_RECEPTION_2026_09_20.md).

## 6. Tests, failure custody and next physical decision

- Native exact run: exit 0, including all eleven paired coefficient
  systems, eight scalar repairs, whole-parent and opposite controls.
- New tests: 20 passed.
- Fifteen-file focused population: 236 passed, FOUR unchanged prior
  failures. Exact failed IDs match R39; the raw failures are retained.
- Incoming unchanged F02/F03/F04: 55 passed, one optional GUI warning.
  Incoming unchanged F05: 24 passed. These reuse the authors' producers;
  they are not independent implementations or proofs of all analytic claims.

No full-suite/main-bank or independent-expert certificate is claimed.
See the receipt checker and [final checks](COEFFICIENT_PARENT_FINAL_CHECKS.txt)
for artifact custody, the retained first law-map citation failure and
known governance debts. No sealed source or failing prior assertion was edited.

Next, test the actual representation-valued source/current and global
positive metric in this parent, keeping the full field equations and
source variations. Then compute the complete physical fermion/gauge/
source/end spectrum and anomaly matching. A block-breaking deformation
would require recomputing these cohomologies rather than carrying them
over by name. The separate R19/R29 sourced route stays live and scoped.

Three physical generations, selected SM breaking, realistic couplings,
quantum consistency, four-dimensional gravity and empirical discrimination
are not derived here. The full mission remains active.

## 7. Pre-execution snapshot is real; the ledger-entry failure is also real

The six full SHA256 values were printed before execution. All six
scientific files were committed at 9e2d43ec, pushed and server-confirmed
before the native run. However the inline Ruby command intended to
generate docs/SEAL_LEDGER.md rows failed parsing its Unicode heading.
Its exit was not checked before its returned text was inserted. Three
US-ASCII error lines, not six hash rows, entered that commit's ledger.
The first custody checker correctly rejected the missing ledger entry.

The erroneous ledger text remains in the original commit, the live
ledger and COEFFICIENT_PARENT_SEAL_LEDGER_FIRST.txt. The failure capture
is retained. The ledger now labels the actual rows POST-EXECUTION
CORRECTION. This does not retroactively earn compliance with the
pre-execution ledger-entry rule, even though the independently verifiable
pre-execution Git snapshot and remote confirmation fixed all science.
No scientific source, hypothesis, computed output or assertion changed.
The custody checker is rerun unchanged after the metadata repair.
