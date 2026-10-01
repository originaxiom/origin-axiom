# B1444 — THE BACKGROUNDS ARE THE REDUCIBLE ENDS OF THE TRACE MAP'S PERIODIC CURVES: the slope is the cusp shape at the end, the banked coupling is the first-order torsion of the sector along the curve, and the generation's index lives only at the end

cc, 2026-10-01. Lead L235 asked what fixes the values an orbit's Higgs classes take, and the owner asked that a chain
be carried to its last computation rather than filed. The chain taken here: a background of the Standard-Model
frame (B1432) carries a rank-two piece that is a reducible, non-split representation of the level. Such a
representation is the limit of irreducible ones, and on a once-punctured-torus bundle the irreducible ones are the
periodic points of the object's own trace map. So every background sits at the end of a curve of actual flat
connections, and everything the frame computes at the background — index, slope, coupling — can be followed along
it. **Verdict: PROVED** (two theorems with proof; five sealed predictions on 27 untouched levels, all held).

## 1. The curve through a background

T is the trace map of the level's monodromy Φ on (X, Y, Z) = (tr x, tr y, tr xy), preserving
κ = X² + Y² + Z² − XYZ − 2. A representation of the level into PSL(2, ℂ) that is irreducible on the fibre is a point
with T(p) = σ·p for a sign twist σ, and conversely each such point is one representation (the meridian is the
intertwiner, unique up to sign).

**Theorem A.** Let ℓ be a non-trivial character of a level, trivial on the meridian, and v a square root of ℓ on the
fibre. Then p₀ = (v(x) + v(x)⁻¹, v(y) + v(y)⁻¹, v(xy) + v(xy)⁻¹) is a smooth point of κ = 2 with
T(p₀) = σ·p₀, and exactly one smooth curve of solutions of T(p) = σ·p passes through p₀; it is transverse to κ = 2.

*Proof.* κ = 2 is the quotient of the torus of characters by inversion, smooth away from the four points v = v⁻¹
(where ℓ = v² is trivial), and T acts on it as the linear map of Φ. Its derivative at p₀ on the surface has the eigenvalues λ, λ⁻¹ of Φ's
matrix, neither equal to ±1, and across the surface the eigenvalue is 1 because κ is preserved. So d(T − σ) has
rank two at p₀ with kernel transverse to the surface, and the implicit function theorem gives the curve. ∎

The points of the curve off κ = 2 are irreducible on the fibre. The reducible non-split representation
[[1, c], [0, ℓ⁻¹]] of the frame is the first-order germ of the curve at p₀: its extension class c is the tangent.
e = 2 − κ is the parameter along the curve at the end.

## 2. The root, exactly (`verification/periodic_curves.sage`, primary decomposition over ℚ)

| level | sign twist | components | on κ = 2 | on κ = −2 |
|---|---|---|---|---|
| 1 | each | one conic, XZ = X + Z, Y = Z (and its three sign images) | the node, and the two characters of order 5 (the sister's) | the geometric representation X = (3 ± √−3)/2, and the quaternion point (0, 0, 0) |
| 2 | each | the conic and two lines, e.g. Y = Z = −1 | characters of order 3 with Φ²χ = χ⁻¹ (the bundle of monodromy −A²) | X² − X + 2 = 0: ℚ(√−7), B448's period-four field |
| 3 | trivial | three lines and the four conics | — | — |
| 3 | non-trivial | one line and two rational quartics | 8 points each: 4 square roots of characters of order 4 (the root's), 4 square roots of characters of order 10 (the sister's) | 8 points each |

On the three-fold cover the quartic is X = u − 1, Y = −Z, Z² = 1 + 1/u², and with **w = u − 1/u**
(`holonomy.sage`, exact over the function field of the curve):

    longitude:  l + 1/l − 2 = κ − 2 = w(w − 1)
    meridian:   m + 1/m − 2 = −w(w² − w + 4)

- **w = 0** (u = ±1): the two extension characters of s961's backgrounds on this twist. Twelve characters of order
  four, in pairs ℓ, ℓ⁻¹, two pairs on each of the three twisted loci; the deck transformation permutes the loci.
- **w = 1** (u = φ, −1/φ): the sister's three-fold level. Between them, 0 < w < 1, is a real arc of irreducible
  representations with real traces and κ between 7/4 and 2: the root's background and the sister's are the two ends
  of one arc of flat connections.
- **w² − w + 4 = 0**: κ = −2 and the meridian parabolic — a complete cusp. w = (1 ± √−15)/2 and
  u⁴ − u³ + 2u² + u + 1 = 0: the coordinates lie in **ℚ(√−3, √5)** (discriminant 3²·5², Galois;
  `cusp_point.sage`). A boundary-parabolic representation of s961 that is not the geometric one. B448 computed the
  periodic-orbit fields on κ = −2 for the untwisted locus only; this point is on a twisted locus.

## 3. The law

For a character χ of the level let s(χ) be B1438's slope. s(χ⁻¹) = s(χ) (s is real and commutes with complex
conjugation; checked on 164 characters of seven levels).

**Theorem B.** On the curve through the background of ℓ:

(i) the cusp shape tends to the slope: with M, l the eigenvalues of the meridian and of the longitude in SL(2),
log M / log l → ± s(ℓ) at the end;

(ii) for a character β of the level with α = ℓβ, both non-trivial, let V be the sector module ρ ⊗ (vβ) on the curve
(at the end it is α ⊕ β) and τ = det(1 − Φ* | H¹(F; V)) its torsion. Then

    τ = (s(α) − s(ℓ)) · (s(β) − s(ℓ)) · e + O(e²).

*Proof (first-order deformation theory; the one universal sign in identifying H² with the pairing on the boundary
torus is fixed by the computation, not derived).* Write the curve as ρ_δ = ρ₀ + δρ₁ + …, ρ₀ = diag(v, v⁻¹). ρ₁ is off-diagonal, with entries cocycles c₊ of ℓ
and c₋ of ℓ⁻¹, both non-zero because the curve leaves κ = 2 at first order in e: tr ρ_δ(λ) − 2 = δ² c₊(λ)c₋(λ), so
e = −δ² c₊(λ)c₋(λ). The meridian is 1 + δ(off-diagonal c₊(μ), c₋(μ)) + …, so tr − 2 = δ² c₊(μ)c₋(μ) =
s(ℓ)² δ² c₊(λ)c₋(λ), which is (i). For (ii): at δ = 0, H¹(F; V) = H¹(F; α) ⊕ H¹(F; β), two lines on which Φ* is the
identity (the class of each is the restriction of the class of the level). The derivative of 1 − Φ* in δ maps the
kernel to the cokernel by the connecting map of V mod δ², which is the cup product with ρ₁: the class of β goes to
c₊ ∪ h_β in H²(M; α) and the class of α to c₋ ∪ h_α in H²(M; β). Each H² is a line read on the boundary torus, where
c₊ ∪ h_β = c₊(λ)h_β(λ)(s(ℓ) − s(β)) and c₋ ∪ h_α = c₋(λ)h_α(λ)(s(ℓ) − s(α)). So 1 − Φ* = δ·(off-diagonal) + O(δ²) and
its determinant is −δ² c₊(λ)c₋(λ)(s(ℓ) − s(α))(s(ℓ) − s(β)) + O(δ³) = e (s(α) − s(ℓ))(s(β) − s(ℓ)) + …; the odd
orders in δ vanish because τ is a function on the curve, analytic in e. ∎

So **the slope law (B1438) is first-order deformation theory along this curve**:

- the slope is the cusp shape at the end of a curve of irreducible flat connections;
- the coupling s(ℓ) − s(η) is the first-order term of a sector's torsion: a sector with no slope match is lifted
  at first order, with coefficient the product of its two couplings;
- **the firing condition is the vanishing of that term.** A sector carries the frame's index exactly when one of
  its two slope differences is zero.

Computed also on every sector (`curve_engine.py`, asserted): the two eigenvalues of the monodromy on H¹(F; V) are
inverse to each other, so τ = 2 − E with E their sum; on the root's three-fold cover E = 2u√(1 − w) exactly for the
generation's family (`torsion_exact.sage`: the torsions for the two signs of the meridian sum to 4 and multiply to
4(u − 1)²(u + 1)).

## 4. The sealed run (preregistered, seal `d88c220e`, pushed to both remotes before the run)

27 levels none of which had been run, 146 backgrounds, 1 734 sector modules. All curves were followed; none was
dropped.

| | prediction | prior | result |
|---|---|---|---|
| P1 | every unmatched sector: order one, coefficient (s(α) − s(ℓ))(s(β) − s(ℓ)) to 10⁻⁶ | 85% | **YES, 1 223 of 1 223** |
| P2 | every matched sector: order at least two, or identically zero; no unmatched sector identically zero | 85% | **YES, 511 of 511** (380 of order two or three, 131 identically zero) |
| P3 | the cusp shape tends to \|s(ℓ)\| | 90% | **YES, 146 of 146** |
| P4 | some matched sector identically zero ⟺ the meridian is ±(longitude)^±s along the curve | 65% | **YES, 146 of 146** (27 and 27) |
| P5 | both kinds of background occur | 80% | **YES** |

With the exploration that preceded the seal (11 other levels, 56 backgrounds, 932 unmatched sectors, all agreeing):
2 155 unmatched sectors, no exception. P1–P3 are Theorem B; P4 has no proof here.

**A guess that failed** and was dropped before the seal: "the order is one plus the number of slope matches". Ten
doubly matched sectors of the exploration have order two (on −LLLR 3, +LRR 3 and +LLRLRRLR 1). In the run the
guess happens to hold — 346 singly matched sectors of order two, 34 doubly matched of order three, 131 identically
zero — and it is still not a law.

## 5. The index lives at the end

Off κ = 2 the longitude has eigenvalues l ≠ 1 on a doublet, so the cusp holonomy has no invariant vector in V or in
its dual, and B1297's identity I = (a₀ − a₀*) + t₀* − r₁ gives **I = 0 at every point of the curve off the end**.
The class index of the frame is a property of the reducible end: the generation is chiral there and nowhere else
on the curve. What exists along the curve is the torsion: it vanishes where the sector has cohomology and is the
quantity that continues the index.

## 6. Two kinds of background

On 38 of the 202 backgrounds (11 in the exploration, 27 in the run) the matched sectors' torsion vanishes
**identically** along the curve — the sector keeps a class however far the background moves — and on exactly those
the meridian equals ±(longitude)^±s for the whole curve: the curve lies in the character variety of the Dehn filling
of slope s, s an integer (0, ±1, −2 in the data). On the others the matched sectors have a non-zero second-order
coefficient. The root's three-fold cover is of the second kind; +LLRLRRLR at its own level (B1439's shortest state
with all four couplings) is of the first kind on all 16 of its backgrounds.

## 7. The frame's backgrounds, sector by sector (`frame_sectors.py`)

The backgrounds are assembled as in B1432 from (θ, ψ_Y, W), with the firing law from slopes computed here; the
counts agree with B1432's on every level (48, 256, 400). In almost every background ψ_Y⁵ = 1, so Q, u^c, e^c are one
module and d^c, L one module; the table gives the second-order coefficient of each.

| level | backgrounds | the ten's module | the five-bar's module |
|---|---|---|---|
| +LR 3 (s961) | 48 | 1/2 | 1/2 |
| −LR 3 | 96 | 3/4 | 3/4 |
| +LLR 3 | 48 | 1/2 | (3 ± √5)/4 = φ^±2 / 2 |
| −LLLR 3 | 48 | 25/2 or −1/14 | the same |
| +LR 4 | 256 | 69/4 ± (15/2)√5 | 67/4 ± (38/5)√5, 79/4 ± 9√5, 287/20 ± (31/5)√5 |
| +LR 5 | 400 | five values (numerical record) | five values |
| +LLRLRRLR 1 | 16 | identically zero | identically zero |

These are the first numbers of the frame that depend on the sector and are computed on irreducible flat
connections. They lie in the field of the level's slopes. No closed formula for them is known here.

## 8. The bulk gives no product of an orbit's Higgs classes (lead L235 (a), `no_bulk_cubic.py`)

B1443 noted that on the root's tower the product of an orbit's three Higgs characters is trivial, so a cubic joining
the three Higgs classes is allowed by the characters. It has no group to live in: h²(M; k) = 0 and h³ = 0 on a
level (computed), the pairwise products vanish because the slopes of an orbit are equal (checked with the cocycles
on 16 + 16 + 80 orbits of three levels), and the triple product then lands in H²(M; k) = 0. A function of the Higgs
classes is not a bulk cup product.

## 9. What it means, and the fence

- **The frame's backgrounds are points of the object's own dynamics.** The trace map is the root's monodromy acting
  on its character variety; its periodic curves at level k are the flat PSL(2) connections of the k-fold cover; the
  frame's backgrounds are where those curves meet the reducible surface, and the frame's non-split extension is the
  direction in which they leave it.
- **What a Higgs value is, in this frame, now has an object:** the position on the curve. The parameter is not
  free of structure — the curve has distinguished points (the other reducible end; the complete cusp, with
  coordinates in ℚ(√−3, √5) on s961) — and nothing computed here selects one. That question is now a question about
  a rational curve with explicit functions on it, not about an unnamed potential.
- **The imported expectation, stated separately:** that the generation's index should persist when the background
  moves. It does not, and cannot: the index is a boundary quantity and the boundary holonomy stops having
  invariants.
- **The curve is not electroweak breaking.** SL(2)_β is the simple factor of the centraliser of the Standard Model's
  gauge algebra in E₆ (sm:B1364, harvested in B1415; recomputed here on the root system, `e6_centraliser.py`: one
  root pair commutes with su(3) ⊕ su(2)_L ⊕ u(1)_Y, its own centraliser has the 30 roots of su(6), and all 20 roots
  of su(5) commute with it). A deformation inside SL(2)_β leaves the Standard Model's gauge group untouched. So
  what the curve shows is this: **the frame's chirality requires the hidden SL(2)_β holonomy to stay reducible**;
  moving it off the reducible surface pairs the generation up (second order, on backgrounds like the root's) or
  leaves a pair of classes (filling type), with the Standard Model's gauge group intact either way. The electroweak
  direction is the Higgs character's (§11).
- **Fenced reading (speculation, with what each step would need):**

| reading | computation it needs |
|---|---|
| the eigenvalue pair e, 1/e of the monodromy on H¹(F; V) is the sector's frequency per period of the flow, so arccos(E/2) is its mass in units of the level | a kinetic normalisation; none exists in the record |
| ratios of second-order coefficients are ratios of the scales at which a hidden modulus pairs up the sectors | the above; they are not electroweak mass ratios (the curve commutes with the Standard Model's gauge group) |
| filling-type backgrounds are those whose generation is protected | a proof of P4 and the meaning of the Dehn filling in the frame |

- **The fence:** main's class index on modules outside the reductive domain; torsion is not a mass; one direction
  (the extension character's) of the background; all three members of a deck orbit have the same data, so nothing
  here distinguishes generations. **0 of 19.**

## 10. Corrections made in the course of the arc

- The order of vanishing is not "one plus the number of matches" (§4).
- "The three sectors of the ten share a coefficient" is not a result: they are the same module where ψ_Y⁵ = 1. It
  was reported to the owner as emergent for a few minutes and corrected in the same session.
- B1438 and B1443 write the firing law with s(β⁻¹); s(β⁻¹) = s(β), so it reads I = [s(α) = s(ℓ)] − [s(β) = s(ℓ)].
- **Characters of order two are not at the nodes.** The sealed preregistration (§2, §6) and the first draft of this
  text restricted Theorem A to extension characters of order above two, taking one of order two to sit at a node of
  κ = 2. A node is a point v = v⁻¹, where ℓ is trivial; a character of order two has a square root of order four,
  a smooth point. Its curve is one of the lines of §2 (on the root's three-fold cover X = Z = 0 and its images),
  Theorem B holds on it (checked on the three characters of order two of s961, 42 sectors: first-order
  coefficients ±1, as predicted), and it is of filling type with the meridian trivial, which is slope zero. Found
  while the certifying suite of this landing was running; the sealed run's population is unaffected (it is the
  characters of order above two), and the statement is carried to B1445, which uses these curves.

## 11. Not computed (each is a lead, L236)

- A formula for the second-order coefficients (a second-order slope).
- A proof of P4, and what the filled manifold is.
- The direction of the Higgs character η of B1435/B1443 from a background whose extension is already switched on:
  the coupling s(ℓ) − s(η) is the obstruction to moving in both directions at once.
- The volume and Chern–Simons invariant of the complete-cusp point on s961.
- Whether anything selects a point of the curve. (For the generation to stay chiral it must be the end.)

## Verification

`verification/curve_engine.py` (the curve, the meridian, the sector torsion; mpmath, 60 digits);
`law_population.py`, `read_law.py`, records `law_population_NN.json`, `law_population_summary.json` (the sealed
run); `exploration_census.py`, `exploration_checks.py` (the exploration, disclosed); `frame_sectors.py` with one
record per level; `periodic_curves.sage`, `holonomy.sage`, `torsion_exact.sage`, `cusp_point.sage` with their
records (exact; these need Sage and are not run by the lock, which checks their statements numerically);
`no_bulk_cubic.py`; `e6_centraliser.py`. Lock: `tests/test_b1444_periodic_curves.py`.
