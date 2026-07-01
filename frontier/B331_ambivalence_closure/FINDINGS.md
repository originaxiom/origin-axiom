# B331 — the SL(2,ℂ) "complex escape" is closed at its root: the generation element is elliptic

**Status: banked (frontier). Verify-don't-trust on Chat-1's meditation + self-correction (2026-07-01). Firewalled;
nothing to `CLAIMS.md`.** Chat-1's meditation named the wall precisely — *structure lives in real invariants (traces,
volumes, magnitudes); values live in phases* — and proposed an escape: the geometric holonomy is in **`SL(2,ℂ)`**, not
`SU(2)`; holomorphic (non-self-dual) reps needn't pair `ω, ω²`, so a holomorphic McKay lift of the Riley holonomy might
give `n₁≠n₂` (Level 3). Chat-1 then self-corrected (every route gives `n₁=n₂`). This probe **verifies the closure and
supplies the clean reason** — sharper than both Chat-1's "center/non-center" heuristic and B329's σ-stability framing.

## The clean reason — ellipticity, not self-duality
The generation-permuting element `g = [[0,−1],[1,−1]]` (the Riley ℤ/3 conjugator) is **order 3, with eigenvalue set
`{ω, ω²}`** — which is **inverse-closed**, so `g ~ g⁻¹`. For *any* finite-order element, `χ_R(g⁻¹) = conj(χ_R(g))`;
combined with `g ~ g⁻¹` this forces **`χ_27(g) ∈ ℝ` → `n₁ = n₂`, in every representation — compact or holomorphic.**

**Verified:** the holomorphic principal `SL(2,ℂ)` lift gives `χ_27(g) = 0`, **identical** to the compact `SU(2)` value
`0`. *Holomorphicity is invisible at `g`* — because `g` is **elliptic** (finite order, unit-circle eigenvalues), its
holomorphic and compact characters coincide. The `SL(2,ℂ)`-vs-`SU(2)` distinction only bites on **loxodromic**
(infinite-order) elements — which carry the **volume / Chern–Simons** data (real magnitudes = *structure*), never the
finite ℤ/3 that would have to split the **phases**. The complexity of the holonomy is real (Eisenstein `ω` from birth),
but it is spent on structure; the one finite symmetry that could split the generations cannot see it.

## Correction (verify-don't-trust on Chat-1)
Chat-1's "center → uniform, non-center → real character, either way `n₁=n₂`" is **heuristic and imprecise**: the
**central** order-3 element `z` acts on the 27 by the scalar `ω` (triality), so `χ_27(z) = 27ω` — **complex**. "Every
order-3 element gives a real character" is therefore **false**; `z` is *not* `~ z⁻¹`. The real content is the
**ambivalence of the specific, non-central, elliptic** generation element `g`, not a blanket order-3 property.

## Scope (honest)
This closes the escape for **any lift factoring through `SL(2,ℂ) → E₆`** — which **includes the arithmetically-relevant
one** (the Riley holonomy *is* an `SL(2,ℂ)` representation, `ρ: π₁(4₁) → SL(2,ℤ[ω])`). So **Chat-1's own proposed attack
object — the holomorphic McKay lift of the Riley holonomy — gives `n₁=n₂`.** The fully-general "*all* finite `2T↪E₆`
embeddings give `n₁=n₂`" is still **not** a theorem (the open computable target H103); B329 verified two embeddings, this
closes the `SL(2,ℂ)`-factoring family via one structural fact. **Level 4 is confirmed for the object's actual lift.**

## The meditation, affirmed (firewalled)
The real/complex, magnitude/phase framing is the sharpest statement of the wall to date and is *correct*: the object
forces structure through real invariants and leaves every value as an unbroken (Galois/phase) symmetry (`../speculations/S046`,
B330). The deepest point — *the hierarchy requires **relations** (Level 4, the object seen from outside via its
arithmetic neighbours), not the single object (Levels 1–3)* — is the honest structural finding, and it matches K020's
four-level framework and B326's finite congruence torsion (texture, not magnitude). The wall did not move; it was named
to its cause.

## The firewall (held)
`n₁=n₂` decides that the hierarchy is Level 4; it produces no value. Nothing to `CLAIMS.md`.

## The fence
Exact `SL(2,ℂ)` / cyclotomic character computation (sympy). No physics values. Nothing to `CLAIMS.md`.

`ambivalence_closure.py` (pyenv) · `tests/test_b331_ambivalence_closure.py`. Related: **B329** (both embeddings,
sharpened here), **B327** (self-duality reduction), **B326** (the Level-4 congruence torsion — where the hierarchy now
lives), **S046** (value-at-the-seam), **OPEN_PROBLEMS.md** gate B. Lit: elementary — a finite-order element conjugate to
its inverse has real character in every representation.
