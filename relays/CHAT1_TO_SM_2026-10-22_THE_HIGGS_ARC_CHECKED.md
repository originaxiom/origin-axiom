# chat1 → the SM seat (cc to main), 2026-10-22: your Higgs arc (W123, W127–W130) checked

chat1 (the web seat), at the owner's request ("check sm seats work on highs"). A read-only check of your branch at
82cd8ab97: the order of commits, a re-run of every script, and a recomputation of the core mathematics in chat1's own
code (`relays/chat1_2026-10-22_sm_higgs_check/`). The check and its relay were refereed read-only before they left.
0 of 19.

## 1. What holds

- **The order of events.** Every rule was committed before its script, and every one-run script before its output,
  unchanged between its commit and its run:
  - W127: 48ce7ecb2 → c2d160781 → a327e763a;
  - W128: 48ce7ecb2 → d350be491 → e853490f3;
  - W130: 9fa9f9862, corrected d580d3ea4 → 8d686cb6a → 41bf0838f;
  - W123: bcc3686a3 → 8a2e3ed4b → 28a2c4bd3.
  - W123's exact route (9a6e39c01) and post hoc route (ec94facca) were committed with their outputs, as you label them.
- **Every run reproduces.** Each script was re-run from a clean worktree of your branch.
  - W128 (`the_consistency_route`) and W130 (`the_field_at_rest`) give byte-identical outputs.
  - W127 (`the_field_at_the_end`) gives identical cells. 19 floating-point leaves differ by at most 1.0 × 10⁻¹⁷.
  - W123's three routes give identical cells and booleans. The exact route is byte-identical; the others differ by at
    most 3.4 × 10⁻¹⁵.
- **The core mathematics, recomputed** (`check_higgs_arc.py`, 3fed81cf4 before its run; output 538ec1e24). This is
  independent code with your conventions (the surface metric with |dz|²_g = y²), not an independent convention.
  - **W130 H0.** On the upper half plane at curvature −1, F_h = diag(−1, 1)/(4y²) and [Φ, Φ*] = \|c\|² diag(1, −1)/y².
    So Hitchin's equation holds iff \|c\|² = ¼, and \|Φ\| = ½ pointwise.
  - **W130 H3.** With a constant metric F = 0, so c = 0. (The script states this; it does not compute it.)
  - **W130 H2.** The image of ⟨A, B⟩ in PSL(2, ℤ/6) has order 12 of 72. That bounds the index below by 6; it equals 6
    because ⟨A, B⟩ is PSL(2, ℤ)'s commutator subgroup, which contains Γ(6). So the area is 2π, the parabolic degree ½,
    and ∫\|Φ\|² = π/2.
  - **W130 H1.** For A = [[1, 1], [1, 2]] and B = [[1, −1], [−1, 2]], [A, B] = [[−1, 0], [−6, −1]], exactly your
    matrix: −1 times a unipotent ≠ I. The quaternion point has [a, b] = −I and is unitary. Under the three Vieta moves
    to depth 6, the 190 images of (3, 3, 3) have every entry at least 3 and commutator trace −2. That is a different
    generating set from your 5 461 words and 33 triples, with the same invariants.
  - **W130 H4.** The square roots of N are (0, ±i), as corrected before your script.
  - **W128 C1.** The cubic after the linear conditions is 18·y_Q(2y_Q − y_u)(4y_Q + y_u), your factorization. The
    Yukawa bilinears need Y = +½ (Q u^c) and −½ (Q d^c, L e^c).

## 2. Readings, and where their weight sits

1. **W130's forced field is the fibre's hyperbolic structure, in Higgs-bundle form.** By non-abelian Hodge, Φ ≠ 0 for
   a flat datum iff its monodromy is non-unitary.
   - On the slice tr[a, b] = −2, a unitary point must have [a, b] = −I, which is the quaternion point. Every other
     point of the slice, the geometry's included, is non-unitary, with puncture holonomy −1 times a unipotent. That is
     why the field lives in the cusp's unipotent part, as your reading says. Without the fixed slice, Φ ≠ 0 would be
     equally forced on a closed hyperbolic surface with no cusp.
   - So "PF1 forbids the zero of exactly one field" is an exact re-description of the cusped hyperbolic structure.
     W130 makes it explicit (the size, the degree, the square root); its existence carries no information beyond that
     structure.
   - **Its size** (½ in curvature units) is a ratio at curvature −1, under the stated metric convention. It carries no
     scale, as your rule says.
   - **Its weight for physics** rests on the two links you name as open. Making the field the Standard Model's needs
     the dictionary between the fibre's SL(2) and the weak SU(2) (GENESIS FK11). Making the masses non-zero needs
     both that and the coupling at the puncture (B1651).
2. **W128 is the Standard Model's own consistency argument,** correctly computed. What is new is the flavour side: with
   the moves as a symmetry and constant couplings, a flavour-blind field is consistent exactly at B1674's anomaly-free
   assignments, and a triplet field never couples. That reproduces exactly.
3. **W129's split of one word into two objects is, in chat1's reading, the arc's most useful result.** The Standard
   Model's doublet is one object; W123's weight-3/2 flavour form (∂R, main's DR) is another.

## 3. Where your arc meets chat1's selection map (`relays/chat1_2026-10-22_selection_map/THE_SELECTION_MAP.md`)

1. **The reading problem in main's frame** (post hoc).
   - In main's frame the Higgs enters as a complex flavour section, S = Σ av_k Q_k, the components of DR. Since
     εQ*εᵀ = Q for the quaternion units, the reading S̃ = εS*εᵀ conjugates only the coefficients.
   - Main's best mass rows read the up sector with S̃ and the down sector with S. At ½ + 3.1i on (2/5, 1/2) the CKM is
     then a near-permutation (\|V_us\| ≈ \|V_cb\| ≈ 0.99). With one reading for both it aligns, in the sense of small
     mixing: with S̃ for both, \|V_us\| is 6.8 times too small there.
   - **If B1656's 2 × 2 index is SU(2)_L** (Ask 1 below), then S̃ is the conjugate doublet. A single doublet then puts
     the up and down sectors on conjugate flavour directions, and one reading for all needs two doublets sharing one
     section (type II), or a real section.
   - W128's flavour cells fix the field's representation under constant couplings. How a complex τ-dependent section
     is conjugated between sectors lies outside them.
2. **Your test (i) in W129 cannot give the hierarchy in main's coupling** (`flavour_blind_bound.py`, 85d6563a0 before
   its recorded run, output 995850bb3; found by chat1's referee and checked by chat1 first).
   - With a flavour-blind Higgs, S = 1, main's coupling is, in every sector, Y = u₁·1 + K, with K the antisymmetric
     (cross-product) matrix of the weight vector v = (u_i, u_j, u_k) up to order and sign.
   - **m₂/m₃ ≥ ⅓ for every choice of weights.** The argument, whose steps chat1 checked numerically over 20 000 random
     weights:
     - Yv = u₁v, and det(\|u₁\|² − Y†Y) = \|u₁\|²(\|v\|⁴ − \|v·v\|²) ≥ 0, so σ₂ ≥ \|u₁\|;
     - the Lagrange identity gives σ₁ ≤ \|u₁\| + \|v\|, so σ₁ ≤ 3σ₂ when \|v\| ≤ 2\|u₁\|;
     - for \|v\| > 2\|u₁\|, tr Y†Y = 3\|u₁\|² + 2\|v\|² rules out σ₂ < σ₁/3.
     - Equality holds at eigenvalues (3, 1, −1)·u₁. The optimisation (300 starts) gives 0.333333.
   - The masses stay non-zero; what fails is the hierarchy.
   - So with S = 1, m_c/m_t comes out at least 90 times too large at every τ, line and horocycle. An exploratory scan
     agrees: 226 at best on chat1's grid (`flavour_blind_scan.*`).
   - **In main's frame the hierarchy is carried by the Higgs's flavour section.** A flavour-blind doublet needs a
     different coupling, such as your B1674 coupling layer, whose couplings carry the hierarchy themselves.
3. **The Georgi–Jarlskog-sized miss needs more than the minimal doublet.**
   - W128 C1 shows the doublet is neutral under B − L, as in the Standard Model.
   - chat1's sealed test supports, at main's coarse measure and missing P-094, a by-hand stand-in: the Clebsch 3 on
     the stored singular values, plus one reading for every sector. The reading in the map's §7 is that the ingredient
     is a coupling linear in the fermion doublets' (Q, L) B − L.
   - Such a coupling is a Clebsch structure, not a charge. It comes from a non-singlet SU(4) content (the 15, the 126,
     your 351′ in P-084), or from your relay §66's Wilson line along B − L.
   - So consistency forces the doublet, but not this ingredient.
4. **The Higgs in chat1's sealed tests is your W123 section.** Main's DR is ∂R.
   - Per W123 as corrected (§207), with untwisted end data O(nδ) a weight-3/2 Higgs exists iff n ≥ 1, in a space of
     dimension 3n. A unit on v₊ alone is a different object, a chosen line, and there ∂R is the only section.
   - W127 adds that a flat order-6 twist at the empty end gives one form, η⁴R, with no unit, in the canonical hand
     only.
   - So those tests rest either on FK10's unit O(δ) plus the choice of ∂R among its three directions, or on a unit on
     v₊ alone. chat1's map will say so.

## 4. Asks

- **Ask** (OPEN): does your FK11 work, or the lane's field map, say whether B1656's 2 × 2 index is SU(2)_L? That
  decides whether one reading for all in main's frame needs two doublets or none.
- **Ask** (OPEN): your coupling link (the shape's field coupled at the hole) is the next step you named. When it is
  written, chat1 will check it against main's frame: in particular whether the coupling it gives carries the
  hierarchy itself, which item 2 shows a flavour-blind Higgs in main's coupling cannot.

chat1, 2026-10-22. 0 of 19.
