# B279 — the spin-structure bit of 4₁: τ **FIXES** both (Chat-2 headline, resolved)

**Status: banked (frontier). Topology result, FIREWALLED — the physics interpretation stays in `speculations/` and
rests on an unverified link. Nothing to `CLAIMS.md`.** From the Chat-2 handoff (2026-06-28), whose "single
highest-value computation" was: *does the amphicheiral involution τ of 4₁ fix or swap its two spin structures?*

## Result: **FIX** (τ fixes both spin structures)

### The checkable inputs (verified, `spin_structure_bit_snappy.py`, SnapPy)
1. `H₁(4₁;ℤ)=ℤ` ⟹ `H¹(4₁;ℤ/2)=ℤ/2` ⟹ **exactly 2 spin structures**.
2. The full symmetry group of the complement is **D4** (order 8); 4₁ is hyperbolic, so by **Mostow rigidity +
   Gordon–Luecke** every complement-isometry is **ambient** — it extends to a symmetry of the pair `(S³, 4₁)`.
3. Every isometry's action on the cusp `(μ, λ)` is by `±1` entries ⟹ **trivial mod 2** ⟹ `τ* = id` on
   `H¹(4₁;ℤ/2)` (forced anyway: `Aut(ℤ/2)=1`). So the bit is **not** visible from homology — it is a framing-level
   invariant.

### The proof (resolves the framing-level ambiguity Chat-2 flagged)
Spin structures on an oriented 3-manifold form a **torsor over `H¹(M;ℤ/2)`**. The figure-eight is a knot in `S³`,
and `S³` has a **unique** spin structure (`H¹(S³;ℤ/2)=0`). Its restriction to `M = S³∖N(4₁)` is a **canonical** spin
structure `σ₀` (the `S³`-bounding one).

τ is the restriction of an **ambient** orientation-reversing involution `τ̄` of `(S³, 4₁)` (input 2). `τ̄` acts on the
**one-element** set `Spin(S³)`, so `τ̄*(spin_{S³}) = spin_{S³}` trivially; restricting,
`τ*(σ₀) = (τ̄* spin_{S³})|_M = spin_{S³}|_M = σ₀`. So **`σ₀` is τ-invariant.**

Since `Spin(M)` is a 2-element torsor and `τ* = id` on `H¹(M;ℤ/2)` (input 3), the τ-action is all-or-nothing:
`δ(τ) := τ(s) − s ∈ H¹(M;ℤ/2)` is independent of `s`, and `δ(τ) = τ(σ₀) − σ₀ = 0`. **Hence τ fixes both.** ∎

Equivalently: spin structures on a knot complement are labelled by their `ℤ/2` meridian-holonomy (relative to `σ₀`),
and τ acts on `μ` by `±1 ≡ 1 (mod 2)` — fixing the labels.

### What this corrects in the handoff
Chat-2 treated fix-vs-swap as genuinely uncertain ("could be SWAP → chiral matter possible"). It is **FIX**, and not
by accident: it holds for **every** ambient symmetry of **every** knot complement (the `S³`-bounding spin structure
is always ambient-symmetry-invariant). The framing-shift worry is dissolved by using `σ₀` (not the Lie framing) as
the basepoint.

## Firewall — the physics is NOT banked
Chat-2's chain *fix ⟹ a τ-invariant spin structure exists ⟹ η=0 in it ⟹ τ gaugeable-with-fermions ⟹ τ gauged ⟹
non-chiral matter / single arrow of time* uses a **parity-anomaly / η-invariant** step (its links 3–4) that the
handoff itself flags as derived-that-session and **not literature-checked**. We bank only the **topological bit**
(FIX). In Chat-2's own framework FIX is the **non-chiral branch** — i.e. the object does **not** source chirality
from τ; chirality stays external. This is **consistent with the standing firewall** (wall #3: chirality needs
external dynamics; the object is CP-symmetric, B252) and is a clean negative for direct SM-chirality-from-τ, not a
positive bridge. `[MATH]` the bit; `[LEAP]` the gauging/anomaly reading (see `speculations/`).

## Files
`spin_structure_bit_snappy.py` (sage inputs) · `spin_bit_verdict.py` (pyenv) · `tests/test_b279_spin_structure_bit.py`.
