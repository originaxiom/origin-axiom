# B326 — The generation ℤ/3-breaking is *finite congruence torsion*, not transcendental (Chat-2 handoff, verified)

**Status: banked (frontier). Verify-don't-trust on the Chat-2 → CC handoff (2026-07-01). Firewalled; nothing to
`CLAIMS.md`.** Chat-2 pushed the mass-hierarchy bottleneck and — after catching three of its own over-reaches — landed a
clean, object-specific, literature-confirmed result about *where* the generation ℤ/3 breaking lives. This seat verified
the load-bearing computation two independent ways (SnapPy 3.3.2 **and** the exact Alexander module) before banking.

## The claim (Chat-2, ranked #1 for CC)
The generation ℤ/3-breaking is controlled by **finite congruence torsion**, not a free continuous / transcendental
parameter:
- `H₁(3-fold cyclic cover of 4₁) = ℤ ⊕ ℤ/4 ⊕ ℤ/4`;
- the deck `ℤ/3` acts on the torsion `(ℤ/4)²` as an order-3 element of `GL(2,ℤ/4)` with characteristic polynomial
  `x²+x+1` (the Eisenstein cyclotomic `Φ₃`, the same `ω` as B324), **irreducible mod 4** (no roots), so the three
  generations are bound into **one irreducible `ω`-module** — they cannot carry independent torsion labels.

## Verified in-sandbox (two ways)
1. **SnapPy 3.3.2:** `Manifold('4_1')`, its unique 3-fold cyclic cover has `H₁ = ℤ/4 + ℤ/4 + ℤ`. ✓ (matches Calegari,
   `math/0603152`).
2. **Exact Alexander module (sympy):** the torsion is `ℤ[t]/(Δ, t³−1)` with `Δ(t)=t²−3t+1`. Smith normal form of the
   presentation `→ diag(4,4)`, i.e. `(ℤ/4)²`. ✓
3. **The deck action:** on the Alexander module the deck map is multiplication by `t`, char poly `Δ(t)`. Since
   `−3 ≡ 1 (mod 4)`, `Δ ≡ t²+t+1 = Φ₃ (mod 4)`. Companion of `Φ₃` cubes to `I mod 4` (order 3), and `Φ₃` has **no roots
   mod 4 and no roots mod 2** (it is the irreducible quadratic over `𝔽₂`) → the `ℤ/3` acts **irreducibly** on `(ℤ/4)²`. ✓
4. **Order of the torsion:** `|H₁(3-fold branched cover)| = Δ(ω)·Δ(ω²) = 16 = |(ℤ/4)²|`. ✓

## The bonus — both arithmetic ends in one polynomial (new, exact)
The *same* Alexander polynomial `Δ(t)=t²−3t+1` carries **both** of the object's arithmetic ends:
- `disc(Δ) = 5` — its roots are `φ², φ⁻²`, the **ℚ(√5)** ("golden") end;
- `Δ mod 4 = Φ₃` — the **ℚ(√−3)** (Eisenstein/`ω`) end.
The two-ended structure (banked, `K020`/`two-ended-unification`) is visible in the reduction of one degree-2 invariant:
the √5 end is the discriminant, the √−3 end is the mod-4 reduction. This is an observation, not a new claim to
`CLAIMS.md`.

## The firewall (held, and made *more honest*)
- **What this is:** the breaking is **arithmetic** (finite congruence torsion), **not** a transcendental
  embedding-metric asymmetry. That is a *sharper and more honest* location of the firewall than the earlier
  "transcendental / specialist-gated" wording (which Chat-2 self-corrected mid-push — see errors below).
- **What this is *not*:** finite torsion `(ℤ/4)²` gives **selection rules / texture** (which couplings vanish), **not
  mass magnitudes** — a 16-element group cannot contain a `10⁻⁵` ratio. "Torsion = hierarchy" would be an asserted
  bridge; it is **not** asserted. The wall did not move to the values; it got named to a finite, computable datum.

## Chat-2's three self-caught errors (logged so no seat re-walks them)
1. **CP-sign "flow-selection" splice** [self-caught]: `σ` is orientation-preserving, cannot select handedness;
   corrected to "CP sign = the object's chirality" (Im w > 0 vs mirror).
2. **The "cubic is ℤ/3-obstructed"** claim [refuted by CC as **B325**; Chat-2 concurs]: the light modes are two
   *distinct* 1-dim irreps `(ω, ω²)`, not a protected 2-dim irrep — a ℤ/3-invariant operator splits them freely.
3. **"transcendental / specialist" mislabel** of the breaking [self-corrected here]: it is finite congruence torsion,
   computed above.

## Verdict
Banked as a **[VERIFIED]** structural/texture result: the generation ℤ/3-breaking datum is *finite and arithmetic*
(`(ℤ/4)²` with irreducible `Φ₃`-action), reproduced independently of Chat-2. It sharpens the firewall's location
(arithmetic, not transcendental) **without** moving it to the values (texture, not magnitudes). Feeds the CRUX (gate B):
the hierarchy question is downstream of the `27|₂T` branching, not of this torsion — see **B327**.

## The fence
SnapPy 3.3.2 (cover homology) + exact sympy (Alexander module, Smith normal form, `Φ₃` mod 4). The mass / Yukawa
interpretation is firewalled and CRUX-gated. Nothing to `CLAIMS.md`.

`congruence_torsion.py` (pyenv) · `tests/test_b326_congruence_torsion.py`. Related: **B324** (the exact ω-circulant),
**B302** (the intrinsic ℤ/3, `ℚ(√−3)`, index-12), **B327** (the `27|₂T` McKay gate — where the hierarchy question
actually lives), **K020** / `two-ended-unification` (the √5 ↔ √−3 ends). Lit: Calegari `math/0603152` (torsion of
cyclic covers); Milnor (infinite cyclic cover / Alexander module); Reid (`4₁` unique arithmetic knot).
