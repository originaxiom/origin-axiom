# Exact transverse jump locus: fifth roots, real tangents, but no nearby index-three route

2026-09-27. Branch `audit/fork-2026-09-20`, local research only.
Initial seal 02ea6154290a34e362337a1e9a36c947ee35d9f8; instrument repair
seal 5e04ddfc905dc681d241de52fad43a1c30f555ba. Direct relative-cone
follow-through seal 3acc022c281dc8e58ad04606fba555bd268a65b9.
No shared-bank completion or independent external review is claimed.

## The exact result, not a parameter scan

For BOTH [five-point monomial families](../five_point_monomial_gate_2026_09_27/FINDINGS.md),
the off-diagonal meridian-relative first-order deformation space has dimension

    0 if t^5 != 1,
    2 if t^5 == 1,

with t=0 excluded because the representation uses Laurent monomials.
This is exact over ALL nonzero complex t for this specified tangent
question. It is NOT a classification of all SL5 components or the
ordinary matter cohomology at every parameter.

The fixed-meridian Fox matrix J is 40 by 40. The residual gauge map G
has eight columns. Their symbolic product is zero. Deterministic nonzero
minors, with only row powers of t cleared, are:

| Family | 32-minor of J | 8-minor of G |
|---|---|---|
| 0 | -320 t^31 (t^5-1)^2 | t^3 (t^5-1) |
| 1 | -320 t^32 (t^5-1)^6 | -t^3 (t^5-1)^3 |

Outside t^5=1, these certify ranks 32 and 8; JG=0 supplies the matching
upper rank constraint. At ALL fifth roots, direct number-field arithmetic
gives ranks 31 and 7, so the quotient dimension is 40-31-7=2.
The loss of a gauge direction matters: subtracting an assumed constant
eight would have undercounted the genuine tangent.

Both candidate factors (t-1 and Phi_5) were completely analysed, of degrees
one and four. The predeclared degree-twelve limit omitted nothing.
A chosen-minor root was treated as a candidate until these direct rank
checks; here every nonzero candidate really is a jump.

## What is present at those points

The table gives actual M6 coefficients, the same in both families.
Interior dimensions are algebraic cohomology, NOT physical fermion counts.

| Parameter | n(E), n(E*) | n(exterior-square E), n(dual) | Index pair |
|---|---|---|---|
| t=1 | (1,1) | (1,1) | (0,0) |
| primitive fifth root | (0,0) | (0,0) | (0,0) |

E has matrix-algebra dimension 17 at both types of point, versus 25 at
the earlier t=2 points. Its invariant bilinear-form dimension is 2 at
t=1 but 0 at primitive fifth roots. Do NOT call every finite-image point
self-dual: the latter is not. At roots of unity these monomial matrices
are unitary with finite image; inversion of the cyclotomic parameter
identifies the dual with a Galois conjugate and forces equality of the
cohomological dimensions. Their zero indices are correspondingly controls,
not a non-vacuous discovery that all non-self-dual backgrounds fail.

For the rank-twenty transverse module, H1 dimension is 10. Full-torus
and meridian restriction ranks are 8, hence relative dimensions 2.
Longitude restriction has rank 7 and kernel dimension 3. No nonlinear
integrability of these directions is asserted.

## The important follow-through: the nearby full-parent bound

A positive tangent does not itself justify chasing a new nonlinear branch.
The [direct relative-cone check and authored proof](LOCAL_CAPACITY_PROOF.md)
find h1(M6,boundary;E)=h1(M6,boundary;E*)=3 at every fifth root.

Consider ANY sufficiently nearby full SL5 background, not just a monomial
one, with the M2 meridian in the same pure order-three conjugacy class.
Longitude is allowed to vary. Assume H0(M6;E)=H0(M6;E*)=0, as needed for
the intended irreducible upstairs candidate. The M6 meridian is then I,
so the common cusp invariant dimensions agree: b=b*. They are at most
three nearby. Upper semicontinuity of the directly checked cone matrices
gives n(E),n(E*)<=3-b, while the exact boundary identity gives |I(E)|<=b.
Together,

    |I(E)| <= min(b,3-b) <= 1.

In particular, retaining capacity three forces both interior dimensions
to vanish nearby. Allowing longitude to change cannot produce index three
in that neighborhood. This leaves the genuine tangent intact; it changes
its priority for the current goal.

Scope is essential: no numerical neighborhood radius was computed; no
distant continuation was classified; the zero-global-invariant hypothesis
does not include the earlier unbalanced nonsplit positives. Meridian-class
changes, sources, other operator domains and physical mechanisms are not
excluded. No claim says chirality is impossible in the framework.

## Verification and preserved failures

The initial producer failed on JSON serialization of a SymPy integer.
Its initial focused suite had five passing tests and one failed
polynomial-domain comparator (same polynomial, QQ versus ZZ).
Both terminal failures are preserved in FIRST_FAILURES.json.
CORRECTION.md and REPAIR_SEAL.json record the narrowly scoped repair
before rerunning; no scientific target was adjusted to pass.

Repaired native producer: exit 0. Repaired focused suite: 6 passed.
Direct cone producer: exit 0. Combined current suite: **85 passed**,
exit 0; optional tkinter GUI warning only. All sealed science sources
and dependencies were unchanged during their runs. Raw stdout, exact
polynomial coefficients, minor row/column selections, number-field
diagnostics and terminal receipts are retained.

This is exact computational evidence plus an authored local proof,
not an independent referee certificate or the full repository suite.

## Consequence for the roadmap

The arbitrary-scan question is now replaced by an exact answer for the
transverse tangent: only fifth roots are exceptional. Their first-order
positives do not provide a nearby zero-global-invariant fixed-meridian
index-three route. Do not spend a nonlinear continuation merely because
the tangent dimension is two.

What remains worth distinguishing before any broader search:
1. The ordinary E interior cohomology over the ENTIRE monomial parameter
   line is not classified by this tangent certificate. An exact relative
   cochain rank certificate, not another numerical grid, can answer that
   bounded question if it changes the candidate decision.
2. A separately motivated changed peripheral class, distant relative
   component, or physical source/domain must be stated and priced; it
   is not already killed by this local result.
3. The monomial family may still offer a finite-norm common-background
   control, but no harmonic-metric or physical-mode theorem is proved
   here. Such a control cannot be renamed a chiral physical model.

The physical mission remains a SINGLE coherent action/background/domain/
spectrum and observable, followed by quantum and gravitational consistency.
None of those obligations is discharged by a rank or a root of unity.
