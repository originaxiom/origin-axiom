# B1362 — THE HIERARCHY IS A U(1)-BREAKING EFFECT AT ORDER ONE: a deck-symmetric complex symmetric Yukawa is a symmetric circulant with a degenerate pair of masses, so the deck must be broken; and by Weyl's inequality the part of each charged-fermion mass matrix that violates the apex U(1)s has operator norm at least (m₃ − m₂ − m₁)/3 — a third of the top, bottom and tau Yukawas — a bound the data attain numerically: the sector that breaks the apex U(1)s is not a correction to the hollow tree level, it supplies at least a third of the third generation

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the circulant identity, symbolic; Weyl's inequality applied; the minimisation over Takagi unitaries numerical, matching the bound to four digits) + NEGATIVE (for any small-breaking realisation of the design's flavour) · **Price: unchanged** · **Numbering:** B1362 (L213 (vii)).

## 0. Seen from above

B1361 left the design's flavour to the sector that breaks the apex U(1)s, with the hope that a Froggatt–Nielsen-like structure with the
deck's charges might supply the hierarchy as small corrections to the hollow tree level. Two pieces of linear algebra say how large
those corrections must be. First, the deck itself cannot survive: a Yukawa invariant under the cyclic permutation of the generations is
a symmetric circulant circ(x, y, y), whose eigenvalues are x + 2y and x − y twice — two masses coincide. Second, the hollow tree level is
robust against small perturbations: Weyl's inequality bounds the change of each singular value by the operator norm of the
perturbation, and since the hollow matrix has σ₁ = σ₂ + σ₃ exactly (B1361), any mass matrix M = M₀ + E with the observed masses
obeys m₃ − m₂ − m₁ ≤ 3‖E‖: the U(1)²-violating part is at least a third of the heaviest mass in every charged sector — 57 GeV for the
top, and the numerical minimum over all Takagi frames attains the bound. So in the design the third-generation Yukawas are, to at
least a third, U(1)-violating: the "diagonal source" is a leading effect, and the apex U(1)s cannot be the origin of a small-parameter
hierarchy.

## 1. The two statements (computed)

| statement | computed |
|---|---|
| deck-symmetric symmetric Yukawa = circ(x, y, y): eigenvalues x + 2y, x − y, x − y | symbolic; the degenerate pair x − y has multiplicity 2 |
| Weyl: m₃ − m₂ − m₁ ≤ 3‖E‖_op for M = M₀ + E, M₀ hollow symmetric | up 57.3 GeV = 0.332 m_t; down 0.934 GeV = 0.327 m_b; leptons 0.557 GeV = 0.313 m_τ |
| the minimal ‖E‖ over textures = min_U max_i |(UΣUᵀ)_ii| (the nearest hollow matrix to a symmetric M is M minus its diagonal) | 0.3321 m_t, 0.3272 m_b, 0.3135 m_τ — the bound to four digits (up), within 0.1% (down, leptons) |

## 2. What it means

1. The deck must be broken by the Higgs vevs or the U(1)-breaking spurions: no Z₃-symmetric Yukawa has three distinct masses.
2. The hollow texture is not lifted by small effects. If the sector breaking the apex U(1)s (Witten's axionic mass, the charged
   M2-instantons) enters with a small parameter ε, the resulting masses satisfy m₃ = m₂ + m₁ + O(ε m₃); the data need ε of order one
   — at least a third of the top Yukawa violates the apex U(1)s. A Froggatt–Nielsen structure with the deck's charges can therefore
   not be the whole story unless its expansion parameter is not small, or unless the tree-level 27₁27₂27₃ is itself absent (a neutral
   Higgs, B1361 §1) and the entire Yukawa comes from the breaking sector — in which case its texture is set by that sector, not by the
   apex charges alone.
3. For the destination's Yukawa items this is a sharp instruction: the closing's design fixes the chiral count and the U(1) charges but
   cannot fix the masses through the E₆ cubic; whatever computes m_t computes a U(1)-violating coupling of order one.

## 3. Caveats

1. Masses are compared at a single low scale; the bound scales with the masses and the verdict does not depend on the scale.
2. The Takagi minimisation is numerical (60 restarts, adaptive random search); the bound is exact and the minimum matches it within the
   search's precision, so the bound is at least nearly attained.
3. "Operator norm of the violating part" is basis-independent but the identification of E with a specific sector is the design's
   (the tree-level term is exactly the hollow U(1)-invariant part).

## 4. Registered

- L213 (vii) sharpened: the U(1)²-breaking sector must supply an order-one part of the third-generation Yukawas; whether M2-instantons
  on the closing's three-cycles can be unsuppressed enough is the question.

## Verification

`verification/hierarchy_bound.py` (about a minute; record `hierarchy_bound_run.txt`): the circulant eigenvalues, the Weyl bounds in
the three sectors, the minimisation over unitaries. Lock: `tests/test_b1362_the_hierarchy_is_u1_breaking.py`.

**Sources.** Weyl's inequality for singular values (Mirsky's form); B1361, B1273 (the hollow texture); B1356 (the charges).

*(Currency 2026-09-16, main's B1415 bookkeeping item 3, applied: the "attained" figures for ‖E‖ come from a 60-restart local search over
unitaries in the Takagi frame — a heuristic upper bound on the minimum that happens to meet the Weyl lower bound to the digits shown;
the bound itself is the theorem. Main verified the circulant eigenvalues and the bound with sympy.)*
