# B1604 — PREREGISTRATION: THE CLASS INDEX IS NOT AN INDEX — on a cusped 3-manifold every twisted Euler characteristic vanishes, so no count of flat-module cohomology can carry the physical index's shape identity; the class index is a difference of interior ranks in degrees one and two, and the dictionary FK11 cannot be earned on a thread or any cover of one

cc (main), 2026-10-08, after S83. A theorem arc with one numerical control. B1603 found eight kinds of reading
(I(W₁), I(Λ²W₁)) across 442 classes where a physical generation count — an index of closed-cycle cohomology, a
holomorphic Euler characteristic χ(X, V) on a Calabi–Yau threefold with the rank-five shape identity n_5̄ = n_10
(B1496) — would give one. The question: can any count on the record's objects be such an index? **Sealed before the
control is run on any thread but −LR.** No physical quantity. 0 of 19.

## Seen first

`VERDICT topic-sweep /Euler characteristic|chi\(N|index theorem|Chern character|ch_3|shape identity|not an index|Poincar/: 10 of 1376 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 8)`
— B1496 (the specification: the count is ∫ch₃(V) = χ(X, V); the class index lacks the identity), B1487 (the class
index is mirror-even for every module), B1297/B1418 (the class index's definitions), B1603 (eight kinds). Seen before the
seal: on −LR's forced cover the constraint of §E1 holds at all 20 modules (the four at 16 characters; W₁ and Λ²W₁ at
two members). **Literature:** χ(N) = ½χ(∂N) for a compact 3-manifold with boundary (standard); Poincaré–Lefschetz
duality with local coefficients; Hirzebruch–Riemann–Roch on a Calabi–Yau threefold (χ(X, V) = ∫ch₃(V) when c₁(V) = 0).

## The theorem (stated before the control)

**T-NO-INDEX-IN-THREE.** Let N be the interior of a compact 3-manifold with torus boundary (a cusped hyperbolic
3-manifold or any finite cover of one) and E any flat module. (i) χ(N; E) = χ(N, ∂N; E) = rank(E) · χ(N) = 0, since
χ(N) = ½χ(∂N) = 0. (ii) By Poincaré–Lefschetz duality h²(N; E) = dim H¹(N, ∂N; E*) = n(E*) + Σ_i t0_i(E*) − h⁰(E*)
and h³(N; E) = 0, so the stacked instrument's numbers satisfy a0(E) − a1(E) + n(E*) + Σ t0(E*) − a0(E*) = 0 at
every module. (iii) The class index I(E) = n(E) − n(E*) equals the interior rank of E in degree one minus its interior
rank in degree two; it is not an Euler characteristic and no characteristic class governs it, so no identity of the
form I(Λ²E) = f(I(E)) holds (B1603 exhibits I(W₁) = −1 with I(Λ²W₁) ∈ {−1, −2} and I(W₁) = 0 with I(Λ²W₁) ∈
{−1, −2, −3}). **Corollary.** The dictionary N(10′) = −I(W₁), N(5̄′) = −I(Λ²W₁) (GENESIS FK11) cannot be earned by any
index on a thread or a cover of a thread: a physical generation count needs an even-dimensional object with a non-flat
bundle (the physics' threefold), or "a generation" means a sector selected by a character (the orbifold standard,
B1495's addendum) — a selection, THE_BAR's baseline, now as a theorem rather than a grading.

## Disclosed

`verification/euler.py` rebuilds the forced cover as B1602 did and reads a0, a1, n, t0 of E and E* with B1492's
instrument (40 digits); h² by the duality formula; the control is a consistency check of the instrument's own
numbers against (i)–(ii). Not blind to −LR (seen) or to B1603.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **E1** | χ = 0 at every module checked on +LR, ±LLR, −LLLLRR, −LLRLRLRR, +LLLLLLRR (the four at every sign character; W₁ and Λ²W₁ at two members each), across the eight kinds | 95% |
| **E2** | at no module does the duality form give h² < 0 or a non-integral χ (the instrument's ranks are mutually consistent) | 95% |

**Reading rules.** E1 false at a module: the instrument's ranks are inconsistent there — an instrument error to find
before anything else (the theorem is not in doubt). E1 true: the theorem's numerical face holds; FK11 is marked
UNEARNABLE within F-HE/F-CI on threads and their covers, with the earning condition stated on GENESIS.

## Instruments

`verification/euler.py`; hashes in `ARTIFACT_HASHES.txt`.
