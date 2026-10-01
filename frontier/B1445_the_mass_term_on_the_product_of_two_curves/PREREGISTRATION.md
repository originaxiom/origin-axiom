# B1445 PREREGISTRATION — THE MASS TERM ON THE PRODUCT OF TWO CURVES: is the frame's coupling the coefficient of an actual mass term when the Higgs character's curve is switched on?

**Sealed 2026-10-01, before the bidoublet is computed on any level of the population below. Seat: cc (main).
Occasion: B1444 found that every background is the reducible end of a curve of flat connections and that moving
along it is not electroweak breaking — SL(2)_β commutes with the Standard Model's gauge group. Lead L236 (b) asked
for the electroweak direction: the Higgs character's. This arc sets it up.**

## 0. The quantifier (P0)

For every level of the population and every case (ℓ, η, A₁) selected in §2: the rank-four module
ρ_ℓ(e₁) ⊗ ρ_η(e₂) ⊗ a on the product of the periodic curves of ℓ and of η, and the quadratic form of its torsion at
e₁ = e₂ = 0. The scope sentence names no level.

## 1. The objects

- The Higgs sectors of the frame are singlets of SL(2)_β, so the SL(2) of a Higgs character η commutes with
  SL(2)_β, and a sector doublet joined by η to another is a bidoublet of SL(2)_β × SL(2)_η. For two non-trivial characters ℓ, η
  of a level, with η ≠ ℓ^±1, the tensor product of the two periodic curves of B1444 is a
  two-parameter family of flat connections of the level: x ↦ a(x)·ρ_ℓ(x) ⊗ ρ_η(x), y likewise, t ↦ T_ℓ ⊗ T_η, with
  a = A₁/(v_ℓ v_η). That it is a module is asserted on every evaluation.
- At e₁ = e₂ = 0 it is the sum of four characters A₁, A₂ = A₁/ℓ, A₃ = A₁/η, A₄ = A₁/(ℓη). With
  aᵢ = s(Aᵢ) − s(ℓ) and bᵢ = s(Aᵢ) − s(η), first-order deformation theory (the derivative of the monodromy on the
  fibre's cohomology is the cup product with the two extension classes; the four lines form a square with ℓ-edges
  1–2, 3–4 and η-edges 1–3, 2–4) gives

      τ = e₁²·a₁a₂a₃a₄ + e₂²·b₁b₂b₃b₄ − e₁e₂·(a₁b₂a₄b₃ + b₁a₃b₄a₂) + (third order).

- **The frame's couplings.** For a background with extension character ℓ and a coupling (A, B) of up, down, lepton
  or neutrino type, η = α_A β_B and A₁ = α_A; then A₂ = β_A, A₃ = β_B⁻¹, A₄ = α_B⁻¹. On a background of sign + the
  firing conditions are a₁ = a₄ = 0 and then b₁ = b₄ = s(ℓ) − s(η) = Y, B1438's coupling; so the prediction reads
  τ = Y²·e₂·(e₂ b₂b₃ − e₁ a₂a₃). On a background of sign − the roles of 1, 4 and 2, 3 are exchanged.

## 2. The population (fixed before the run)

- **FRAME:** the sixteen levels −LR 3, +LLR 3, +LRR 3, −LLRLR 1, −LRLRR 1, −LLLRLR 1, −LRLRRR 1, +LLLRR 2, −LLLRR 2,
  +LLRRR 2, −LLRRR 2, +LLLLLR 2, −LLLLLR 2, +LRRRRR 2, −LRRRRR 2, +LR 4: every level with fibre torsion at most 64
  among the word states to length six and their levels to four that carries a generation-shaped background with
  an extension character of order above two, except the control (−LR 4 is the same level as +LR 4 and is listed once). On each, every coupling of every background with
  η non-trivial, η ≠ ℓ^±1 and no trivial character in the bidoublet; up to 24 distinct (ℓ, η, A₁) per
  level, spread evenly over the sorted list.
- **FREE:** the eight levels +LR 2, −LR 1, −LLR 2, −LLLR 1, +LLRLR 1, −LLLRR 1, +LLRLRR 1, −LLRLRR 1, up to eight
  triples (ℓ, η, A₁) each, spread over the characters, with no reference to the frame.

Instrument `verification/mass_term.py` on B1444's sealed `curve_engine.py`; reader `verification/read_mass.py`
(run twice on the control before the seal, identical output).

## 3. What has been seen before the seal (disclosed in full)

- **One free triple** on the root's three-fold cover (ℓ = (2, 1), η = (1, 0)): twelve values of A₁, the predicted
  form on each (8, 8, −16 where it is non-zero).
- **Characters of order two have curves.** B1444 took an extension character of order two to sit at a node of
  κ = 2. It does not: its square root has order four and is a smooth point; the curve is one of the lines of
  B1444's decomposition, the law of B1444 holds on it (three characters of the root's three-fold cover, 42
  sectors), and it is of filling type with the meridian trivial. B1444's text is corrected in its own landing.
- **The control**, the root's three-fold cover through the sealed instrument and reader: 48 backgrounds, all four
  couplings reachable on all 48, 96 distinct cases, 24 run, 24 agree. Up: Y² = 4 and τ = −16·e₁e₂. Down, lepton
  and neutrino: Y² = 1 and τ = −4·e₁e₂ + e₂².
- The sizes of §2: which levels carry backgrounds and extension characters of order above two (from slopes).
- **Exploration at the boundary-parabolic points of the control level**, not predicted on here and owed to a later
  sealed arc: at the complete-cusp point of a background's curve on the root's three-fold cover the generation
  sector's torsion is −(√5 + √−3); the bidoublet's class index at the doubly-parabolic points is zero, computed
  by singular values at 60 digits; with the Higgs at its complete point and the extension at its end the
  bidoublet's torsion is 2 ± 2√−15 for the up coupling and 16 for the down, lepton and neutrino couplings.
- **Not seen:** the list of cases on any level of §2, which couplings are reachable there, or any bidoublet.

## 4. Sealed predictions (each can come out either way)

| | prediction | prior |
|---|---|---|
| Q1 | On every case followed, the three coefficients of the quadratic form agree with the prediction to 10⁻⁶ (relative, absolute below one). | 80% |
| Q2 | On every frame case: no e₁² term; the e₁e₂ coefficient is −Y² times the product of the two unmatched differences to ℓ; the e₂² coefficient is Y² times the product of the two other differences to η. | 85% |
| Q3 | Some background of the frame population has an up-type and a down-type (down or lepton) coupling both reachable. | 80% |
| Q4 | Some case with a slope outside (1/60)ℤ is tested and agrees. | 75% |

A case whose curves the instrument cannot follow is reported and counted, not dropped.

## 5. What each outcome would mean (written before the data)

- **Q1, Q2 YES:** the coupling of B1438 is the coefficient of a mass term on actual flat connections: with the
  Higgs character's curve switched on, the two zero modes of a coupled pair are lifted with torsion
  −Y²·a₂a₃·e₁e₂ — the Yukawa squared, times the Higgs value, times the extension parameter. The Higgs value then
  has the same kind of object as B1444 gave the extension: a position on a curve.
- **Q1 NO:** the hopping form is wrong somewhere (a sign for the states of sign −, or a normalisation), and the
  statement is withdrawn to the control.
- **Q3** decides whether a ratio of an up-type to a down-type mass term is available within one background by this
  method on levels other than the control.
- None of the outcomes is a value of the Standard Model: the two parameters e₁, e₂ are positions on curves that
  nothing computed selects, torsion is not a mass, and the members of a deck orbit are not distinguished. 0 of 19.

## 6. Not in this arc

Third-order terms; the exact function on the product of curves beyond the quadratic form; what selects
the positions.

## 7. Hashes at seal

See `ARTIFACT_HASHES.txt`.
