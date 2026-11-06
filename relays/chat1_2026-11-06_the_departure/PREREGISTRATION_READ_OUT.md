# THE READ-OUT THE HISTORY'S SYMMETRY FORCES — pre-registration (the web seat, 2026-11-06)

**For:** the owner's answer to this seat, "Keep me on the choices": keep reducing the named choices, starting with
the read-out point after P-723. The read-out is choice 6 in 21cfbc3c2's list ("the apex read-out: a symmetry
criterion").

**Where the record stands:**
- B1845: P-455's period average along the k = 5 thread washes the hierarchy out; "the apex read-out is
  load-bearing and its derivation needs a kinetic structure along the circle (FL-05)".
- P-723: the layered triangulation's deepest shapes are "a second object-native candidate for τ, with the same kind
  of read-out choice (which layer)".
- 904f19136 § 4: "The apex is the one point of the palindromic excursion fixed by its reflection. That is a symmetry
  criterion, not a derivation."
- B716 (NEGATIVE): the object has no canonical arrow of time.
- B1749's withdrawal concerned the thread rule as a selector of τ across many threads. That is not the question
  here.

**Kind:** data-free. PGL(2, ℤ) geometry, plus SnapPy 3.3.2's shapes.
- No coupling, no ratio of the six, no θ̄ and no held-out quantity is computed, and nothing is compared with data.
- The six are not used as a criterion (P-708).
- **Written before** `read_out_check.py` is run. A reduced smoke copy ran outside the tree; its values were not read.

## The claim

Three premises:
- **(N1)** The read-out is one point.
- **(N2)** It is a point of the conformal history: the fibre's modulus along its Teichmüller geodesic.
- **(N3)** It is fixed by every symmetry of the history in PGL(2, ℤ), including the direction-reversing ones, since
  the object has no arrow (B716).

**Then the apex is forced for every run n ≥ 2, with no kinetic structure.** The argument:
- **The history.** The one-departure history is the geodesic from a = −1/φ to b = n + 1/φ.
- **No element fixes both ends.** An element g ∈ GL(2, ℤ) fixing both ends would have a and b as the roots of one
  integer quadratic, so they would be Galois conjugates. They are not, for n ≠ 1.
- **Only ρ_n swaps them.** Write g = [[p, q], [r, s]].
  - g(a) = b and g(b) = a give s = −p and p·n + q − r·ab = 0, with ab = (n − 3)/2 + ((1 − n)/2)√5.
  - The √5 part forces r = 0 for n ≠ 1. Then q = −pn and det = −p², so g = ±[[1, −n], [0, −1]]. This is the
    reflection ρ_n: τ ↦ n − τ̄.
- **So the stabiliser is {1, ρ_n}.** ρ_n's mirror Re τ = n/2 meets the history once, at its top: the apex
  n/2 + i(n − 1 + √5)/2.
- **The 3-manifold.** ρ_n reverses the history's direction and the fibre's orientation. On the 3-manifold it is
  therefore an orientation-preserving involution, not a chirality.

**What would refute:**
- any other stabiliser element at some n in 2…12;
- a closed axis below with a number of classes other than two;
- a failure of the predictions P5 to P8.

## Predictions

**P1 (part A).** For n = 2…12, each condition has a solution space of dimension 1:
- swap: spanned by ±(1, −n, 0, −1), det −1, which fixes the apex, and the apex lies on the history;
- fix: spanned by the identity.

For n = 1 (the golden loop's own ends, which are conjugate), both spaces have dimension 2: the stabiliser is
infinite.

**P2 (part B, the golden loop LR).**
- LR has a glide root G = [[0, 1], [1, 1]], with G² = LR. So the minimal translation is l(LR)/2 = 2 log φ.
- The symmetric points fall into exactly two classes, log φ apart:
  - one reduced to ½ + (√5/2)i, the golden apex (|Re| ½, Im 1.118034);
  - one reduced to i (|Re| 0, Im 1).
- So without a departure the premises give two candidates, not one.

**P3 (part B, the closed threads L^n R (LR)^k, n = 5, 6, k = 0…6).**
- There is no root, so the minimal translation is l.
- There are exactly two classes, l/2 apart:
  - **the departure's**, with reduced |Re| ½ for n = 5 and 0 for n = 6, and Im equal to the apex table of
    904f19136 / P-717's control to 5 decimals:
    - n = 6, k = 0…4: 3.87298, 3.65148, 3.62284, 3.61873, 3.61814;
    - n = 5, k = 0…3: 3.35410, 3.14907, 3.12250, 3.11868.
  - **an anti-apex** in the golden stretch, with reduced Im below 1.3.
- So every closed thread offers two candidates. In the one-departure limit the anti-apex lies l/2 → ∞ from the
  departure, and only the apex remains.

**P4 (part C).**
- For even n the apex lies on the Farey edge (n/2, ∞), so the 3D symmetric object is a flip (a tetrahedron).
- For odd n it lies inside the triangle ((n − 1)/2, (n + 1)/2, ∞), so the 3D symmetric object is a triangulated
  surface.
- Reading (ii)'s run of 6 is even.

**P5 (part D).**
- l(L^n R (LR)^k) − k·l(LR) converges in k: l(LR) = 4 log φ = 1.924847.
- The one-departure arc above Im 2 has fixed length A_n = 2 acosh(r_n/2), with r_n = (n − 1 + √5)/2:
  A₅ ≈ 2.027 and A₆ ≈ 2.398.
- The sampled fraction of the period above Im 2 in the fundamental domain equals A_n/l to within 0.005 at
  (n, k) = (5, 5), (6, 5), (5, 20), (6, 20): about 0.149, 0.173, 0.048 and 0.056.
- So nothing outside the departure's top arc rises above Im 2, and the departure's share falls like 1/k.
- **The consequence (a standard shadowing argument, not a computation):** a period-averaged read-out of any bounded
  function converges to the golden loop's average, whatever n is. It is blind to the departure in the
  one-departure limit, which is (N1)'s ground.

**P6 (part E, SnapPy, b++ L^n R (LR)^k, n = 5, 6, k = 8, 12).**
- There is one tetrahedron per letter, and all tetrahedra are positively oriented.
- Exactly one reflection i ↦ t − i (mod m) of the cyclic sequence of tetrahedra preserves the shapes as Z/3 orbits
  (to 10⁻²⁰). Its two centres are:
  - **n = 6** (m odd): one integer centre, a tetrahedron fixed by the reflection, inside the run's tetrahedra (at
    (n − 2)/2 or n/2, depending on whether SnapPy's tetrahedron i is the flip leaving or entering letter i); and one
    half-integer centre in the alternating block;
  - **n = 5** (m even): two half-integer centres, one in the run and one in the block.
- If SnapPy does not build one tetrahedron per letter, part E is void for that case, not a refutation.

**P7 (part E, the orientation).**
- The run's pairs are equal as Z/3 orbits but not conjugate: their conjugate-orbit distance (z ↦ 1/z̄) exceeds
  10⁻³. So the symmetry acts on the 3-manifold as an orientation-preserving involution, as derived above.
- For n = 6 the central tetrahedron's conjugate-orbit self-distance also exceeds 10⁻³.

**P8 (part E, the central shape).**
- The highest tetrahedra (height = Im of the shape reduced to the fundamental domain) are:
  - for n = 6, the central tetrahedron, at height ≈ 2.459;
  - for n = 5, the central pair, equal, at height ≈ 2.146;
  as P-723 found.
- Their shapes agree between k = 8 and k = 12 to 10⁻³.
- The n = 6 central shape, reduced, lies off every mirror: its Re is more than 10⁻⁶ from 0 and from ±½. The
  symmetry does not pin it, while it pins the apex to Re ∈ {0, ½}.

## What follows if all hold

- **The apex is derived** under (N1)–(N3), for every run, without a kinetic structure. B1845's "needs a kinetic
  structure" narrows to (N1) and (N2).
- **The departure is what makes the read-out unique.** The golden loop and every closed thread offer two symmetric
  candidates.
- **The same premises fix P-723's "which layer":** the central tetrahedron at even n, the central pair at odd n.
  - But the 3D shape is not pinned to a mirror, and it is not a point of the fibre's history.
  - The choice between the two candidates is (N2): what τ is.
- **(N3) rests on** B716 and on naturality.

**What stays chosen for the read-out:**
- (N1), a point rather than an average (an average is blind to the departure, P5);
- (N2), the conformal history rather than the 3D shapes.

0 of 19.
