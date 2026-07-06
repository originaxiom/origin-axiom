# B445 — the E₆ H¹ at the principal point: 6 for the figure-eight, 6 for the control

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`.** Runs the L50 "Computation B"
gate correctly (the handoff script computed it in the wrong representation) and adds the control the
handoff omitted. Result: the E₆ deformation count is **universal (= rank E₆), not a figure-eight
fingerprint.** The decisive dichotomy of the handoff ("nonzero ⟹ fingerprint, zero ⟹ dead") is
**false**: nonzero is generic.

## What was asked (L50 handoff, "Computation B")

Compute `dim H¹(π₁(4₁), Ad_{E₆} ρ₀)` at the principal point `ρ₀ = (principal SL(2)→E₆) ∘ ρ_geo`.
Expected 6, "one per E₆ exponent {1,4,5,7,8,11}." The handoff's decisive question: *does the E₆
character variety of `4₁` have irreducible components that don't come from SL(3)? Nonzero ⟹ the
components are the fingerprint.*

## Two corrections to the handoff scripts (verify-before-run)

1. **Wrong representation.** `computation_B_e6_cocycle.py` builds the **27-dim minuscule** rep and
   takes H¹ in `gl(27)` (729-dim). The E₆ character-variety tangent space is H¹ in the **adjoint 78**,
   not gl(27) — a different object. Fixed here.
2. **The trace-3 solver is unnecessary.** The script's `fsolve` search for fiber generators failed;
   it isn't needed. SnapPy's own holonomy `M.fundamental_group().SL2C(g)` gives the generators
   directly, and the computation uses SnapPy's presentation self-consistently.

**Key simplification that makes it exact and cheap:** the principal SL(2) acts on the adjoint 𝔢₆ as
`⊕ₘ Sym^{2m}` over the **exponents** `m ∈ {1,4,5,7,8,11}` (dims 3,9,11,15,17,23; sum 78). So H¹
**decouples**:
```
H¹(π₁, ad E₆ ρ₀) = Σ_{m∈{1,4,5,7,8,11}} H¹(π₁, Sym^{2m} ρ_geo).
```
No E₆ bracket needed — just six symmetric-power SL(2) cohomologies from the holonomy.

## Result (exact; mpmath dps=60, so the Sym²² |λ|⁴⁴≈10¹³ range is trivially resolved)

| block `Sym^{2m}` | m | `4₁` H¹ | `5₂` H¹ | rank-gap (both) |
|---|---|---|---|---|
| Sym² | 1 | 1 | 1 | ≥10⁵⁹ |
| Sym⁸ | 4 (θ-odd, E₆-only) | **1** | **1** | ≥10⁴⁹ |
| Sym¹⁰ | 5 | 1 | 1 | ≥10⁴⁶ |
| Sym¹⁴ | 7 | 1 | 1 | ≥10⁴⁰ |
| Sym¹⁶ | 8 (θ-odd, E₆-only) | **1** | **1** | ≥10³⁶ |
| Sym²² | 11 | 1 | 1 | ≥10²⁵ |
| **total** | | **6** | **6** | |

Every block gives H⁰=0 (irreducible, as required) and H¹=1 — the Menal-Ferrer–Porti result (one
cusp ⟹ one deformation per even symmetric power). **`H¹ = 6 = rank(E₆)` for the figure-eight AND
for `5₂`.**

Double-precision (numpy) gives the *wrong* answer here — the high blocks' rank collapses (gaps fall
to ~10¹, H⁰ spuriously inflates to 16). Recorded as a cautionary control: this computation is
precision-critical; anything under ~40 digits is unreliable for the exponent-8/11 blocks.

## Verdict — the "6" confirms the deflation, not a fingerprint

1. **`H¹ = 6` is universal.** It equals `rank(E₆)` and is the *same for every one-cusped hyperbolic
   knot* (Menal-Ferrer–Porti: the principal geometric component of the G-character variety is smooth
   of dimension `rank(G)`, for any `G`, any one-cusped `M`). `5₂` — not amphichiral, not
   commensurable with `4₁`, different SL(3) fields (B444) — gives the **identical** 6, block by block.
   So the count carries **zero figure-eight-specific information.**
2. **The θ-odd / E₆-only directions DO exist — for both knots equally.** The F₄ exponents are
   {1,5,7,11}; the E₆/F₄ coset adds {4,8}. Those two blocks (Sym⁸, Sym¹⁶) each contribute H¹=1, so
   the E₆ variety genuinely deforms in directions invisible to F₄ (and, since SL(3) principal gives
   only `rank=2`, invisible to SL(3) too: E₆'s 6 vs SL(3)'s 2). **But `5₂` has the same 2 θ-odd
   directions.** "Beyond SL(3)" is the generic behaviour of the principal geometric component, not a
   fingerprint.
3. **The handoff dichotomy is false.** "Nonzero E₆-beyond-SL(3) content ⟹ fingerprint" — no: the
   nonzero content (4 extra directions over SL(3), 2 of them θ-odd) is universal. Zero would have
   been the surprise. This is Menal-Ferrer–Porti, a **known framework**, not new content.

## Computation A (trinification amplification) — counts the wrong object

`computation_A_triangle_group.sage` performs **no computation** — it prints a hardcoded combinatorial
table asserting "2 SL(3) components → up to 26 E₆ components" by assigning `{1, V₁, V₂}` to the three
SL(3) slots of the trinification Levi `SL(3)³ ⊂ E₆`. Two fatal problems:
- A rep landing in one SL(3) Levi factor is **reducible** as an E₆ rep: under `SL(3)³`,
  `78 = (8,1,1)⊕(1,8,1)⊕(1,1,8)⊕(3,3,3̄)⊕(3̄,3̄,3)`, so a single-factor rep decomposes `ad E₆` into
  an `sl(3)` block plus `3/3̄` blocks — it does **not** give a new E₆-irreducible component. These are
  exactly the reps that *do* factor through SL(3) — the opposite of the decisive question.
- The count `3³` is **knot-independent** — any knot with any SL(3) reps yields it. It cannot
  distinguish the figure-eight.

## Where this leaves L50

The only figure-eight-specific invariant in this whole rung remains the **arithmetic field** (B444:
fig-8 SL(3) = `ℚ(√−7)`), and that is already known (Falbel 2008) and already banked (the chirality
field, B316/B147). The **dimension** data (`H¹ = 6`) launders completely — it is `rank(E₆)`, shared
by the control. Consistent with the Child-Program zero-bar verdict and the Inversion Law: every
value the object produces is either numerator-forced (here: `rank E₆`, shared by all knots) or
already-known arithmetic. The "3 generations / path to physics" reading is the repeatedly-killed
trap (B428 "three folds = three generations DEAD"); a deformation dimension is not a particle count.

## Reproduce

```
python3 e6_h1_hp.py     # needs snappy (ManifoldHP) + mpmath; ~11 s, dps=60
```
Prints the per-block H¹ and the total 6 for both `4₁` and `5₂`.
