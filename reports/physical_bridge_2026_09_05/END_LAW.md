# Boundary variation and the limits of the cone completion

September 30, 2026. Path-local R60. The adopted superpotential now has
an explicit checked boundary variation, and B1504's finite-symmetry
result survives independently. Neither supplies a physical boundary
law. The audit identifies the next load-bearing test: the actual
fermion reality and supersymmetry conditions on that boundary.

All **30 exact controls** and **15 focused tests** pass. The unchanged
B1504 lattice lemma also reproduces its 26 subgroup entries and seven
entries containing rotations. These are entries across two ambient
dihedral groups, not 26 distinct conjugacy classes. No 209-member
geometric census or full repository suite was rerun.

## What survives and what needs a narrower reading

| Claim | Audit result |
|---|---|
| Rotations of order 3, 4 or 6 prevent an invariant real torus-link line | Retained. Independent exhaustive subgroup-subset enumeration agrees with the proof and the unchanged foreign lemma. |
| No invariant neutral-sector completion at a rotated cusp | Retained IF the neutral sector must use a Poincare-self-dual line and each completion is individually invariant. Not a classification of all self-adjoint physical domains. |
| The order bit disappears from the oriented unmarked manifold | Retained: L inverse times LR times L equals RL with determinant one. A physical rule required to descend to that quotient cannot distinguish the bit. |
| Therefore no boundary law can depend on retained marking | Not established by forgetting it. Marked equivariance and unmarked invariance are different requirements. No A7-dependent physical or chiral law is constructed here. |
| A completion at a rotated hexagonal point must pick one of three root lines | Too broad for arbitrary ideal lines. The primitive line (1,3) has a distinct three-element orbit. The three-root restriction remains valid for B1502's specified Bryant-Salamon smooth phases. |

The last distinction is visible in B1504's own producer: `shortest_lines`
selects the first three short slopes before checking their orbit. That
checks a root orbit, not the exhaustion of all Lagrangian lines. The
mathematical space of real lines is infinite; rational lines are the
Dehn-slope subset. A finite set of smoothings is not that whole space.

## Self adjointness is not the extra self duality condition

The cited Hodge-theory paper treats self-adjoint de Rham domains for
arbitrary mezzoperversities, and adds Poincare self-duality separately.
See its Theorems 1--2, equation 1.3, Lemma 5.1 and section 6.1:
[Albin et al.](https://arxiv.org/html/1307.5473v3).

Our exact Green-form check makes this distinction concrete. On doubled
Cauchy data, W direct-sum W-perpendicular is maximal isotropic for
W=0, W=V, and a line W. The first two choices are rotation-invariant;
neither is Poincare-self-dual. Thus an absence of an invariant LINE
is not an absence of invariant self-adjoint de Rham domains. These
examples do not satisfy B1504's added self-dual hypothesis and do not
refute its conditional theorem.

Nor do they yet provide admissible gauge or matter boundary conditions
for the full physical theory. In particular, the seven-dimensional
fermion reality operation may include Hodge duality, unlike bare complex
conjugation of the coefficient bundle. If it does require the same
sector's domain to be Poincare-self-dual, the neutral-sector obstruction
can apply. Derive that map rather than either assuming it or discarding it.

## A cone completion changes the norm problem

Adding a topological cusp point does not change the complete hyperbolic
metric into an incomplete cone metric. Our local calculation compares

    g_cusp = d rho^2/rho^2 + rho^2 h,
    g_cone = d rho^2 + rho^2 h.

A constant tangential one-form has radial norm integral d rho/rho on
the first and d rho on the second. It is not L2 at the cusp, but it is
L2 at the cone tip. The end distances differ too. This is a norm control,
not a global zero mode. The fork's F02 unique complete-space closure and
B1500's cone-domain choices are different analytic problems, not rival
answers on a single fixed physical metric. The physical choice between
them still needs justification.

## What the supplied action actually determines

Use the complex Chern-Simons superpotential adopted from
[Pantev and Wijnholt, equation 2.25](https://arxiv.org/html/0905.1968v1).
For an oriented compact regulator and fixed coefficient c, direct
variation gives

    delta W = 2c integral_M tr(delta C wedge F_C)
              - c integral_boundary tr(C wedge delta C).

The nonabelian polynomial control verifies the full cubic and the
boundary sign. Both a wrong sign and deletion of the cubic fail.
Flatness removes the bulk term; it does not automatically remove the
boundary term for the allowed variations.

In the local abelian boundary chart C=u dx+v dy, this term is
theta=c(v du-u dv). A specified boundary counterterm c*u*v changes
theta to 2c*v du. Adding a supplied U(u) then imposes
2c*v+U'(u)=0 when u is free. At c=1, U=k*u^2 gives v=-k*u.
Different k give different conditions with the SAME marking. All
preserve the boundary two-form d theta=-2c du wedge dv because the
counterterms are exact variations.

This is the positive action-level result: the variational boundary
structure is explicit, so a proposed selector can now be tested against
it. It is not a derived U, quantum level or physical polarization.
These local counterterms have not been shown globally gauge-invariant,
supersymmetric or anomaly-free. Neither their existence nor the symmetry
classification fixes the full end law.

## Next physical test

Use the SAME supplied parent and its R59 coefficient and cubic maps.
Derive the twisted fermion reality operation and preserved supercharges
on the cone Cauchy data. Then ask which bosonic and fermionic domains
close together under gauge transformations, supersymmetry and the
interaction maps. Only after that test may an admitted end domain be
used for a physical chiral index. A boundary potential or extra end
field is an explicit changed physical input, not a free rescue.

Follow-on reading after the sealed runs found a direct starting point:
Pantev--Wijnholt section 3.1, equations 3.1--3.4, already relates the
doubled differential-form description through Hodge star and discusses
the Majorana condition. This supports testing the extra duality
requirement, not treating the self-adjoint examples as a physical
loophole. Transport to the singular boundary domain and the full
interaction/supercharge compatibility still need their explicit maps.

Retain R57's distinction between a symmetric law and its individual
solutions. B1504's census of invariant completions neither constructs
a symmetry-breaking dynamical completion nor excludes all such laws.
The existence of a mathematical alternative is not evidence that it
describes nature. The full physical mission remains uncompleted.

## Evidence and limits

Seal **48c04785b641d57b103ae21e2bc9d6c9426dfa1d** was pushed and
server-confirmed before the first scientific execution. The four sealed
files stayed fixed during all three successful runs. Nine source pins
record the received inputs; no other branch was edited.

See [design and arguments](END_LAW_DESIGN.md), [input pins](END_LAW_INPUTS.json),
[producer](end_law.py), [tests](../../tests/test_physical_bridge_end_law.py),
[run receipts](END_LAW_RECEIPTS.json) and [custody checker](end_law_receipt_check.rb).
The independent code checks the stated finite identities; the global
analytic theorems are cited, not machine-certified. The B1500/B1502/B1396
findings are read and scoped, not independently banked in this lane.
No full-suite green or independent physical-domain review is claimed.

Custody checks pass for four sealed files, nine source pins and all three
science captures. The cumulative checker validates 975 current artifact
digests, 333 distinct seal paths and the same 24 historical failed/error
test IDs; it is not a fresh run of that old suite. The governance check
has 26 passes and the same four failures as R59: attribution on four old
files, two old vacuous tests, five old seal-provenance debts, and 41 stale
relay debts. No new failure is hidden or counted as a pass. The audit
outputs are retained separately from the successful science runs.

A pre-seal metadata patch initially used a path relative to the parent
workspace and was rejected without edits. It was reapplied with resolved
paths before sealing. No scientific run or result was overwritten.
