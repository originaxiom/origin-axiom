# Actual common-parent seed: three in one matter bundle, zero in its partner

2026-09-27. Seal `0b58f3c92eec4655e8bbd3e3f19f377b3601ab0b`.
Both native phases completed with exit zero. Sixteen new tests and the
combined **57-test** global/parent/boundary/deck suite passed. Sealed
sources retained their hashes. No first scientific failure or correction.
The sole warning concerns an unused tkinter GUI, not exact arithmetic.

## Result on the actual rank-five and rank-ten coefficients

The global native seed is E_q=(rho_2 + Reg(C3)) tensor chi^q, with chi
the specified order-five character on M2. It lies in SL5 and restricts to
M6. For ALL five central twists, exact arithmetic gives the paired
interior indices on M6:

| q | I(E_q) | I(exterior-square E_q) |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 0 | 3 |
| 2 | 1 | 0 |
| 3 | -1 | 0 |
| 4 | 0 | -3 |

**The +3 is real as an algebraic cohomology result in the ACTUAL
exterior-square coefficient of the specified parent**, not the wrong
rank-six mixed block relabeled as matter. For q=1 it splits (1,1,1)
over the three deck characters. Its full M6 data are

    V:    (a0,a1,t0,t1,r1) = (0,7,7,14,4),  n=3;
    dual: (a0,a1,t0,t1,r1) = (0,10,7,14,10), n*=0.

But its E partner has n=n*=0: (0,3,4,8,3) versus (1,5,4,8,5).
In the fixed parent dictionary E supplies the 10-like sectors while
exterior-square E supplies the 5-bar-like sectors. Consequently this is
NOT three complete Standard Model generations, not a physical spectrum,
and not the sought irreducible rank-five background. At q=2 the E index
is +1 with deck distribution (1,0,0), while its exterior square has zero.

This closes the joint target (3,3), with common sign convention, only on
the FIVE specified central twists of this ONE reducible native seed.
It does not close all SL5 representations, all twists/end conditions,
or the original rank-six positive. The mathematical positive is retained.

## Why the calculation is stronger than a receipt check

The source's small verify.py checks saved JSON/CSV. Here the cocycle was
rebuilt from Fox equations independently, over Q(zeta5), and checked not
to be a coboundary. All global relators and cochain identities were checked.
The field exterior square was explicitly constructed by minors. Direct
seven-generator M6 cohomology agrees in all FIVE dimensions and their
duals with both:

1. the exact split decompositions E_q=rho_q+3 chi^q and
   exterior-square E_q=3 rho_(2q)+4 chi^(2q) on M6;
2. relative transfer from M2, computed as the trivial deck sector plus
   the independently represented pair of nontrivial cubic characters.

Ranks use rational FLINT 0.9.0, divided by field degree only after exact
divisibility checks. No modular or numerical rank is promoted to a proof.
The central-twist parameter is shared by the parent; the exterior square
gets 2q automatically. It is not an independently adjustable sector knob.

## A concrete warning against dropping global invariant terms

At q=1 the E index is ZERO despite t0-r1=4-3=1. The missing term is
a0-a0*=0-1=-1. At q=2 the exterior-square index is ZERO despite
t0-r1=7-10=-3, canceled by a0-a0*=3. These are actual manifold/module
examples of the correction retained in the preceding boundary audit,
not abstract dimension counterexamples.

## Input marking independently recovered from the knot diagram

Spherogram's figure-eight diagram supplied four Wirtinger relations.
Two explicit Tietze eliminations and a meridian relabeling gave the
native Riley presentation. The diagram's preferred longitude became
EXACTLY b a^-1 b^-1 a a b^-1 a^-1 b as a freely reduced word, with no
approximate holonomy comparison. A separate normal-closure certificate
proves it commutes with the meridian.

Independent Schreier edge rewriting recovers the literal M2 relations,
M2-to-C3 weights (1,0,1), the seven M6 generator inclusions, meridian
cubing, and the same longitude. Exact Smith forms give H1(M2)=Z+Z/5 and
H1(M6)=Z+Z/8+Z/40. This verifies the marked group input; it does not
re-prove hyperbolic geometry or a physical selection of the figure-eight.

## The local negative has an important qualification

The original native mixed-H1 computation is reproduced exactly, in both
directions: (0,1,1,2,1), hence the kernel of restriction to the TORUS is
zero. However restriction to EITHER peripheral CIRCLE has rank zero,
and its kernel has dimension one. Separate circle coboundaries need not
come from the same vector, so the two statements are consistent.

Thus "no torus-relative mixed direction" does not by itself prove "no
meridian-preserving mixed direction." A search fixing only the meridian
while solving the longitude cannot use that stronger negative.
This does NOT yet exhibit a full irreducible SL5 deformation: the live
direction might connect only rho_2 with the trivial family line, leaving
the other two family lines isolated. The separately sealed
[meridian-only follow-through](MERIDIAN_FINDINGS.md) now checks that question:
an invertible full off-block Jacobian forces local 3+1+1 splitting even
with longitude free. The smaller-block direction is retained, but it
does not open a nearby irreducible SL5 representation at fixed meridian.

## Remaining physics and verification limits

This is ordinary interior cohomology for reducible, nonsplit backgrounds.
Neither a normalizable fermion spectrum nor a global solution of one
physical parent action has been supplied. The source-free finite-energy
admissibility obstruction retains its original hypotheses; one cannot
discard it or impose its energy class without deriving the physical norm.

Only ONE of the source's nine native loci was reproduced in characteristic
zero here. No full relative SL5 component search or nonlinear neighborhood
classification has yet been executed in this arc. Tests and an authored
proof are not an independent referee review or full repository certification.
