# B318 — Amphichirality is the *geometric* firewall for the Eisenstein end; the golden end is arithmetic-only

**Status: banked (frontier). Verify-don't-trust on two cross-chat handoffs (Chat-1 Result 3, Chat-2 Part 1). Firewalled;
nothing to `CLAIMS.md`.** Chat-1 proposed "the amphichiral involution `τ` symmetrizes *every* invariant → the firewall
*is* amphichirality — a geometric theorem." Checking it: **half right, and the half that fails is instructive.**

## What `τ` is, and what it covers
The figure-eight is amphichiral (`CS = 0`), so it admits an orientation-reversing self-homeomorphism `τ`, which acts on
the geometric representation as **complex conjugation**. On the invariant hyperbolic **trace field `ℚ(√−3)`**, complex
conjugation is `√−3 → −√−3` — **the nontrivial Galois automorphism**. So `τ` symmetrizes every Eisenstein-end invariant
as a `τ`-odd `±`pair (the `±π/6` CP sign, B285; `CS = 0`; all `ℚ(√−3)` data), and `τ`-even invariants (volume, `|κ| =
√3`) are determined. **This confirms Chat-1's core insight for the Eisenstein end, and deepens B285: the CP-sign Galois
is not merely arithmetic — it is the *geometric* amphichiral involution (complex conjugation).**

## Where it fails — the golden end
`τ` (complex conjugation) is **trivial** on the real **golden monodromy field `ℚ(√5)`** (`conj(√5) = √5`; and `τ`
reverses the fiber monodromy `A=LR → A⁻¹`, i.e. `φ² ↔ φ⁻²`, which fixes `ℚ(√5)`). So **B314's golden symmetrization
(`√5 → −√5`, the colored Jones `1∓√5`) is *not* realized by any geometric involution — it is a purely arithmetic
Galois.** Chat-1's "`τ` symmetrizes *all* invariants" overclaims: the golden end has no `τ`.

## The result
The firewall's **two ends have two different symmetrizing mechanisms**:

| end | field | mechanism | nature |
|---|---|---|---|
| Eisenstein | `ℚ(√−3)` (imaginary, the trace field) | `τ` = complex conjugation | **geometric** (the amphichiral involution) |
| golden | `ℚ(√5)` (real, the monodromy field) | `√5 → −√5` | **arithmetic** (no geometric involution) |

This **refines K020/B314** ("two ends, two ℤ/2") by identifying *which* ℤ/2 is geometric and which is arithmetic. "The
firewall is amphichirality" is true for the Eisenstein end and false for the golden end.

## Absorbed: the B311 correction (Chat-2 Part 1)
Chat-2 correctly caught that B311's "the two arithmetic ends sit in one A-poly discriminant" slightly overclaimed the
*golden* factor. The discriminant `(x−1)²(x+1)²(x²−3x+1)(x²+x+1)` `[x=M²]` has golden factor `x²−3x+1` = the figure-eight's
**own monodromy eigenvalue quadratic** (roots `φ², φ⁻²`, trace 3) — **definitional** (every metallic `m` has its own),
`ℚ(√5)`-real, `τ`-fixed — not a surprising coincidence. The Eisenstein factor `x²+x+1` is the meridian torsion point
`M=ζ₁₂` (`M²=ω`), on the curve because the trace field is `ℚ(√−3)` = **arithmeticity (B282)**. Consistent with this
finding: golden = definitional/arithmetic/`τ`-fixed, Eisenstein = the atom (B282) / the geometric `τ`. The honest residue
is a new **B282 certificate**: the Eisenstein arithmetic is visible as the A-polynomial branch point `M=ζ₁₂`.

## The fence
Elementary Galois action of complex conjugation on `ℚ(√−3)` vs `ℚ(√5)` (sympy) + the fiber-monodromy inversion. The
"amphichirality = the firewall" reading is honest only for the Eisenstein end. Nothing to `CLAIMS.md`.

`amphichiral_mechanism.py` (pyenv) · `tests/test_b318_amphichiral_mechanism.py`. Related: **B285** (the CP-sign Galois —
now identified as the geometric `τ`), **B314** (the golden/arithmetic Galois — no geometric involution), **B311** (the
two-ends discriminant — corrected here), **K017** (amphichirality/chirality), **K020** (the two-ended Galois structure —
refined), **B282** (the arithmetic atom — new `M=ζ₁₂` certificate). Lit: amphichirality and complex conjugation of the
geometric representation (Maclachlan–Reid; the invariant trace field).
