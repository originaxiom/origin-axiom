# B1746 — THE CUBE GROUP'S FORMS AS THE HIGGS (P-357; THE WEB SEAT'S STEP 3 (c)): THE FRAME'S FAMILY GROUP'S OWN FORMS GIVE R AT WEIGHT 4 AND ∂R AT WEIGHT 6 (EXACT) AS ITS NEARLY NULL DIRECTIONS, ITS UNTWISTED WEIGHT-6 SPACE IS span{F₆, F₋₆}, AND NO TWO-DIMENSIONAL SPACE OF ITS FORMS REACHES THE NINE

**Verdict: NEGATIVE for its question** (does a form of the frame's family group Γ₄, or a pencil of two, reach the
nine's target?), **with the identities PROVED** (data-free). The data look is post hoc, labelled. cc (main), 2026-10-24,
answering the web seat's THE_NEXT_ATTACK step 3 (c) and the SM seat's open question there ("whether W136's level-4 forms
have a direction of DR's shape with larger cusp coefficients at the band"). **0 of 19.**

## 1. The forms (`verification/cube_forms.py` → `cube_forms.json`, `cube_forms_run.txt`)

The frame's family group is Γ₄ = PSL(2, ℤ/4) acting by ρ′, the cube's rotations (the SM seat's W136; B1736). Its forms
are polynomials in v = (−θ₂², −θ₄², iθ₃²) = 2η³R, which transforms as ρ′ ⊗ χ_η⁶; a degree-d triplet P is a form in ρ′
when P(gv) = parity(g)^{d/2} g P(v) for the 24 signed permutation matrices g of determinant 1, and in ρ′ ⊗ sgn with one
more factor of the parity. Solved as a linear system over the monomials and counted on the null cone:

| weight | ρ′ (dimension) | ρ′ ⊗ sgn (dimension) | W136's table |
|---|---|---|---|
| 2 | 1: Y₂ = (v₂v₃, v₃v₁, v₁v₂) | 0 | 1, 0 |
| 4 | 1 | 1: v₁v₂v₃·v (R's direction) | 1, 1 |
| 6 | 2 | 1 | 2, 1 |
| 8 | 2 | 2 | 2, 2 |

**Directions at the band** (0.4375 + 2.1i):
- Every ρ′ generator is led by e₁ (ρ′(T)'s exponent-0 line): Y₂ (= −4iη·F₋₂, W136) has ∣e₁∣ 4.8 times its null part and
  the invariant 0.96; the weight-4 form 9.6 and 0.99. Far from null: as B1740 found for F₋₂, these lose the hierarchy.
- The ρ′ ⊗ sgn forms are led by a null line: weight 4 is R (invariant 5 × 10⁻¹⁵); **weight 6 is ∂R's direction — collinear
  to 2 × 10⁻¹⁶ at four τ (1.4 ≤ Im τ ≤ 3.6): the record's census Higgs is the family group's own weight-6 form**; weight 8
  is a two-dimensional space containing E₄R's direction and a new octic.
- **The weight-6 ρ′ space is span{F₆, F₋₆}** (the h(12, 1) pair of W143), to 4.2 × 10⁻⁸ and 0 at two τ (`cube_forms.py` part D); the two weight-8
  spaces are new (they match neither span{F₂₂, F₋₂} nor span{F₁₄, F₋₁₀}).

## 2. As Higgs pencils (post hoc, labelled; `verification/cube_pencils.py` → `cube_pencils_run.txt`)

Each two-dimensional space scanned as h = A + λB (λ fitted from thirteen starts, read S in every sector and conjugated,
c = 3) on B1742's 1 280 points, both horocycles, as B1743's pencils:

| space | reading | min χ²_nine | where | rows below 21.67 |
|---|---|---|---|---|
| ρ′, weight 6 (= span{F₆, F₋₆}) | S | 41.9 | (2/5, 3/10), 0.3125 + 3.30i, L_max | 0 |
| ρ′, weight 6 (= span{F₆, F₋₆}) | S̃ | 956.8 | (2/5, 4/5), 0.4375 + 3.00i, L₂ | 0 |
| ρ′, weight 8 | S | 42.7 | (2/5, 3/10), 0.6875 + 3.30i, L_max | 0 |
| ρ′, weight 8 | S̃ | 959.5 | (2/5, 4/5), 0.4375 + 3.00i, L₂ | 0 |
| ρ′ ⊗ sgn, weight 8 | S | 881.1 | (2/5, 0), 0.8125 + 2.00i, L₂ | 0 |
| ρ′ ⊗ sgn, weight 8 | S̃ | 47.5 | (2/5, 3/10), 0.4375 + 3.30i, L_max | 0 |

The best rows sit where B1743's pencils did ((2/5, 3/10), Im τ 3.3, L_max, about 42): the weight-6 ρ′ space gives B1743's F₆ ∣ F₋₆ value exactly, as its span identity says; the weight-8 spaces 42.7 and 47.5. No row below the bar.

## 3. What it means

- **The frame's family group places the record's Higgs:** R is its weight-4 twisted form and ∂R its weight-6 one; the
  untwisted forms are e₁-led and lose the hierarchy (B1740), their weight-6 space is the zero-free pair F₆, F₋₆.
- **No form of Γ₄ up to weight 8, alone or as a pencil with one complex number free, reaches the nine's target** on this
  grid. With B1743 (the record's pencils, 41.9 at best) and B1744 (the Higgs's own twist), the target (a nearly null Higgs
  with its invariant fixed near 0.017 and an e₁ admixture near 0.3) is not produced by anything the frame's own symmetry
  and the record's forms supply at these weights (P-357).
- **Scope:** weights up to 8; one Higgs for every sector; B1742's grid for §2.

## Seen first

`VERDICT topic-sweep /cube (group|forms|rotations)|Gamma_?4|Γ₄|PSL\(2, ?ℤ/4\)|level.4 forms|rho' ?x ?sgn|ρ′ ⊗ sgn/ (full text)`: 16 of 1526 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 13) [corrected 2026-10-24 at Review 70: the arc landed with the placeholder unfilled, which the seen-first gate did not catch (it now does); the sweep run at the review, its count including later arcs].
Bearing on it: B1736, B1730, B1691, B1740, B1743, B1744; the SM seat's W136 and W143; the web seat's cube_forms_count.
**Literature:** modular-S₄ (Γ₄) flavour models' forms (standard).

## Disclosed

- Post hoc: the target (B1743) was known before §2 ran; the three spaces were fixed by the count before any was compared
  with data. The weight-8 twisted space was first scanned in the audit room (`audit/verify_p357/cube_pencil.py`, best
  47.5), and rerun here with the other two.
- `cube_pencils.py` writes `cube_pencils.json` (every row), not committed; `cube_pencils_run.txt` carries the summary.

## Files

- `verification/cube_forms.py` → `cube_forms.json`, `cube_forms_run.txt`; `verification/cube_pencils.py` → `cube_pencils_run.txt`.
- The lock: `tests/test_b1746_the_cube_groups_forms_as_the_higgs.py`.
