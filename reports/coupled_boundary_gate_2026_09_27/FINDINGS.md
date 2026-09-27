# Coupled boundary gate: the cover class stays open; the principal class does not

2026-09-27. Seal `02c7889c06a10e9ce0b008f44d1318698a4d17f4`.
Native exact calculation passed; **17 focused tests and 15 unchanged parent
tests passed**, each with actual exit zero. All five sealed input/source
hashes remained unchanged. No failed scientific run or correction occurred.
This is not an independent referee review or whole-repository certification.

## What changed

The proposed rank-five parent search now has a necessary boundary screen
for its ACTUAL charged coefficients, E and exterior-square E. The earlier
rank-six mixed count cannot be substituted for either coefficient.

| Meridian class | E fixed-space bound | Exterior-square E bound | Mixed Hom(3,2) bound | E index bound if global H0 is balanced |
|---|---:|---:|---:|---:|
| Principal unipotent J5 | 1 | 2 | Not this decomposition | absolute value at most 1 |
| Proposed M2 2+3 class | 2 | 3 | 1 | absolute value at most 2 |
| Its cubed M6 meridian | 4 | 7 | 3 | absolute value at most 4 |

The meridian data of the last two rows are exactly the boundary MODEL in
the handoff. They are not certified global M2/M6 holonomies. A declared
commuting toy longitude attains these bounds; another exact commuting
longitude reduces them. Consequently the table is not the actual t0 of
an as-yet-unconstructed global candidate.

**Principal class:** even without balanced global H0, the weaker universal
bound is absolute value at most TWO. Thus the ordinary interior index
three is impossible for E with this meridian, including nonsplit E and
arbitrary scalar meridian twists. This conclusion applies to the whole
specified peripheral class, not just the known geometric representation.
It does not exclude other cusp classes, source domains or physical indices.

**Proposed cover class:** three is not excluded. Bounds four and seven are
capacity constraints, not counts of generations. There is no global E here,
no jointly computed index pair, and no physical zero-mode result.

**Proposed quotient class:** balanced H0 excludes three in E downstairs.
Without balance it is NOT excluded: the unconditional bound is four.
An index +3 would require a0(E)>a0(E*); an index -3 the opposite inequality.
For an irreducible rank-five coefficient, both invariant counts are zero,
so the balanced bound applies. Restriction to a cover and keeping only
deck-invariant modes must not be confused.

## The correction that prevents a false exclusion

Writing delta=a0(V)-a0(V*), the full identity and bounds are

    I(V) = delta + t0(V*) - r1(V),
    delta-t0(V) <= I(V) <= delta+t0(V*).

One cannot silently set delta to zero on all nonsplit modules, nor assume
common cusp invariant dimensions are equal for every commuting pair. The
countercontrol U=1+E12, W=1+E13 has dimensions one and two in V and V*.
The proof also gives the weaker unconditional bound |I|<=t0+t0*.
This is a direct application/refinement of main B1297, not a new index.

## One line, not independent sector knobs

For the cover's unipotent meridian, a nontrivial scalar twist eliminates
all fixed vectors and forces the interior index to vanish. Since Q uses
E tensor L, target three requires L(mu_up)=1. If the actual longitude is
also unipotent, the same is necessary for L(lambda_up). The longitude
hypothesis must be checked; it is not supplied by a meridian matrix.

This does not eliminate downstairs cubic phases: L(mu_down)=omega pulls
back to L(mu_up)=omega^3=1. The exact cubic-phase meridian bounds are
(2,1,1) for downstairs E and (3,2,2) for its exterior square. Upstairs they
are (4,0,0) and (7,0,0), respectively. These phases belong to one common
hypercharge line with exponents 1,-4,6,2,-3, not five independent choices.
The established 6Y convention is not a derivation of physical normalization.

## Prior result reproduced, not rediscovered

All seven nilpotent partitions reproduce the handoff's local kernel fact:
none gives dimensions (3,3) on E and exterior-square E. **That is not a
three-generation no-go.** It confuses a local fixed-space dimension with
the global interior index if used that way. The independent Jordan/sl2
formula and exact wedge-minor ranks agree in all seven cases.

## Immediate next question and physics debt

Before a large relative-representation search, split the cover index into
the three deck-character contributions. The same E must meet those and
the exterior-square constraints. Obtain the actual longitude and compute
global invariants rather than importing the toy boundary pair.

Then, and only for a certified global candidate, solve the background and
normalizability/domain problem in one parent action. The current result
does not identify interior cohomology with L2 fermions, lift mirrors, derive
interactions or gravity, or establish that the programme describes nature.

## Cross-seat freshness

Ordinary SSH fetch failed (`73cdda`); plain HTTPS was rewritten to the same
SSH route and failed (`0a6401`). Read-only HTTPS with global/system config
disabled for that command succeeded (`5ff366`), advertising exactly the
seven already pinned heads. Fetch to the existing remote-tracking refs
then succeeded (`891c87`). No persistent Git/SSH config was changed, no
branch merged, and nothing was pushed. The unrelated F20 draft is untouched.
