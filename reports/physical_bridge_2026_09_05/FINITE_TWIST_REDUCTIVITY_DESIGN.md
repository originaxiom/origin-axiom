# R27 follow-on: the positive, its actual domain, and a possible exact lift

2026-09-12. After-observation design, sealed before its own execution.
The original design/producer/tests at dbb55201 remain unchanged.

BANKED IDENTITY: the original R27 run reproduced B1335's finite-field
index +1 with its dual -1, all cochain identities, both dimension
equalities, and the dual cup matrix [[0,3],[3,0]]. It failed two
author-added assertions: the generated algebra has dimension 9, not
16; Hom(V,V*) has dimension 1, not 0. The generator trace obstruction
still proves non-self-duality. A nonzero intertwiner need not be an
isomorphism; a reducible module need not be semisimple. Both are to be
checked, not conflated. No successful arithmetic output is discarded.

PRIOR ART: FINITE_TWIST_PRIOR.md, the full first outputs, and B1297's
original domain sentence (reductive representation, with a0=a0* as a
consequence). The received B1335 `primescan.py` and `broad.py` were now
read in full at the pinned c83b6b8 snapshot. The former's irreducibility
filter tests only a COMMON EIGENVALUE across generators. It misses an
invariant line whose generator eigenvalues differ. It tests the base
two-dimensional module, not the final twisted symmetric-power module.
The later equality-only in-domain check cannot repair this omission.

## What is already observed and what is only proposed

The first native run, exit 1, elapsed 14.222525 seconds, raw SHA-256
b7b7646e9745ee78660e89d4f9a350571a2904757c01c04ee68ad5a809d0b959.
The first focused run, exit 1, 33 passed/2 failed/one optional GUI
warning in 74.68 pytest seconds, raw SHA-256
99bc8dac6948ea618ae18c1d073f38c4f1d6d6e190f091a45fe42212b6a98688.
Both public transcripts preserve their first outputs with path-prefix
redaction only; raw originals remain in the local supplied-data area.
The tree stayed read-only while both ran, and both are now terminal.

The exact target exposed by SnapPy 3.3.2 was:

    pi1(m010)=<a,b | aabaBaaBab>, mu=AbAA, longitude=babA,
    triangulation isosig=dLQbccchhsj_Bbab,
    A=[[0,1],[12,1]], B=[[0,3],[4,11]] over F13,
    chi(a)=4, chi(b)=12; V=Sym^3(rho) tensor chi.

Desk substitution gives a common line (1,4), eigenvalues 4 and 12;
this explains why the received filter can miss it. A candidate lift
uses K=Q(u), u^2-u+1=0, reduction u->4 modulo 13:

    A=[[0,1],[-1,1]], B=[[0,u^2],[u,-2]], chi=(u,-1).

These are observed-data-informed SMALL COEFFICIENT CHOICES, not a
unique reconstruction from one prime and not blind prediction. Whether
they satisfy the relation, preserve the positive index in characteristic
zero and fail semisimplicity will be computed; none is yet adopted.

## Frozen discriminating computation

Use a separate Sage exact-ring producer on F13 and K, independent of
the first producer's modular-rank implementation. No other-seat module
is imported. Pin the displayed presentation and witness matrices;
check every relator and peripheral chain-map equation again. Compute
cocycles by both explicit Fox blocks and crossed-homomorphism recurrence,
and boundary restriction on a kernel basis and by the stacked-rank
identity. Compare their n, dual and index results. If the proposed
characteristic-zero lift fails, report that exact failure without
relabeling the finite-field positive false.

Exhibit the common line and simultaneous upper-triangularizing matrix
P=[[1,0],[u,1]], and induce its symmetric cube. Check the entire
invariant flag and the unipotent B Jordan ranks on V. Solve for a
commuting projection onto the first invariant line: a complemented
line must admit such a projection. Compare ranks of that linear system
and its augmented system, not a numerical tolerance. Perform this for
both the base and V. A full invariant flag with one-dimensional
quotients plus a nontrivial nonsplit unipotent action proves the module
is not completely reducible. Do not equate finite image with modular
semisimplicity or equate reducible with nonsemisimple without this check.

Compute every V->V* intertwiner and its determinant/rank. A one-dimensional
space spanned by a singular map does not make V isomorphic to V*.
Retain the independent trace obstruction from the original run.

Build the actual diagonal semisimplification from the simultaneous
triangular form and recompute its cohomology and dual index. This is a
DIFFERENT local system, a control for extension data, not permission
to replace the original positive or its boundary invariant dimensions.
Use the upper-triangular flag to explain the distinction algebraically.

Reproduce the received same-eigenvalue filter as a deliberately flawed
control and show it accepts the target while the invariant-line and
complement tests reject irreducibility/semisimplicity. Recover both
an irreducible standard two-unipotent-generator SL2 module and a
reducible-but-semisimple diagonal pair as positive instrument controls.
The declaration that the finite-field identities/equalities alone
allow nonzero I is retained if the calculations hold; actual membership
in B1297's reductive domain is a separate outcome.

## Scope and physical consequence

All-member geometric vanishing is still the finite-cover proof, not
these sample calculations. If an exact non-geometric, nonsemisimple
complex positive exists, do not call the phenomenon merely a
characteristic-p artifact or assert all complex characters vanish.
It still would not be a reductive geometric vacuum or R19's normalizable
source spectrum. No all-representation nonexistence claim, no change
to the sourced chirality theorem, and no TOE conclusion is licensed.

Save first outputs and any failures; hash/commit this design and its
new producer/tests before execution. Do not modify or xfail the two
original failed tests just to obtain green. A later report explicitly
disposes of their too-strong assertions. Broad regression must name
the added failures; full banking remains unachieved.
