# Common hypercharge checked: paired matter survives, the joint index target does not

2026-09-27. Lifecycle: mechanism audit. Uses: the marked global SL5 seed,
E8 parent admission, coupled-boundary index identity, monomial and exact
matter-locus producers in this fork. Branch `audit/fork-2026-09-20`.
Local research result, no shared bank ID or independent-referee certificate.

## The decision, with its quantifier

For BOTH declared monomial SL5 structure families E(t), ALL nonzero
complex t, and EVERY globally lifted common flat hypercharge line L on
the marked cusped M6, the five charged coefficients cannot simultaneously
have ordinary interior index +3 (or all -3).

The reason is now computed, not assumed from the earlier untwisted result:

- If L has nontrivial meridian transport, the Q coefficient E L has
  index zero by the paired-boundary identity.
- If its meridian transport is trivial, the u-like coefficient E L^-4
  has index zero for every t and every such L, by the exact reduction
  and all-parameter calculation below.

Thus one necessary charged sector always fails this particular common
three-generation target. No independent sector fitting is allowed.
This does NOT prove that all five sectors have zero index, classify
all SL5 backgrounds, or settle physical chirality. The full exterior-square
line spectrum has not been computed and is not needed for this decision.

## The reduction actually verified

The preferred longitude has zero exponent sum on each marked generator,
so every one-dimensional character is trivial on it. Killing the ACTUAL
meridian gives relation matrix

    [-3  1  0  0  0  1]
    [ 1 -3  1  0  0  0]
    [ 0  1 -3  1  0  0]
    [ 0  0  1 -3  1  0]
    [ 0  0  0  1 -3  1]
    [ 1  0  0  0  1 -3].

Its Smith factors are (1,1,1,1,8,40). The 320 meridian-trivial line
characters are enumerated from its inverse and checked against the
determinant and all relators. This is a complete finite dual, not a loop
count interpreted as a vacuum census. Complex and unitary lines coincide
on this finite group. Other meridian transports were disposed of by the
Q-sector argument, not silently omitted.

The map L -> L^-4 has 20 distinct values. They split uniquely into four
quadratic characters times five powers of the restriction of the M2 chi5.
The quadratic generator-exponent vectors, modulo 2, are

    (0,0,0,0,0,0,0), (0,0,1,1,0,1,1),
    (0,1,0,1,1,0,1), (0,1,1,0,1,1,0).

Independent mod-2 and mod-5 kernel enumeration agrees. On every generator
the fifth-root factor is absorbed by t -> zeta5*t and an explicit diagonal
conjugation, with chi powers 2 and 4 in the two seeds. These are invertible
modulo 5, so they cover every fifth-root twist. The entrywise all-t proof
was additionally checked by actual rational matrices over Q(zeta5), for
all five rotations and both seeds, with a wrong-conjugation control.

The regular parent center kernel and charge dictionary were also checked:
(z,z^-2) on the two SU5 centers, and the simultaneous invisible change
(E,L) -> (E chi^-1,L chi), chi^5=1. Honest E,L lift to the parent. This
does NOT classify nonliftable quotient bundles or derive the 6Y coupling
normalization. Both qualifications matter to the scope of the result.

## Complete signed-family outcome, not only a vanishing difference

After the fifth-root reparametrization, write s for the reduced parameter.
For each seed the four signed families have:

| Reduced character | Parameter | Interior n(V)=n(V*) | Index |
|---|---|---:|---:|
| trivial | s=1 | 1 | 0 |
| trivial | s=-1,+i,-i | 2 | 0 |
| each of the three nontrivial quadratics | s=+i,-i | 1 | 0 |
| any of the four | all other nonzero s | 0 | 0 |

Do not read s as the same unrotated t for every original line. These
are mathematical interior cohomology dimensions, not physical fermion
counts. The nonzero equal spaces are retained and cannot be added across
different parameter values or lines to manufacture a single spectrum.

All eight families and their actual inverse-transpose duals have global
d0 rank-five and relative-cone rank-32 certificates outside explicit
polynomial roots. The actual cusp fixed dimension remains three. Hence
the pair exact sequence forces both interior dimensions to vanish there.

All 28 seed/character/irreducible-factor cases were then computed exactly
over Q or quadratic fields, covering every complex embedding. No factor
exceeded the declared cap and none was left unanalysed. Besides the fourth
roots, selected minors introduce s^2-4s+1. Full-matrix checks at
s=2+/-sqrt(3) show no extra matter and no H0 jump. These are spurious
minor zeros, not a new nonunitary spectrum or selected physical scale.

The determinants, their selected rows/columns, factor multiplicities,
ordinary tuples, direct relative cones and character vectors are in
[RESULTS.json](RESULTS.json). The generic-open-set plus root-coverage
argument is in [PROOF.md](PROOF.md).

## What this changes, and what it preserves

The earlier untwisted negative left common hypercharge lines untested.
That specific loophole is now paid for this lifted family. Repeating a
larger numerical parameter/Wilson-line scan in the same family is not
a useful next chirality search. Its mathematical paired classes remain
positive data, as do the distinct nonsplit M6 index results elsewhere.

The next constructive test is whether the rank-five monomial family admits
a source-free finite-norm global solution of the supplied parent action.
That would join an actual charged-parent coefficient to dynamics, without
changing the zero index proved here. Any later chiral mechanism must name
what changes: a different component, source/end law, nonflat background,
operator prescription or quantum phase. None is supplied by this negative.

The full mission still owes a common physical spectrum and interactions,
anomaly/quantum consistency, gravitational dynamics and empirical tests.
We have not completed a TOE or established that the framework must describe
nature. The current [roadmap](ROADMAP.md) keeps those obligations explicit.

## Verification and other-seat intake

Pre-execution seal: `abeb838c0273b90131a1428e11177e345752cff6`.
Native run: exit 0. Initial focused tests: 7 passed in 10.07 seconds.
First-result receipt commit: `36883314`.
Post-result locks/control seal: `83d147ccd793d1c0abd645a26cf9ba8f864ed6f0`.
Combined regression: **102 passed in 22.17 seconds**, terminal exit 0;
optional tkinter GUI warning only. All 16 scientific/dependency/lock
hashes stayed unchanged. No scientific correction was required.

Raw output and terminal exits are retained in RUN.log, TESTS.log,
REGRESSION.log and the two receipt JSONs. This is not the full repository
suite or a completed independent/shared-banking review.

Fresh fetch received physical-bridge head `f8c6ed1a`. Its R50 report and
R51 design/proof were personally read in full. R50 reports a finite-action
second-order neutral deformation with two older comparator failures
preserved. R51 is a sealed, not yet execution-reported, finite-energy
harmonic-completion/uniqueness test on a different rank-four canonical
background; its strong-domain/tangent join is expressly unpaid. Neither
new producer was independently rerun here. No result was transferred to
this SL5 hyperbolic family by analogy.
