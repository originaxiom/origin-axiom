# SM-C14 — m000 and its tick levels in the harmonic E₈ frame (F-HE) and the G₂ apex frame (F-AP)

*Card of the SM seat, 2026-11-14, offered by main (M28: "m000 in your two frames") and taken. Committed and pushed, with
its expectations, before any sealed quantity is computed. Data-free: nothing is compared with a measured number.*

*Disclosed before the seal: to make sure the instrument can be built, this seat solved for an exact holonomy of m000
(§ 1) and checked one relation (the orientation-reversing generator has a unit determinant). No cohomology, index or
cusp shape of m000 or its levels has been computed.*

## 0. The objects

- **The tick and its levels** (B1926). G_n = ⟨a, b, t ∣ t x t⁻¹ = σⁿ(x)⟩, with σ: a ↦ ab, b ↦ a (det −1).
  - G_1 is m000. G_2 is m004. Level 2k is m004's level M_k.
  - An odd level is non-orientable, with orientation character w (w(t) = −1, w = 1 on the fibre). Its double cover is
    level 2n = M_n.
  - The scar is λ = [a, b], and the meridian is μ = g_n⁻¹ t, with μ λ μ⁻¹ = λ^((−1)ⁿ). The cusp is a Klein bottle at odd
    n and a torus at even n.
- **The frames, as GENESIS's table states them.**
  - F-HE: E₈ ⊃ SU(5) × SU(5)′ on the harmonic convex-projective vacuum (Ballas' ρ_q on m004; the hyperbolic point is
    q = 1). Rank-five extensions W, with N(10′) = −I(W) and N(5̄′) = −I(Λ²W). On m004 it was computed at the μ = −1
    points (sm:B1509) and at q = 1 on M₁–M₆ (sm:B1515).
  - F-AP: matter at the cone points of a G₂ space built over the cusps. A cusp point's local model is an ADE locus
    coned over the cusp's cross-section (sm:B1500). B1501's cones complete only hexagonal cusp tori.

## 1. What is derived before any run

- **T-HE1 (the vacuum family does not descend).**
  - At odd n the meridian conjugates λ to λ⁻¹, so a representation of G_n restricted from one of the double cover
    must send λ to a matrix conjugate to the inverse of its own image, up to a scalar c with c⁴ = 1.
  - Ballas' ρ_q(λ) has spectrum {q, q, q, q⁻³} (B1509 § 1). Inverting gives {q⁻¹, q⁻¹, q⁻¹, q³}. Matching the triple
    eigenvalue forces c = q², and then the fourth forces q⁸ = 1. For q > 0, that leaves q = 1.
  - So no member of the family with q ≠ 1, with or without a central twist, extends to m000 or to any odd level. The
    deck transformation sends ρ_q to a representation with longitude parameter 1/q.
  - **The expected reading:** the vacuum's deformation reaches the odd ticks only twisted by the orientation. At first
    order, the deformation lies in H¹(V₉ ⊗ w), not in H¹(V₉), where V₉ is the q-symmetric traceless part of sl(4).
- **T-HE2 (the frame's extensions at odd ticks are B1926's twisted ones).**
  - The geometric four ρ₁ of m000 has det ρ₁ = w: the orientation-reversing elements are reflections in O(3, 1).
  - A rank-five W = [[ν ⊗ ρ₁, cL], [0, L]] lies in SL(5) only if L = ν⁻⁴ w. So every extension the frame can build on
    an odd level carries the orientation character in its corner.
  - That is B1926's twisted form, with diagonal characters differing by w. On m004 the corner was ν⁻⁴ (B1515).
- **T-AP1 (no G₂ locus is non-orientable).**
  - An ADE locus of a G₂ space is the fixed set of Γ ⊂ SU(2), acting on the normal 4-space. That fixed set is
    associative, so φ restricts to its volume form, and it is oriented.
  - Hence neither m000 nor any odd level can be F-AP's locus, and neither can a cone over a Klein bottle. F-AP is not
    defined on them, and that reason is the result.
- **T-AP2 (a Klein bottle cusp never has a hexagonal double cover).**
  - In a flat Klein bottle the glide g reflects the translation lattice, so the translation y with g y g⁻¹ = y⁻¹ is
    perpendicular to the glide's axis, and g² lies along it. The double cover's lattice ⟨g², y⟩ has an orthogonal
    basis: it is rectangular, never hexagonal.
  - The even levels' cusp tori ⟨μ^(2k), λ⟩ are rectangular too, as m004's is (shape 2√−3).
  - So B1501's cones complete no cusp of any tick level, even after passing to an orientation cover.

## 2. What is computed

**The instrument** is this seat's own Fox calculus over GF(p). Its parts:
- m000's holonomy, exact over ℚ(√−3):
  - A = [[1 + ζ, 1], [−1, 0]] and B = [[ζ̄, −ζ̄], [−ζ̄, 1]], with ζ = (1 + √−3)/2, a primitive sixth root of unity;
  - the anti-holomorphic generator z ↦ M z̄, with M = [[−ζ̄, 0], [ζ̄, 1]] (det M = −ζ̄, a unit);
  - all of it acting on 2 × 2 matrices, X ↦ G X G* and X ↦ M Xᵀ M*. This is the complexified Minkowski four ρ₁.
- The peripheral group at every level, the torus or the Klein bottle, with its own presentation.
- n(V) = dim ker(H¹(G_n; V) → H¹(P; V)).
- I(V) = n(V) − n(V*), as the frame defines it on m004, and I_w(V) = n(V) − n(V* ⊗ w), the pairing that
  non-orientable duality uses. Both are reported.
- Three primes per level, with p ≡ 1 mod lcm(N, 12). The ranks must agree.

- **HE-1, the vacuum's first-order deformation.**
  - h¹(G_n; V₉) and h¹(G_n; V₉ ⊗ w) at the odd levels n = 1, 3, 5 and 7, with V₉ = S²ρ₁ minus its invariant line.
  - Also the rank of their restriction to the cusp, and the even levels 2, 4 and 6.
- **HE-2, F-HE's count at q = 1, as sm:B1515 reads it on m004.**
  - At the odd levels 1, 3, 5 and 7, for every character ν (a fibre-torsion character, times ν(t) any 12th root of
    unity, which takes in B1926's twisted characters):
    - V = ν ⊗ ρ₁ and L = ν⁻⁴ w;
    - n(V), n(V ⊗ w) and h¹(V ⊗ L⁻¹);
    - for every member (h¹(V ⊗ L⁻¹) > 0) and every class trial (each basis class, the first two summed, and a generic
      combination), W₁ = [[V, cL], [0, L]] and the opposite order W₂.
  - For each W: I(W), I_w(W), I(Λ²W) and I_w(Λ²W).
  - A member is generation-shaped if I(W) = I(Λ²W) ≠ 0 (R40's 10 + 5̄), and likewise for I_w.
- **AP-2, the cusp shapes.** SnapPy's m000 and its cyclic covers of degree n = 1 to 8 (the tick levels). Each shape is
  reduced to the fundamental domain and tested for rectangular (real part 0) and hexagonal (ω).

## 3. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| HE-1a | h¹(m004; V₉) = 1 (Heusener–Porti; a control of the instrument) | 98% |
| HE-1b | m000: h¹(V₉) = 0 and h¹(V₉ ⊗ w) = 1, and the twisted class restricts non-trivially to the Klein bottle | 85% |
| HE-1c | odd levels 3, 5, 7: h¹(V₉) = 0 and h¹(V₉ ⊗ w) ≥ 1 | 65% |
| HE-2a | n(ν ⊗ ρ₁) = 0 for every ν at levels 1, 3, 5 (this follows from sm:B1515's M₁–M₅ by transfer: interior classes inject under pull-back) | 90% |
| HE-2a′ | the same at level 7 (M₇ was never computed) | 70% |
| HE-2b | no generation-shaped member at any odd level, in either pairing or order | 85% |
| AP-1 | φ restricted to the fixed 3-plane of ℤ_k ⊂ SU(2), k = 2 to 6, is ± its volume form (numerical check of T-AP1) | 99% |
| AP-2 | every level's cusp shape reduces to a purely imaginary τ, never ω; the modulus is 2√3/n or n/(2√3), whichever is ≥ 1, at both n and 2n | 80% |

## 4. Controls that must fail if the work is broken

- **C1.** Every module satisfies the relators exactly, and every W has determinant one.
- **C2 (the hyperbolic check).**
  - At level 2, μ and λ are parabolic with a common fixed point.
  - Their translation ratio reduces to m004's cusp shape 2√−3, which SnapPy also reports.
- **C3 (duality, built in).** On every module:
  - at even levels, r₁(V) + r₁(V*) = h¹(T; V);
  - at odd levels, r₁(V) + r₁(V* ⊗ w) = h¹(K; V).
  - If either fails, the run stops.
- **C4 (transfer).** h¹(level 2n; π*V) = h¹(n; V) + h¹(n; V ⊗ w), on every character of levels 1 and 3.
- **C5 (a positive control of the index).** R40's module on m010 (route T's m010_reps, rebuilt by this seat's code)
  must give I(W) = I(Λ²W) = +1.
- **The plants:**
  - P1: L = ν⁻⁴ without w. The determinant check must fire at every odd level.
  - P2: ρ₁(t) replaced by −ρ₁(t), which is the twist by w. HE-1's two numbers must swap.
  - P3: the torus formula used on a Klein-bottle cusp. C3 must fail somewhere.

## 5. What the outcomes mean

- **If HE-1b holds:** m000 is projectively rigid at its hyperbolic point. F-HE's vacuum reaches the odd ticks only at
  q = 1, and its deformation exists there only twisted by the orientation. This is B1926's pattern, met in the vacuum
  itself.
- **HE-2:** F-HE's count on m000 and its odd levels, read as on m004. Either it is a NEGATIVE, or the members are named.
  It is PROVISIONAL under main's rule (M26) until another seat recomputes it.
- **F-AP:** it is not defined on m000 or any odd level (T-AP1), and on the even levels it reads as on m004 (T-AP2).
- **B1926's twisted modules:**
  - in F-HE, they are the only rank-five extensions an odd level allows (T-HE2), and the vacuum's deformation (HE-1);
  - in F-AP, they have no counterpart. An orientation twist of the locus would have to reverse φ, which is M-theory's
    parity (C ↦ −C), not a G₂ structure. This is a reading, not a computation.

## 6. Files

relays/sm_c14/, with its scripts, outputs and runs. The page will be relays/SM_C14_M000_IN_F_HE_AND_F_AP.md.
