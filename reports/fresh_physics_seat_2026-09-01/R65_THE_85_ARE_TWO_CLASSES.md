# R65 — THE 85 ARE TWO CLASSES: 40 of B1264's trinification gradings are trinification elements and 45 are not; the founding ratio's E₆ factor selects the 40

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 87a2eb3d** · **Status:** seat report, not banked. Exact; script `computations/r65_gradings_by_class.py`. Follows R64.

## 0. Result

B1264 measured I-14's multiplicity: of the 3⁶ labellings c ∈ {0,1,2}⁶, **170** give a coweight h_c = Σ cᵢωᵢ^∨ integral on the 27 and splitting it 9+9+9, i.e. **85** colourings up to permuting the three colours, and it recorded that *"every such grading operator has eigenvalues 1, ω, ω²."* True — but they are not all conjugate. Classifying each labelling by the centralizer dimension of its grading operator, 6 + #{roots α : ⟨α, h_c⟩ ≡ 0 mod 3} (B1264's own convention, its 170 and 85 reproduced first):

| E₆ conjugacy class of the order-3 element (Kac) | centralizer | labellings | colourings |
|---|---|---|---|
| the mark-3 node: **A₂ × A₂ × A₂** — the trinification element | dim **24** | **80** | **40** |
| the three mark-1 nodes: **D₄ × T²** | dim **30** | **90** | **45** |

No colouring appears in both classes. So **45 of B1264's 85 "trinification gradings" are not trinification elements**: their centralizer is SO(8)×U(1)², not SU(3)³, and their 9+9+9 is 8+1 / 8+1 / 8+1 under D₄, not (3,3̄,1)/(1,3,3̄)/(3̄,1,3). The name attached to the whole family applies to 40 of them.

R64 showed the founding ratio's E₆ factor w₃ has 24 three-cycles on the 72 roots and no fixed vector on the Cartan, so its lift has Ad-fixed dimension 24: **the A₂³ class**. Therefore

> **The object's own order-3 element selects the trinification class and rejects the D₄ class: I-14's multiplicity falls from 85 to 40.** Not to a point — within the A₂³ class the 40 colourings are Weyl-conjugate representatives in B1264's fixed torus, and nothing in g distinguishes them (the E₆ lattice cut out of the icosians comes with no preferred Cartan). This is a partial H5 collapse, of the same kind as B1272–B1274's: a selector that halves a family and names what it discards.

## 1. Controls

- B1264's counts reproduced exactly (170, 85) with its formula ⟨λ, h_c⟩ = λ·C⁻¹·c on the 27 weights, using this bench's own 27 (Weyl orbit of ω₁) and root system, not B883's file.
- The class dimensions 24 and 30 are the only ones occurring; Kac's list for order 3 in E₆ is {24, 28, 30, 36, 78}, and the absent ones (28, 36, 78) do not split the 27 as 9+9+9 — consistent.
- Colourings are class-pure (0 appear in two classes), so the 85 → 40 statement is well-defined at the colouring level B1264 uses.
- w₃'s class is taken from R64's cycle count under the order-3-lift caveat stated there.

## 2. What it changes

- **B1264's I-14 row** should read: 170 labellings in **two** classes; the trinification class has 80 (40 colourings); the object's g (R64) lies in it. The "L3 = L4 same ω" observation is now explained (R64) *and* sharpened: L3's admissible gradings are the 40, not the 85.
- **B1275's chain** (L3, L4, A₂ "three order-3 structures"): after R64 and this report, L3 (the A₂³ element, 40 representatives), L4 (ω on the cusp/commensurator) and the family rotation are one element's factors and classes — the remaining question is the one B1264 already had, *which of the 40*, and it is a Cartan choice, not an object datum.

*Swept before writing: B1264's script and FINDINGS contain no conjugacy classification; "centralizer" does not occur in the arc. The Kac-coordinate classification of order-3 elements is standard (cited).*
