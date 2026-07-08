# B479 — the held breath is torsion: the order-d cusp points for divisors d ≥ 3 of m

**The breath campaign's structural law.** For the metallic family, the *breath* is the
period-2 orbit of the geometric character under the half-monodromy σ_m (BR3 wave 2: the
geometric fiber character is σ_m-SWAPPED at every m — it never sits still). A character
that IS fixed by σ_m — a *held breath* — is non-geometric. This note computes the entire
held-breath locus Fix(σ_m) on the cusp and identifies it exactly.

## The law (computed m = 1…16, both directions, exact)

Fix(T_m) ∩ {κ = −2} beyond the trivial z = 0 point:

| m | held-breath components (field) |
|---|---|
| 1, 2, 4 | **none** (only z = 0) |
| 3, 6, 9, 12, 15 | ℚ(√−7), the SAME point z² − z + 2 = 0 |
| 5, 10, 15 | ℚ(√41) (real!), the SAME quartic z⁴ − 3z³ + 7z² − 4z + 4 |
| 8, 16 | ℚ(√−3) |
| 7, 14 | ℚ(√−239) |
| others | one growing-degree component (m = 11 → deg 10, m = 13 → deg 12) |

**Two exact divisibility laws, verified m ≤ 16 in both directions:**
- **3 | m ⟺ the ℚ(√−7) held breath is present** (m = 3,6,9,12,15 yes; 1,2,4,5,7,8,10,11,13,14,16 no).
- **5 | m ⟺ the ℚ(√41) held breath is present** (m = 5,10,15 yes; else no).
- m = 15 (the seam level, = 3·5) carries BOTH — the crux confirming both laws at once.

## The mechanism — PROVEN, not fitted

σ_m: a ↦ aᵐb, b ↦ a. On the locus where **a has finite order d** (tr a = 2cos(2πk/d)),
if d | m then aᵐ = I, so σ_m degenerates to the **swap** τ: a ↔ b. The τ-fixed
characters are exactly the symmetric locus {tr a = tr b}; intersecting with the cusp
κ = −2 pins the held-breath point. Hence:

> **The held breath at m is the union, over divisors d ≥ 3 of m, of the order-d
> symmetric cusp point** (the order-d torsion character of the once-punctured torus).
> The divisors d = 1, 2, 4 contribute NOTHING — d = 1 is the identity (z = 0), d = 2
> has trace −2 (parabolic, not elliptic), d = 4 has trace 0 (the cusp collapses to
> z = 0). This is exactly why m ∈ {1, 2, 4} are breathless: none has a divisor d ≥ 3
> with a non-degenerate order-d cusp point.

Certificates (exact):
- d = 3: tr a = tr b = **−1** = 2cos(2π/3); order(−1) = 3 ✓; the point is z² − z + 2 = 0,
  ℚ(√−7), the SAME point for every 3 | m (m = 3,6,9,12,15 all give z² − z + 2 verbatim).
- d = 5: tr a = tr b ∈ {**(√5−1)/2, −(√5+1)/2**} = {2cos(2π/5), 2cos(4π/5)}; order = 5 ✓;
  the SAME quartic for every 5 | m (m = 5,10,15).
- m = 1,2,4: no order-3 or order-5 torsion divides m and the order-d cusp points for
  d | m are trivial, so the locus is empty beyond z = 0.

**Why this matters (firewalled, structural).** The metallic family's "held breath" is
its ORBIFOLD skeleton: the finite-order (elliptic) characters where a generator becomes
a rotation. The geometric (hyperbolic) character always breathes; only the torsion
points can hold still, and member m sees exactly the torsion of its divisors. The field
of the held breath is the field of the torsion character (ℚ(√−7) for order 3, ℚ(√41)
for order 5). Per the banked B461 discipline the recurrence of disc −7 gets NO
cumulative reading — but here the mechanism is explicit (order-3 torsion), so it is a
derived fact, not a coincidence to be weighed.

Reproducers: `held_breath_tower.py` (m ≤ 12), `held_breath_ext.py` (m = 13…16, the
crux), `held_breath_mechanism.py` (same-point + order-d certificates),
`../B469_breath_campaign/br3_wave2_exact.py` (the geometric-character-always-swaps
companion fact). Firewall: exact character-variety computation; no physics claim.

## Addendum (same session): the completed divisor-union law + closed-form field

Self-audit (verify-don't-trust on the banked headline): the first statement "every
divisor of m" was too strong — m = 4 has divisors 2, 4 yet holds NO breath. The precise,
fully-verified law:

**Held-breath(m) = ⋃ over divisors d ≥ 3 of m of the order-d symmetric cusp point.**

- Contributing divisors verified: m=8→{8}; m=9→{3,9}; m=12→{3,6,12}; m=15→{3,5,15} —
  each reproduces the exact component list of the computed tower.
- **Closed-form field.** The order-d point solves z² − τ_d² z + 2τ_d² = 0 with
  τ_d = 2cos(2π/d), single-τ discriminant **Δ_d = τ_d²(τ_d² − 8)**:
  Δ₃ = −7 (ℚ(√−7)), Δ₈ = −12 (ℚ(√−3)), Δ₁₂ = −15 (ℚ(√−15)) — the m=8 order-8 breath is
  ℚ(√−3) and the m=12 order-12 breath is ℚ(√−15), both confirmed. For composite φ(d) the
  Galois-conjugate τ's combine (d=5: the two golden τ's → the √41 quartic; the norm of the
  per-τ discs is 41).
- **d = 3 and d = 6 give the SAME point** (τ² = 1 for both, so identical cusp quadratic
  z² − z + 2): the √−7 breath is reached via order-3 whenever 3 | m; the order-6 element
  is a coincident trace, not a second point. Hence the clean law **3 | m ⟺ ℚ(√−7)** stands
  (order-3 mechanism), and likewise **5 | m ⟺ ℚ(√41)** (order-5).
- **Why d = 1, 2, 4 are breathless:** τ₁ = 2, τ₂ = −2 (both parabolic, |τ| = 2, not
  elliptic), τ₄ = 0 (Δ₄ = 0, cusp → z = 0). The three smallest metallic members m = 1, 2, 4
  have no other divisor ≥ 3, so they hold no breath — the figure-eight (m=1) and silver
  (m=2) bundles breathe but never hold. Reproducer: `held_breath_divisor_law.py` (this
  session's audit).

## Capstone (same session): the held breath is EXACTLY torsion — no rogue components

The remaining gap: could there be σ_m-fixed characters on the cusp that are NOT order-d
torsion (non-elliptic fixed points)? Verified NO, by matching the trace coordinate of the
large-degree components at prime m against the cyclotomic trace minimal polynomial:

| m (prime) | held-breath component: tr(a) minpoly | = minpoly of 2cos(2π/m)? |
|---|---|---|
| 7 | x³ + x² − 2x − 1 | ✓ (order-7) |
| 11 | x⁵ + x⁴ − 4x³ − 3x² + 3x + 1 | ✓ (order-11) |
| 13 | x⁶ + x⁵ − 5x⁴ − 4x³ + 6x² + 3x − 1 | ✓ (order-13) |

Each prime-m held-breath component's tr(a) is EXACTLY the order-m cyclotomic trace — the
component is the order-m torsion character, nothing more. With the composite cases
(divisor union) this closes the law:

> **THEOREM (held breath = torsion).** For the metallic once-punctured-torus bundle
> monodromy A_m, the σ_m-fixed characters on the cusp locus κ = −2 are exactly the
> order-d torsion characters for divisors d ≥ 3 of m — no non-elliptic fixed points. The
> geometric (hyperbolic) character is never among them (BR3 wave 2: always σ_m-swapped).

The mapping-class reading: σ_m acting on the relative SL(2,ℂ) character variety of the
once-punctured torus fixes exactly the elliptic (orbifold) points whose order divides m.
The metallic family's "held breath" is its orbifold skeleton; the geometric structure
breathes, the torsion holds still. Reproducer: `held_breath_capstone.py`.
