# B479 — the held breath is torsion: member m holds the breath of every divisor of m

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

> **The held breath at d | m is the order-d torsion character of the once-punctured
> torus.** Member m holds the breath of every divisor d of m for which the order-d
> character survives the cusp condition.

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
