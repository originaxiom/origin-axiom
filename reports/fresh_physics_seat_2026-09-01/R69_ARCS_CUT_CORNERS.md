# R69 — ARCS CUT CORNERS: Fix(θ) as a charge locus gives net = ±2, R61's θ-even clause is retracted, R56's "closed ⇒ zero" is scoped to smooth fields, and every filling closes the arcs back to χ = 0

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat correction + result, not banked. Owner's question, verbatim: *"do R61's two Fix(θ) arcs give χ(∂⁺M) ≠ 0? Arcs cut corners."* Answer: **yes, ±2.** Script `computations/r69_arcs_cut_corners.py`.

## 1. The arithmetic

Pantev–Wijnholt: net(R) = χ(M′, ∂⁺M′) = χ(M′) − χ(∂⁺M′), M′ = Q minus the charge locus Δ, ∂⁺ the boundary of a neighbourhood of the positive locus (PW §3.5; their (3.63) is the S³ case, and their §3.6 example — **three** chiral 16's — is on the **compact** Q = S³). The formula reduces to **net = χ(Δ⁻) − χ(Δ⁺)** for closed or cusped Q alike.

For Q = m004 and Δ = Fix(θ), the two arcs of R61 (endpoints at the four 2-torsion points of the cusp torus): removing a properly embedded arc lowers χ by 1 (χ(M) = χ(M∖N) + χ(N) − χ(annulus)), so χ(M′) = 0 − 2 = **−2**; the tubes are annuli, χ = 0.

| signs on the two arcs | χ(Δ⁻) − χ(Δ⁺) | net |
|---|---|---|
| (+, +) | 0 − 2 | **−2** |
| (−, −) | 2 − 0 | **+2** |
| (+, −) | 1 − 1 | 0 |
| control: the knot 4₁ as locus | 0 (one component, one loop) | 0 (R56) |

**Two, with a list:** the arc 0 ↔ τ/2 and the arc ½ ↔ ½+τ/2. A knot has no endpoints; the θ-arcs have four. That is the whole difference.

## 2. What this corrects

- **R61 §3, second clause — RETRACTED.** It claimed a θ-even field (u ∈ 𝔣₄, f∘σ = f) gives zero because "the unbroken group contains an F₄-type subalgebra and every charged component comes with its conjugate in a real representation." False: u breaks F₄ as well; R_q and R_{−q} are distinct representations of the actual unbroken group (the centralizer of u), and net(R_q) = −net(R_{−q}) is a consistency relation, not zero. Charges on Fix(θ) are exactly a θ-**even** configuration (Fix(θ) is σ-invariant, equal signs are σ-invariant), and it carries |net| = 2. **The lemma reduces to its first clause: θ-odd equivariant configurations have net 0 (the region swap); θ-even ones need not.**
- **R56 §0/§2 — SCOPED.** "Identically zero on a closed 3-manifold" is the smooth statement (Poincaré–Hopf; Braun et al. 2.50), which is the right frame for the record's flat-connection walls (E65, B1260, B1267, B1086) and for R56's knot computation. With a singular charge locus the count is χ(Δ⁻) − χ(Δ⁺) on closed Q too. R56's actual content — the object as a knot has χ = 0; three generations need three endpoints — stands.
- **R62 §0 — the inference "hence no count" RETRACTED**, the fact kept: θ = −I extends over every filling. The corrected consequence is in §3.
- B1268's bound |N(27)| ≤ 1 (SM-derivation branch) concerns flat deformations near the geometric point and does not constrain a singular Higgs field; it is not in tension with ±2.

## 3. The fillings, corrected

In M(p/q) the strong inversion of the solid torus, (w, e^{iφ}) ↦ (w̄, e^{−iφ}), fixes two arcs that join the four boundary 2-torsion points in pairs; the pairing is decided by the slope mod 2 (the meridian through 0 passes through the 2-torsion point (p mod 2, q mod 2)). Joined to M's arcs (0↔τ/2, ½↔½+τ/2), Fix(θ) becomes **one closed loop** (slopes ≡ (1,0), (1,1) mod 2) or **two** (slopes ≡ (0,1) mod 2) — closed either way, χ = 0. **The cusp is what keeps the endpoints; every closing removes them.** So R62's headline survives in the form that matters: no Dehn filling can carry this count.

> **Banner (R72, 2026-09-06).** The clause below "the U(1) direction u must be θ-even (u ∈ 𝔣₄ …)" is the record's *outer* lift of θ to E₆ (the diagram involution, B353). B353's own item (B) — θ_D commutes with the holonomy — means the involution also lifts *inner*, as Ad(ι(N)) with fixed algebra A₅⊕A₁ and the whole Cartan fixed; under that lift every u is even and the ±2 on the SO(10) direction is 2 × (16 ⊕ 10 ⊕ 1). The count ±2 itself is unchanged; R72 §2 refines its derivation with the cusp torus as a boundary component (B1291's −4 enters for one sign).

## 4. What the ±2 is and is not

It is a θ-even, θ-equivariant, object-supplied charge locus whose Euler characteristic is 2 — the first nonzero count in this seat's reports, obtained exactly where R56 said one must be: at endpoints. It is not three, and it is not a derivation of anything physical: the sign assignment (equal versus opposite) is a binary the object does not pick, the U(1) direction u must be θ-even (u ∈ 𝔣₄ — the D₂ direction is θ-**odd**, its generator lies in the 26, so along D₂ the count is 0), and "generation" would mean a charged component of the 27 under that u, not a 27. The number 2 also appears at B1086 (h¹ = 2 on the θ-odd double) and in R57/R58's ι-structure; those are different objects and no identification is made here.

*Owner's rule applied: the correction is made at source (banners on R56, R61, R62), and the positive statement carries its list and its fences.*
