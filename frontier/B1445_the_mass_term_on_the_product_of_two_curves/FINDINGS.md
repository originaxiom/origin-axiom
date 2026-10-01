# B1445 — THE MASS TERM ON THE PRODUCT OF TWO CURVES: with the Higgs character's curve switched on, a coupled pair of the frame's sectors is lifted with torsion equal to the banked coupling squared, times the Higgs value, times the extension parameter

cc, 2026-10-01. B1444 found that every background is the reducible end of a curve of flat connections, and that
moving along that curve is not electroweak breaking, because SL(2)_β commutes with the Standard Model's gauge
group. The electroweak direction is the Higgs character's. This arc sets it up and tests it under seal.
**Verdict: PROVED** (one theorem with proof; four sealed predictions on 24 untouched levels, all held).

## 1. The two-parameter family

The Higgs sectors of the frame are singlets of SL(2)_β, so the SL(2) of a Higgs character η commutes with SL(2)_β.
For two non-trivial characters ℓ, η of a level with η ≠ ℓ^±1, the tensor product of their periodic curves (B1444)

    x ↦ a(x)·ρ_ℓ(x) ⊗ ρ_η(x),   y likewise,   t ↦ T_ℓ ⊗ T_η,      a = A₁ / (v_ℓ v_η),

is a module of the level for every pair of points (asserted on every evaluation): a two-parameter family of flat
connections with parameters e₁ = 2 − κ_ℓ and e₂ = 2 − κ_η. A doublet of SL(2)_β joined by η to another is a
**bidoublet** of it. At e₁ = e₂ = 0 it is the sum of four characters

    A₁,   A₂ = A₁/ℓ,   A₃ = A₁/η,   A₄ = A₁/(ℓη).

## 2. The theorem

**Theorem C.** With aᵢ = s(Aᵢ) − s(ℓ) and bᵢ = s(Aᵢ) − s(η), the torsion τ = det(1 − Φ* | H¹(F; V)) of the bidoublet is

    τ = (e₁·a₂a₃ − e₂·b₂b₃)·(e₁·a₁a₄ − e₂·b₁b₄)  to second order, that is

    τ = e₁²·a₁a₂a₃a₄ + e₂²·b₁b₂b₃b₄ − e₁e₂·(a₁b₂a₄b₃ + b₁a₃b₄a₂) + (third order).

*Proof.* At the reducible point H¹(F; V) is four lines, one for each character, on which Φ* is the identity. By the
argument of B1444's Theorem B the derivative of 1 − Φ* is the cup product with the two extension classes: the four
lines are the vertices of a square, with ℓ-edges 1–2 and 3–4 carrying δ₁ and the slope difference to ℓ of the
source, and η-edges 1–3 and 2–4 carrying δ₂ and the slope difference to η of the source (δᵢ² ∝ eᵢ). The square is
bipartite ({1, 4} against {2, 3}), so the determinant of the hopping matrix is the product of the determinants of
its two off-diagonal blocks, which is the first line; odd orders vanish because τ is a function on the product of
curves. The universal sign is the one fixed in B1444. ∎

**The frame's couplings.** For a background with extension character ℓ and a coupling (A, B) of up, down, lepton
or neutrino type, put η = α_A β_B and A₁ = α_A; then A₂ = β_A, A₃ = β_B⁻¹, A₄ = α_B⁻¹. On a background of sign + the
firing conditions are a₁ = a₄ = 0, and then b₁ = b₄ = s(ℓ) − s(η) = Y, B1438's coupling. So

    τ = Y²·e₂·(e₂·b₂b₃ − e₁·a₂a₃) + (third order),

and on a background of sign − the same with the roles of 1, 4 and 2, 3 exchanged. **The coupling of B1438 is the
coefficient of a mass term on actual flat connections:** the two zero modes of a coupled pair are lifted as soon as
the Higgs character's curve is entered, at a rate Y² times the Higgs value, and the term that survives when the
extension is switched on is −Y²·a₂a₃·e₁e₂ — coupling squared, times Higgs value, times extension parameter.

## 3. The sealed run (seal `d3b50c0f`, pushed to both remotes before the run)

24 levels none of which had been run: 16 carrying generation-shaped backgrounds (752 backgrounds, 352 distinct
cases run of the frame's couplings, at most 24 per level) and 8 without (53 free triples). All curves were
followed; none was dropped.

| | prediction | prior | result |
|---|---|---|---|
| Q1 | the three coefficients of the quadratic form agree with the prediction to 10⁻⁶ | 80% | **YES, 405 of 405** |
| Q2 | frame cases: no e₁² term; e₁e₂ coefficient −Y²·(the two unmatched differences to ℓ); e₂² coefficient Y²·(the two other differences to η) | 85% | **YES, 352 of 352** |
| Q3 | some background has an up-type and a down-type coupling both reachable | 80% | **YES, 432 backgrounds** |
| Q4 | some case with a slope outside (1/60)ℤ agrees | 75% | **YES, 365 cases** |

With the control (the root's three-fold cover, 24 of 24): 429 cases, no exception. The mass term is non-zero
(Y ≠ 0 and both unmatched differences non-zero) on 336 of the 352 frame cases.

## 4. The couplings, level by level (`mass_population_summary.json`)

Y² and the coefficient of e₁e₂ in τ, for the cases run:

| level | up | down = lepton | neutrino |
|---|---|---|---|
| +LR 3 (s961, control) | Y² = 4; −16 | Y² = 1; −4 | Y² = 1; −4 |
| −LR 3 | 16/5; −4 | 16/5; −8 | does not fire |
| +LLR 3, +LRR 3 | 5φ^±2; −25 | η = ℓ^±1 | — |
| −LLRLR 1, −LRLRR 1 | 9/4; −4 | **0** | — |
| −LLLRLR 1, −LRLRRR 1 | (9/5)φ^±2; −5φ^±2 | η = ℓ^±1 | — |
| ±LLLRR 2, ±LLRRR 2 | (9/5)φ^±4; −1 | (9/5)φ^±4; −3φ^∓2 (−1.146, −7.854) | — |
| ±LLLLLR 2, ±LRRRRR 2 | (9/5)φ^±2 | (9/5)φ^±2 | — |
| +LR 4 | (9/5)φ^±4 | 9 or (9/5)φ⁴ | — |

(numerical record in the summary; the closed forms in ℚ(√5) are read off the decimals and are not separately
certified.) Down and lepton agree on every level, as B1438 proved. On several levels the backgrounds fall into two
classes whose couplings differ by a power of the golden ratio: on the root's four-fold cover the up coupling is
(3/√5)φ^−2 on one class and (3/√5)φ^2 on the other, a ratio of φ⁴ ≈ 6.85.

**Two things the run showed that were not predicted on:**

- **On 624 couplings the Higgs character is the extension character or its inverse** (η = ℓ^±1), on eleven of the
  sixteen levels. There the two SL(2)s are the same and the tensor product is not a bidoublet; those couplings are
  not tested here. On the levels of the root (+LR 3, +LR 4) it does not happen.
- **The neutrino coupling** is reachable only where the ν^c sector fires with the generation's sign: on the control
  level throughout, and on none of the 720 neutrino couplings of the population.

## 5. What it means, and the fence

- **A Higgs value now has the same kind of object as the extension had in B1444:** a position on a curve of flat
  connections, here the curve of the Higgs character, and the frame's coupling is the rate at which that position
  lifts the generation. Before this arc the coupling was a number attached to a triple product of classes at a
  non-semisimple point; it is now checked on irreducible flat connections of the level.
- **The mass term needs both parameters.** With the extension at its end (e₁ = 0) the term is Y²·b₂b₃·e₂², which
  vanishes when one of the partner characters has the Higgs character's slope — on the root's three-fold cover
  that is the up coupling, whose mass term is −16·e₁e₂ and nothing else at this order.
- **Imported expectation, stated separately:** that there is one Higgs. The frame has a Higgs character for each
  coupling type of each background, with its own curve and its own parameter; nothing here relates the up-type
  value to the down-type one.
- **The fence:** torsion is not a mass; the parameters e₁, e₂ are positions that nothing computed here selects; the
  three members of a deck orbit have the same quadratic form; the reading of SL(2)_η as the electroweak direction
  rests on the Higgs sector's charges in the frame (B1432), not on a computation here. **0 of 19.**

## 6. Correction carried from B1444

Characters of order two are smooth points of κ = 2 and have curves (B1444 §10). This arc uses them: on the root's
three-fold cover the down, lepton and neutrino Higgs characters have order two, and their couplings are reachable
only because of that.

## 7. Not computed (lead L237)

- The couplings with η = ℓ^±1 (one SL(2), not two).
- The third-order terms and the exact function on the product of curves.
- The boundary-parabolic points of the product, where the parameters are not free. Seen in exploration on the
  control level and disclosed in the preregistration (the generation sector's torsion −(√5 + √−3) at the complete
  cusp; the bidoublet's class index zero at the doubly-parabolic points; torsion 2 ± 2√−15 for the up coupling and
  16 for the others with the Higgs at its complete point). Owed to the next arc.
- Whether a second member's Higgs can be switched on along the first's curve: what tells the members of a deck
  orbit apart.

## Verification

`verification/mass_term.py` (the bidoublet, the fit of the quadratic form, the population) on B1444's sealed
`curve_engine.py`; `read_mass.py`; records `mass_frame_NN.json`, `mass_free_NN.json`, `mass_population_summary.json`,
the control's `mass_control_+LR_3.json`. Lock: `tests/test_b1445_mass_term.py`.
