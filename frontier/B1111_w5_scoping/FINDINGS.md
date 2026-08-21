# B1111 — THE W5 SCOPING (F7): isolated collisions are NOT rigidly forbidden — 1,656 transversal pairs, and order-24 pairs among them

**Status: banked (frontier). Verdict PROVED (the scoping's three computed layers,
each complete over the stored 96). The wave's third arc. Gate 5 untouched. Lock
`tests/test_b1109_b1110_b1111_wave.py`.**

## The question (IV.2 / W5, typed at B1084's bank)

B1084 proved every ADE-enhancement collision on THE flat cone is non-isolated
(fixed sets of dimensions 3 and 1 only; zero 0-dimensional, over all 95
nontrivial elements). W5 asked: can any G₂-compatible MODIFICATION of the
order-96 action produce an isolated (0-dim) collision — the configuration the
Acharya–Witten chirality mechanism needs?

## The three computed layers

1. **Per-element rigidity (deformations lose).** Fixed-space dimensions are
   eigenvalue data — invariant under conjugation of the embedding. And at the
   affine-crystallographic level, a translation part with a component in the
   fixed space EMPTIES the locus (a screw motion); when nonempty, the affine
   fixed set is a translate of the linear one — SAME dimension. **No
   deformation in the affine class makes any single element's locus 0-dim.**
   (B1084's census reproduced en route: 53 three-dim, 42 one-dim.)
2. **Joint loci are NOT rigid — the door is open at pairs.** Over all pairs of
   nontrivial elements: joint fixed-space dimensions {0: 1656, 1: 2556,
   3: 253}. **1,656 transversal pairs** (joint dimension zero) exist. *(The counts were
re-derived EXACTLY over Q(sqrt2) at the owner's cross-verification demand:
{0: 1656, 1: 2556, 3: 253} confirmed, and the per-element census re-matched
B1084's banked {1: 42, 3: 53} — after a first verification attempt whose
rational-approximation of the 1/sqrt2 entries collapsed eigenspaces and
DISAGREED with the bank, was thereby caught, and was replaced: the banked
census acted as the positive control that exposed the broken verifier.)* For such
   a pair, the affine translates of the two loci meet in exactly ONE POINT
   whenever a single codimension coincidence holds — an isolated joint
   collision is GEOMETRICALLY AVAILABLE.
3. **And the pairs have interesting stabilizers.** Sampling 25 transversal
   pairs: the generated subgroups have orders {8: three, 16: eight, 24: three,
   96: eleven} — **order-24 transversal pairs exist**, i.e. candidate
   isolated-2T-point configurations: exactly the E₆-at-a-point shape the
   mechanism wants.

## The verdict and the named residue

**W5's answer: the ≥1-dim census is per-element rigid, but isolated JOINT
collisions are constructively available — the hatch is not shut.** The residue,
typed in two steps, neither claimed: (i) the COCYCLE feasibility — an affine
twist realizing the coincidence must satisfy the crystallographic consistency
conditions over the WHOLE group, not just the pair; (ii) the STABILIZER TYPING —
whether an order-24 transversal pair's point-stabilizer acts with the ADE
structure (and the chirality-capable content) the mechanism requires. Both are
finite computations on the stored 96; neither is run here.

## Road disposition

IV.2 sharpens from "can any modification produce 0-dim?" to: **available at
1,656 transversal pairs (order-24 among them); residue = cocycle feasibility +
stabilizer typing, both finite, both named.** Still NAMED-OPEN — now with a
constructive route instead of a question mark.
