# Whole-parameter E5 result: zero index, with paired fourth-root states retained

2026-09-27. Local branch `audit/fork-2026-09-20`.
Science sealed at 86b0d3729479900943c66c6169c8934bdedb3354;
post-result locks separately sealed at 1f9b4ec2ec8b6ded4f6423ca373e38c47f91622a.
No physical chirality, independent referee acceptance or shared-bank claim.

## Complete result on the declared coefficient

For BOTH exact monomial families, on the actual cusped M6 cover, the
defining coefficient E and its actual dual satisfy, for ALL t in C*:

| Parameter | n(E) | n(E*) | I(E)=n(E)-n(E*) |
|---|---:|---:|---:|
| t=1 | 1 | 1 | 0 |
| t=-1,+i,-i | 2 | 2 | 0 |
| every other nonzero complex t | 0 | 0 | 0 |

These are interior cohomology dimensions, not yet physical fermion counts.
The equal nonzero spaces are retained. Their zero difference must not
be misreported as empty matter, and counts from different values of t
must not be added together to manufacture three on one background.

This completes the all-parameter UNTWISTED E question, not every allowed
hypercharge Wilson-line twist of the charged coefficients. That distinction
is essential to the broader common-parent decision below.

## Exact coverage, not an extrapolated grid

The actual M6 paired cusp is fixed as (I,T) or (I,T inverse), where T is
a three-cycle fixing two coordinates. The common fixed dimension is
therefore three for every parameter.

For each family and each of E,E*, the producer constructs global d0 and
the relative cochain cone symbolically. All relators and chain/restriction
identities are checked. The cone has degree-one matrix size 40 by 40
and preceding differential rank five.

Selected minors have the following exact cleared determinants; only
powers of t were used to clear denominators:

| Family / coefficient | five-minor of d0 | thirty-two-minor of relative cone |
|---|---|---|
| 0 / E | t(t-1) | 9 t^21 (t+1)^6 (t^2+1)^2 |
| 0 / dual | -t^2(t-1) | 9 t^16 (t+1)^6 (t^2+1)^2 |
| 1 / E | t(t-1)^3(t+1) | 9 t^29 (t-1)^2(t+1)^6(t^2+1)^2 |
| 1 / dual | -t(t-1)^3(t+1) | 9 t^26 (t-1)^2(t+1)^6(t^2+1)^2 |

Outside {1,-1,+i,-i}, the first minor forces a0=0 and the second
forces h1_relative<=35-32=3. The exact sequence
h1_relative=n+t0-a0 with t0=3 and n>=0 then forces n=0.
This proves the entire open-set statement, not just sampled parameters.

Every remaining root is recomputed exactly over Q or Q(i).
No candidate factor exceeded the predeclared degree limit and none
remains unanalysed. At t=1, global H0 is one and h1_relative is three.
At the other three roots, global H0 is zero and h1_relative is five.
The resulting interior dimensions are exactly those in the table.
Both ordinary and direct cone calculations agree.

The selected family-1 d0 minor also vanishes at -1, but global H0
does NOT jump there. That zero is a minor-choice artifact, removed
by checking the full matrix. The synthetic spurious-minor-root control
guards against interpreting every determinant zero as physical content.

## A useful distinction revealed by the two tests

The earlier [transverse deformation locus](../monomial_exceptional_locus_2026_09_27/FINDINGS.md)
is t^5=1. The matter-support locus here is t^4=1. They intersect only
at t=1 and answer different questions.

- Fourth roots support paired E interior classes even though the
  meridian-relative OFF-MONOMIAL tangent is zero there (except at 1).
- Nontrivial fifth roots admit extra transverse tangents but have no
  E interior cohomology.
- Neither a positive tangent nor a nonzero kernel alone is a chiral index.

This is a concrete reason not to use one diagnostic as a proxy for the
other. It is not a new observed physical coincidence or a selected vacuum.

## Scope for the Standard-Model goal

The [verified E8 parent dictionary](../m6_parent_admission_2026_09_27/FINDINGS.md)
uses E and its actual exterior square. These unmodified families cannot
meet the joint ordinary target (3,3), since their E index is identically
zero. A complete exterior-square census is unnecessary to decide THAT
unmodified target; no all-parameter exterior-square result is claimed.

However the dictionary also permits a COMMON hypercharge line L, if its
global form and physical status are admitted. Then Q,u,e use E tensor
L, L^-4, L^6 respectively, while d and lepton doublets use exterior-square
E tensor L^2 and L^-3. This calculation did NOT apply those additional
coefficient lines. Consequently it does not close all gauge-Wilson
backgrounds built from the same structural family. Check that coupled
option before declaring a broader family-to-SM obstruction.

No conclusion excludes distant off-monomial components, altered peripheral
classes, nonflat/source mechanisms, other physical operators or the
framework's earlier nonsplit positive indices.

## Verification

Initial native execution and five initial focused tests exit zero.
Two discovered-result regression locks separately preserve the entire
candidate set and the equal nonzero interior dimensions. The combined
current suite has **92 passing tests**, exit zero; optional tkinter GUI
warning only. All sealed science sources/dependencies and the new locks
were unchanged during runs. Raw stdout, structured exact results, row/column
minor choices and terminal receipts are retained.

This is a complete computational certificate plus the explicit linear
algebra argument for the declared family, not the full repository suite
or independent specialist certification.

## Next physics-facing decisions

1. Check admissible common hypercharge Wilson lines and the actual coupled
   charge dictionary, starting with a coefficient that can decide the
   full-generation target without independent sector fitting.
2. Separately assess whether the monomial exponent class yields a global
   finite-norm harmonic background in the supplied parent action. That
   would be a constructive control, not a restoration of an absent index.
3. Do not silently insert source fields, select a vacuum, change the
   physical operator, or equate a supplied effective action with derived
   gravity to turn this mathematical result into a physical success.

The [next-step note](NEXT_COUPLED_AND_PHYSICAL_GATE.md) states these tasks
without claiming they are executed.
